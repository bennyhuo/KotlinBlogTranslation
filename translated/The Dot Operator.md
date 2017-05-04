---
title: "[译]The Dot Operator"
date: 2013-04-01 10:00:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2013/04/the-dot-operator/
translator:
translator_url:
---

**警告：这是愚人节的帖子** [无点](http://en.wikipedia.org/wiki/Point-free_programming) 风格是现代功能编程中的一个大趋势：它允许操纵函数，而不用提及它们的参数，这使得代码简洁和组合。以下是维基百科的例子：

{% raw %}
<p></p>
{% endraw %}

```kotlin
mf = (. map) . (.) . filter
```

{% raw %}
<p></p>
{% endraw %}

这个函数用Haskell编写，它构成了一个带有filter（）函数的map（）函数。如您所见，无点式的风格主要依靠点。
Kotlin本身不是功能性语言，但我们很乐意借用其他语言的实用功能。所以，今天我会写点点。<span id =“more-1007”> </span>
# 点

我们在Kotlin中介绍**点**运算符。像往常一样，它按照惯例工作。如果有这样的功能

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun Foo.dot() {
    println("a dot!")
}
```

{% raw %}
<p></p>
{% endraw %}

在Foo类型的表达式后面会有一个点（“。”）被调用：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun test(f: Foo) {
    f.foo()
    Foo().bar().baz()
}
```

{% raw %}
<p></p>
{% endraw %}

此功能打印“一个点！”两次：一个Foo后每个点一次。 bar（）函数不返回Foo，所以后面的点不算。
# 点链

如果我的dot（）函数返回某些东西，例如另一个Foo，该怎么办？

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Foo(val count: Int)
 
fun Foo.dot(): Foo {
    return Foo(count + 1)
}
```

{% raw %}
<p></p>
{% endraw %}

那么当然，它的结果是用来调用点后的任何东西：

{% raw %}
<p></p>
{% endraw %}

```kotlin
println(Foo(1).count)
```

{% raw %}
<p></p>
{% endraw %}

这打印2，因为dot（）函数返回一个新的Foo增加计数器。
你可以看到，点运算符给了我们很多的权力，解决了以前解决的大多数问题 [面向方面的编程](http://en.wikipedia.org/wiki/Aspect-oriented_programming) 。
# 味道的味道

当您使用参数声明时，点操作符的真实力量来自：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun Any.dot(p: Dot) {
   ...
}
```

{% raw %}
<p></p>
{% endraw %}

该参数必须是Dot类型，其中有一些有趣的预定义值：

{% raw %}
<p></p>
{% endraw %}

```kotlin
LEFT
RIGHT
TOP
BOTTOM
```

{% raw %}
<p></p>
{% endraw %}

这些值显然对应于点的位置：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun test() {
    println(a.b[1..2])
}
```

{% raw %}
<p></p>
{% endraw %}

有人可能认为在这个例子中，dot（）被调用三次：一个用于“ab”，参数BOTTOM，然后是“1..2”两次：首先用LEFT，然后用RIGHT（这些不是两个BOTTOM ，因为“..”是一个单一的 [令牌](http://en.wikipedia.org/wiki/Token_(parser)#Token)  在Kotlin），但事实上它被称为四次，第四次（实际上是第一次）与TOP作为参数。
我相信你已经明白了为什么：在Kotlin，我们永远不会忘记点点我的，这个点也是如此;其立场显然是TOP（我们可以单独介绍） [滴滴](http://en.wikipedia.org/wiki/Tittle) （）函数，但是我们发现它太不方便了）。在j的计数以上也是一样，点数也相同！ ？等等
# 点的深度

你可能会想知道如果定义了这样的点（），会发生什么：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun Foo.dot() {
    println(this.count)
}
```

{% raw %}
<p></p>
{% endraw %}

在**这个**之间有一个点，它在Foo.dot（）函数本身中具有Foo类型，所以在这一点上应该递归调用dot（），并且似乎从不终止。这被称为高阶点</em>，只有在Foo上定义了一个函数dot1（）时才执行。如果dot1（）又包含高阶点，则调用dot2（）等等：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun Foo.dot1() {
    println(this.count) // a call to dot2() if that is defined
}
```

{% raw %}
<p></p>
{% endraw %}

这对应于罗素的设定理论的方法 [类型理论](http://en.wikipedia.org/wiki/Type_theory) （与它的概念 [类](http://en.wikipedia.org/wiki/Class_(set_theory)) ），这是静态类型的面向对象编程的坚实基础。
# 结论

我们计划很快支持点运营商。第一个版本将被限制为基本的ASCII字符，如。 ：; ！ ？当然，我，但在将来我们计划将其扩展到其他角色，如ё。
**有一个不错的点！**
