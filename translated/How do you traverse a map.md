---
title: "[译]How do you traverse a map?"
date: 2012-09-13 15:00:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2012/09/how-do-you-traverse-a-map/
translator:
translator_url:
---

自从我上次在Kotlin M2上博客以来已经有一段时间了。现在，炎热的夏天已经过去了，而**M3**将很快出局。在这篇文章中，我描述了M3中增加的两个小功能，使我们的生活更轻松，并将导致语言的简化。
## 你如何穿越地图？

假设你有一个这样的地图：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val counts: Map<User, Int> = database.howManyDocumentsEachUserHas()
```

{% raw %}
<p></p>
{% endraw %}

你做什么来遍历它并处理每个条目？ <span id =“more-628”> </span>可能会想到以下几点：

{% raw %}
<p></p>
{% endraw %}

```kotlin
for (entry in counts) {
    if (!entry.getKey().isBanned() && entry.getValue() > 1) {
        println("User ${entry.getValue()}
                                 has ${entry.getKey()} documents")
    }
}
```

{% raw %}
<p></p>
{% endraw %}

这段代码显然是坏的，因为你不记得哪一个是：entry.getKey（）一个用户和entry.getValue（） - 一个数字，反之亦然（你甚至注意到这两个是混合在一起的消息？）。更好的版本是将它们分配给变量：

{% raw %}
<p></p>
{% endraw %}

```kotlin
for (entry in counts) {
    val user = entry.getKey()
    val count = entry.getValue()
    if (!user.isBanned() && count > 1) {
        println("User $user has $count documents")
    }
}
```

{% raw %}
<p></p>
{% endraw %}

这更好，但仍然太冗长。这个怎么样：

{% raw %}
<p></p>
{% endraw %}

```kotlin
for ((user, count) in counts) {
    if (!user.isBanned() && count > 1) {
        println("User $user has $count documents")
    }
}
```

{% raw %}
<p></p>
{% endraw %}

看起来像我们想要的，但是**我们该怎么做？**
## 配对对象

要迭代一些东西，我们必须提供一个iterator（）函数。由于地图没有一个，它将是一个扩展功能。应该怎么回事？一个选项将是对（例如Tuple2的对象）的迭代器。明显的缺点是需要为地图中的每个条目**创建一个新对象**。 **我们可以做得更好吗？**
## Kotlin的多重声明

Kotlin M3引入了一个我们称之为**多声明**的新概念。你可以写这样的东西：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val (a, b) = aAndB
println(a)
println(b)
```

{% raw %}
<p></p>
{% endraw %}

多声明一次创建多个变量。它被编译为以下代码：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val a = aAndB.component1()
val b = aAndB.component2()
```

{% raw %}
<p></p>
{% endraw %}

component1（）和component2（）函数是Kotlin广泛使用的<em>约定原理的另一个例子（例如+和*，for-loops等运算符）。只要可以调用所需数量的组件函数，任何内容都可以在多分配的右侧。而且，当然可以有component3（）和component4（）等等。
同样的事情在循环中起作用：当你说

{% raw %}
<p></p>
{% endraw %}

```kotlin
for ((a, b) in collection) { ... }
```

{% raw %}
<p></p>
{% endraw %}

变量a和b获取由集合元素调用的component1（）和component2（）返回的值。不用说，**这些功能可以是扩展名**。
**注意**：即将到来的Kotlin M3将提供多种声明，目前您可以使用我们的夜间版本来尝试。
## 回到地图

现在，让我们回到地图的例子。现在很容易：我们可以简单地为Map.Entry提供组件功能，上面的例子将会起作用。

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun <K, V> Map.Entry<K, V>.component1() = getKey()
fun <K, V> Map.Entry<K, V>.component2() = getValue()
```

{% raw %}
<p></p>
{% endraw %}

## 数据类

我们经常创建除了保存数据之外什么都不做的类。如你所知，Kotlin通过提供可以声明属性的主要构造函数使它们尽可能短：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class User(val name: String, val age: Int)
```

{% raw %}
<p></p>
{% endraw %}

但是经常我们需要一些更多的代码：一个明显的equals（）/ hashCode（）对，一个toString（）和现在的组件函数。我们有很多支持的请求，现在Kotlin编译器支持的**数据**注释：

{% raw %}
<p></p>
{% endraw %}

```kotlin
data class User(val name: String, val age: Int)
```

{% raw %}
<p></p>
{% endraw %}

此类获取**组件函数**，在主构造函数中声明的每个属性一个**自动生成**（这已经实现），对于数据通用的所有其他好处都是相同的： strong> toString（）**，**equals（）**和**hashCode（）**（即将在那里）。
## 多个返回值

如何从函数返回多个东西？有些人认为**元组**提供了一个很好的方法，但是与Map.Entry相同的问题：tuple组件没有名称，所以调用站点被空白“_1”和“_2”或非常相似的东西。因此，使用数据类来处理多个回报似乎更好：

{% raw %}
<p></p>
{% endraw %}

```kotlin
data class TwoThings(val id: String, val number: Int)
 
fun returnTwoThings(): TwoThings {
    // Complex computation...
    return TwoThings(strId, number)
}
 
fun test() {
    val data = returnTwoThings()
    println("id = ${data.id}, number = ${data.number}")
 
    // or
 
    val (id, num) = returnTwoThings()
    println("id = ${id}, number = ${num}")
}
```

{% raw %}
<p></p>
{% endraw %}

无论我们是否决定使用多声明，名称都不会丢失：它们在数据类中声明。
有些人抱怨需要提供返回的实体的名称，但在许多情况下，很高兴认识到这件事情</em>** ...
## 结论

我们讨论了在**Kotlin M3**中引入的新功能。 **多声明**允许短时间绑定多个名称，例如，以不错的方式遍历地图条目，而不需要创建不需要的对象。 **数据类**可以使用简单处理数据但附带所有必要功能的类的一行定义。
**您的反馈非常受欢迎**，像往常一样。更多关于即将到来的M3和我们未来计划中出现的新内容，敬请期待下周。
