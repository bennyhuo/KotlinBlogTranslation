---
title: Kotlin 1.2 Beta2 is out
author: Dmitry Petrov
date: 2017-10-19 13:43:00
source_url: https://blog.jetbrains.com/kotlin/2017/10/kotlin-1-2-beta2-is-out/
tags: 
categories:  官方动态
---

We’re happy to announce the second Beta release for Kotlin 1.2. In this release, we’ve been mostly focusing on smaller internal changes and on adding some missing pieces to our multiplatform project story.
We’d like to thank Andrey Mischenko, Francesco Vasco, Jake Wharton, Jonathan Leitschuh, Kirill Rakhman, Pap Lorinc, Paul Merlin, Raluca Sauciuc, Toshiaki Kameyama, and Yoshinori Isogai for their contributions to Kotlin 1.2 Beta2.
The complete changelog since 1.2-Beta can be found here with the significant changes listed below.

{% raw %}
<p><span id="more-5350"></span></p>
{% endraw %}

## Compiler

### Compiler performance improvements

There is a range of compiler performance improvements since the previous public release. An average project build time is decreased by nearly 20%.
### Generated code normalization for bytecode postprocessing tools

Ever since version 1.0, Kotlin supported expressions with complex control flow, such as try-catch expressions and inline function calls. Such code is valid according to the Java Virtual Machine specification. Unfortunately, some bytecode processing tools do not handle such code quite well when such expressions are present in the arguments of constructor calls.
To mitigate this problem for the users of such bytecode processing tools, we’ve added a command-line option (-Xnormalize-constructor-calls=MODE) that tells the compiler to generate more Java-like bytecode for such constructs. Here MODE is one of:

* disable (default) – generate bytecode in the same way as in Kotlin 1.0 and 1.1;
* enable – generate Java-like bytecode for constructor calls. This can change the order in which the classes are loaded and initialized;
* preserve-class-initialization – generate Java-like bytecode for constructor calls, ensuring that the class initialization order is preserved. This can affect overall performance of your application; use it only if you have some complex state shared between multiple classes and updated on class initialization.

The “manual” workaround is to store the values of sub-expressions with control flow in variables, instead of evaluating them directly inside the call arguments. It’s similar to -Xnormalize-constructor-calls=enable.
See KT-19251 for more details.
## Multiplatform projects

There are numerous improvements regarding multiplatform projects support, mainly in IDE, but not only. The most notable are the following ones.
### Annotations for writing multiplatform unit tests

Now it is possible to write tests in a common project so that they will be compiled and run in each platform project. There are 4 annotations provided in kotlin-test package to markup tests in common code: @Test, @Ignore, @BeforeTest and @AfterTest.
In JVM platform these annotations are mapped to the corresponding JUnit 4 annotations and in JS they are already available since 1.1.4 to support JS unit testing, see this announce.
In order to use them you need to add a dependency on kotlin-test-annotations-common to your common module, on kotlin-test-junit to your JVM module, and on kotlin-test-js to the JS module.
### “implement” is renamed to “expectedBy”

Following the expect/actual naming, the Gradle dependency configuration implement (that is used by platform projects to point at their corresponding common project) is now renamed to expectedBy, and the old name is deprecated.

{% raw %}
<p></p>
{% endraw %}

```kotlin
dependencies {
    expectedBy project(':lib-common')
}
 
```

{% raw %}
<p></p>
{% endraw %}

### Correct importing of multiplatform projects with multiple modules

There was an annoying issue with references to common code in a platform module being unresolved in a multiplatform project with multiple modules. Now the importing of such projects from Gradle is fixed and you don’t have to add extra dependencies manually to make these references resolved anymore.
## Gradle plugin

### “warningsAsErrors” is renamed to “allWarningsAsErrors”

The warningsAsErrors flag that was introduced in Kotlin 1.2 Beta is renamed to allWarningsAsErrors :

{% raw %}
<p></p>
{% endraw %}

```kotlin
compileKotlin.kotlinOptions.allWarningsAsErrors = true
 
```

{% raw %}
<p></p>
{% endraw %}

## Standard library

### “Closeable.use” calls “Throwable.addSuppressed” when available

Finally, Closeable.use function calls Throwable.addSuppressed when an exception was thrown during closing the resource after some other exception. To enable this behavior you’ll need to have kotlin-stdlib-jdk7 in your dependencies.
## Pre-release notes

As with other milestone releases, we give no backward compatibility guarantees for new language and library features. Anything introduced in milestone releases of 1.2 is subject to change before the final 1.2 release. When we reach final RC, all binaries produced by pre-release versions will be outlawed by the compiler: you’ll be required to recompile everything that was compiled by 1.2‑Mx, 1.2-Beta, or 1.2-Beta2.
However, all the code compiled by 1.1.x and earlier releases is perfectly fine without recompilation.
## How to try it

In Maven/Gradle: Add http://dl.bintray.com/kotlin/kotlin-eap-1.2 as a repository for the build script and your projects; use 1.2.0-beta-88 as the version number for the compiler plugin and the standard library.
In IntelliJ IDEA: Go to Tools → Kotlin → Configure Kotlin Plugin Updates, then select “Early Access Preview 1.2” in the Update channel drop-down list, then press Check for updates.
The command-line compiler can be downloaded from the GitHub release page.
On try.kotlinlang.org: Use the drop-down list at the bottom-right corner to change the compiler version to 1.2‑Beta2 (coming soon).
