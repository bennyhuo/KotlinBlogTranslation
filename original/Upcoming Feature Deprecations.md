---
title: "Upcoming Feature Deprecations"
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

As we are finalizing the language design, many things have to be cleaned up, and among these are features that were initially designed and (often partly) implemented, but turned out not to be worth the trouble supporting them.
In the upcoming M12 milestone, we are going to deprecate such features, so that you could migrate your code before they are removed completely.<span id="more-1996"></span>
## Required Classes

Some of you might have heard of this feature: traits in Kotlin can “extend” classes (we actually use the term “require”).
Technically it means that when a class extends such a trait, it must (directly or indirectly) extend the required class as well. This feature has very few use cases, so we are deprecating it.
## Captured Type Parameters

When a generic class `Outer` has an <strong>inner</strong> class `Inner`, Java allows us to use generic parameters of `Outer` inside `Inner`:

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

Although very logical, this feature also has rather few use cases, and current implementation we have in Kotlin requires a lot of work before it is production quality. So, we are going to forbid this, and maybe implement it in later releases of Kotlin.
If you happened to use this (which is very unlikely), your workaround is rather straightforward:

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

## Covariant Specialization for Supertypes

I’m really skeptical about anyone even knowing that this feature exists <img alt=":)" class="wp-smiley" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1" style="height: 1em; max-height: 1em;"/>
The current compiler allows a class/trait to have more than one (indirect) supertype of the same class, if one of them is a subtype of the other:

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

Note that `List` is co-variant in Kotlin.
Although, again, logical, this has almost no use-cases, to our knowledge, but supporting this involves a lot of compiler magic and breaks Java interop right and left, so we are going to drop this.
## More Deprecations Coming

We’ll share some more plans of this sort soon. And will keep you updated on the features we are implementing now.
