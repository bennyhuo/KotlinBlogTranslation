---
title: "[译]Upcoming Change: Syntax For Annotations"
date: 2015-04-03 13:13:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/04/upcoming-change-syntax-for-annotations/
translator:
translator_url:
---

Kotlin的注释语法灵感来自C＃，它围绕着它们的方括号：

{% raw %}
<p></p>
{% endraw %}

```kotlin
[Inject]
fun setFoo(foo: Foo) { ... }
 
```

{% raw %}
<p></p>
{% endraw %}

但是括号对于一个语言设计者而言是宝贵的，我们真的希望稍后再使用它们，因此我们正在考虑将注释语法更改为更类似Java的<code> @ </code>。

{% raw %}
<p></p>
{% endraw %}

```kotlin
@Inject
fun setFoo(foo: Foo) { ... }
 
```

{% raw %}
<p></p>
{% endraw %}

<strong>注意</strong>：不需要<code> [...] </code>或<code> @ </code>的短语将被保留，所以你仍然可以说这个：

{% raw %}
<p></p>
{% endraw %}

```kotlin
data class Foo
 
volatile var bar: Bar = ...
 
```

{% raw %}
<p></p>
{% endraw %}

尽管如此，这种变化有一些影响。<span id =“more-2021”> </span>
## 标签

首先，<code> @ </code> -syntax已经在使用，对于标签：

{% raw %}
<p></p>
{% endraw %}

```kotlin
@loop
for (i in 1..20) {
    if (enough(i)) break@loop
    println(i)
}
 
```

{% raw %}
<p></p>
{% endraw %}

因为表达式可以被注释和声明，我们需要在这里改变一些东西。最简单的选择是将<code> @ </code>移到标签声明的末尾：

{% raw %}
<p></p>
{% endraw %}

```kotlin
loop@
for (i in 1..20) {
    if (enough(i)) break@loop
    println(i)
}
 
```

{% raw %}
<p></p>
{% endraw %}

请注意，使用网站（<code> break @ loop </code>）没有更改，仍然看起来很不错<img alt =“:)”class =“wp-smiley”data-recalc-dims =“1” src =“https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1”style =“height：1em; max-height：1em;“/>
## 定位

我们还在研究如何在生成的<code> .class </code> -file中规定一个注释应该附加什么：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class C(@Ann("arg") var foo: Int)
 
```

{% raw %}
<p></p>
{% endraw %}

我们在这里有很多选项：可以放置<code> @Ann </code>注释

* 存储foo的字段
* 属性foo本身（不是Java声明）
* foo的吸气剂
* foo的设置者
* C的主要构造函数的参数foo

一些注释只适用于，例如，字段，对于那些没有问题，但有些允许许多可能的目标。为了表达意图，需要一些额外的语法。
一个选项是将注释类型名称与目标文件前缀：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class C(@field:Ann("arg") var foo: Int)
 
```

{% raw %}
<p></p>
{% endraw %}

（许多目标可以用逗号分隔）
另一个选择是做Scala做的事情：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class C(@(Ann@field)("arg") var foo: Int)
 
```

{% raw %}
<p></p>
{% endraw %}


* 下降：括号太多
* 颠倒：@field也是一个注释（是的，Ann是一个注释注释），这意味着更多的可扩展语法和较少的语言概念

另一个选择是使用<code> @field </code>注释，其参数是该字段的注释：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class C(@field(@Ann("arg")) var foo: Int)
 
```

{% raw %}
<p></p>
{% endraw %}


* 颠倒：比以前的情况更少的语言变化
* 缺点：如果相同的注释到达两个目标（例如吸气剂和设定器），则必须重复

这种方法的修改：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class C(@at(FIELD, @Ann1("arg"), @Ann2) var foo: Int)
class C(@atMany(array(FIELD, PROPERTY), @Ann1("arg"), @Ann2) var foo: Int)
 
```

{% raw %}
<p></p>
{% endraw %}

那么定义如下：

{% raw %}
<p></p>
{% endraw %}

```kotlin
annotation class at(val target: AnnotationTarget, vararg val annotations: Annotation)
annotation class atMany(val target: Array<AnnotationTarget>, vararg val annotations: Annotation)
 
```

{% raw %}
<p></p>
{% endraw %}

而且，为了完整性，另一种方法涉及为声明域（内部属性）添加一个显式（可选）语法：

{% raw %}
<p></p>
{% endraw %}

```kotlin
@Ann1("arg") @Ann2
val foo: Int = 1
    @Ann1("arg") @Ann2
    field _foo
    @GetterAnnotation
    get
 
```

{% raw %}
<p></p>
{% endraw %}


* 缺点：在这里没有办法减轻重复
* 缺点：它很可能成为一个模糊的语法（像$ backingField），它很少被使用，并且被工具支持很差

## 本地声明注释

我们的用户似乎经常写这样的东西：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun example() {
    data class Example(val foo: String, val bar: Int) // Error on this line
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

这不正确解析，因为<code>数据</code>不是一个关键字（既不是<code> open </code>，btw），所以我们需要这样写：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun example() {
    @data class Example(val foo: String, val bar: Int) // OK
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

现在，如果我想要一个<code> open </code>本地类，或者<code> abstract </code>，那该怎么办？那些是<em>修饰符</em>，而不是注释，我们不能说<code> @open </code>或<code> @abstract </code>。
一个选项是允许使用<code> @ </code>转义修饰符以及注释：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun example() {
    @open class Example(val foo: String, val bar: Int)
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

其他选项包括允许与类同一行</em>上的修饰符<em>，但这并不直接扩展到函数， [现在表达](http://kotlinlang.org/docs/reference/lambdas.html#function-expressions) 。查看更多 [这里](https://github.com/JetBrains/kotlin/blob/spec-at-based-annotations/spec-docs/at-based-annotation-syntax.md#reserving-space-for-future-syntactic-changes) ## 


反馈欢迎

你怎么看？
美国BTW，我们正在制定规范文件草案 [这里](https://github.com/JetBrains/kotlin/pull/624) 