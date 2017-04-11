---
title: Kotlin 1.1 is also for Android Developers
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

We’re all really excited about the release of Kotlin 1.1. The new features this release includes are extremely useful for Java developers and lead JVM development to a new world of possibilities.
But these new features, such as coroutines, or type aliases (to put a couple of examples), look like science fiction for Android developers.
We’re still stuck in an ancient Java 6 with little improvements that forces us to develop in ways almost forgotten for most developers in any other platforms.
So a sane question would be: has the Kotlin team been able to keep compatibility to Java 6 while bringing all these new features alive? And the answer is: of course!
All the new stuff is still available for Java 6 and, as an extension, for Android developers. And today, I want to show you some of them, and how they can make your life even easier when developing Android Apps.

{% raw %}
<p><span id="more-4826"></span></p>
{% endraw %}

# Type aliases: You can make your listener much more readable

Of course, type aliases have a lot of different applications. But the first that came to my mind was the ability to make listeners more readable while keeping the use of lambdas.
If you haven’t heard about type aliases before, they’re basically a way to rename complex types into more readable ones.
For instance, you could have an RecyclerViewadapter which will receive a listener. As you may know, RecyclerView doesn’t have a standard way to deal with item clicks, just as ListView had, so we have to come out with our own.
Let’s imagine we want a listener that has access to the view. Our adapter class could look like this:

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

And your ViewHolder would probably need to receive that listener too, to assign it to the click listener of the view:

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

This is not a very complicated case, but as you can see, we need to repeat that lambda definition which, out of context, could lead to a difficult read.
But we can create a type alias that represents a click listener:
typealias ClickListener = (View) -> Unit
And then use it in every place we need that listener:
class MyAdapter(val items: List<Item>, val listener: ClickListener)
or
fun bind(item: Item, listener: ClickListener) { ... }
# Data classes are now more powerful

Data classes are great because the avoid a huge amount of boilerplate. But they were lacking some powers, which made them unusable in some cases.
One of the new inclusions in Kotlin 1.1 is inheritance: data classes can now inherit other classes.
This allows data classes to be part of sealed classes:

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

And now, as sealed classes can be defined out of the parent class, this could also be like this:

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

# Destructuring inside lambdas

Data classes could be destructured since the first version thanks to the componentX() methods they generate. You could assign the content of a data class into several variables like this:

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

But a really powerful feature was missing: being able to do this on lambdas. But the wait is over! You could now do something like this:

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

This is also really helpful for pairs or key/value sets in a map, for instance.
# Local delegated properties

Delegated properties have proven to be really useful to give extra abilities to the properties in our classes.
For instance, one of the most useful ones is the lazy delegation, which defers the execution of the assignment until the property is used for the first time.
But lazy would also be really helpful too on variables, and Kotlin was lacking this feature.
Now, with local delegated properties, we can do it:

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

Though this example could be resolved without using lazy delegation, it helps understand the concept.
We have a couple of heavy objects that may or may not be used. By using lazy, we can delay the instantiation until we are sure we are going to use it.
The first time is used, the code inside the braces is executed, and it will be cached in case it’s used again later.
# Forget about declaring unused variables on lambdas anymore

It was very common having to declare variables for arguments in lambdas that in the end weren’t used anywhere.
This was because in Kotlin 1.0 we didn’t have a way to discard unused parameters.
As an example, in this article where I explained how to update a RecyclerView adapter using delegation, I ended up with this code:

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

The prop was never used but, until now, it was necessary to declare it. You can avoid it now by using an underscore:

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

But it was even worse the case where you didn’t use any of them. If you have more than one arguments for a lambda, you need to write them all even though you don’t use them.
Now we can ignore them:

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

It’s not only that you are defining less variables, but also that the code becomes more readable. Now you don’t need to detect whether those arguments are used or not. It’s crystal clear.
# Coroutines

Coroutines are the most exciting news in Kotlin 1.1. Though finally left as “experimental” in this release, they are fully functional and you can start using them on your projects as of today.
Coroutines will let you write asynchronous code in a synchronous way, allowing to suspend the execution at some point and wait for a result, all while writing sequential code.
One thing you may already know about coroutines in Kotlin is that they are not a library or a specific implementation, but a language feature that allows creating libraries over it.
So, though the resulting code may look similar, it’s important to know what’s the “gear” that is creating those secondary threads and returning to the main thread, which is quite important in Android.
Luckily, the Kotlin community moves fast and there are already several libraries that bring the power of coroutines to Android. Here you have some examples:
The first ones you may want to take a look are the official ones provided by Jetbrains:

* kotlinx-coroutines-android, which provides a coroutines implementation ready to be used on Android.
* Anko, which in its latest beta it’s including coroutines support to many framework listeners.

But there are also many other third-party libraries implementing their own versions of the coroutines:

* AsyncAwait-Android by Niek Haarman
* Async / Await by Metalab
* If you just want Retrofit support, you can check kotlin-coroutines-retrofit by Andrey Mischenko

I urge you not only to use them, but also to check how they are implemented. That’s the magic of open source.
# Some other cool things for Android Devs

There are many more improvements on this release, but I wanted to highlight some that are more focused to Android development.
The first one of them is that now you can enable the support with the Jack compiler by using: jackOptions { true }. Google has announced they are deprecating Jack toolchain, but if you were using it for Java 8, this may be helpful for you until the final version of Android Studio 2.4 is released.
Also, there’s a new intention that will use @JvmOverloads to implement the constructors of a custom view, which literally allows to implement custom view constructors in one line (well, one really long line) by using one constructor and default values for arguments:

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

# Conclusion

Kotlin 1.1 has brought a good bunch of new awesome features that make the question of why we still use Java even more inevitable.
The power that Kotlin brings to Android developers is out of question, and you can start writing your Android apps in Kotlin from today.
And if you want to learn Kotlin for Android from scratch while developing an App, you might find Kotlin for Android Developers book of your interest.
