---
title: M9 is coming
date: 2014-10-01 22:10:00
author: Hadi Hariri
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2014/10/m9-is-coming/
---

We’ve been working hard on the next upcoming release for Kotlin, M9, and it contains quite a good number of new features and some important changes.
## Platform Interoperability Improvements

One of Kotlin’s goals has always been about leveraging existing code, libraries and the JVM ecosystem and being able to mix and match Kotlin and Java. With M9 we’re going to considerably reduce the friction. Types with unknown nullity for consuming or implementing Java-authored API’s, exporting functions as static methods, removing conflicts, and also traits are now compiled in a more straightforward fashion, thus solving the problem with certain code generation libraries that only support simple interfaces.
## Incremental Compilation

We want Kotlin compilation to be as fast as Java and to this end we’ve introduced incremental compilation. This optimisation significantly reduces compilation time. It is also compatible with auto-make feature of IntelliJ IDEA, which compiles code in the background as changes are made.
## Modules

The Compiler and IDE now share understanding of modules, making it consistent between design time and compile time. Completion no longer suggests symbols from libraries that are not included as a dependency for a specific module, improving isolation and reducing chances of having unnecessary external dependencies. For now, the internal visibility modifier will still be treated as public. We still need to see how the user experience for consuming DSLs is before making a definitive commitment in this area.
## Debugger

General debugger improvements which allow for better understanding of Kotlin generated code, providing a better experience with breakpoints and Kotlin specific constructs.
## Refactorings and Intellisense

Improvements in usability and new features for IntelliJ IDEA including the long awaited Create from Usage, more intentions (quick-fixes) and code completion enhancements. The Extract Method refactoring now also analyses for code duplication on extracting a new method, suggesting replacements of these with the new method. The Java to Kotlin converter has also been greatly improved, providing a much better conversion of individual or multiple files from Java to Kotlin.
## JVM Code Generation

Improvements in code generation for JVM reducing byte code size, increasing performance of generated code, better compatibility with modern HotSpot optimisations in Java8 runtime and enhanced function inlining are amongst some of the things to expect from M9.
## JavaScript

Support for JavaScript platforms has been improved to the point where almost all language features can be used in modules targeting JavaScript runtimes. The standard library has been pre-compiled and now ships with the compiler, allowing to write code that uses a JavaScript-compatibile subset of the standard functions, such as those dealing with collection manipulations. And with a tiny modification, the code can also run on node.js.
M9 is coming soon, so stay tuned for more!
