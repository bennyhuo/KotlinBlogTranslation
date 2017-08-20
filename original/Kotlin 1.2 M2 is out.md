---
title: Kotlin 1.2 M2 is out
author: Alexey Sedunov
date: 2017-08-09 17:56:00
source_url: https://blog.jetbrains.com/kotlin/2017/08/kotlin-1-2-m2-is-out/
tags: 
categories:  官方动态
---

We’re happy to announce the second milestone release for Kotlin 1.2. The primary focus of this release is concerned with stability and bugfixes in Kotlin compiler and tooling as well as improvements of Kotlin standard library. It also includes many of the tooling features available in the upcoming release of Kotlin 1.1.4.
We appreciate your feedback regarding the new features or any problems that you may run into with this release.
The complete changelog since 1.2 M1 can be found here with some major changes listed below.

{% raw %}
<p><span id="more-5160"></span></p>
{% endraw %}

## Compiler

### Breaking change: Java-default method calls

Up to now Kotlin interface members overriding Java-default methods while targeting JVM 1.6 produced a warning on super calls: Super calls to Java default methods are deprecated in JVM target 1.6. Recompile with '-jvm-target 1.8'. In 1.2-M2 release we’ve replaced the warning with error, thus requiring any such code to be compiled with -jvm-target 1.8 option
## Standard library

### Revised windowed/pairwise operations

We have been listening to your feedback about chunked/windowed/pairwise functions KEEP-11, which were released to preview in the previous milestone 1.2-M1, and based on it we decided to make some changes to these functions:

* windowed function now has its step parameter defaulting to 1.
It also gets an additional optional parameter partialWindows, which controls what to do with incomplete windows in the end. By default it is false, which means incomplete windows are dropped.
* pairwise function name was too confusing, it was unclear how it paired the elements together. Now it is called zipWithNext, so it is more clear that each element is zipped with the next element in a collection.

### Common math operations in the standard library

There was a longstanding request to support math operations in the standard library KT-4900. Until now one had to resort to math functions and constants from java.lang.Math class in JVM platform and to kotlin.js.Math which exposed native JS Math functions to Kotlin code in JS platform.
But now we’re introducing the following groups of API in the kotlin.math package:

* constants: PI and E;
* trigonometric: cos, sin, tan and inverse of them: acos, asin, atan, atan2;
* hyperbolic: cosh, sinh, tanh;
* exponentation: pow (an extension function), sqrt, hypot, exp, expm1;
* logarithms: log, log2, log10, ln, ln1p;
* rounding:

ceil, floor, truncate, round (half to even) functions;
roundToInt, roundToLong (half to integer) extension functions;
* ceil, floor, truncate, round (half to even) functions;
* roundToInt, roundToLong (half to integer) extension functions;
* sign and absolute value:

abs and sign functions;
absoluteValue and sign extension properties;
withSign extension function;
* abs and sign functions;
* absoluteValue and sign extension properties;
* withSign extension function;
* max and min of two values;
* binary representation:

ulp extension property;
nextUp, nextDown, nextTowards extension functions;
toBits, toRawBits, Double.fromBits (these are in the kotlin package).
* ulp extension property;
* nextUp, nextDown, nextTowards extension functions;
* toBits, toRawBits, Double.fromBits (these are in the kotlin package).

The same set of functions (but without constants) is also available for Float arguments.
Most of these functions (except the binary representation group) are also available in JS, thus solving the problem of writing the same calculations for both platforms.
## Pre-release notes

As with other milestone releases, we give no backwards compatibility guarantees for new language and library features. Anything introduced in milestone releases of 1.2 is subject to change before the final 1.2 release. When we reach final RC, all binaries produced by pre-release versions will be outlawed by the compiler: you’ll be required to recompile everything that was compiled by 1.2‑Mx.
  However all the code compiled by 1.1.x and earlier releases is perfectly fine without recompilation.
## How to Try It

In Maven/Gradle: Add http://dl.bintray.com/kotlin/kotlin-eap-1.2 as a repository for the build script and your projects; use 1.2-M2 as the version number for the compiler plugin and the standard library.
In IntelliJ IDEA: Go to Tools → Kotlin → Configure Kotlin Plugin Updates, then select “Early Access Preview 1.2” in the Update channel drop-down list, then press Check for updates.
The command-line compiler can be downloaded from the Github release page.
On try.kotlinlang.org: Use the drop-down list at the bottom-right corner to change the compiler version to 1.2‑M2 (coming soon).
