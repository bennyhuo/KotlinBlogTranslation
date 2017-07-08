---
title: Early access program for Kotlin 1.2 has been started
author: Ilya Gorbunov
date: 2017-06-27 21:45:00
source_url: https://blog.jetbrains.com/kotlin/2017/06/early-access-program-for-kotlin-1-2-has-been-started/
tags: 
categories:  官方动态
---

We’re excited to announce the start of the early access program for Kotlin 1.2: today its first milestone release 1.2-M1 is out.
This release enables by default new language features that were previously available in 1.1.x releases under experimental 1.2 language version setting. Also in the standard library you can preview the new API.
The complete though not so big list of changes in this release can be found in the changelog.

{% raw %}
<p><span id="more-5090"></span></p>
{% endraw %}

## Language feature: array literals in annotations

The single notable language feature proposed in this milestone is array literals, whose usages are constrained to annotation arguments.
Earlier one had to write something like following to specify an array of values:

{% raw %}
<p></p>
{% endraw %}

```kotlin
@CacheConfig(cacheNames = arrayOf("books", "default"))
public class BookRepositoryImpl {
    // ....
}
 
```

{% raw %}
<p></p>
{% endraw %}

In Kotlin 1.2 a literal can be used instead of the arrayOf function:

{% raw %}
<p></p>
{% endraw %}

```kotlin
@CacheConfig(cacheNames = ["books", "default"])
public class BookRepositoryImpl {
    // ....
}
 
```

{% raw %}
<p></p>
{% endraw %}

An IDE inspection will propose you to use the new syntax of collection literals where appropriate.
### Inline function with optional functional parameters

Up until now it was impossible to declare an inline higher order function with an optional functional parameter like the following:

{% raw %}
<p></p>
{% endraw %}

```kotlin
inline fun <E> List<E>.printItems(transform: (E) -> String = { it.toString() })
 
```

{% raw %}
<p></p>
{% endraw %}

One had to either make the function itself non-inline or mark the functional parameter as noinline. In either case that defeated the purpose of functional parameter inlining.
Now this case is fully supported.
## Standard Library API

This release features two KEEPs (Kotlin Evolution and Enhancement Proposals) regarding the standard library API.
The first is KEEP-49  introducing additional operations and conversion extensions for BigInteger and BigDecimal types, for which we’d like to thank Daniil Vodopian.
The second one is KEEP-11 which covers a number of functions related to partitioning collections and sequences:

* chunked(size: Int) extension function partitions a collection into blocks of the given size;
* windowed(size: Int, step: Int) takes a window of the given size and moves it along the collection with the given step returning the sublists of elements falling into each window;
* pairwise() extension returns all subsequent pairs in a collection.

Please try these extensions if you’re interested and tell us, whether they fit your use cases.
There are some other enhancements, such as fill() and shuffle() extensions for MutableList as well as shuffled() for List, also Regex class became serializable.
## JavaScript

Earlier in 1.1.2 release we have introduced the opt-in JS typed arrays support. When enabled it translates Kotlin primitive arrays, such as IntArray, DoubleArray etc, into JavaScript typed arrays. Now the opt-in is no longer required as this support is enabled by default.
## Pre-release notes

Note that the backward compatibility guarantees do not cover pre-release versions: the features and API can change in the subsequent releases. When we reach final RC, all binaries produced by pre-release versions will be outlawed by the compiler: you’ll be required to recompile everything that was compiled by 1.2‑Mx.
  However all the code compiled by 1.1.x and earlier releases is perfectly fine without recompilation.
In this release you won’t be able to compile against the old runtime if you’re authoring inline suspend functions.
## How to Try It

In Maven/Gradle: Add http://dl.bintray.com/kotlin/kotlin-eap-1.2 as a repository for the build script and your projects; use 1.2-M1 as the version number for the compiler plugin and the standard library.
In IntelliJ IDEA: Go to Tools → Kotlin → Configure Kotlin Plugin Updates, then select “Early Access Preview 1.2” in the Update channel drop-down list, then press Check for updates.
The command-line compiler can be downloaded from the Github release page.
On try.kotlinlang.org: Use the drop-down list at the bottom-right corner to change the compiler version to 1.2‑M1.
