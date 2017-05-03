---
title: "Kotlin 1.1.1 is out"
date: 2017-03-14 20:29:00
author: Dmitry Jemerov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/03/kotlin-1-1-1-is-out/
translator:
translator_url:
---

Today we’re releasing the first bugfix update for <strong>Kotlin 1.1</strong>. The primary focus of this update is to address regressions causing incorrect code generation; we wanted to get those fixes out as quickly as possible. The details are available in the [changelog](https://github.com/JetBrains/kotlin/blob/1.1.1/ChangeLog.md) .
The specific changes worth highlighting are:

* Gradle incremental compilation is now enabled by default. You can still turn it off as described in the documentation if you need to.
* Kotlin plugins are now available in the Gradle plugin portal. See the documentation for usage instructions.
* Using function types with receivers as parameter types of JavaScript external declarations is no longer allowed. Previously, lambdas passed to such parameters weren’t invoked with correct arguments, and there’s no easy workaround for this issue, so for now we’ve decided to disable the functionality.

We’ve also updated the Kotlin [Eclipse](https://marketplace.eclipse.org/content/kotlin-plugin-eclipse) and [NetBeans](http://plugins.netbeans.org/plugin/68590/kotlin) plugins to include Kotlin 1.1.1, so you can enjoy the benefits of the new Kotlin version regardless of your IDE choice.
## How to update

To update the IDEA plugin, use Tools | Kotlin | Configure Kotlin Plugin Updates and press the “Check for updates now” button. Also, don’t forget to update the compiler and standard library version in your Maven and Gradle build scripts.<br/>

The command-line compiler can be downloaded from the [Github release page](https://github.com/JetBrains/kotlin/releases/tag/v1.1.1) .
As usual, if you run into any problems with the new release, you’re welcome to ask for help on the [forums](https://discuss.kotlinlang.org/) , on Slack (get an invite [here](http://kotlinslackin.herokuapp.com/) ), or to report issues in the [issue tracker](https://youtrack.jetbrains.com/issues/KT) .
Let’s Kotlin!
