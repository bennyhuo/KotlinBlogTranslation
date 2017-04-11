---
title: [译]Kotlin M2 Candidate
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
---

自Kotlin M1发布以来已经有七个星期了，我很高兴邀请您尝试Kotlin M2的候选版本！这篇文章概述了即将到来的里程碑版本以及使用说明。
## 谢谢你，M1！

我们的M1版本做得相当不错：大约有800个下载，并在我们的论坛和问题跟踪器中提供了广泛的反馈。
看起来好像你有一些乐趣，我们的目标是更加有趣
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

像往常一样，修复了很多错误。我想指出，我们正在研究IDE的性能。在M2方面有所改善，并将在下一个里程碑上达到真正的速度。
## 语言特点

科特林现在尊重知名度调节器。我们有四个：

* 私人，保护，公开 - 像往常一样，
* 内部 - 在模块内可见（这不仅仅是一个包）。

您现在可以将一组值传递给vararg函数：

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

扩展运算符将数组转换为变量列表。与Java不同，这并不表示任何丑角。
稍后会有更多的好东西。
## IDE中的JavaScript支持

虽然您仍然可以使用Kotlin Web Demo在浏览器中直接播放Kotlin，但现在有一个真正的IDE用于Kotlin编译为JavaScript。
当您安装IntelliJ IDEA插件的M2候选版本时，请按照以下说明尝试一些Kotlin-to-JS编译：

* 从github查看kotlin-js-hello项目
* 将其作为IntelliJ IDEA项目打开
* 将其设置为Kotlin-JS项目
* 选择您喜欢的浏览器并运行。结果将在浏览器中打开。
* 随时随地编辑JavaScript文件，并重新运行...

目前，API文档正在准备中。同时，您可以在这里学习Kotlin的JS API。
## Android

修复了一些错误并发现了很多有趣的东西（特别感谢Aleksandro Eterverda），我们已经准备好在Android上运行Kotlin！

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

本页的部分内容是根据Google创建和共享的作品进行的修改，并根据Creative Commons 3.0 Attribution License中描述的条款使用。
