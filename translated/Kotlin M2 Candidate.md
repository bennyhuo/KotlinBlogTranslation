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

这是七个星期了 [Kotlin M1发行](http://blog.jetbrains.com/kotlin/2012/04/kotlin-m1-is-out/) ，我很高兴邀请您尝试一下Kotlin M2**的候选版本！这篇文章概述了即将到来的里程碑版本以及使用说明。
## 谢谢你，M1！

我们的M1建设做得相当不错：有了 [800下载](http://plugins.intellij.net/plugin/?id=6954) ，并给我们带来了广泛的反馈 [论坛](http://devnet.jetbrains.com/community/kotlin) 和 [问题追踪器](http://youtrack.jetbrains.net/issues/KT) 。
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

和往常一样 [修复了很多错误](http://youtrack.jetbrains.com/issues/KT?q=resolved+date%3A+2012-04-12+..+2012-06-07) 。我想指出，我们正在研究IDE的性能。在M2方面有所改善，并将在下一个里程碑上达到真正的速度。
## 语言特点

现在Kotlin尊重**可见性修饰符**。我们有四个：

* 私人，保护，公开 - 像往常一样，
* 内部 - 在模块内可见（这不仅仅是一个包）。

您现在可以将**数组值传递给vararg函数**：

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

**传播**操作符将“数组”转换为变量列表。与Java不同，这并不表示任何丑角。
稍后会有更多的好东西。
## IDE中的JavaScript支持

虽然您仍然可以直接在浏览器中与Kotlin一起玩 [Kotlin网络演示](http://kotlin-demo.jetbrains.com) 现在，Kotlin现在已经编译成了一个真正的IDE。
当你 [安装IntelliJ IDEA插件的M2候选版本](#install) ，请按照以下说明尝试一些Kotlin-to-JS编译：

* 从github查看kotlin-js-hello项目
* 将其作为IntelliJ IDEA项目打开
* 将其设置为Kotlin-JS项目
* 选择您喜欢的浏览器并运行。结果将在浏览器中打开。
* 随时随地编辑JavaScript文件，并重新运行...

目前，API文档正在准备中。同时，您可以学习Kotlin的JS API [这里](https://github.com/JetBrains/kotlin/tree/master/js/js.libraries/src) 。
## Android

修复一些bug后，发现很多有趣的东西（特别感谢 [Aleksandro Eterverda](https://github.com/eterverda) ），我们准备在Android上运行Kotlin！

{% raw %}
<p style="text-align: center"><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/06/KotlinDroid.png"><img alt="" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/06/KotlinDroid.png?resize=250%2C136&amp;ssl=1"/></a></p>
{% endraw %}


* 您需要安装Android SDK并进行设置
* IntelliJ IDEA的开源版本提供对Android的IDE支持
* 安装IntelliJ IDEA插件的M2候选版本
* 要快速启动，请查看github中的kotlin-android-hello项目
* 设置运行配置，并运行项目（在这里一步一步）
* 请享用

在Android上运行的其他一些Kotlin程序

* 我们正在将标准Android样本移植到Kotlin：kotlin-samples-for-android。随意贡献！
* Vladimir Lichonos为Android安装了一组有用的Kotlin实用程序：kotlinAndroidLib

## 如何安装候选版本


* 获取IntelliJ IDEA（Community或Ultimate）版本11.1。

如果您想将您的工作环境与Kotlin实验分开，请按照此处的说明进行操作
* 如果您想将您的工作环境与Kotlin实验分开，请按照此处的说明进行操作
* 设置Integration Build Plugin Repository并安装插件。分步说明。

## 像往常一样，您的反馈非常受欢迎。有一个漂亮的Kotlin！


{% raw %}
<hr/>
{% endraw %}


{% raw %}
<p> </p>
{% endraw %}

此页面的部分是基于创建的工作进行的修改 [由Google分享](http://code.google.com/policies.html) 并根据术语描述使用 [知识共享3.0归属许可](http://creativecommons.org/licenses/by/3.0/) 。
