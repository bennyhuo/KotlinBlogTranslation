---
title: "[译]Gradle Daemon Support for Faster Compilation"
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

我们正在努力改进编译时间。今天我们很高兴邀请您尝试使用Gradle守护进程的Kotlin `0.12.1230`。它消除了启动成本，并且您的构建运行速度更快。 <span id =“more-2419”> </span>
## 背景

除了其他的方式，JVM的编译器和预热活动的加载类似乎在执行`kotlinc`的时候有很大的贡献。这就是为什么我们正在研究如何一次又一次地使用相同的编译器实例：不需要加载可以提供更好的编译时间。
由于在JVM上运行的其他工具似乎也遇到同样的问题，因此有大量的基础设施可以帮助这些事情。 Gradle有它的 [守护进程](https://docs.gradle.org/current/userguide/gradle_daemon.html) ，一个长期运行的过程（实际上可以是许多进程），其基本功能是保持工具加载，从而运行它们，而不需要加载类和JIT编译的启动成本。
## 试试看

我们已经修复了一些阻止Kotlin利用此功能的问题。它在Gradle 2.4及更高版本中可靠工作（对于Gradle升级说明，请参阅 [Gradle文档](https://docs.gradle.org/current/userguide/gradle_wrapper.html) ）。默认情况下，Android Studio会使用该守护程序，因此您无需太多工作，只需在您的`build.gradle`文件中指定Kotlin版本“0.12.1230”即可：

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

**注意**：仅在几次运行构建之后才能获得全面的加速。我们第一次感冒，等待热身，第二次大部分的预热都消失了，构建速度更快。由于JIT，后续运行也可能稍快一些。
## 反馈

请告诉我们，如果您的版本随着这一变化而变得更快。一些项目细节（如LOC和实际构建时间）将不胜感激。
谢谢！
