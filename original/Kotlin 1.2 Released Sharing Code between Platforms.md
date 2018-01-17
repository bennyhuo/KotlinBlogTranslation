---
title: Kotlin 1.2 Released: Sharing Code between Platforms
author: Dmitry Jemerov
date: 2017-11-28 19:52:00
source_url: https://blog.jetbrains.com/kotlin/2017/11/kotlin-1-2-released/
tags: 
categories:  官方动态
---

Today we’re releasing Kotlin 1.2. This is a major new release and a big step on our road towards enabling the use of Kotlin across all components of a modern application.

In Kotlin 1.1, we officially released the **JavaScript target**, allowing you to compile Kotlin code to JS and to run it in your browser. In Kotlin 1.2, we’re adding the possibility to **reuse code between the JVM and JavaScript**. Now you can write the business logic of your application once, and reuse it across all tiers of your application – the backend, the browser frontend and the Android mobile app. We’re also working on libraries to help you reuse more of the code, such as a cross-platform serialization library.

![Kotlin 1.2](https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/11/cake3-1.png)

Kotlin 1.2 is already bundled in [IntelliJ IDEA 2017.3](https://www.jetbrains.com/idea/), which is being released this week. If you’re using Android Studio or an older version of IntelliJ IDEA, you can install the new version from the Tools | Kotlin | Configure Kotlin Plugin Updates dialog.

This release includes a lot of work done by external contributors, and we’d like to thank everyone who sent us feedback, reported issues, and especially those who submitted pull requests.

## Multiplatform Projects

A multiplatform project allows you to build multiple tiers of your application – backend, frontend and Android app – from the same codebase. Such a project contains both **common modules**, which contain platform-independent code, as well as **platform-specific modules**, which contain code for a specific platform (JVM or JS) and can use platform-specific libraries. To call platform-specific code from a common module, you can specify **expected declarations**– declarations for which all platform-specific modules need to provide **actual implementations**.

![MPP](https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/11/MPP.png)

For more information on the feature, please check out the [documentation](http://kotlinlang.org/docs/reference/multiplatform.html).

As mentioned previously, we’re also working on a set of common libraries to allow you to move more of the logic to common code:

- [kotlin.test](http://kotlinlang.org/api/latest/kotlin.test/index.html), included out of the box in Kotlin 1.2, lets you write your test once and run it under both the JVM and JS;
- [kotlinx.html](https://github.com/kotlin/kotlinx.html) supports **isomorphic rendering** – using the same code to render HTML in the backend and in the frontend;
- [kotlinx.serialization](https://github.com/kotlin/kotlinx.serialization) allows you to easily marshal Kotlin objects between different tiers of your application, using JSON or ProtoBuf as serialization formats.

Note that multiplatform projects are currently an experimental feature; it means that the feature is ready for use, but we may need to change the design in the subsequent release (and if we do, we’ll provide migration tools for existing code).

## Compilation Performance

Over the course of development of 1.2, we’ve put a lot of effort in making the compilation process faster. We’ve already reached approximately 25% improvement over Kotlin 1.1, and we see significant potential for further improvements, which will be released in 1.2.x updates.

The graph below shows the difference in compilation times for two large JetBrains projects built with Kotlin:
![CompilationSpeed](https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/11/CompilationSpeed.png)

## Other Language and Library Improvements

We’ve also made a number of smaller improvements to the language and the standard library:

- [A more concise syntax](http://kotlinlang.org/docs/reference/whatsnew12.html#array-literals-in-annotations) for passing multiple arguments to an annotation (array literals);
- Support for the `lateinit` modifier on top-level properties and local variables, as well as checking whether a `lateinit` variable is initialized;
- [Smarter smart casts](http://kotlinlang.org/docs/reference/whatsnew12.html#smart-cast-improvements) and [improved type inference](http://kotlinlang.org/docs/reference/whatsnew12.html#information-from-explicit-casts-is-used-for-type-inference) in certain cases;
- Compatibility of the standard library with the split package restrictions introduced in Java 9;
- New `kotlin.math` package in the standard library;
- New standard library functions for working with sequences and collections, including a [set of functions](http://kotlinlang.org/docs/reference/whatsnew12.html#windowed-chunked-zipwithnext) for breaking a collection or sequence into potentially overlapping groups of a fixed size.

For more information and code examples, please see the [What’s New in Kotlin 1.2](http://kotlinlang.org/docs/reference/whatsnew12.html)documentation page.

# Kotlin Around the World

Since the release of Kotlin 1.1 in March of this year, Kotlin has made huge gains in adoption all around the world. The culmination of that was [KotlinConf](https://kotlinconf.com/), our first worldwide conference, with around 1200 attendees gathering in San Francisco on November 2-3rd. We’ve recorded all the talks, and the videos are [now available](https://kotlinconf.com/talks/).

Kotlin is now an officially supported language for Android development, with out-of-the-box support in Android Studio 3.0, as well as official [samples](https://developer.android.com/samples/index.html?language=kotlin) and [style guides](https://android.github.io/kotlin-guides/) published by Google. As a result, Kotlin is already used in [more than 17% of projects in Android Studio 3.0](https://android-developers.googleblog.com/2017/11/update-on-kotlin-for-android.html), including many apps from the hottest startups as well as Fortune 500 companies.

![Users](https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/11/KotlinConfUsers.jpg)

On the server side, [Spring Framework 5.0 has been released](https://spring.io/blog/2017/09/28/spring-framework-5-0-goes-ga) with [many Kotlin support features](https://docs.spring.io/spring/docs/current/spring-framework-reference/languages.html#kotlin), and [vert.x](http://vertx.io/) has been [supporting Kotlin](http://vertx.io/docs/vertx-core/kotlin/) since their 3.4.0 release. Also, Gradle now comes with support for Kotlin DSL out of the box, and the [Gradle Kotlin DSL project](https://github.com/gradle/kotlin-dsl) is rapidly approaching the 1.0 release.

The number of lines of open-source Kotlin code on GitHub has now exceeded 25 million. And on Stack Overflow, Kotlin is both one of the [fastest-growing and one of the least-disliked languages](https://stackoverflow.blog/2017/10/31/disliked-programming-languages/).

![KotlinAdoption](https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/11/KotlinAdoption.png)

The community growing around Kotlin is also really amazing. There are over 100 user groups all around the world, and so many talks that we have a hard time keeping track of all of them – but for those that we do know about, the [talks map](http://kotlinlang.org/community/talks.html) gives you a very good idea of how wide-spread the use of Kotlin really is.

![KUGmap](https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/11/KUGmap.png)

And for those who’re just starting to learn Kotlin, there’s an ever-growing number of [books](http://kotlinlang.org/docs/books.html)(including our own “Kotlin in Action”, now available in [English](https://manning.com/books/kotlin-in-action), [Russian](https://dmkpress.com/catalog/computer/programming/java/978-5-97060-497-7/), [Japanese](https://www.amazon.co.jp/Kotlin%E3%82%A4%E3%83%B3%E3%83%BB%E3%82%A2%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3-Dmitry-Jemerov/dp/4839961743/ref=sr_1_2?ie=UTF8&qid=1511539431&sr=8-2&keywords=kotlin), [Chinese](https://www.amazon.com/Kotlin%E5%AE%9E%E6%88%98-Svetlana-Isakova-Dmitry-Jemerov/dp/B07568C58F/ref=sr_1_3?s=books&ie=UTF8&qid=1511539582&sr=1-3) and [Portuguese](https://novatec.com.br/livros/kotlin-em-acao/)), online courses, tutorials and [other resources](http://kotlinlang.org/community/).

## Meet the Team: Webinar and Reddit AMA

To share with you more information on the new release, we plan to host a [webinar on multiplatform projects with Kotlin 1.2](https://info.jetbrains.com/Kotlin-Webinar-December2017.html) on December 7th, 18:00 CET. Please register; space is limited!

The Kotlin team will also conduct an AMA (Ask Me Anything) on the [Kotlin Reddit](https://www.reddit.com/r/Kotlin/) on December 5th. We’ll start at noon CET, and we’ll be there with you for the next 24 hours.

## How to Upgrade

As always, you can **try Kotlin online** at [try.kotlinlang.org](http://try.kotlinlang.org/).

- **In Maven, Gradle and npm**: Use `1.2.0` as the version number for the compiler and the standard library. See the docs [here](http://kotlinlang.org/docs/reference/using-gradle.html).
- **In IntelliJ IDEA**: 2017.3 has Kotlin 1.2 bundled, in earlier versions Install or update the Kotlin plugin to version 1.2.
- **In Android Studio**: Install or update the plugin through *Plugin Manager*.
- **In Eclipse**: install the plugin using [Marketplace](https://marketplace.eclipse.org/content/kotlin-plugin-eclipse).
- **The command-line compiler** can be downloaded from the [Github release page](https://github.com/JetBrains/kotlin/releases/tag/v1.2.0).

**Compatibility**. In Kotlin 1.2 the language and the standard library are [backwards compatible (modulo bugs)](http://kotlinlang.org/docs/reference/compatibility.html): if something compiled and ran in 1.0 or 1.1, it will keep working in 1.2. To aid big teams that update gradually, we provide a compiler switch that disables new features. [Here](http://kotlinlang.org/docs/reference/compatibility.html#binary-compatibility-warnings) is a document covering possible pitfalls.

*Have a nice Kotlin!*