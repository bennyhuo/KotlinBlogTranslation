---
title: "Upcoming Change: More Null-safety for Java"
date: 2015-04-10 15:34:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/04/upcoming-change-more-null-safety-for-java/
translator:
translator_url:
---

Our battle for combining null-safety and Java interop has been a long one already:

* we started off treating all Java reference types as nullable, and it was too inconvenient;
* then we employed external annotations to specify nullability, created KAnnotator, but the whole thing was too fragile when versioning was concerned, and sometimes the users couldn’t do what they needed to (especially when it came to inheritance);
* in M9 we discarded the annotations (for the time being), and introduced platform types, now anything could be done, but we lost (some) type-safety;
* in M11 we started bringing the useful aspects of annotations back by issuing warnings where Java nullability constraints were violated.

Now, we are planning to make one more step and use annotations in combination with platform types to **bring back as much type-safety as possible**.<span id="more-2090"></span>
## Overview

The details are described in [this spec-document](https://github.com/JetBrains/kotlin/blob/types-from-annotations/spec-docs/flexible-java-types.md#enhancing-signatures-with-annotated-declarations) , but the overall idea is as follows: whenever we encounter nullability annotations in Java, *and they do not conflict with anything* around them (like overridden declarations in supertypes), we use precise types. For example:

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Java
 
class Foo {
    @Nullable String bar(@NotNull String baz) {...}
}
 
// Kotlin
 
foo.bar(nullableString ?: "default")?.length()
```

{% raw %}
<p></p>
{% endraw %}

In the last line the compiler requires us to deal with both the argument of `bar()` requiring a non-null value (so we use “elvis” to provide a default) and the result being nullable (we use a safe call to guard from NPE). If we neglected any of those, it would have been a compilation error.
## Conflicts

It may seem that we are just bringing back what we dropped before (and were so happy about it), but this is not so. The details are rather involved, but in a nutshell, a huge difference with what we had before platform types were introduced is that you could not have a type that admitted both an `ArrayList&lt;String&gt;` and `ArrayList&lt;String?&gt;`, and it lead to painful workarounds being necessary when we needed to feed something we got from Java back into another Java method. Yes, if it wasn’t for generics, almost nothing would have changed, but generics always make a compiler writer’s world brighter <img alt=":)" class="wp-smiley" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1" style="height: 1em; max-height: 1em;"/>
Another thing that changed is how we treat conflicts in overriding signatures:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Super {
    String foo(String bar) { ... }
}
 
class Sub extends Super {
    @Override
    String foo(@NotNull String bar) { ... }
}
```

{% raw %}
<p></p>
{% endraw %}

When we treated unannotated Java types as nullable, in the example above Kotlin could only see two unrelated methods: `foo(String?)` and `foo(String)` have incompatible type signatures.
There are many more possible sources of conflicts, most of them are actually inconsistencies in the annotations, but users keep having them in their code, and we have to be able to work with it. So, whenever we encounter a conflict now, we simply stick to the platform types. Warnings introduced in M11 are kept for such cases, so that that code does not break in weird ways, but we do everything in our power to keep you informed on the possible runtime issues.
Note that whatever stays unannotated in Java still bears platform types, including all generic type arguments in the pre-Java 8 code.
## Which Annotations?

The actual set of annotations supported by the Kotlin compiler will likely be configurable, but in any case we are going to support the following ones:

* org.jetbrains.annotation that we always used
* android.support.annotation
* javax.annotation (and the ones from FindBugs)
* javax.validation.constraints
* lombok
* org.eclipse.jdt.annotation
* org.checkerframework.checker.nullness.qual

## Conclusion

We hope that the battle for nulls in Java will be over after M12. Stay tuned, though <img alt=":)" class="wp-smiley" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1" style="height: 1em; max-height: 1em;"/>
