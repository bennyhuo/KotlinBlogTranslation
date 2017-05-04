---
title: "Kotlin 1.0 Beta 4 is Out!"
date: 2015-12-22 22:25:00
author: Roman Belov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/12/kotlin-1-0-beta-4-is-out/
translator:
translator_url:
---

We are happy to announce Kotlin Beta 4, another step towards 1.0! We are now mostly focused on the infrastructure and future-proof changes. Full list of changes is available [here](https://github.com/JetBrains/kotlin/releases/tag/build-1.0.0-beta-4583) . More details below.
It’s also time to let you know about what else we are going to do before 1.0.<span id="more-3328"></span>
## Improved incremental compilation (Experimental)

We have rolled out a new precise algorithm for dependency detection that makes Kotlin’s incremental compilation much faster. It’s still experimental, but works pretty well for our use cases already. To try it out:
<p>

  Settings | Build, Execution, Deployment | Compiler | Kotlin Compiler | Enable precise incremental compilation (experimental)

</p>
Soon: same incremental compilation support is coming to Gradle! Stay tuned.
## Language

Some highlights from the [full list of changes](https://github.com/JetBrains/kotlin/releases/tag/build-1.0.0-beta-4583) .
### Changes in overload resolution

Due to a fix in the overload resolution algorithm, Kotlin now treats SAM-converted Java functions more like members (they used to behave like extensions before). This fix is important, because otherwise many cases were interpreted in cumbersome ways by the compiler.
Unfortunately, there’s at least one relatively common case that has broken as a result. The fix is very easy, though. Now the compiler complains about `file.listFiles { it.name == "..." }`.<br/>

The reason is rather complicated:

* there are three overloads of listFiles in java.io.File
* two of them take a SAM-interface, which we convert so that they can take a lambda
* so, when a parameterless lambda is passed in we don’t know which one should be chosen
* it worked before, because an old library extension function (dating back to the pre-SAM era) was selected instead of a SAM-converted member.

**The workaround** is simple, just specify the parameter, e.g.:

{% raw %}
<p></p>
{% endraw %}

```kotlin
file.listFiles { it -> ... }
```

{% raw %}
<p></p>
{% endraw %}

### Properties can be used as parameterless function objects

Example: in Kotlin `String::length` is a property, not a function, but it’s convenient to be able to use it where a function is expected, e.g.

{% raw %}
<p></p>
{% endraw %}

```kotlin
val lengths = strs.map(String::length)
```

{% raw %}
<p></p>
{% endraw %}

So, we now allow this. In other words, whenever some API expects a function of type `(R) -&gt; T` we can use a reference to a property of `R` whose return type is `T`.
### Reserving keywords for future use

We are planning to add new features in the future releases of Kotlin, so we decided to reserve the necessary keywords in advance. We understand that one can’t predict all of the future, but here’s our best guess (no detailed design for the future features is available yet, but we’ll do our best to make them as useful as can be):

* yield is reserved as a keyword
* sealed is reserved in front of “when“
* typeof is reserved as a keyword. In JS, use jsTypeOf()
* async is reserved in front of “{” and “fun“

So, now, instead of `async {...}` we’ll have to say `async () {...}`. We understand that it’s not as clean, but we didn’t find a better option. Code completion will insert `()` automatically.
*Code Cleanup* will help you migrate existing code.
### Java Wildcards

There were issues with how Kotlin translated variant types, e.g. whether a `List&lt;Foo&gt;` should be `List&lt;? extends Foo&gt;` in Java or simply `List&lt;Foo&gt;`. Subtleties details aside, we did the following:

* By default, we do not generate wildcards in return types and where they make no sense
* When a wildcard is needed, one can enforce its presence with a type annotation: List<@JvmWildcard String> is always List<? extends String> in Java
* When we need to get rid of a wildcards, we can use @JvmSuppressWildcards (this can be used on a type or any declaration that contains it)

Examples:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun foo(l: List<String>) // in Java: List<String> (String is final)
fun foo(l: List<@JvmWildcard String>) // in Java: List<? extends String>
 
interface Open
fun bar(p: List<Open>) // in Java: List<? extends Open> (Open is not final)
@JvmSuppressWildcards
fun bar(p: List<Open>) // in Java: List<Open>
```

{% raw %}
<p></p>
{% endraw %}

NOTE: this concerns not only collections, but all types that involve declaration-site variance
## Library changes

We are cleaning up the Standard Library, and this includes some repackaging:

* The kotlin.test package has been moved to a separate jar-file: kotlin-test.jar. A quick-fix is available in the IDE to add this dependency automatically.
* In preparation to rearranging packages in the Standard Library, we have created the new packages and copied all functions to them. The old functions are kept for binary compatibility. No migration needed for Kotlin code, Code Cleanup is available for Java code.

Later, we are planning to extract one more JAR from the library: it will contain array utilities that are infrequently used, so we’d like to keep them outside the main JAR to reduce its size.
**Some more highlights**:
Kotlin’s `Int::class` may correspond to Java’s `int.class` or `Integer.class` in different contexts (and it’s justified). To facilitate use cases when a specific one of the two is needed, we have introduced two properties:

* Int::class.javaPrimitiveType returns Int.class
* Int::class.javaObjectType returns Integer.class

Also, we can now say things like `IntArray(5) { it * 3 }`, i.e. create initialized primitive arrays.
### Future change: meaning of null in collections

The later versions of the JDK are making collections more and more null-intolerant. For example, here’s what the [JavaDoc](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html#computeIfAbsent-K-java.util.function.Function-) says about `java.util.Map.computeIfAbsent`:
<p>

  If the specified key is not already associated with a value **(or is mapped to null)**, attempts to compute its value using the given mapping function and enters it into this map unless null.

</p>
These contracts are intrinsic to atomicity properties of such operations, so we decided that we have to meet them too, otherwise we won’t be able to guarantee proper behavior for Kotlin’s extension functions when they operate on null-free concurrent collections. So, we are going to change the behavior of `getOrPut` and other such functions so that they treat `null` value the same as the value was not present.
To update your code, follow the recommendations given in deprecation warnings.
## What’s new in the IDE


* Quick-fix for renaming unresolved references was added. It’s handy for adjusting symbols’ names when pasting some code to a different context:

