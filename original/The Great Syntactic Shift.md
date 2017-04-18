---
title: "The Great Syntactic Shift"
date: 2012-01-04 09:38:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2012/01/the-great-syntactic-shift/
---

As the first public preview of Kotlin is approaching (it will be announced on Jan 10th, 2012, which is <strong>less than a week</strong> from now!), we are putting some things in order…
In particular, we have reviewed syntactic forms available in the language, and decided to change a few. These changes are incompatible with the old syntax, and we have migrated all our test data, and will update the  [publicly available documentation](http://jetbrains.com/kotlin)  soon.
I would like to point out that this is not the last change of this sort. Kotlin is not released yet, and until it is we are constantly gathering feedback and sometimes find out that something needs to be changed. Consequently, there are no backward-compatibility guarantees before the 1.0. We realize how important backward compatibility is, but we’d better be backward compatible to a really good design created according to the needs of real people.
Here’s an overview of the changes we’ve made.<br/>
<span id="more-291"></span><br/>
<strong>The Namespace is dead. Long live the Package.</strong>
The concept of <em>namespaces</em> evolved into something so close to Java packages, that we decided to rename it. The <strong>namespace</strong> keyword is replaced by <strong>package</strong> keyword. Additionally, <em>namespace blocks</em> are no longer supported.
<strong>The Arrow loses weight</strong>
An arrow is used in function literals and <strong>when</strong> expressions. Some languages use a “fat arrow” (=>) and some use a “thin arrow” (->). Initially, we used the fat one, but is has some unfortunate interactions with comparisons, like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
  val higherThanY  = {x => y <= x}
```

{% raw %}
<p></p>
{% endraw %}

So we decided to switch to a thin arrow:

{% raw %}
<p></p>
{% endraw %}

```kotlin
  val higherThanY  = {x -> y <= x}
```

{% raw %}
<p></p>
{% endraw %}

<strong>More readable function types</strong>
In the old syntax we wrote function types as follows:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val f : fun(Int) : String
```

{% raw %}
<p></p>
{% endraw %}

which is very close to Kotlin’s function declaration syntax, and seems perfectly logical. Unfortunately, as this feature starts interacting with others, things get a lot worse:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun max(col : Collection<Int>, compare : fun(Int, Int) : Int) : Int
```

{% raw %}
<p></p>
{% endraw %}

Have you got lost in colons? Yes, me too…
So we decided to change the function type syntax to the following:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun max(col : Collection<Int>, compare : (Int, Int) -> Int) : Int
```

{% raw %}
<p></p>
{% endraw %}

<strong>And a little more</strong>
Additionally, we introduced optional parentheses in types, changed the tuple syntax to be distinguishable from parenthesized expression lists and made some minor (backward compatible) changes. All this will be reflected in the docs soon. As usual, your feedback is very welcome.
Stay tuned, and don’t miss the announcement next Tuesday!
