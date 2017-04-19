---
title: "[译]Call for Feedback: Upcoming Changes in Kotlin"
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

如前所述，我们正在使用语言设计，这篇文章是即将到来的更改的主要内容+请求您的反馈。<span id =“more-2657”> </ span>
## 背景领域

之前我提到我们对现在的支持字段语法感到不满，这是<code> $ propertyName </ code>：

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

最大的问题是这个语法与语法相冲突 [字符串模板](http://kotlinlang.org/docs/reference/basic-types.html#string-templates) 。
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

请注意，<code>字段</ code>只是一个隐式定义的变量（非常类似于lambdas中的<code> it </ code>）。
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

过去已经有很多争议了，我们终于决定要在Kotlin中介绍一下操作符重载和中缀函数调用的方法。目前可以称为<code> a.plus（b）</ code>的任何名为<code> plus </ code>的函数可以称为<code> a + b </ code>。我们将要求这些函数用<code>运算符</ code>修饰符标记，否则运算符符号将不可用。这使得操作员使用更加规范，并消除了随机标点符号侵入API的可能性。最常见的例子是使用一个名为<code> get </ code>的方法，但完全不打算用作方括号。
对于中缀函数调用是一样的：我们需要一个函数被标记为<code>中缀</ code>。这将减少通用API中不寻常的样式多样性：

* list add 1 vs list.add（1）
* 列表地图{...} vs list.map {...}
* 等等

Infix函数仍然可以使用旧的标准语法<code> x.or（y）</ code>进行调用，但是这个工具将会暗示你的语法是中缀。
请注意，标准库中的常见功能（例如<code> map </ code>或<code> filter </ code>）不会被标记为<code>中缀</ code>，因为使用它们有时会导致隐藏如果这样一个表达式后面是一个点，则会出现错误：

{% raw %}
<p></p>
{% endraw %}

```kotlin
list map {...}.toSet() // Error: toSet() is not applicable to a lambda
 
```

{% raw %}
<p></p>
{% endraw %}

如果某些Java方法没有标记为<code> operator </ code>或<code> infix </ code>，我们可以随时定义一个扩展名，标准库将为大多数流行的案例提供此类扩展。
## 常数

对于注解，编译时常数很重要：只有它们可以用作参数（以及很少的额外表达式，即数组和注释构造函数）。到目前为止，我们采用相同的“隐含”方法来检测它们，如Java所示：如果<code>对象</ code>或顶层的<code> val </ code>在其初始化程序中只有常量，它是一个编译时常数。这是脆弱的，并提出了破解API的可能性，而不知道，所以我们决定要求这样的<code> val </ code>的<code> const </ code>修饰符：

{% raw %}
<p></p>
{% endraw %}

```kotlin
const val SCREEN_WIDTH = 2048
 
```

{% raw %}
<p></p>
{% endraw %}

注意：<code> const </ code>值只能有以下类型：“primitives”，<code> String </ code>，枚举，类文字。
## invokeExtension（）约定

到目前为止，这已经非常模糊，但是我们将会改变它。现在，如果一个值需要作为扩展函数调用，它必须有一个成员，它是一个扩展名，并被命名为<code> invoke </ code>：

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

内部成员被编译为<code> public </ code>，这可能会导致意外覆盖：

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

由于父函数不可见，编译器不需要<code> Derived :: foo </ code>中的<code> override </ code>，而是在字节码中具有相同的签名，并且运行时将绑定它们作为覆盖，这不是作者的意图。当模块X和Y独立演进（例如，一个是库和另一个用户的项目）时，问题最为困难，因此，当Y编译时，<code> foo </ code>尚未出现在<code> X < / code>。
为了避免这种情况，我们决定修改内部成员的名称，以免与超类成员冲突。
<strong>更新</ strong>：调整可能会导致此成员无法从Java调用。这似乎很难解决，但解决方法很简单：只需使其<code> public </ code>或<code> protected </ code>即可。
## 其他变化


* Java 6上接口的默认实现类将被命名为Foo.DefaultImpls而不是Foo $$ TImpl
* _，__，___将被禁止作为标识符，即我们可以使用_foo，但不能单独使用（保留供将来使用）
* 我们将在界面中删除最终的，受保护的和内部的：这些不能在JVM上表达，所以我们推迟他们的实现，直到后来
* 我们要放弃identityEquals（）函数，有利于===

## 反馈

您的意见和用例是最受欢迎的！
