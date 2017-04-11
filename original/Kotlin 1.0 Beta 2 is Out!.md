---
title: Kotlin 1.0 Beta 2 is Out!
date: 2015-11-16 21:01:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/11/kotlin-1-0-beta-2-is-out/
---

The first update to our Beta is here! We are stabilizing, so it’s mostly bug-fixing and changes to the standard library.
## Language changes

We are now enforcing single-instantiation inheritance constraint on type parameters: the same T can not have both List<Int> and List<String> as its upper bounds. This has been always forbidden for classes, now the same check applies for type parameters.
Diagnostics were improved for the cases when a smart cast is impossible:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class C {
    var x: String? = ""
    fun foo(): String {
        if (x != null) return x // ERROR: smart cast to String is impossible,
                                // because 'x' is a member variable
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

Also, the compiler is now smart enough to warn us when a value is always null at a particular point:

{% raw %}
<p></p>
{% endraw %}

```kotlin
    var x: Foo? = ...
    if (x != null) return
    x?.bar() // WARNING: bar() will never run, because x is always null here
 
```

{% raw %}
<p></p>
{% endraw %}

## Library changes

We cleaning up the APIs of the standard library. Most visible changes this time concern ranges. We intended the common use cases such as “if (x in 1..10)” or “for (i in 1..10)” to remain without changes, but did some renaming and hierarchy rearrangements under the hoods:

* Double and Float progressions are dropped
* Byte and Short progressions are deprecated, the .. operator for bytes and shorts now returns IntRange
* Range<T> renamed to ClosedRange<T> and its end property renamed to endInclusive
* Progression<T> is deprecated in favor of concrete progression implementations instead: IntProgression, LongProrgession, CharProgression
* start and end properties in progressions are renamed to first and last

Then, utility extensions for strings were generalized to work with CharSequence where possible.
The filterIsInstance extension now requires an explicit specification of its type parameter:

{% raw %}
<p></p>
{% endraw %}

```kotlin
foo(list.filterIsInstance()) // error: what is the type the checks are done for?!
foo(list.filterIsInstance<Bar>()) // OK: we are checking for Bar
 
```

{% raw %}
<p></p>
{% endraw %}

NOTE: To reduce the size of the runtime library (which is especially important for Android applications), we removed the kotlin.dom and kotlin.browser packages from the standard library. They are now available as a separate library, kotlinx.dom. If you’re using any of these packages in your project, please add the new library as a dependency and update the import statements in your code (change kotlin.dom and kotlin.browser to kotlinx.dom and kotlinx.browser). Otherwise, the API of the library has not changed.
Other changes:

* Added

in-place reversing and sorting for MutableLists and Arrays
naturalOrder and reverseOrder comparators
mapNotNull, mapIndexedNotNull, filterIndexed
String.toByte()
* in-place reversing and sorting for MutableLists and Arrays
* naturalOrder and reverseOrder comparators
* mapNotNull, mapIndexedNotNull, filterIndexed
* String.toByte()
* Deprecated (run Code Cleanup to migrate your code)

Function.toGenerator
toLinkedList
* Function.toGenerator
* toLinkedList
* Dropped

join, merge
Delegates.lazy
FileTreeWalk.filter, File.recurse, BufferedReader.lines and lineIterator
assert, check and require with non-lazy message argument
* join, merge
* Delegates.lazy
* FileTreeWalk.filter, File.recurse, BufferedReader.lines and lineIterator
* assert, check and require with non-lazy message argument

## Dokka

Dokka, the new documentation generation tool for Kotlin projects, has finally reached a full release. Dokka supports mixed-language projects and understands KDoc comments in Kotlin code and JavaDoc comments in Java code. Dokka has plugins for Gradle, Maven and Ant, so you can easily integrate it with the build system of your project. Download Dokka and find more information on the Dokka project site.
## IDE changes


* Completion now works for Java static members and members of objects. Just press Ctrl+Space for the second time:

