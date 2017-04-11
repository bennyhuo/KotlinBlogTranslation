---
title: Kotlin M6 is here!
date: 2013-08-12 21:09:00
author: Hadi Hariri
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2013/08/kotlin-m6-is-here/
---

We’ve reached our sixth milestone, and with it, have some great features in store, both in terms of language improvements as well as tooling.
## Language Improvements


{% raw %}
<p><a name="SAM-conversions"></a></p>
{% endraw %}

### SAM Conversions

We have completed the initial support we provided for calling Java interfaces with Single Abstract Methods in M5.2. You can now simply do

{% raw %}
<p></p>
{% endraw %}

```kotlin
SwingUtilities.invokeLater { doItNow() }
```

{% raw %}
<p></p>
{% endraw %}

and is now on any SAM interface (i.e. Callable(), Comparator(), etc.). The Runnable function is still available for those cases where required.
### Annotation Improvements

You can now have annotations with arguments of type enum, as well as arrays and the possibility of passing in a variable number of arguments with vararg.

{% raw %}
<p></p>
{% endraw %}

```kotlin
annotation class validate(val side: Side, vararg val props: String)
```

{% raw %}
<p></p>
{% endraw %}

where Side can be an enum

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Side {
   Client
   Server
   Both
}
```

{% raw %}
<p></p>
{% endraw %}

### Static Fields

We covered Static constants in Kotlin previously. With this release, you can now use class objects and have their properties represented as true static fields in Java to assure 100% interoperability.
## Maven

For those of you using Maven, you’ll be pleased to know that Kotlin is now available on Maven Central. Snapshot repository has also been moved to oss.sonatype.org. For more information about Maven support please see the documentation on Maven support.
## Android Studio Support

You probably heard the news a few months back that Google has been working on a new development IDE called Android Studio for developing Android applications, based on IntelliJ IDEA Community Edition. With this milestone, we now provide support for this IDE. You now have all the functionality you get for Kotlin in IntelliJ IDEA, in Android Studio also.   We’ll be taking a more in-depth look at Android Studio support including how to set up Gradle in to work with Kotlin as well as laying out the project in a separate post.
## New Refactorings

In addition to supporting Android Studio, we also have some new IDE refactoring available in M6.
### Inline Variable

You can make a variable inline with a simple key press.
### Split / Join Property Declarations

As you know, Kotlin allows properties to initialized on the declaration. IntelliJ IDEA now allows us to easily refactor this to two separate expressions using the Split property declaration intention or join them up again in a single one (using Edit | Join Lines).
### Safe Delete

You can now safely remove symbols that are not referenced in the project, including checking for references in comments and strings
### Unwrap / Remove Expressions

Same as the support for other languages in IDEA, you can now unwrap or remove expressions from inside the enclosing statements, via the Code | Unwrap/Remove Refactoring.
## Other Features and Improvements

In addition to the above features, this release also brings some other goodies

* Performance improvements. We have been working to improve performance including faster completion and some other general performance enhancements. More work is needed but we’re on the right track.
* TestNG. You can now right-click on a class or function and run the test using TestNG (thanks to Jayson Minard).

Download it now and give it a try and please let us know if you have any issues. Important: If you’re using IntelliJ 13 EAP, please note you need the latest build to work with this release.
