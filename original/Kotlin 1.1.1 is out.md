---
title: Kotlin 1.1.1 is out
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
---

Today we’re releasing the first bugfix update for Kotlin 1.1. The primary focus of this update is to address regressions causing incorrect code generation; we wanted to get those fixes out as quickly as possible. The details are available in the changelog.
The specific changes worth highlighting are:

* Gradle incremental compilation is now enabled by default. You can still turn it off as described in the documentation if you need to.
* Kotlin plugins are now available in the Gradle plugin portal. See the documentation for usage instructions.
* Using function types with receivers as parameter types of JavaScript external declarations is no longer allowed. Previously, lambdas passed to such parameters weren’t invoked with correct arguments, and there’s no easy workaround for this issue, so for now we’ve decided to disable the functionality.

We’ve also updated the Kotlin Eclipse and NetBeans plugins to include Kotlin 1.1.1, so you can enjoy the benefits of the new Kotlin version regardless of your IDE choice.
## How to update

To update the IDEA plugin, use Tools | Kotlin | Configure Kotlin Plugin Updates and press the “Check for updates now” button. Also, don’t forget to update the compiler and standard library version in your Maven and Gradle build scripts.
The command-line compiler can be downloaded from the Github release page.
As usual, if you run into any problems with the new release, you’re welcome to ask for help on the forums, on Slack (get an invite here), or to report issues in the issue tracker.
Let’s Kotlin!
