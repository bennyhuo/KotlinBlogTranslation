---
title: "[译]Kotlin 1.1 is also for Android Developers"
date: 2017-04-05 16:13:00
author: Roman Belov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/04/kotlin-1-1-is-also-for-android-developers/
---

我们对Kotlin 1.1的发布感到非常兴奋。此版本包含的新功能对Java开发人员非常有用，并将JVM开发引向了一个新的可能性世界。
但这些新功能，如 [协程](https://github.com/Kotlin/kotlin-coroutines/blob/master/kotlin-coroutines-informal.md) ， 要么 [键入别名](https://github.com/Kotlin/KEEP/blob/master/proposals/type-aliases.md)  （举几个例子），看起来像Android的开发人员的科幻小说。
我们仍然停留在古老的Java 6中，几乎没有什么改进，迫使我们以其他平台中大多数开发人员几乎被遗忘的方式开发。
所以一个理所当然的问题是：Kotlin团队能够保持与Java 6的兼容性，同时使所有这些新功能还活着吗？答案是：当然！
<strong>所有新的东西仍然可用于Java 6，作为Android开发人员的扩展。</ strong>今天，我想向您展示一些，并且如何在开发过程中使您的人生更加容易Android应用程式

{% raw %}
<p><span id="more-4826"></span></p>
{% endraw %}

# 键入别名：您可以使您的监听器更易读

当然，类别别名有很多不同的应用。但是，我想到的第一个就是让听众更加可读，同时保持使用lambdas的能力。
如果你还没听说过 [键入别名](https://github.com/Kotlin/KEEP/issues/4)  以前，它们基本上是将复杂类型重命名为更可读的类型。
例如，你可以有一个<code> RecyclerViewadapter </ code>，它会收到一个监听器。您可能知道，<code> RecyclerView </ code>没有一个标准的方式来处理项目点击，就像<code> ListView </ code>一样，所以我们必须自己出来。
让我们想象一下，我们希望有一个可以访问视图的监听器。我们的适配器类可能如下所示：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class MyAdapter(val items: List<Item>, val listener: (View) -> Unit) : RecyclerView.Adapter<MyAdapter.ViewHolder>() {
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

而您的<code> ViewHolder </ code>可能需要接收该监听器，才能将其分配给视图的点击监听器：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
    fun bind(item: Item, listener: (View) -> Unit) {
        itemView.setOnClickListener(listener)
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

这不是一个非常复杂的情况，但是正如你所看到的，我们需要重复一下这个lambda定义，这种定义在上下文之中可能会导致读取困难。
但是，我们可以创建一个代表点击监听器的类型别名：<br/>
<code> typealias ClickListener =（View） - ＆gt;单位</ code> <br/>

然后在我们需要的那个听众的每一个地方使用它：<br/>
<code> class MyAdapter（val items：List＆lt; Item＆gt，val listener：ClickListener）</ code> <br/>

或者
<code> fun bind（item：Item，listener：ClickListener）{...} </ code>
# 数据类现在更强大了

数据类是伟大的，因为避免了大量的样板。但是他们缺乏一些权力，这使得它们在某些情况下不可用。
Kotlin 1.1中的新内容之一是继承：数据类现在可以继承其他类

这允许数据类成为密封类的一部分：

{% raw %}
<p></p>
{% endraw %}

```kotlin
sealed class UiOp {
    object Show : UiOp()
    object Hide : UiOp()
    data class Translate(val axis: Axis, val amount: Int): UiOp()
}
 
```

{% raw %}
<p></p>
{% endraw %}

而现在，<strong>作为密封类可以从父类</ strong>中定义，这也可以是这样的：

{% raw %}
<p></p>
{% endraw %}

```kotlin
sealed class UiOp
object Show : UiOp()
object Hide : UiOp()
data class Translate(val axis: Axis, val amount: Int)
 
```

{% raw %}
<p></p>
{% endraw %}

# 羔羊内部破坏

自从第一个版本以来，数据类可以被解构，因为它们生成的<code> componentX（）</ code>方法。您可以将数据类的内容分配成若干变量，如下所示：

{% raw %}
<p></p>
{% endraw %}

```kotlin
data class Item(val text: String, val url: String)
 
val (text, url) = item
 
```

{% raw %}
<p></p>
{% endraw %}

但是，一个非常强大的功能缺失：能够在lambdas上做到这一点。但是等待结束了！你现在可以这样做：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun bind(item: Item) = item.let { (text, url) ->
    textView.text = text
    imageView.loadUrl(url)
}
 
```

{% raw %}
<p></p>
{% endraw %}

这对地图中的对或键/值集也是非常有用的。
# 本地委托属性

已授权的属性已被证明是非常有用的，为我们的课程中的属性提供额外的能力。
例如，最有用的一个是<strong>懒惰委托</ strong>，它会延迟分配的执行，直到该属性第一次使用为止。
但懒惰对变量也是非常有帮助的，而Kotlin缺乏这个功能。
现在，通过本地委托的属性，我们可以做到：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun testLocalDelegation() {
    val database by lazy { createDatabase() }
    val cache by lazy { createMemoryCache() }
 
    if (mustUseDatabase()) {
        database.use { ... }
    } else {
        cache.use { ... }
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

虽然这个例子可以在没有使用懒惰代理的情况下解决，但它有助于理解这个概念。
我们有几个重物可能会被使用，也可能不会被使用。通过使用懒惰，我们可以延迟实例化，直到我们确定我们要使用它。
使用第一次，大括号内的代码被执行，并且它将被缓存，以备稍后再次使用。
# 忘记在lambdas上声明未使用的变量了

在lambdas中声明变量的参数是非常常见的，最终在任何地方都没有使用。
这是因为在Kotlin 1.0中，我们没有办法丢弃未使用的参数。
例如，在本文中，我介绍了如何使用委托更新RecyclerView适配器，最后我使用了以下代码：

{% raw %}
<p></p>
{% endraw %}

```kotlin
var items: List<Content> by Delegates.observable(emptyList()) {
    prop, old, new ->
    autoNotify(old, new) { o, n -> o.id == n.id }
}
 
```

{% raw %}
<p></p>
{% endraw %}

道具从未被使用过，但到现在为止，这是有必要的。现在可以使用下划线来避免这种情况：

{% raw %}
<p></p>
{% endraw %}

```kotlin
var items: List<Content> by Delegates.observable(emptyList()) {
    _, old, new ->
    autoNotify(old, new) { o, n -> o.id == n.id }
}
 
```

{% raw %}
<p></p>
{% endraw %}

但是，如果您没有使用任何一种，则更糟糕。如果lambda有多个参数，那么即使不使用lambda，也需要写入所有参数。
现在我们可以忽略它们：

{% raw %}
<p></p>
{% endraw %}

```kotlin
var items: List<Item> by Delegates.observable(emptyList()) {
    _, _, _ ->
    notifyDataSetChanged()
}
 
```

{% raw %}
<p></p>
{% endraw %}

不仅您定义较少的变量，而且代码变得更易读。现在你不需要检测这些参数是否被使用。很清楚
# 协调程序

科图林是Kotlin1.1中最令人兴奋的消息。尽管此版本最终成为“实验性”，但它们功能齐全，您可以在今天开始在项目中使用它们</ strong>。
协调程序将让您以同步方式编写异步代码，允许在某些时候暂停执行，并等待结果，同时编写顺序代码。
您可能已经知道Kotlin中的协同程序的一件事是，它们不是一个图书馆或具体的实现，而是一种允许通过它创建图书馆的语言功能</ strong>。
因此，尽管结果代码看起来可能相似，但重要的是要知道创建这些辅助线程并返回主线程的“齿轮”是什么，这在Android中非常重要。
幸运的是，Kotlin社区移动速度很快，已经有几个图书馆将协同程序的功能带入Android </ strong>。这里有一些例子：
你可能想看看的第一个是Jetbrains提供的官方的：

* kotlinx-coroutines-android，它提供了可以在Android上使用的协同程序实现。
* 安科，在其最新的beta版中，它包括协调支持许多框架听众。

但是还有许多其他第三方库实现自己的协同版本：

* AsyncAwait-Android由Niek Haarman
* Async /等待Metalab
* 如果您只想改装支援，您可以通过Andrey Mischenko来检查kotlin-coctines-改装

我敦促你不仅要使用它们，还要检查它们是如何实现的。这是开源的魔力。
# Android Devs的其他一些很酷的东西

这个版本还有更多的改进，但是我想强调一些更侧重于Android开发。
第一个是现在，您可以通过使用以下命令来启用Jack编译器的支持：<code> jackOptions {true} </ code>。 Google已宣布他们不赞成Jack工具链，但如果您将其用于Java 8，这可能对您有帮助，直到Android Studio 2.4的最终版本被发布。
另外，<strong>一个新的意图将使用</ strong> <code> @JvmOverloads </ code> <strong>来实现自定义视图</ strong>的构造函数，该字体上允许实现自定义视图构造函数通过使用一个构造函数和参数的默认值，一行（好，一个真正的长行）

{% raw %}
<p></p>
{% endraw %}

```kotlin
class CustomView @JvmOverloads constructor(
        context: Context, attrs: AttributeSet? = null, defStyleAttr: Int = 0
) : View(context, attrs, defStyleAttr) {
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

# 结论

Kotlin 1.1带来了一大批新的功能，使我们为什么还要使用Java更加不可避免的问题。
Kotlin为Android开发人员带来的强大功能是无关紧要的，您可以从今天开始在Kotlin编写您的Android应用程序。
如果您想开发应用程序时从头开始学习Kotlin for Android，那么您可能会发现<a href="https://antonioleiva.com/kotlin-android-developers-book/"> Kotlin for Android Developers < / a>您感兴趣的书籍</ strong>。
