---
title: "Kotlin M1 is Out!"
date: 2012-04-12 09:37:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2012/04/kotlin-m1-is-out/
---

Today we are pleased to announce M1: the first milestone release of <strong>Kotlin</strong>.<br/>
Kotlin’s homepage ( [kotlin.jetbrains.org](http://kotlin.jetbrains.org) ) provides full details about the language. In this post I give some highlights associated with the milestone release.
## What’s in the box

Kotlin comes in form of a <strong>standalone compiler </strong>and a <strong>plugin for IntelliJ IDEA</strong>.

* IntelliJ IDEA Plugin

Kotlin has graduated to the official plugin repository!
* Kotlin has graduated to the official plugin repository!
* Standalone Compiler (download here)

See the  [Getting Started guide](http://confluence.jetbrains.net/display/Kotlin/Getting+Started)  for details.
## Standard library

Kotlin’s  [Standard Library](http://jetbrains.github.com/kotlin/versions/snapshot/apidocs/index.html)  provides many useful functions, including enhancements for existing Java APIs. For example, <span id="more-514"></span>it enables bulk data processing with map()/filter()/etc available on collections:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val minors = users.filter { it.age < 21 }
```

{% raw %}
<p></p>
{% endraw %}

Or you can <em>simply</em> read text from a java.io.File:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val text = file.readText("UTF-8")
```

{% raw %}
<p></p>
{% endraw %}

And even java.util.concurrent becomes nicer:

{% raw %}
<p></p>
{% endraw %}

```kotlin
myReentrantLock.read {
    // read your data
}
```

{% raw %}
<p></p>
{% endraw %}

See the Standard Library API documentation  [here](http://jetbrains.github.com/kotlin/versions/snapshot/apidocs/index.html) .
## Build tools

We have significantly improved Kotlin’s Maven Integration.
First of all, Kotlin’s maven artifacts are now published in  [repository.jetbrains.com](http://repository.jetbrains.com/) .<br/>
Find the instructions for building Kotlin projects as well as mixed Java/Kotlin code  [here](http://confluence.jetbrains.com/display/Kotlin/Kotlin+Build+Tools#KotlinBuildTools-Maven) .
You can still use Kotlin with  [Ant](http://confluence.jetbrains.com/display/Kotlin/Kotlin+Build+Tools#KotlinBuildTools-Ant)  and  [Griffon](https://github.com/griffon/griffon-kotlin-plugin) , of course.
## What’s new

Here I’d like to point out one improvement: the IDEA plugin now does very rich semantic highlighting that can be tweaked in the Settings dialog:

{% raw %}
<p style="text-align: center"><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012/04/Settings.png"><img alt="" class="alignnone size-medium wp-image-520" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012/04/Settings.png?resize=300%2C292&amp;ssl=1"/></a></p>
{% endraw %}

For the full list of changes, please see the commit history on  [github](https://github.com/JetBrains/kotlin/commits/)  and the closed issues in  [YouTrack](http://youtrack.jetbrains.com/issues/KT?q=resolved+date%3A+2012-02-14+..+2012-04-11) .
The  [previous post](http://blog.jetbrains.com/kotlin/2012/03/kotlin-m1-candidate/)  provides some details on the following features:

* JDK API enhancements
* Code completion for extension functions
* KDoc — API documentation generator for Kotlin
* GitHub support
* Annotations
* Multiline String Templates
* Simple Enums
* Local Functions
* “Assert not null” operator (!!)
* Byte code viewer

## Many thanks

Working on a cool project is a lot of fun, but working with great people is even better. I would like to thank our team at JetBrains, JetBrains guys who are not on the team, but still help us as well as the external contributors who make Kotlin move even faster, namely:

* James Strachan: Standard Library and KDoc
* Hiram Chirino, Franck Rasolo, Mark Petrovic, Taro Nagasawa: Standard Library improvements
* Sergey Lukjanov, Stephen Milligan, Oleg Kunov: IDE improvements
* Danno Ferrin: JVM back-end bug fix

## Have a nice Kotlin!

