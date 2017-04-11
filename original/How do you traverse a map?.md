---
title: How do you traverse a map?
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
---

It’s been a while since I blogged last time on Kotlin M2. Now, the hot summer has passed, and M3 will be out very soon. In this post I describe two small features added in M3 that make our lives easier and will lead to simplification of the language.
## How do you traverse a map?

Assume you have a map like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val counts: Map<User, Int> = database.howManyDocumentsEachUserHas()
```

{% raw %}
<p></p>
{% endraw %}

What do you do to traverse it and handle each entry? One might think of something along these lines:

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

This code is obviously bad, because you don’t remember which one is which: is entry.getKey() a user and entry.getValue() — a number, or vice versa (did you even notice that the two are mixed up in the message?). A better version would be to assign them to variables upfront:

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

This is better, but still too wordy. How about this:

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

Looks like what we want, but how can we do it?
## Pair objects

To iterate through something, we have to supply an iterator() function. As Map doesn’t have one, it will be an extension function. What should it return? One option would be an iterator over pairs (e.g. objects of Tuple2). The obvious downside is that would need to create a new object for every entry in the map. Can we do better?
## Multi-declarations in Kotlin

Kotlin M3 introduces a new concept that we call multi-declarations. You can write things like this:

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

A multi-declaration creates multiple variable at once. It is compiled down to the following code:

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

The component1() and component2() functions are another example of the principle of conventions widely used in Kotlin (e.g. operators like + and *, for-loops etc.). Anything can be on the right-hand side of a multi-assignment, as long as the required number of component functions can be called on it. And, of course, there can be component3() and component4() and so on.
The same thing works in a for-loop: when you say

{% raw %}
<p></p>
{% endraw %}

```kotlin
for ((a, b) in collection) { ... }
```

{% raw %}
<p></p>
{% endraw %}

Variables a and b get the values returned by component1() and component2() called on element of the collection. Goes without saying, these functions can be extensions.
Note: Multi-declarations will be available in the upcoming Kotlin M3, currently you can try them out using our nightly builds.
## Back to maps

Now, let’s come back to the map example. It’s easy now: we can simple provide component functions for Map.Entry, and the example above will work.

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

## Data classes

We frequently create classes that do nothing but hold data. As you know, Kotlin makes them as short as possible by providing primary constructors that can declare properties:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class User(val name: String, val age: Int)
```

{% raw %}
<p></p>
{% endraw %}

But often times we need a little more: an obvious equals()/hashCode() pair, a toString(), and now — component functions. We had quite a few requests for supporting this, and now there is data annotation supported by Kotlin compiler:

{% raw %}
<p></p>
{% endraw %}

```kotlin
data class User(val name: String, val age: Int)
```

{% raw %}
<p></p>
{% endraw %}

This class gets component functions, one for each property declared in the primary constructor, generated automatically (this is already implemented), same for all the other goodies common for data: toString(), equals() and hashCode() (will be there soon).
## Multiple return values

How to return multiple things from a function? Some think that tuples provide a good way of doing this, but the problem there is the same as with Map.Entry: tuple components have no names, so the call site is cluttered with blank “_1” and “_2” or something very similar. So it seems much nicer to handle multiple returns with data classes:

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

No matter whether we decide to use a multi-declaration or not, the names are not lost: they are declared in the data class.
Some people complain about the need to come up with the name for the returned entity, but in many cases it is good to realize what this thing is…
## Conclusion

We discussed new features introduced in Kotlin M3. Multi-declarations allow to bind several names shortly, and, as an example, traverse map entries in a nice way without creating unneeded objects. Data classes enable one-line definitions of classes that simply handle data and yet come with all the necessary functions attached.
Your feedback is very welcome, as usual. For more on the new things to appear in the upcoming M3 and our future plans — stay tuned until next week.
