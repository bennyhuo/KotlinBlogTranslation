---
title: "Gradle Daemon Support for Faster Compilation"
date: 2015-08-05 15:20:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/08/gradle-daemon-support-for-faster-compilation/
translator:
translator_url:
---

We are currently working on improving compilation times. Today we are happy to invite you to try Kotlin <code>0.12.1230</code> making use of the Gradle Daemon. It eliminates startup costs, and your builds run faster. <span id="more-2419"></span>
## Background

Among other things, loading classes of the compiler and warmup activities of the JVM seem to contribute a lot to the time it takes <code>kotlinc</code> to run. This is why we are looking into ways of using the same compiler instance over and over again: no need for loading gives better compilation times.
Since other tools running on the JVM seem to suffer from the same issues, there’s substantial infrastructure facilitating such things. Gradle has its [Daemon](https://docs.gradle.org/current/userguide/gradle_daemon.html) , a long-running process (actually, it can be many processes) whose essential function is to keep tools loaded and therefore run them without the startup costs of class loading and JIT-compilation.
## Try it out

We have fixed some issues that prevented Kotlin to leverage this functionality. It works reliably in Gradle 2.4 and higher (for Gradle upgrade instructions see [Gradle docs](https://docs.gradle.org/current/userguide/gradle_wrapper.html) ). Android Studio uses the daemon by default, so you don’t have much to do, simply specify Kotlin version “0.12.1230” in your <code>build.gradle</code> file:

{% raw %}
<p></p>
{% endraw %}

```kotlin
buildscript {
  repositories {
    ...
  }
  dependencies {
    classpath 'org.jetbrains.kotlin:kotlin-gradle-plugin:0.12.1230'
    ...
  }
}
 
```

{% raw %}
<p></p>
{% endraw %}

<strong>NOTE</strong>: we get the full-scale speedups only after a few runs of the build. The first time we run cold and wait for the warmup, the second time most of the warmup is gone, and the build completes faster. Subsequent runs may get slightly faster too, because of the JIT.
## Feedback

Please tell us if your builds have gotten faster with this change. Some project details (like LOCs and actual build times) would be appreciated.
Thanks!
