---
title: "Fibers and Actors in Kotlin with Quasar"
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
translator:
translator_url:
---

In the [previous post](http://blog.jetbrains.com/kotlin/2015/05/kotlin-m12-is-out/) we mentioned that the [Quasar](http://docs.paralleluniverse.co/quasar/) library now supports Kotlin, providing awesome support for fibers (lightweight threads), Go-like channels, Erlang-like actors, and other asynchronous tools.
Our friends from [Parallel Universe](http://www.paralleluniverse.co/) have published a [blog post](http://blog.paralleluniverse.co/2015/06/04/quasar-kotlin/) that dives into details of using Quasar with Kotlin. Even in the unlikely case that multithreading doesn’t concern you much, Quasar/Kotlin integration is a great example of a “DSL” library written in Kotlin, it uses

* data classes
* top-level functions
* lambdas
* annotated expressions
* when-expressions
* inline functions

to build a natural-looking and efficient API, and the [blog post](http://blog.paralleluniverse.co/2015/06/04/quasar-kotlin/) explains it very well.
Enjoy!
