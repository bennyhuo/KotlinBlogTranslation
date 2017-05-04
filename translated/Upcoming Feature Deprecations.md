---
title: "[译]Upcoming Feature Deprecations"
date: 2015-04-02 13:00:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/04/upcoming-changes-and-more/
translator:
translator_url:
---

当我们完成语言设计时，许多事情都要被清理，其中包括最初设计的（通常是部分的）实现的功能，但是不是值得支持的。
在即将到来的 M12 里程碑中，我们将不赞成使用这些功能，因此您可以在完全删除代码之前迁移代码。<span id =“more-1996”> </span>
## 所需类

有些人可能已经听说过这个功能：Kotlin 的特质可以“扩展”类（我们实际上使用术语“require”）。
从技术上讲，这意味着当一个类扩展这样的特征时，它必须（直接或间接地）扩展所需的类。这个功能很少使用，所以我们弃用它。
## 捕获类型参数

当通用类`Outer`具有**内部**类`Inner`时，Java 允许我们使用`Outer`代码> Inner`：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Outer<T> {
    inner class Inner {
        fun takeT(p: T) { ... }
    }
 
    fun inOuter(t: T) {
        Inner().takeT(t)
    }
}
```

{% raw %}
<p></p>
{% endraw %}

虽然这个功能非常合乎逻辑，但是这个功能也很少使用，而且在 Kotlin 目前的实现中，在生产质量之前需要大量的工作。所以，我们将禁止这一点，也可能在后来的 Kotlin 版本中实现。
如果你碰巧使用这个（这是不太可能的），你的解决方法是相当直截了当的：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Outer<T> {
    inner class Inner<T> {
        fun takeT(p: T) { ... }
    }
 
    fun inOuter(t: T) {
        Inner<T>().takeT(t)
    }
}
```

{% raw %}
<p></p>
{% endraw %}

## 超类型协同专业化

我真的怀疑任何人，即使知道这个功能存在<img alt =“:)”class =“wp-smiley”data-recalc-dims =“1”src =“https://i2.wp.com/ blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1“style =”height：1em; max-height：1em;“/>
当前的编译器允许一个类/ trait 具有同一个类的多个（间接）超类型，如果其中一个是另一个的子类型：

{% raw %}
<p></p>
{% endraw %}

```kotlin
open class Base : List<Number> {
    ...
}
 
class Derived : Base(), List<Int> { // no error
 
}
```

{% raw %}
<p></p>
{% endraw %}

请注意，Kotlin 中的`List`是共同的。
尽管如此，逻辑上，我们知道这几乎没有任何用例，但支持这一点涉及到很多编译器的魔法，并且断开了 Java 的互操作，所以我们要放弃这个。
## 更多的鄙视来了

我们会尽快分享一些这样的计划。并将随时更新我们正在实施的功能。
