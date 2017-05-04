---
title: "Kotlin 1.1 Release Candidate is Here"
date: 2017-02-17 13:37:00
author: Mikhail Glukhikh
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/02/kotlin-1-1-release-candidate-is-here/
translator:
translator_url:
---

As of today, Kotlin 1.1 has finally reached the release candidate stage. This means that most of our development work is done, we’re happy with the results, and we’ll soon publish them as a final Kotlin 1.1 release. We’ve done a lot of testing for this release internally, but the real world is always more varied than any test environment, so we need your help. Please try this build, and let us know about your experience!

{% raw %}
<p><img alt="11RC-01" class="alignnone size-full wp-image-4599" height="251" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/02/11RC-01.png" width="1300"/><br/>
<span id="more-4589"></span></p>
{% endraw %}

The only new feature in the release candidate is the `takeUnless` function – a counterpart of [takeIf](https://kotlinlang.org/docs/reference/whatsnew11.html#takeif-and-also) (added earlier in 1.1) but with an inverted condition. As for bugfixes, there’s much more, and the [changelog](https://github.com/JetBrains/kotlin/blob/1.1-rc/ChangeLog.md) gives you a complete list. Among other things, we’ve fixed several performance problems in the IDE – both long-standing sore points and recent regressions.
## Migration Notes

As we [noted](https://blog.jetbrains.com/kotlin/2017/01/kotlin-1-1-beta-is-here/) earlier, all binaries produced by pre-release versions are outlawed by the compiler: you’re now **required to recompile** everything that was compiled by 1.1‑M0x and Beta’s. All the code from 1.0.x is, of course, perfectly fine without recompilation.
Up until now, you could run the Kotlin compiler under any version of Java starting with Java 6, but this is about to change – starting with one of the first 1.1.x updates, the compiler will only run under Java 8 or 9. To prepare you for the migration, the compiler now emits a warning if you run it under Java 6 or 7. Note that this only affects the build environment; **the compiled code is still compatible with Java 6 by default**, and we have no plans to remove the support for that.
The `.javaClass` extension property is now deprecated. As a replacement, please use `::class.java`. The IDE offers a quickfix to update usages, both individually and across the entire project.
To reduce the size of the JavaScript standard library, we’ve deprecated a lot of helper functions in the `kotlin.dom` and `kotlin.dom.build` packages, and we’re going to remove them in a future update.
## How to try it

**In Maven/Gradle:** Add `http://dl.bintray.com/kotlin/kotlin-eap-1.1` as a repository for the build script and your projects; use `1.1.0-rc-91` as the version number for the compiler and the standard library.
**In IntelliJ IDEA:** Go to <i>Tools → Kotlin → Configure Kotlin Plugin Updates</i>, then select “Early Access Preview 1.1” in the <i>Update channel</i> drop-down list, then press <i>Check for updates</i>.
**In Eclipse**: install the plugin with the following update site<br/>
`https://dl.bintray.com/jetbrains/kotlin/eclipse-plugin/0.8.0`
**The command-line compiler** can be downloaded from the [Github release page](https://github.com/JetBrains/kotlin/releases/tag/v1.1-rc) .
**On <a href="http://try.kotlinlang.org/">try.kotlinlang.org</a>**.
Let’s Kotlin!
