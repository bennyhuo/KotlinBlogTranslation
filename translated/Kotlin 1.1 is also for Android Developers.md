---
title: "[译]Kotlin 1.1 也适用于 Android 开发者"
date: 2017-04-05 16:13:00
author: Roman Belov
tags: [Android, Coroutine, typealias]
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/04/kotlin-1-1-is-also-for-android-developers/
---

Kotlin 1.1的发布令人们感到非常兴奋。此版本包含的新功能对 Java 开发者非常有用，并将 引领 JVM 走向一个充满发展潜力的新世界。

但有些新功能，如 [coroutine](https://github.com/Kotlin/kotlin-coroutines/blob/master/kotlin-coroutines-informal.md) 和 [type alias](https://github.com/Kotlin/KEEP/blob/master/proposals/type-aliases.md)（下文有几个例子）对于 Android 开发者来说就像科幻小说。

我们仍然停留在几乎没有什么改进的古老 Java 6 中，迫使我们以其他平台已经被被遗忘的方式进行开发。

所以一个理所当然的问题是：Kotlin 团队能够保持与 Java 6 的兼容性，同时保留所有这些新功能吗？答案是：当然！

**所有新特性仍然兼容 Java 6 为 Android 开发者所用。** 今天我想向您展示其中的一部分，看看它们是如何使你更容易的开发 Android 应用程式。

<!--more-->

# type alias 使你的 listener 更易读

当然 type alias 有很多不同的应用场景，不过我首先想到的是使用 lambda 作为 listener 的类型时会使代码更易读。

如果没接触过 [type alias](https://github.com/Kotlin/KEEP/issues/4) 的话，可以简单的理解为给复杂的类型名起个别名，使其更为可读。

例如你有个接收 listener 的 `RecyclerViewAdapter`。`RecyclerView` 没有 `ListView` 那样 标准的方式来处理条目点击事件，必须由开发者自己实现。

假如我们希望有一个可以访问 view 的 listener，那 adapter 可能如下所示：

```kotlin
class MyAdapter(val items: List<Item>, val listener: (View) -> Unit) : RecyclerView.Adapter<MyAdapter.ViewHolder>() {
    ...
}
```

而你的 `ViewHolder` 可能需要接收该 listener，才能将其分配给 view：

```kotlin
class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
    fun bind(item: Item, listener: (View) -> Unit) {
        itemView.setOnClickListener(listener)
    }
}
```

这不是一个复杂的例子，但是正如你所看到的我们需要重复定义这个 lambda ，会导致这段代码不太好阅读。

但是现在我们可以创建一个代表点击 listener 的 type alias：
`typealias ClickListener = (View) -> Unit`
然后在需要的每一个地方使用它：
`class MyAdapter(val items: List<Item>, val listener: ClickListener)`
或者
`fun bind(item: Item, listener: ClickListener) { ... }`

# data class 更强大了

data class 可以为我们避免大量的样板代码，但是它不能继承其它类所以某些情况下不可用。

Kotlin 1.1 取消了这个限制，例如 data class 可以定义为 sealed class 的子类了：

```kotlin
sealed class UiOp {
    object Show : UiOp()
    object Hide : UiOp()
    data class Translate(val axis: Axis, val amount: Int): UiOp()
}
```

同时 **sealed class 可以在父类之外定义**，就像这样的：

```kotlin
sealed class UiOp
object Show : UiOp()
object Hide : UiOp()
data class Translate(val axis: Axis, val amount: Int) : UiOp()
```

# 在 lambda 中使用 destructuring

从 Kotlin 最早的版本开始 data class 就能够使用 destructuring declarations 了，因为它会自动生成 `componentX()` 方法，借助这些方法可以将 data class 对象拆分成若干变量，如下所示：

```kotlin
data class Item(val text: String, val url: String)
 
val (text, url) = item
```

可是在 Kotlin 1.1 之前你并不能在 lambda 上这么做。不过等待结束了！现在可以这么写：

```kotlin
fun bind(item: Item) = item.let { (text, url) ->
    textView.text = text
    imageView.loadUrl(url)
}
```

这个改进十分适用于操作 Pair 和 Map 等类型的对象

# 适用与局部变量的 delegated property

delegated property 已被证明是非常有用的，可以为类中的 property 提供附加的能力。

例如最有用的一个是 **lazy property**，它会推迟赋值操作，直到变量第一次使用。

但其实 lazy 对于局部变量来说也是十分有用的，而之前 Kotlin 缺乏这个功能。

现在通过 delegated property，我们可以做到：

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

虽然这个例子可以在没有使用 lazy 的情况下解决，但它有助于理解这个概念。

有一些占用比较多的对象不一定会被使用，可以通过使用 lazy 延迟实例化，直到我们初次使用它。

这时大括号内的代码会被执行，并且将结果缓存下来以备稍后再次使用。

# 再也不用在 lambda 中定义未使用的变量了

在 lambda 中定义了变量但最终没使用情况很常见。

这是因为在 Kotlin 1.0 中没有办法丢弃 lambda 中未使用的参数。

例如使用 delegated property 更新 RecyclerView adapter，我使用了以下代码：

```kotlin
var items: List<Content> by Delegates.observable(emptyList()) {
    prop, old, new ->
    autoNotify(old, new) { o, n -> o.id == n.id }
}
```

prop 变量从未被使用过，这时我们就可以使用下划线来替换它：

```kotlin
var items: List<Content> by Delegates.observable(emptyList()) {
    _, old, new ->
    autoNotify(old, new) { o, n -> o.id == n.id }
}
```

还有种更糟的情况，如果 lambda 有多个参数，即使你一个也不用还是需要写上所有参数。现在我们可以忽略它们了：

```kotlin
var items: List<Item> by Delegates.observable(emptyList()) {
    _, _, _ ->
    notifyDataSetChanged()
}
```

不仅可以定义较少的变量，而且代码还变得更易读了，那些有用的变量一眼就能看到。

# Coroutine

coroutine 是 Kotlin 1.1 中最令人兴奋的特性。尽管在此版本中带着“实验性”的标签，**但 coroutine 功能齐全，你完全可以开始在项目中使用它们**。

coroutine 能让你以同步的方式编写异步代码，允许你在某些时候暂停执行并等待结果，同时写下顺序相连代码。

您可能已经知道在 Kotlin 中 coroutine 并不是指一个库或者具体的实现，**而是一种能力，通过它能够创建具有 coroutine 特性的库**。

因此尽管某些代码看起来可能相似，但重要的是要知道创建这些辅助线程并返回主线程的“齿轮”是什么，这在 Android 中非常重要。

幸运的是 Kotlin 社区的动作很快，已经有几个库引入了 coroutine 方便我们在 Android 上使用。

首先来看看 Jetbrains 官方提供的：

* [kotlinx-coroutines-android](https://github.com/Kotlin/kotlinx.coroutines/tree/master/ui/kotlinx-coroutines-android) 提供了在 Android 上使用 coroutine 的实现。
* [Anko](https://github.com/Kotlin/anko) 在其最新的 beta 版中改写了部分框架引入 coroutine。

还有许多其他第三方库实现了自己的 coroutine 版本：

* [AsyncAwait-Android by Niek Haarman](https://github.com/nhaarman/AsyncAwait-Android)
* [Async / Await by Metalab](https://github.com/metalabdesign/AsyncAwait)
* 如果你在寻找 Retrofit 的 coroutine 版本，那么可以试试 [kotlin-coroutines-retrofit by Andrey Mischenko](https://github.com/gildor/kotlin-coroutines-retrofit)

建议你们使用的时候看看它们是如何实现的，这就是开源的好处。

# 其它对 Android 开发者有用的东西

这个版本还有更多的改进，但是我更想强调一些侧重于 Android 开发的内容。

首先，现在可以通过使用以下配置来启用 Jack 编译器的支持了：`jackOptions {true}`。虽然 Google 已经宣布放弃 Jack 工具链了，但是如果你对 Java 8 有需求那么会有一点用处，然后等到 Android Studio 2.4 的正式版发布就可以彻底弃用 Jack 了。（从 Android Studio 2.4 Preview 4 版本开始支持所有 Java 7 语言特性，部分 Java 8 语言特性）

另外介绍一个小技巧，就是用 `@JvmOverloads` **来实现自定义 View** 的构造函数，在 Kotlin 中借助参数默认值一个构造函数就能满足自定义 View 的多种构造需求（嗯，很长的一个构造函数）

```kotlin
class CustomView @JvmOverloads constructor(
        context: Context, attrs: AttributeSet? = null, defStyleAttr: Int = 0
) : View(context, attrs, defStyleAttr) {
    ...
}
```

# 结论

Kotlin 1.1 带来了大量的新功能，不禁让人产生为什么还要使用 Java 的想法。

Kotlin 为 Android 开发者带来的好处是毋庸置疑的，从现在开始使用 Kotlin 编写你的 Android 应用吧。

如果你想从头开始学习使用 Kotlin 开发 Android 应用，那么你应该会对 [Kotlin for Android Developers](https://antonioleiva.com/kotlin-android-developers-book/) 这本书感兴趣。