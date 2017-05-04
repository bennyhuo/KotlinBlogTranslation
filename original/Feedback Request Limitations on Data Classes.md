---
title: "Feedback Request: Limitations on Data Classes"
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

While M13 is approaching, we are planning a little ahead. This is a request for feedback on some future changes in Kotlin.
We want to deliver Kotlin 1.0 rather sooner than later, and this makes us postpone some design choices we don’t have enough confidence about. Today let’s discuss *data classes*.<span id="more-2472"></span>
## Introduction

The concept of [data classes](http://kotlinlang.org/docs/reference/data-classes.html) has proven very useful when it comes to simply storing data. All you need is say:

{% raw %}
<p></p>
{% endraw %}

```kotlin
data class Foo(val a: A, val b: B)
```

{% raw %}
<p></p>
{% endraw %}

and you get `equals()/hashCode()`, `toString()`, `copy()` and component functions for free.
The most common use case works like a charm, but interaction of data classes with other language features may lead to surprising results.
## Issues

For example, what if I want to extend a data class? What if the derived class is also a data class?

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

Now, how does `equals()` or `copy()` work in `Derived`? All the well-known issues arise at once:

* should an instance of Base be equal to an instance of Derived if they have the same values for a and b?
* what about transitivity of equals()?
* what if I copy an instance of Derived through a reference of type Base?

And what about component functions that enable [multi-declarations](http://kotlinlang.org/docs/reference/multi-declarations.html) ? It seems more or less logical that `c` simply becomes the third component in `Derived` **in this basic case**:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val (a, b, c) = Derived(...)
```

{% raw %}
<p></p>
{% endraw %}

But nothing prevents us from writing something like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
data class Derived(b: B, a: A, val c: C) : Base(a, b)
```

{% raw %}
<p></p>
{% endraw %}

Note that the parameter order is reversed: first `b`, than `a`. Now it’s not that clear any more. And it may get worse:

{% raw %}
<p></p>
{% endraw %}

```kotlin
data class Derived(val c: C, b: B, a: A) : Base(a, b)
```

{% raw %}
<p></p>
{% endraw %}

Now `c` comes first, and the inherited `component1(): A` is simply a conflict, it is not an override, but such an overload is not legal either.
And these are only some examples, there’re many more issues, big and small.
## Our strategy

On the one hand, we are not sure whether there is an elegant design for inheritance involving data classes. We have some sketches, but none of them looks promising enough.
On the other hand, we want to finalize the language design now, to be able to ship 1.0.
So, we decided to restrict data classes quite a bit to rule out all the problematic cases in 1.0, so that we can get back to them later and maybe lift some of the restrictions.
## Proposed restrictions

We are going to do the following:

* allow to inherit data classes from interfaces
* forbid to inherit data classes from other classes
* forbid open data classes (i.e. other classes can not extend data classes)
* forbid inner data classes (not clear how equals()/hashCode() should treat the outer reference)
* allow local data classes (the closure is not structured, so it’s OK for equals()/hashCode() to ignore it)
* require val/var on all primary constructor parameters for data classes
* require at least one primary constructor parameter for data classes
* allow private primary constructor parameters for data classes
* var’s are as good as val’s in all respects (they participate in equals()/hashCode() etc)
* forbid varargs in primary constructor parameters for data classes

Again, some of the restrictions in this list may be lifted later, but for now we don’t want to deal with these cases.
## Appendix. Comparing arrays

It’s a long-standing well-known issue on the JVM: `equals()` works differently for arrays and collections. Collections are compared structurally, while arrays are not, `equals()` for them simply resorts to referential equality: `this === other`.
Currently, Kotlin data classes are ill-behaved with respect to this issue:

* if you declare a component to be an array, it will be compared structurally,
* but if it is a multidimensional array (array of arrays), the subarrays will be compared referentially (through equals() on arrays),
* and if the declared type of a component is Any or T, but at runtime it happens to be an array, equals() will be called too.

This behavior is inconsistent, and we decided to fix it following the path of least resistance:

* arrays are always compared using equals(), as all other objects

So, whenever you say

* arr1 == arr2
* arr in setOfArrays
* DataClass(arr1) == DataClass(arr2)
* or anything else along these lines,

you get the arrays compared through `equals()`, i.e. referentially.
We’d love to fix the inconsistency with collections, but the only sane way of fixing it seems to be fixing it in Java first, which is beyond anybody’s power, AFAIK <img alt=":)" class="wp-smiley" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1" style="height: 1em; max-height: 1em;"/>
## Call for feedback

Please share your opinion on the proposed changes. We are more or less sure about arrays, and pretty confident about limitations on data classes too, but it’s always a good idea to double-check with a wider range of use cases.
Thanks for your help!
