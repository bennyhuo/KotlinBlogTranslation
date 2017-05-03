---
title: "[译]Call for Feedback: Java Statics, Result Expressions and More"
date: 2015-09-25 18:27:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/09/call-for-feedback-java-statics-result-expressions-and-more/
translator:
translator_url:
---

感谢大家对我们的反馈 [以前的电话](http://blog.jetbrains.com/kotlin/2015/09/call-for-feedback-upcoming-changes-in-kotlin/) ！这里有另一轮变化和调整。欢迎您的意见和用例。<span id =“more-2707”> </span>
## Java静态和继承

我们将通过允许Kotlin子类访问其超类的静态成员来提高与Kotlin中的Java静态的互操作性：现在我们可以使用常量，嵌套类和静态实用程序来定义继承树。与超类型的伴侣对象的成员相同。
我们还将允许在继承它们的Java类上调用Java静态。
在Kotlin类上调用一个继承的静态成员是不允许的：

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Java
public class Base {
    public static void foo() {}
}
 
// Kotlin
class Derived : Base() {
    fun test() {
        foo() // OK
        Base.foo() // OK
 
        Derived.foo() // ERROR!
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

## Lateinit val的

在我们的用户的帮助下，我们发现我们以前错过了在<code> lateinit val </code>的设计中的一个不愉快的漏洞：这样的属性的备份字段不是最终的，因此Java代码可以自由地修改它们。这使得这些属性的<code> val </code> -ness消失，因为没有代码可以对它们承担任何不变性，所以我们决定采取这个功能：从现在开始，只有<code> var </code >可以标记为<code> lateinit </code>。我们将继续考虑用例和改进此功能。
## 支持字段和自定义设置器

除了以前宣布的 [更改]()  在备份字段语法中：如果属性具有自定义设置器或是<code>打开</code>，则setter可能会在写入该字段之前读取该字段，所以没有第一次初始化该属性的语法，除非它已经完成声明后所以，我们现在需要这样的属性的初始化器：

{% raw %}
<p></p>
{% endraw %}

```kotlin
var foo: Foo? = makeFoo() // initializer required
    set(v) {
        if (field != null)
            notifyListeners()
        field = v
    }
 
```

{% raw %}
<p></p>
{% endraw %}

如果我们真的需要在构造函数中初始化这样的属性，那么我们必须引入一个<em>后缀属性</em>：

{% raw %}
<p></p>
{% endraw %}

```kotlin
private var _foo: Foo?
var foo: Foo?
    get() = _foo
    set(v) {
        if (_foo != null)
            notifyListeners()
        _foo = v
    }
 
init {
    _foo = ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

## 键入参数声明

历史上，Kotlin有两种形式的函数类型参数声明的语法：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun <T> T.foo() = ...
 
fun T.foo<T>() = ...
 
```

{% raw %}
<p></p>
{% endraw %}

二是太多了，所以我们决定只保留第一个，因为它在使用之前放置了<code> T </code>的声明，这更容易阅读，代码完成将更有帮助。
## 子类和声明元素的可见性

这是一个技术要求，但直观性：如果某些东西是<code> public </code>，它不应该公开一个<code> private </code>类型：

{% raw %}
<p></p>
{% endraw %}

```kotlin
private open class Super
 
class Public : Super() {
    private class Private
 
    fun public(p: Private): Private = ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

从现在开始，公共类不能扩展私有类，公共成员不能公开私有类。
更正式地：声明的超类型或元素必须（有效地）至少与声明/类本身一样可见。
## 标记结果表达式

这不是真的决定，而且确实是非常有争议的，但它不能在1.0之后添加，所以我们一直在考虑一段时间：
像你们中的一些人 [正确观察](https://youtrack.jetbrains.com/issue/KT-8695) ，有时可能难以看到使用什么表达式作为块或羔羊的结果。
在以下情况下，我们正在考虑使用<code> ^ </code>符号（或可能还有一些其他前缀）将这些结果表达式前缀，使其可见：

* 表达式是多行块或lambda的结果
* 它的类型不是Unit，也不是Nothing。

示例（从Kotlin代码库）：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val getter = target.getGetter() ?: run {
    val defaultGetter = DescriptorFactory.createDefaultGetter(target, Annotations.EMPTY)
    defaultGetter.initialize(target.getType())
    ^defaultGetter
}
 
```

{% raw %}
<p></p>
{% endraw %}

要么

{% raw %}
<p></p>
{% endraw %}

```kotlin
private fun transformTryCatchBlocks(methodNode: MethodNode, newTryStartLabels: HashMap<LabelNode, LabelNode>) {
     methodNode.tryCatchBlocks = methodNode.tryCatchBlocks.map { tcb ->
         val newTryStartLabel = newTryStartLabels[tcb.start]
         ^if (newTryStartLabel == null)
             tcb
         else
             TryCatchBlockNode(newTryStartLabel, tcb.end, tcb.handler, tcb.type)
     }
}
 
```

{% raw %}
<p></p>
{% endraw %}

请注意，只需在IDE中突出显示结果表达式并不是一个解决方案：

* 它不会通过在末尾添加无害的println（）来防止意外变化的羔羊或块的结果，
* 它在GitHub，终端或IDE之外的任何地方都不起作用

我们对Kotlin代码库进行了快速实验，并添加了所有必需的前缀：
<p>
<a href="https://github.com/JetBrains/kotlin/compare/hats">请参阅差异github </a>
</p>
上面的diff将使您了解这些代码的外观。
为了让您了解代码中会发生多久的一个想法：我们在约230,000行Kotlin代码（0.21％）中更改了493行，而在我们的代码中我们所拥有的2190个Kotlin文件中有233个文件被更改基数（每第10个文件）。
