---
title: "Kotlin 1.1: What’s coming in the standard library"
date: 2017-01-25 00:15:00
author: ilya.gorbunov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
translator:
translator_url:
source_url: https://blog.jetbrains.com/kotlin/2017/01/kotlin-1-1-whats-coming-in-the-standard-library/
---

## Java 9 preparations

Java 9 is coming and brings  [Project Jigsaw](http://openjdk.java.net/projects/jigsaw/spec/sotms/)  to the table — the Java platform module system. One of the constraints it imposes is that no two modules can declare public API in the same package. The situation, when there are two modules that contribute to the same package, is called “split” package.
We face this issue with split packages in our runtime artifacts: first, kotlin-runtime and kotlin-stdlib modules share a lot of kotlin.* packages, second, kotlin-runtime and kotlin-reflect share kotlin.reflect package. What we’re going to do to make our artifacts more friendly to the module system:

0. We merge kotlin-runtime and kotlin-stdlib into the single artifact kotlin-stdlib. Also we’re going to rename kotlin-runtime.jar, shipped in the compiler distribution, to kotlin-stdlib.jar, to reduce the amount of confusion caused by having differently named standard library in different build systems.

That rename will happen in two stages: in 1.1 there will be both kotlin-runtime.jar and kotlin-stdlib.jar with the same content in the compiler distribution, and in 1.2 the former will be removed.

