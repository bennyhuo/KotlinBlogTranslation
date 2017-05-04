---
title: "[译]Kotlin M2 Candidate"
date: 2012-06-04 08:53:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2012/06/kotlin-m2-candidate/
translator:
translator_url:
---

这是七个星期了 [Kotlin M1 发行](http://blog.jetbrains.com/kotlin/2012/04/kotlin-m1-is-out/) ，我很高兴邀请您尝试一下 Kotlin M2**的候选版本！这篇文章概述了即将到来的里程碑版本以及使用说明。
## 谢谢你，M1！

我们的 M1 建设做得相当不错：有了 [800 下载](http://plugins.intellij.net/plugin/?id=6954) ，并给我们带来了广泛的反馈 [论坛](http://devnet.jetbrains.com/community/kotlin) 和 [问题追踪器](http://youtrack.jetbrains.net/issues/KT) 。
似乎你已经有了一些乐趣，我们的目标是更加有趣的<img alt =“:)”class =“wp-smiley”data-recalc-dims =“1”src =“https：// i2 .wp.com / blog.jetbrains.com / kotlin / wp-includes / images / smilies / simple-smile.png？w = 640＆amp; ssl = 1“style =”height：1em; max-height：1em“ >
## 什么是新的


* 小东西
* 语言特点
* JavaScript
* Android
* 如何安装候选版本


{% raw %}
<p><span id="more-550"></span></p>
{% endraw %}

## 小东西

和往常一样 [修复了很多错误](http://youtrack.jetbrains.com/issues/KT?q=resolved+date%3A+2012-04-12+..+2012-06-07) 。我想指出，我们正在研究 IDE 的性能。在 M2 方面有所改善，并将在下一个里程碑上达到真正的速度。
## 语言特点

现在 Kotlin 尊重**可见性修饰符**。我们有四个：

* 私人，保护，公开 - 像往常一样，
* 内部 - 在模块内可见（这不仅仅是一个包）。

您现在可以将**数组值传递给 vararg 函数**：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun printAll(vararg a : String) {
    for (item in a) println(item)
}
 
fun main(args: Array<String>) {
    printAll("one", "two")
    printAll(*args)
}
```

{% raw %}
<p></p>
{% endraw %}

**传播**操作符将“数组”转换为变量列表。与 Java 不同，这并不表示任何丑角。
稍后会有更多的好东西。
## IDE 中的 JavaScript 支持

虽然您仍然可以直接在浏览器中与 Kotlin 一起玩 [Kotlin 网络演示](http://kotlin-demo.jetbrains.com) 现在，Kotlin 现在已经编译成了一个真正的 IDE。
当你 [安装 IntelliJ IDEA 插件的 M2 候选版本](#install) ，请按照以下说明尝试一些 Kotlin-to-JS 编译：

* 从 github 查看 kotlin-js-hello 项目
* 将其作为 IntelliJ IDEA 项目打开
* 将其设置为 Kotlin-JS 项目
* 选择您喜欢的浏览器并运行。结果将在浏览器中打开。
* 随时随地编辑 JavaScript 文件，并重新运行...

目前，API 文档正在准备中。同时，您可以学习 Kotlin 的 JS API [这里](https://github.com/JetBrains/kotlin/tree/master/js/js.libraries/src) 。
## Android

修复一些 bug 后，发现很多有趣的东西（特别感谢 [Aleksandro Eterverda](https://github.com/eterverda) ），我们准备在 Android 上运行 Kotlin！

{% raw %}
<p style="text-align: center"><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/06/KotlinDroid.png"><img alt="" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/06/KotlinDroid.png?resize=250%2C136&amp;ssl=1"/></a></p>
{% endraw %}


* 您需要安装 Android SDK 并进行设置
* IntelliJ IDEA 的开源版本提供对 Android 的 IDE 支持
* 安装 IntelliJ IDEA 插件的 M2 候选版本
* 要快速启动，请查看 github 中的 kotlin-android-hello 项目
* 设置运行配置，并运行项目（在这里一步一步）
* 请享用

在 Android 上运行的其他一些 Kotlin 程序

* 我们正在将标准 Android 样本移植到 Kotlin：kotlin-samples-for-android。随意贡献！
* Vladimir Lichonos 为 Android 安装了一组有用的 Kotlin 实用程序：kotlinAndroidLib

## 如何安装候选版本


* 获取 IntelliJ IDEA（Community 或 Ultimate）版本 11.1。

如果您想将您的工作环境与 Kotlin 实验分开，请按照此处的说明进行操作
* 如果您想将您的工作环境与 Kotlin 实验分开，请按照此处的说明进行操作
* 设置 Integration Build Plugin Repository 并安装插件。分步说明。

## 像往常一样，您的反馈非常受欢迎。有一个漂亮的 Kotlin！


{% raw %}
<hr/>
{% endraw %}


{% raw %}
<p> </p>
{% endraw %}

此页面的部分是基于创建的工作进行的修改 [由 Google 分享](http://code.google.com/policies.html) 并根据术语描述使用 [知识共享 3.0 归属许可](http://creativecommons.org/licenses/by/3.0/) 。
