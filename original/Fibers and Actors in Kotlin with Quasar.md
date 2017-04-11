---
title: Fibers and Actors in Kotlin with Quasar
date: 2015-06-04 18:44:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/06/fibers-and-actors-in-kotlin-with-quasar/
---

In the previous post we mentioned that the Quasar library now supports Kotlin, providing awesome support for fibers (lightweight threads), Go-like channels, Erlang-like actors, and other asynchronous tools.
Our friends from Parallel Universe have published a blog post that dives into details of using Quasar with Kotlin. Even in the unlikely case that multithreading doesn’t concern you much, Quasar/Kotlin integration is a great example of a “DSL” library written in Kotlin, it uses

* data classes
* top-level functions
* lambdas
* annotated expressions
* when-expressions
* inline functions

to build a natural-looking and efficient API, and the blog post explains it very well.
Enjoy!
