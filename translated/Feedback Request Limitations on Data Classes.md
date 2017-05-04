---
title: "[译]Feedback Request: Limitations on Data Classes"
date: 2015-09-09 16:26:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/09/feedback-request-limitations-on-data-classes/
translator:
translator_url:
---

M13即将到来，我们计划稍后一点。这是对Kotlin未来变化的反馈请求。
我们希望比以后提供Kotlin 1.0，这使我们推迟了一些我们没有足够的信心的设计选择。今天我们讨论*数据类*。<span id =“more-2472”> </span>
## 介绍

的概念 [数据类](http://kotlinlang.org/docs/reference/data-classes.html) 当简单地存储数据时，已被证明非常有用。所有你需要的是说：

{% raw %}
<p></p>
{% endraw %}

```kotlin
data class Foo(val a: A, val b: B)
```

{% raw %}
<p></p>
{% endraw %}

并且您可以免费获得`equals（）/ hashCode（）`，`toString（）`，`copy（）`和组件函数。
最常见的用例类似于魅力，但数据类与其他语言功能的交互可能会导致令人惊讶的结果。
## 问题

例如，如果我想扩展一个数据类呢？如果派生类也是数据类怎么办？

{% raw %}
<p></p>
{% endraw %}

```kotlin
open data class Base(val a: A, val b: B)
 
data class Derived(a: A, b: B, val c: C) : Base(a, b)
```

{% raw %}
<p></p>
{% endraw %}

现在，`equals（）`或`copy（）`在`Derived`中的工作如何？所有众所周知的问题立即出现：

* 如果一个Base的实例等于Derived的实例，如果它们对于a和b具有相同的值？
* 等于（）的传递性怎么样？
* 如果我通过Base类型的引用复制Derived的实例？

以及组件功能如何启用 [多重声明](http://kotlinlang.org/docs/reference/multi-declarations.html) ？在这种基本情况下，`c`简单地成为`Derived` **中的第三个组件似乎或多或少是逻辑的：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val (a, b, c) = Derived(...)
```

{% raw %}
<p></p>
{% endraw %}

但没有什么能阻止我们写这样的东西：

{% raw %}
<p></p>
{% endraw %}

```kotlin
data class Derived(b: B, a: A, val c: C) : Base(a, b)
```

{% raw %}
<p></p>
{% endraw %}

请注意，参数顺序相反：first `b`，比`a`。现在还不清楚。而且可能会变得更糟：

{% raw %}
<p></p>
{% endraw %}

```kotlin
data class Derived(val c: C, b: B, a: A) : Base(a, b)
```

{% raw %}
<p></p>
{% endraw %}

现在，第一个`c`，继承的`component1（）：A`只是一个冲突，它不是一个覆盖，但是这样的重载也不合法。
这些只是一些例子，还有更多的问题，大小。
## 我们的策略

一方面，我们不确定是否有一个优雅的继承涉及数据类的设计。我们有一些草图，但没有一个看起来很有前途。
另一方面，我们现在想完成语言设计，能够发货1.0。
所以，我们决定限制数据类，以排除1.0中的所有有问题的案例，以便我们稍后再回来，也许解除一些限制。
## 建议限制

我们将要做以下事情：

* 允许从接口继承数据类
* 禁止从其他类继承数据类
* 禁止开放的数据类（即其他类不能扩展数据类）
* 禁止内部数据类（不清楚等于（）/ hashCode（）应该如何处理外部引用）
* 允许本地数据类（闭包不是结构化的，所以equals（）/ hashCode（）可以忽略它）
* 要求数据类的所有主构造函数的val / var
* 需要至少一个数据类的主要构造函数参数
* 允许数据类的私有主构造函数参数
* var在各方​​面都与val一样好（他们参与equals（）/ hashCode（）等）
* 在数据类的主构造函数参数中禁止varargs

再次，这个清单中的一些限制可能会稍后解决，但现在我们不想处理这些情况。
## 附录。比较数组

这是JVM上一个长期以来的众所周知的问题：`equals（）`对于数组和集合的工作方式不同。集合在结构上进行了比较，而数组不是，`equals（）`对于他们来说只是采用参考平等：`this === other`。
目前，Kotlin数据类在这个问题上表现不好：

* 如果你声明一个组件是一个数组，它将在结构上进行比较，
* 但是如果它是一个多维数组（数组数组），那么子阵列将被比较（通过数组上的equals（）），
* 并且如果组件的声明类型是Any或T，但在运行时它恰好是一个数组，equals（）也将被调用。

这种行为是不一致的，我们决定按照最小阻力的路径解决它：

* 总是使用equals（）作为所有其他对象来比较数组

所以，每当你说

* arr1 == arr2
* arr在setOfArrays中
* DataClass（arr1）== DataClass（arr2）
* 或沿着这些线路的其他任何东西，

你可以通过`equals（）`来比较数组，也就是说。
我们很乐意解决与集合不一致的问题，但唯一平凡的修复方式似乎是将它固定在Java中，这超出了任何人的力量，AFAIK <img alt =“:)”class =“wp-smiley” data-recalc-dims =“1”src =“https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl= 1“style =”height：1em; max-height：1em;“/>
## 征求反馈意见

请分享您对建议变更的意见。我们或多或少对数组有所了解，对数据类的限制也很有信心，但是对于更广泛的用例来说，总是一个好主意。
谢谢你的帮助！
