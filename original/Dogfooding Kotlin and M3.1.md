---
title: Dogfooding Kotlin and M3.1
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

After releasing Kotlin M3, we immediately started dogfooding Kotlin. Working on KAnnotator — a static analysis tool that will automatically infer nullability annotations for libraries — helps us tremendously at prioritizing issues. As a result, we roll out a bugfix update: Kotlin M3.1 (list of closed issues). We recommend to run it with the latest IntelliJ IDEA 12 EAP.
A few highlights:

* A bunch of annoying exceptions and performance problems.
* Referring to inner enums fixed.
* Super-calls from object literals fixed.
* A few back-end fixes, including bridge methods and debugger-related things.
* You can now run all tests in a package/module.

BTW, this talk I presented at JavaOne a week ago covers some new features in M3. Slides are available here. Other talks can be watched here.

{% raw %}
<p> </p>
{% endraw %}

