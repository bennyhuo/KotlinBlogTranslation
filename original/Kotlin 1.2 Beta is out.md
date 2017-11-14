---
title: Kotlin 1.2 Beta is out
author: Roman Belov
date: 2017-09-29 13:51:00
source_url: https://blog.jetbrains.com/kotlin/2017/09/kotlin-1-2-beta-is-out/
tags: 
categories:  官方动态
---

We’re happy to announce the Beta release for Kotlin 1.2. With this release, we’re unveiling the major new feature of Kotlin 1.2 – experimental support for multiplatform projects. Also, the language and standard library are now feature complete – all the new features planned for Kotlin 1.2 have been implemented. Now is a great time to give us feedback on the changes – we still have time to take the feedback into account and adjust the design for the final 1.2 release, if needed.
In terms of tooling, Kotlin 1.2 Beta includes the same set of features as the recently released 1.1.50 update. The beta is compatible with all versions of IntelliJ IDEA from 2016.3 until 2017.3, as well as with Android Studio 2.3 and 3.0.
The complete changelog since 1.2-M2 can be found here with the significant changes listed below.

{% raw %}
<p><img alt="12beta" class="alignnone size-full wp-image-5314" height="750" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/09/12beta.png" width="1500"/></p>
{% endraw %}


{% raw %}
<p><span id="more-5287"></span></p>
{% endraw %}

# Multiplatform Projects

Multiplatform projects are a new experimental feature in Kotlin 1.2, allowing you to reuse code between target platforms supported by Kotlin – JVM, JavaScript and (in the future) Native. In a multiplatform project, you put code which is shared between platforms into a common module, and platform-dependent parts into platform-specific modules that depend on it. When you compile such a project for a specific platform, the code for both the common and platform-specific parts is generated.
A key feature of the multiplatform project support is the possibility to express dependencies of common code on platform-specific parts through expected and actual declarations. An expected declaration specifies an API (class, interface, annotation, top-level declaration etc.). An actual declaration is either a platform-dependent implementation of the API or a typealias referring to an existing implementation of the API in an external library:

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Common code
expect fun hello(world: String)
 
expect class URL(spec: String) {
  open fun getHost(): String
  open fun getPath(): String
}
 
// JVM code
actual fun hello(world: String) {
  println("Hello JVM $world")
}
 
actual typealias URL = java.net.URL
 
```

{% raw %}
<p></p>
{% endraw %}

For more information on multiplatform projects, please check out the documentation.
If you’ve already tried this feature before it was announced, please be aware that you need to update your projects: the header and impl keywords have been renamed to expect and actual. To update your code automatically, use Analyze | Cleanup Code… in IntelliJ IDEA.
# Language and Compiler

## Array Literals in Annotations

A new language feature in Kotlin 1.2 is the support for array literals in annotations. Now, instead of writing something like @CacheConfig(cacheNames = arrayOf("books", "default")), you can simply use a literal expression:
@CacheConfig(cacheNames = ["books", "default"])
The feature was already available in previous milestone releases of Kotlin 1.2. In 1.2 Beta, we’ve made the syntax more consistent and allowed to use array literals both for array and for vararg parameters:
@RequestMapping(value = ["value1", "value2"], path = ["path1", "path2"])
In order to enable that change, we decided to make some adjustments to the syntax of using named arguments together with varargs, both in regular method calls and in annotations. You may be surprised, but in Kotlin 1.1, when calling a vararg method using the named argument syntax, it was possible to pass a single argument as an immediate value:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun foo(vararg strs: String) { ... }
 
foo(strs = "abc")
 
```

{% raw %}
<p></p>
{% endraw %}

Saying that strs equals one string “abc” is a little unintuitive, and also it makes us use the spread operator when passing an entire array as a named argument:
foo(strs = *arr)
We’d really like to make it foo(strs = arr), but for compatibility, it requires a gradual migration, so in 1.2 we deprecate foo(strs = "abc"). As a replacement (in the unlikely case that you’ve been using this syntax), you can use the spread operator and the arrayOf method:
foo(x = *arrayOf("abc"))
We plan to implement a compiler optimization to elide the array allocation and copy in such calls.
Since annotations are a more constrained context, we can skip one step in migration, so you can simply enclose the value in an array literal, without the spread operator:

{% raw %}
<p></p>
{% endraw %}

```kotlin
annotation class Foo(vararg value: String)
 
@Foo(value = "a") // deprecated
@Foo(value = ["a"]) // correct
 
```

{% raw %}
<p></p>
{% endraw %}

See the YouTrack issue for more information.
## lateinit improvements

We’ve added a new reflection API allowing you to check whether a lateinit variable has been initialized:

{% raw %}
<p></p>
{% endraw %}

