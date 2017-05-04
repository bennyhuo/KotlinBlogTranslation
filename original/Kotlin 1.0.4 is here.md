---
title: "Kotlin 1.0.4 is here"
date: 2016-09-22 20:18:00
author: Dmitry Jemerov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2016/09/kotlin-1-0-4-is-here/
translator:
translator_url:
---

We’re happy to announce the release of a new bugfix and tooling update of Kotlin, version <b>1.0.4</b>. This version brings many improvements related to the IDE and build tools, as well as JavaScript support.
Once again we’d like to thank our external contributors who implemented some of the features in this release, [Kirill Rakhman](https://github.com/cypressious) and [Yoshinori Isogai](https://github.com/shiraji) , as well as everyone who tried the EAP builds of 1.0.4 and sent us feedback.
You can find the full list of fixes and improvements in the [changelog](https://github.com/JetBrains/kotlin/blob/1.0.4/ChangeLog.md) . Some of the changes deserve special mention:
### Language Change: Assignment of ‘val’ in try/catch

In versions of Kotlin before 1.0.4, you could initialize the same `val` both in the `try` and `catch` branches of a `try/catch` statement. For example, the following code was allowed:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val x: Int
try {
    x = 1
}
catch(e: Exception) {
    x = 2
}
 
```

{% raw %}
<p></p>
{% endraw %}

In effect, a final variable could be assigned twice, and it was possible to observe two different values for it (for example, if the value in the `try` statement was captured in a lambda). In Java, the equivalent code is not allowed.
To maintain consistent semantics, the code which assigns the same `val` in both `try` and `catch` branches <b>becomes a warning</b> in Kotlin 1.0.4 and will <b>become an error</b> in version 1.0.5. In most cases, the code can be easily fixed by converting the code to an expression form, and the IDE will <b>offer a quickfix</b> to convert this code automatically. The above example would be converted to:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val x = try {
    1
}
catch(e: Exception) {
    2
}
 
```

{% raw %}
<p></p>
{% endraw %}


{% raw %}
<p><span id="more-4275"></span></p>
{% endraw %}

### New Experimental Annotation Processing

Kotlin 1.0.4 includes a new experimental implementation of the annotation processing API. To enable it, add the following to your build.gradle:
`apply plugin: 'kotlin-kapt'`
You also need to <b>remove</b> the snippet that enables old annotation processing:

{% raw %}
<p></p>
{% endraw %}

```kotlin
kapt {
    generateStubs = true
}
 
```

{% raw %}
<p></p>
{% endraw %}

The new annotation processing still has known issues and may not be compatible with all annotation processors. You should enable it only if you’ve run into problems with the default `kapt` annotation processing implementation.
### JavaScript Backend Improvements

The JavaScript backend can now compile code to modules which are compatible with AMD, CommonJS and UMD module systems. See [the documentation](http://kotlinlang.org/docs/reference/js-modules.html) for more details.
In addition to that, a limited form of reflection is now supported: you can use the `jsClass` property to access the runtime class of any object, and `jsClass&lt;TypeName&gt;()` to get the runtime representation of a specific class. Here’s a more complete example:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class A
class B
class C
 
inline fun <reified T> foo() {
    println(jsClass<T>().name)
}
 
println(A().jsClass.name) // prints "A"
println(jsClass<B>().name) // prints "B"
foo<C>() // prints "C"
 
```

{% raw %}
<p></p>
{% endraw %}

### Compiler Improvements


* Better type inference for callable expressions

More efficient bytecode for several cases of when and for expressions

Better parser recovery after syntax errors

Fixed several cases when “Cast never succeeds” warning was incorrectly reported
* More efficient bytecode for several cases of when and for expressions

Better parser recovery after syntax errors

Fixed several cases when “Cast never succeeds” warning was incorrectly reported
* Better parser recovery after syntax errors

Fixed several cases when “Cast never succeeds” warning was incorrectly reported
* Fixed several cases when “Cast never succeeds” warning was incorrectly reported

### Build Tools Improvements


* Full compatibility with Gradle 2.14 and later.

Gradle incremental compilation can now track changes between subprojects.

CLI and Ant builds add the Kotlin reflection library to the classpath by default; use the no-reflect switch to disable.
* Gradle incremental compilation can now track changes between subprojects.

CLI and Ant builds add the Kotlin reflection library to the classpath by default; use the no-reflect switch to disable.
* CLI and Ant builds add the Kotlin reflection library to the classpath by default; use the no-reflect switch to disable.

### New Features in the IDE


{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2016/09/KotlinEvaluate.png?ssl=1" rel="attachment wp-att-4285"><img alt="kotlinevaluate" class="alignnone size-full wp-image-4285" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2016/09/KotlinEvaluate.png?resize=640%2C648&amp;ssl=1"/></a></p>
{% endraw %}


* You now have the option to use Kotlin syntax when evaluating expressions and watches in Java files

New inspection to detect “leaking this” – possible NullPointerException issues caused by access to incompletely initialized data.

Intention to convert a lambda to a function reference

Inspection to detect mismatches between Gradle version and Kotlin plugin version

Many other new intentions, inspections and quickfixes
* New inspection to detect “leaking this” – possible NullPointerException issues caused by access to incompletely initialized data.

Intention to convert a lambda to a function reference

Inspection to detect mismatches between Gradle version and Kotlin plugin version

Many other new intentions, inspections and quickfixes
* Intention to convert a lambda to a function reference

Inspection to detect mismatches between Gradle version and Kotlin plugin version

Many other new intentions, inspections and quickfixes
* Inspection to detect mismatches between Gradle version and Kotlin plugin version

Many other new intentions, inspections and quickfixes
* Many other new intentions, inspections and quickfixes

### How to update

To update the plugin, use Tools | Kotlin | Configure Kotlin Plugin Updates and press the “Check for updates now” button. Also, don’t forget to update the compiler and standard library version in your Maven and Gradle build scripts.
As usual, if you run into any problems with the new release, you’re welcome to ask for help on the [forums](https://discuss.kotlinlang.org/) , on Slack (get an invite [here](http://kotlinslackin.herokuapp.com/) ), or to report issues in the [issue tracker](https://youtrack.jetbrains.com/issues/KT) .
Let’s Kotlin!
