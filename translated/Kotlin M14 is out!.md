---
title: "[译]Kotlin M14 is out!"
date: 2015-10-01 16:16:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/10/kotlin-m14-is-out/
translator:
translator_url:
---

随着即将到来，我们转向更短的里程碑。认识M14带来以下变化：

* 支持文件类的注释
* 标准库的新Java API
* 操作员操作符修饰符
* 现在通过合成字段变量访问备份字段

## 语言

我们正在用语言变化来包装，所以在M14中没有什么真正戏剧性的。
<strong>注意</strong>：我们正在删除以前不推荐使用的功能和功能，因此请确保在安装M14之前运行代码清理</em>。
### 背景领域

旧的`$ propertyName`语法已弃用。要访问getter / setter内的后备字段，请使用`字段`合成变量：

{% raw %}
<p></p>
{% endraw %}

```kotlin
var prop: Int = 1
    get() {
        notifyRead(field)
        return field
    }
    set(v) {
        notifyWrite(field, v)
        field = v
    }
```

{% raw %}
<p></p>
{% endraw %}

如果同一范围内的另一个属性被命名为`field`，我们需要使用“`this。`”来限定其使用。
需要在声明（而不是在构造函数中）初始化具有后备字段和自定义设置器的Var属性，因为这种初始化器将绕过设置器直接写入到后台字段。
在这种模式不够灵活的情况下（可能很少见），请考虑引入后台属性（可以使用相应的重构）或使用属性委托。
### 经营者

正如宣布的那样 [先前](http://blog.jetbrains.com/kotlin/2015/09/call-for-feedback-upcoming-changes-in-kotlin/) ，Kotlin M14期望通过运算符符号（例如`plus`，`iterator`等）调用的函数被标记为`operator`修饰符。注意：当我们扩展`Any`，`Iterable`或`Comparable`时，`运算符`修饰符将自动继承，因此不需要担心他们当需要以操作员形式使用Java方法时，请使用标记为`operator`的扩展功能：

{% raw %}
<p></p>
{% endraw %}

```kotlin
operator fun JavaClass.plus(other: JavaClass): JavaClass = this.plus(other)
```

{% raw %}
<p></p>
{% endraw %}

使用<em>代码清理</em>可以自动向项目中使用的所有运算符添加修饰符。
注意：Infix功能将在最近的将来迁移到相同的方案。
### 编译时常数

由于M14我们需要使用`const`前缀Kotlin常量，以便能够在注释中使用它们，并从Java中看到字段：

{% raw %}
<p></p>
{% endraw %}

```kotlin
const val MAX = 239
```

{% raw %}
<p></p>
{% endraw %}

代码清理</em>将为您添加缺少的`const`修饰符。
### 注释文件类

由于M13，默认情况下，每个源文件的顶级函数和属性都将放在一个单独的类文件中（详细信息 [这里](http://blog.jetbrains.com/kotlin/2015/09/kotlin-m13-is-out/) ）。现在我们可以通过应用文件注释来注释这些类：

{% raw %}
<p></p>
{% endraw %}

```kotlin
// FILE: foo.kt
 
@file:MyClassAnnotation
 
package bar
 
fun baz() {}
```

{% raw %}
<p></p>
{% endraw %}

将被编译成

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Pseudo-Java
@MyClassAnnotation
public final class FooKt {
    public static void baz() {...}
}
```

{% raw %}
<p></p>
{% endraw %}

### 从旧的“包装外观”迁移

当我们转向了 [新的类文件布局](http://blog.jetbrains.com/kotlin/2015/06/improving-java-interop-top-level-functions-and-properties/) ，现在是退休老人的时候了。由于M14旧程序包外观类（例如`FooPackage`）已被弃用，IDE可帮助您通过代码清理</em>将Java代码迁移到新的方案。
<strong>注意</strong>：包立面将很快丢弃，因此请务必迁移您的代码。
标准库（以前的`kotlin.KotlinPackage`类）也被迁移到新的方案中：见下文。
### 其他语言变化


* 私有的顶级文件现在是私有的
* 内部在编译器中检查（不仅IDE）
* 私有的接口是真正的私人现在
* 数据类中的等于通过调用他们的.equals（）方法（通过身份工作）比较数组，
* 被禁止
* 许多遗传和其他自由度的数据被禁止进行数据分类（见本博客）
* 接口中禁止受保护的内部成员
* _，__，___被禁止在标识符中，即我们可以使用_foo，但不能单独使用（保留供将来使用）
* identityEquals（）函数不赞成使用===

## 标准库更改

对于Java的观点，Kotlin的标准库现在被组织成实用程序类，每个类都专用于其自己的数据类型和/或操作。例如：

* ArraysKt  - 数组操作，数组扩展，阵列工厂方法
* CharsKt  -  Char和Char.Companion的扩展名，大多数应该被隐藏
* CollectionsKt  - 对迭代，集合和列表的操作，列出工厂方法
* ComparisonsKt  - 比较器操作，比较器工厂方法和执行比较的功能

在API文档中查看更多内容。
## IDE更改

像往常一样，IDE可以帮助您通过<em>代码清理</em>从M13无缝迁移。 M14还有几个新的便捷功能：

* 如上所述，在某些情况下，我们需要私人支持属性。您可以通过意图行动轻松介绍：