```kotlin
lateinit var file: File
 
// ...
 
if (::file.isInitialized) {
  ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

This is a partial implementation of this KEEP proposal; the remaining part (the deinitialize method) has been postponed, tentatively until 1.3.
Also, the lateinit modifier can now be used on top-level properties and local variables. The latter can be used, for example, when you’re initializing an object graph and you have a circular dependency between the properties of the objects in the graph (e.g. the lambda passed as a constructor argument to one object refers to another object which has to be defined later):

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun test() {
  lateinit var x: Component
 
  // inject takes a lambda which must return the Component though
  val injector = inject(
    ...,
    componentProvider = { x },
    ...
  )
 
  // Initialization is only possible via injector, once it has been run
  x = injector.createComponent()
}
 
```

{% raw %}
<p></p>
{% endraw %}

See the KEEP for more detailed information.
## Bound callable reference improvements

You can now omit this in expressions like this::foo, which create callable references bound to a member of this. Instead, you can simply write ::foo. Previously the syntax with the empty left side could only be used to create callable references to top-level declarations. For more information, see the YouTrack issue.
## Type inference improvements

The Kotlin compiler can now use information from type casts in type inference. If you’re calling a generic method that returns a type parameter T and casting the return value to a specific type Foo, the compiler now understands that  T for this call needs to be bound to the type Foo. This is particularly important for Android developers, because the compiler can now correctly analyze findViewById calls in Android API level 26:
val button = findViewById(R.id.button) as Button
As the method has been changed to <T extends View> T findViewById(int id), Kotlin 1.1 was unable to infer the type argument for T in such calls. For more information, see the YouTrack issue.
## Warnings as errors

The compiler now provides an option to treat all warnings as errors. Use -Werror on the command line, or the following Gradle snippet:

{% raw %}
<p></p>
{% endraw %}

```kotlin
compileKotlin {
  kotlinOptions.warningsAsErrors = true
}
 
```

{% raw %}
<p></p>
{% endraw %}

## Smart cast improvements

Smart casts are now applied to subjects of safe casts:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun foo(x: Foo?) {
  val b = (x as? SubClass)?.subclassMethod1()
  if (b != null) {
    x.subclassMethod2() // x is smart cast to SubClass
  }
}
 
```

{% raw %}
<p></p>
{% endraw %}

Also, smart casts in a lambda are now allowed for var variables that are only modified before the lambda:

{% raw %}
<p></p>
{% endraw %}

```kotlin
var x: String? = null
if (flag) x = "Yahoo!"
 
run {
  if (x != null) {
    println(x.length) // x is smart cast to String
  }
}
 
```

{% raw %}
<p></p>
{% endraw %}

## Nested classes in enum entries

Nested classes inside enum entries are now deprecated; as a fix, mark the class as inner.
# Standard library

## Split package compatibility

The Kotlin standard library is now fully compatible with the Java 9 module system, which forbids split packages (multiple jar files declaring classes in the same package). In order to support that, we’ve created new artifacts kotlin-stdlib-jdk7 and kotlin-stdlib-jdk8, which replace the old kotlin-stdlib-jre7 and kotlin-stdlib-jre8. The declarations in the new artifacts are visible under the same package names from the Kotlin point of view, but, due to special compiler magic we’ve added, are visible under different package names for Java. Therefore, switching to the new artifacts will not require any changes to your source code.
Another change we made to ensure compatibility with the new module system is removing the deprecated declarations in the kotlin.reflect package from the kotlin-reflect library. If you were using them, you need to switch to using the declarations in the kotlin.reflect.full package, which is supported since Kotlin 1.1.
## kotlin.math

kotlin.math is a new package in the Kotlin 1.2 standard library, allowing you to perform mathematical operations in cross-platform code. In 1.2-Beta, we made several improvements to it:

* Inverse hyperbolic functions (asinh, acosh, atanh) are now supported
* Functions related to binary representation of floating point numbers (toBits, nextUp and so on), added in 1.2-M2, are now available for JavaScript
* Improved precision of math polyfills for JavaScript

# Pre-release notes

As with other milestone releases, we give no backwards compatibility guarantees for new language and library features. Anything introduced in milestone releases of 1.2 is subject to change before the final 1.2 release. When we reach final RC, all binaries produced by pre-release versions will be outlawed by the compiler: you’ll be required to recompile everything that was compiled by 1.2‑Mx or 1.2-Beta.
However all the code compiled by 1.1.x and earlier releases is perfectly fine without recompilation.
# How to try it

In Maven/Gradle: Add http://dl.bintray.com/kotlin/kotlin-eap-1.2 as a repository for the build script and your projects; use 1.2.0-beta-31 as the version number for the compiler plugin and the standard library.
In IntelliJ IDEA: Go to Tools → Kotlin → Configure Kotlin Plugin Updates, then select “Early Access Preview 1.2” in the Update channel drop-down list, then press Check for updates.
The command-line compiler can be downloaded from the GitHub release page.
On try.kotlinlang.org: Use the drop-down list at the bottom-right corner to change the compiler version to 1.2‑Beta (coming soon).
