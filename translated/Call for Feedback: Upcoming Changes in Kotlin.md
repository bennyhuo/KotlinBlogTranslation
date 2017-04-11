---
title: [译]Call for Feedback: Upcoming Changes in Kotlin
date: 2015-09-18 14:06:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/09/call-for-feedback-upcoming-changes-in-kotlin/
---

如前所述，我们正在使用语言设计，这篇文章是即将到来的变化的主角+请求您的反馈。
## 背景领域

之前我提到我们对现在的支持字段语法感到不满，这是$ propertyName：

{% raw %}
<p></p>
{% endraw %}

```kotlin
var foo: Foo = ...
    get() { beforeRead(); return $foo }
    set(v) { beforeWrite($foo, v); $foo = v }
 
```

{% raw %}
<p></p>
{% endraw %}

最大的问题是这种语法与字符串模板的语法相冲突。
所以，我们决定在这里改变规则：

* $ foo语法将被弃用，然后删除
* 相反，我们可以通过getters / setters中的名称字段访问支持字段：


{% raw %}
<p></p>
{% endraw %}

```kotlin
var foo: Foo = ...
    get() { beforeRead(); return field }
    set(v) { beforeWrite(field, v); field = v }
 
```

{% raw %}
<p></p>
{% endraw %}

请注意，该字段只是一个隐式定义的变量（非常类似于lambdas）。
这种方法不支持一些用例：我们以前可以在类中的任何位置访问支持字段，现在只能在getter / setter中显示。我们已经在GitHub上检查了Kotlin代码，并且意识到只有很小一部分的用例没有被覆盖，对于这些，我们可以随时使用“支持属性”：

{% raw %}
<p></p>
{% endraw %}

```kotlin
private var _foo = ...
public var foo: Foo
    get() = ...
    set(v) { ... }
 
```

{% raw %}
<p></p>
{% endraw %}

## 运算符和中缀功能

过去已经有很多争议了，我们终于决定要在Kotlin中介绍一下操作符重载和中缀函数调用的方法。目前可以称为加号（可称为a.plus（b））的任何函数也可以称为+ b。我们将要求这些功能用操作符修饰符标记，否则操作符符号将不可用。这使得操作员使用更加规范，并消除了随机标点符号侵入API的可能性。最常见的例子是使用一个叫做get的方法，但完全不打算用作方括号。
对于中缀函数调用是一样的：我们将要求一个函数被标记为中缀。这将减少通用API中不寻常的样式多样性：

* list add 1 vs list.add（1）
* 列表地图{...} vs list.map {...}
* 等等

Infix函数仍然可以使用旧的标准语法x.or（y）进行调用，但是这个工具将会暗示你的语法是中缀。
请注意，标准库中的常见功能（例如地图或过滤器）不会被标记为中缀，因为如果这样的表达式后面跟着一个点，则使用它们有时会导致隐含错误：

{% raw %}
<p></p>
{% endraw %}

```kotlin
list map {...}.toSet() // Error: toSet() is not applicable to a lambda
 
```

{% raw %}
<p></p>
{% endraw %}

如果一些Java方法没有被标记为运算符或中缀，我们可以随时定义一个扩展名，标准库将为大多数常见的案例提供这样的扩展。
## 常数

对于注解，编译时常数很重要：只有它们可以用作参数（以及很少的额外表达式，即数组和注释构造函数）。到目前为止，我们采用相同的“隐式”方法来检测它们，如Java所示：如果一个对象或顶层的val只在其初始化器中只有常量，那么它是一个编译时常量。这是脆弱的，并提出了破解API的可能性，而不知道，所以我们决定要求在这样的vals上的const修饰符：

{% raw %}
<p></p>
{% endraw %}

```kotlin
const val SCREEN_WIDTH = 2048
 
```

{% raw %}
<p></p>
{% endraw %}

注意：const值只能有以下类型：“primitives”，String，枚举，类文字。
## invokeExtension（）约定

到目前为止，这已经非常模糊，但是我们将会改变它。现在如果一个值需要作为扩展函数调用，它必须有一个成员是一个扩展名，并被命名为invoke：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Foo {
    operator fun String.invoke() { ... }
}
 
fun test(foo: Foo) {
    "".foo()
}
 
```

{% raw %}
<p></p>
{% endraw %}

这在某些情况下是不方便的，所以我们要将其更改为

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Foo {
    operator fun invokeExtension(s: String) { ... }
}
 
fun test(foo: Foo) {
    "".foo()
}
 
```

{% raw %}
<p></p>
{% endraw %}

作为副作用，可以添加如扩展名的功能：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Foo
 
operator fun Foo.invokeExtension(s: String) { ... }
 
```

{% raw %}
<p></p>
{% endraw %}

## 内部能见度和扭曲

目前内部成员公开编辑，这可能会导致意外超越：

{% raw %}
<p></p>
{% endraw %}

```kotlin
// module X
 
open class Base {
    internal fun foo() {...}
}
 
// module Y
 
class Derived : Base() {
    fun foo() {...}
}
 
```

{% raw %}
<p></p>
{% endraw %}

编译器不需要对Derived :: foo进行重写，因为父函数不可见，但是在字节码中这些具有相同的签名，并且运行时将将它们绑定为覆盖，这不是作者的意图。当模块X和Y独立演进（例如，一个是一个库，另一个是用户的项目）时，这个问题最为困难，所以当Y编译时，foo还没有出现在X中
为了避免这种情况，我们决定修改内部成员的名称，以免与超类成员冲突。
更新：破坏可能会导致这个成员不可能从Java调用。这似乎很难解决，但解决方法很简单：只是使其公开或受保护。
## 其他变化


* Java 6上接口的默认实现类将被命名为Foo.DefaultImpls而不是Foo $$ TImpl
* _，__，___将被禁止作为标识符，即我们可以使用_foo，但不能单独使用（保留供将来使用）
* 我们将在界面中删除最终的，受保护的和内部的：这些不能在JVM上表达，所以我们推迟他们的实现，直到后来
* 我们要放弃identityEquals（）函数，有利于===

## 反馈

您的意见和用例是最受欢迎的！
