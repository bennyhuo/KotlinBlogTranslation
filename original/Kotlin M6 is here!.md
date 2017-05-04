---
title: "Kotlin M6 is here!"
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
translator:
translator_url:
---

We’ve reached our sixth milestone, and with it, have some great features in store, both in terms of language improvements as well as tooling.<span id="more-1155"></span>
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

and is now on any SAM interface (i.e. Callable(), Comparator(), etc.). The <em>Runnable </em>function is still available for those cases where required.
### Annotation Improvements

You can now have annotations with arguments of type <em>enum</em>, as well as arrays and the possibility of passing in a variable number of arguments with <em>vararg</em>.

{% raw %}
<p></p>
{% endraw %}

```kotlin
annotation class validate(val side: Side, vararg val props: String)
```

{% raw %}
<p></p>
{% endraw %}

where <em>Side</em> can be an enum

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

We covered [Static constants in Kotlin](http://blog.jetbrains.com/kotlin/2013/06/static-constants-in-kotlin/) previously. With this release, you can now use class objects and have their properties represented as true static fields in Java to assure 100% interoperability.
## Maven

For those of you using Maven, you’ll be pleased to know that Kotlin is now available on [Maven Central](http://www.maven.org) . Snapshot repository has also been moved to oss.sonatype.org. For more information about Maven support please see the documentation on [Maven support](http://confluence.jetbrains.com/display/Kotlin/Kotlin+Build+Tools#KotlinBuildTools-Maven) .
## Android Studio Support

You probably heard the news a few months back that Google has been working on a new development IDE called [Android Studio](http://developer.android.com/sdk/installing/studio.html) for developing Android applications, based on IntelliJ IDEA Community Edition. With this milestone, we now provide support for this IDE. You now have all the functionality you get for Kotlin in IntelliJ IDEA, in Android Studio also.  <img alt="Android Studio" border="0" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image.png?resize=640%2C477&amp;ssl=1" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;border-width: 0px"/> We’ll be taking a more in-depth look at Android Studio support including how to set up Gradle in to work with Kotlin as well as laying out the project in a separate post.
## New Refactorings

In addition to supporting Android Studio, we also have some new IDE refactoring available in M6.
### Inline Variable

You can make a variable inline with a simple key press.  <img alt="image" border="0" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image1.png?resize=381%2C162&amp;ssl=1" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;border-width: 0px"/>
### Split / Join Property Declarations

As you know, Kotlin allows properties to initialized on the declaration. IntelliJ IDEA now allows us to easily refactor this to two separate expressions using the <em>Split property declaration intention</em> or join them up again in a single one (using <em>Edit | Join Lines</em>).  <img alt="image" border="0" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image2.png?resize=247%2C68&amp;ssl=1" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;border-width: 0px"/>
### Safe Delete

You can now safely remove symbols that are not referenced in the project, including checking for references in comments and strings  <img alt="image" border="0" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image3.png?resize=189%2C164&amp;ssl=1" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;border-width: 0px"/>
### Unwrap / Remove Expressions

Same as the support for other languages in IDEA, you can now unwrap or remove expressions from inside the enclosing statements, via the <strong>Code | Unwrap/Remove</strong> Refactoring.  <img alt="image" border="0" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/08/image4.png?resize=384%2C123&amp;ssl=1" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;border-width: 0px"/>
## Other Features and Improvements

In addition to the above features, this release also brings some other goodies

* Performance improvements. We have been working to improve performance including faster completion and some other general performance enhancements. More work is needed but we’re on the right track.
* TestNG. You can now right-click on a class or function and run the test using TestNG (thanks to Jayson Minard).

<span><a href="http://plugins.jetbrains.com/plugin?pr=idea&amp;pluginId=6954">Download</a> it now</span> and give it a try and [please let us know if you have any issues](http://youtrack.jetbrains.com/issues/kotlin) . Important: If you’re using [IntelliJ 13 EAP](http://eap.jetbrains.com/idea) , please note you need the latest build to work with this release.
