---
title: "M7 Release Available"
date: 2014-03-20 00:00:00
author: Hadi Hariri
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2014/03/m7-release-available/
translator:
translator_url:
---

Kotlin M7 is here and with it some long awaited features.
## Compiler and Language Changes

### Inline support

One of the biggest features of M7 is support for inline functions. Kotlin encourages the use of higher-order functions (some people call this “functional style”) which entails extensive use of lambda expressions. Starting with M7, you can declare a higher-order function as “inline” which means that its body will be inlined at the call site along with any lambdas passed to it. This means that the performance penalty of using such functions is next to nothing. For instance, having a <em>for </em>loop as opposed to using <em>forEach </em>and passing a lambda will have very little difference in terms of speed.
<span id="more-1439"></span><br/>
Inlining provides benefits such as the number of generated classes, bytecode size, fewer allocations and fewer megamorphic calls, all of which contribute to these performance gains.
Many functions from Kotlin’s standard library are now inlined.
NOTE: If inlining breaks your code (due to compiler bugs, for example), you can switch it off by passing the <i>-inline off </i>command line option to the compiler (see Preferences -> Compiler -> Kotlin Compiler):

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2014/03/inline1.png"><img alt="inline" class="alignnone size-full wp-image-1462" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2014/03/inline1.png?resize=381%2C115&amp;ssl=1"/></a></p>
{% endraw %}

### toString(), equals() and hashCode() need override directive

When declaring <em>toString()</em>,<em> equals() </em>and <em>hashCode()</em> we now need to prefix them with the <em>override </em>keyword. This is a **breaking change** from the previous release and applies to all classes. Use the provided quick-fix in the IDE (Alt+Enter on an error) to quickly add “override” to all such methods in project.
### “jet” package renamed to “kotlin”

The <em>jet</em> core classes have been renamed to <em>kotlin</em>, which also means that, yes you guessed it, Kotlin is now the official and final name of, well, Kotlin. This is, again, a potentially **breaking change**. Most imports will happen automatically. In case you encounter any issues, rename the imports manually.
### References to local functions

In Kotlin you can reference a function by name using the <em>::functionName</em> syntax. This is also available now for local functions

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun foo() {
 
    fun bar() {
 
    }
 
    fun biz(func: () -> Unit) {
 
    }
 
    biz(::bar)
}
```

{% raw %}
<p></p>
{% endraw %}

## Interoperability

### <em>[throws]</em> annotation

You can now decorate a function with the <em>throws </em>annotation to indicate what exceptions should be declared by the function when compiled to the JVM.

{% raw %}
<p></p>
{% endraw %}

```kotlin
[throws(javaClass<SocketException>()]
fun connect(host: String) {
...
}
```

{% raw %}
<p></p>
{% endraw %}

would be translated to

{% raw %}
<p></p>
{% endraw %}

```kotlin
void connect(String host) throws SocketException {
...
}
```

{% raw %}
<p></p>
{% endraw %}

in Java.
### JavaScript enhancements

You can now provide overloaded functions and have them compiled to JavaScript. Kotlin creates new functions with the suffix _1, _2, and so on.

{% raw %}
<p></p>
{% endraw %}

```kotlin
    foo: function () {
    },
    foo_1: function (param) {
    },
    foo_2: function (param, anotherParam) {
    }
```

{% raw %}
<p></p>
{% endraw %}

In addition, JavaScript native functions also allow passing extension literals as parameters.
## Standard Library

The standard library is being severely reworked. This includes introduction of <em>streams</em> (among other things, this will serve better compatibility with Java 8) and deprecation of some functions.
Some of the redesign has led to **breaking changes** to the library API. Most of the functionality is still available, but you may need to fix existing code slightly.
## IntelliJ IDEA Enhancements

### Copy/Paste now inserts imports

When copying and pasting code from one file to another, IntelliJ IDEA will now automatically import any packages required.
### Find Usages improvements

Find Usages now covers local classes. In addition you can now see the overrides as well as a hierarchical view of these.
### Smart Completion

Enhancements in code completion with support for enums, Java static members as well as anonymous objects.

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2014/03/smartcompletion1.gif"><img alt="smartcompletion1" class="alignnone size-full wp-image-1479" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2014/03/smartcompletion1.gif?resize=557%2C206&amp;ssl=1"/></a></p>
{% endraw %}

### Refactoring support

Certain rename refactoring such as local variables can now be done in-place without having to use a dialog box.

{% raw %}
<p><img alt="In-Place Rename Refactoring" class="alignnone wp-image-1452" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2014/03/inplacerename1.gif?resize=312%2C89&amp;ssl=1"/></p>
{% endraw %}

### Safe Delete

You can now safely delete symbols that are not used throughout the project with the Safe Delete refactoring
### Rename packages

Package rename and corresponding updates of all imports is now supported

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2014/03/renamepackage.png"><img alt="Rename Package" class="alignnone wp-image-1453" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2014/03/renamepackage.png?resize=321%2C116&amp;ssl=1"/></a></p>
{% endraw %}

### Integration with Java’s Move refactoring

When performing a Move refactoring of Java code, it now updates the corresponding usages in Kotlin code.
### Intentions

This release also brings a series of Intentions to IntelliJ IDEA, including:
#### Replacing Elvis operator with If conditional

The safe access operator, or elvis operator, can be now replaced with a more explicit if conditional when required just by simply using intentions.

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2014/03/elvis3.gif"><img alt="elvis3" class="alignnone size-full wp-image-1482" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2014/03/elvis3.gif?resize=473%2C116&amp;ssl=1"/></a></p>
{% endraw %}

####  Infix calls to dot qualified calls

Infix calls can be converted to dot qualified calls

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2014/03/infix.gif"><img alt="infix" class="alignnone size-full wp-image-1471" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2014/03/infix.gif?resize=473%2C90&amp;ssl=1"/></a></p>
{% endraw %}

#### Convert to expression body

Ability to convert a function with a simple return statement to an expression

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2014/03/convertbody.gif"><img alt="convertbody" class="alignnone size-full wp-image-1472" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2014/03/convertbody.gif?resize=473%2C90&amp;ssl=1"/></a></p>
{% endraw %}

#### Add and remove braces from simple variable names in string templates

When we have variable names in string templates, we can easily add or remove curly braces

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2014/03/stringtemplates.gif"><img alt="stringtemplates" class="alignnone size-full wp-image-1473" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2014/03/stringtemplates.gif?resize=473%2C90&amp;ssl=1"/></a></p>
{% endraw %}

In addition to the above, there’s also

* Support for IntelliJ IDEA 13.1 and Android Studio
* Performance improvements through lazy analysis, leading to better interop speed with Java also.
* Improvements in the Java2Kotlin Converter, leading to cleaner code and including better copy/paste behaviour.
* Improvements in Code Formatter

## Other improvements

In addition, there are some other bug fixes and features

* Improved Control-Flow Analysis resulting in fixing some existing bugs.
* More bootstrapping. We’re using more and more Kotlin in Kotlin.
* Some more improvements to the Kotlin standard library.

You can find the Compiler and Plugin on our [release page on GitHub](https://github.com/JetBrains/kotlin/releases/tag/build-0.7.270) .<br/>
If you’re using IntelliJ IDEA, you can download the latest plugin from [our repository](http://plugins.jetbrains.com/plugin?pr=idea&pluginId=6954) or update it directly via Plugins in IntelliJ IDEA. Kotlin M7 requires IntelliJ IDEA 13.1.
