---
title: "Kotlin 1.1 Beta Is Here!"
date: 2017-01-19 13:51:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/01/kotlin-1-1-beta-is-here/
---

Congratulations! Today Kotlin 1.1 has reached Beta, and this means that

* it’s time to try it out,
* there’s still time to give us your feedback (and we really need it!),
* the release is coming fairly soon.


{% raw %}
<p><center><img alt="Kotlin 1.1 Beta" class="alignnone size-full wp-image-4514" height="650" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/01/1.1-Beta-Banner-2-01.png" width="1300"/></center></p>
{% endraw %}

We’ve seen a lot of interest in Kotlin over the past year, and would like to thank all our users, contributors and supporters. Special thanks to early adopters of new features for their bravery and feedback to our EAP builds!

{% raw %}
<p><span id="more-4484"></span></p>
{% endraw %}

## An overview of what is coming in Kotlin 1.1

The biggest news of Kotlin 1.1 are

* full support of compilation to JavaScript, and
* Coroutines on the JVM, Android and JavaScript.

We’ll give some more details about these below, but they are not the only exciting news of 1.1. Many more language improvements and new features are coming (more details are available on our  [What’s new](https://kotlinlang.org/docs/reference/whatsnew11.html)  page):

* Type aliases: typealias Action<T> = (T) -> Unit
* Bound callable references: expr::foo
* Type inference based on getters: val myString get() = "hi"
* Compiler plugins for


making classes open by default
generating no-arg constructors by default
extension lambdas in SAM conversions
* making classes open by default
* generating no-arg constructors by default
* extension lambdas in SAM conversions
* Inheritance for data classes
* Subclasses of sealed classes in the same file
* Destructuring in lambdas: map.forEach { (k, v) -> ...}
* Underscore for unused parameters
* Scope control for builder-like DSL’s: @DslMarker
* provideDelegate operator convention
* Local delegated properties
* JDK 8 methods on Kotlin collections: list.parallelStream()
* Inline properties
* enumValues()/enumValueOf() for generic access to enums
* Underscore in numeric literals: 1_000_000

## Deprecation

We deprecate the unfortunate name <code>mod</code> that we used for the <code>%</code> operator, and replace it with <code>rem</code>, which is semantically correct and agrees with existing libraries such as <code>java.math.BigInteger</code>. Deprecation warnings and the tooling will guide you through the migration process.
## JavaScript

It’s simple: the full Kotlin language can be now compiled to JavaScript. It doesn’t mean that we have ported all of the JDK into the browser: the language and its Standard Library are not coupled with JDK, but you can use Kotlin strings, collections, sequences, arrays and other core APIs on JS as well as JVM/Android.
Numerous popular JS libraries will be available through typed headers (converted from  [DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped) ). We support all popular runtime module systems for JavaScript as well as  [webpack](https://webpack.github.io/)  and other important tools.
We’ll dedicate a lot of effort in Kotlin 1.2 and beyond to making the JavaScript tooling smooth and helpful. Our goal is to enable pleasant full-stack development with Kotlin.
## Coroutines

Honestly, it’s hard to over-emphasize coroutines. The future has come, and we are stuck with it: we need non-blocking asynchronous APIs to keep up with the loads of data we are processing. We’ve been through callback hell and conquered it, but we deserve better. We want to simply write the code following its natural <em>sequential</em> logic, and let the compiler figure the asynchrony out for us. This is what coroutines are about: async/await, generate/yield, non-blocking IO, Rx and much more brought under the single unified paradigm of a <em>suspending function</em>. Such a function (or lambda) represents a computation that can be suspended (without blocking any threads) and resumed later.

{% raw %}
<p></p>
{% endraw %}

```kotlin
future {
    val original = asyncLoadImage("...original...") // creates a Future
    val overlay = asyncLoadImage("...overlay...") // creates a Future
    ...
    // suspend while awaiting the loading of the images
    // then run `applyOverlay(...)` when they are both loaded
    return applyOverlay(original.await(), overlay.await())
}
 
```

{% raw %}
<p></p>
{% endraw %}

The main benefit of coroutines is their flexibility:

* The language part is minimal
* Everything can be written as a library
* Libraries are in total control of all aspects of suspending and resuming computations: threads, exceptions and other aspects of computation are entirely customizable.

We have written a set of libraries for interesting common use cases:  [kotlinx.coroutines](https://github.com/Kotlin/kotlinx.coroutines) 
Read more about coroutines  [here](https://github.com/Kotlin/kotlin-coroutines/blob/master/kotlin-coroutines-informal.md) .
<strong>An important note</strong>. With all the benefits that they bring, Kotlin coroutines are a fairly new design that needs extensive battle-testing before we can be sure it’s 100% right and complete. This is why we will release it under an “experimental” opt-in flag. We do not expect the language rules to change, but APIs may require some adjustments in Kotlin 1.2.

* Command line: -Xcoroutines=enabled
* Gradle: kotlin.coroutines=enable in gradle.properties or local.properties
* Maven: <configuration> <args> <arg>-Xcoroutines=enable</arg> </args> </configuration>
* IDE: Use a quick-fix (Alt+Enter) or modify the facet options (Project Structure -> Modules -> Your Module -> Compiler -> Coroutines (experimental))

## Standard Library, Tooling and Frameworks

Kotlin’s Standard Library is getting updated with  [many useful utilities](https://kotlinlang.org/docs/reference/whatsnew11.html#standard-library)  and extensions including those specific for JDK 7 and 8.
Our collaboration with  [Gradle](https://blog.gradle.org/kotlin-meets-gradle)  has resulted in gradle-script-kotlin which means that you can now write type-safe build scripts for Gradle, using Kotlin scripting.
We now support JSR 223, which is utilized by  [the Spring Framework](https://spring.io/blog/2017/01/04/introducing-kotlin-support-in-spring-framework-5-0)  along with type-safe DSLs and other things.
## How to Try It

As with other pre-release versions, we give <strong>no backward compatibility guarantees</strong> for Kotlin 1.1‑Beta. Moreover, when we reach final RC, all binaries produced by pre-release versions will be outlawed by the compiler: you’ll be required to recompile everything that was compiled by 1.1‑M0x and Beta (all the code from 1.0.x is perfectly fine without recompilation).
<strong>In Maven/Gradle:</strong> Add  [http://dl.bintray.com/kotlin/kotlin-eap-1.1](http://dl.bintray.com/kotlin/kotlin-eap-1.1)  as a repository for the build script and your projects; use <code>1.1.0-beta-17</code> as the version number for the compiler and the standard library.
<strong>In IntelliJ IDEA:</strong> Go to <em>Tools → Kotlin → Configure Kotlin Plugin Updates</em>, then select “Early Access Preview 1.1” in the <em>Update channel</em> drop-down list, then press <em>Check for updates</em>.
The command-line compiler can be downloaded from the  [Github release page](https://github.com/JetBrains/kotlin/releases/tag/v1.1-beta) .
<strong>On <a href="http://try.kotlinlang.org/">try.kotlinlang.org</a></strong>. Use the drop-down list at the bottom-right corner to change the compiler version to 1.1‑Beta.
Let’s Kotlin!
