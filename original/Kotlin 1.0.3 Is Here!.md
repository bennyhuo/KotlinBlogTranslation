---
title: Kotlin 1.0.3 Is Here!
date: 2016-06-30 18:52:00
author: Roman Belov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2016/06/kotlin-1-0-3-is-here/
---

We are delighted to present Kotlin 1.0.3. This update is not full of brand new and shiny features, it is more about bug fixes, tooling improvements and performance boosts. That’s why you’ll like it 😉 Take a look at the full change log and issues stats by subsystem:
Specifically we want to express our gratitude to our contributors whose commits are included in 1.0.3 namely Yaroslav Ulanovych, Jake Wharton and Kirill Rakhman. Kirill has done more than a dozen improvements to formatter and submitted 20+ commits — great job, Kirill, we really appreciate it. Here we also want to thank each and every one of our EAP users who tested and provided their priceless feedback on 1.0.3 prerelease builds.
Although this update is not feature-rich, there are several important improvements and features which are worth highlighting here:
## What’s new in the compiler:


* New option -jdk-home to specify the JDK against which the code is compiled
* Options to specify Kotlin language version (-language-version) and target Java version (-jvm-target) (will have effect in 1.1, added now for forward compatibility)
* More efficient bytecode (no more iterator in indices loop, avoid unnecessary operations with Unit)
* Various improvements to diagnostic messages

## What’s new in the IDE:


* Autosuggestion for Java to Kotlin conversion for Java code copied from browser and other sources outside of the IDE

