---
title: "Dogfooding Kotlin and M3.1"
date: 2012-10-10 13:06:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2012/10/dogfooding-kotlin-and-m3-1/
---

After releasing  [Kotlin M3](http://blog.jetbrains.com/kotlin/2012/09/kotlin-m3-is-out/) , we immediately started  [dogfooding](http://en.wikipedia.org/wiki/Eating_your_own_dog_food)  Kotlin. Working on  [KAnnotator](https://github.com/abreslav/kannotator)  — a static analysis tool that will automatically infer nullability annotations for libraries — helps us tremendously at prioritizing issues. As a result, we roll out a bugfix update:  [Kotlin M3.1](http://plugins.intellij.net/plugin?pr=idea&pluginId=6954)  ( [list of closed issues](http://youtrack.jetbrains.com/issues/KT?q=resolved+date%3A+2012-09-12+..+2012-10-10) ). We recommend to run it with the latest  [IntelliJ IDEA 12 EAP](http://confluence.jetbrains.com/display/IDEADEV/IDEA+12+EAP) .
A few highlights:<span id="more-710"></span>

* A bunch of annoying exceptions and performance problems.
* Referring to inner enums fixed.
* Super-calls from object literals fixed.
* A few back-end fixes, including bridge methods and debugger-related things.
* You can now run all tests in a package/module.

BTW,  [this talk](http://blueskybd.vo.llnwd.net/o16/oracle/CON5934_mp4_5934_001.html)  I presented at  [JavaOne](https://oracleus.activeevents.com/connect/sessionDetail.ww?SESSION_ID=5934)  a week ago covers some new features in M3. Slides are available  [here](http://confluence.jetbrains.net/display/Kotlin/Talks+and+Publications) . Other talks can be watched  [here](http://confluence.jetbrains.net/display/Kotlin/Talks+and+Publications) .

{% raw %}
<p> </p>
{% endraw %}

