---
title: "[译]Kotlin M1 is Out!"
date: 2012-04-12 09:37:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2012/04/kotlin-m1-is-out/
translator:
translator_url:
---

今天，我们很高兴地宣布：M1：Kotlin的第一个里程碑版本**
Kotlin的主页（ [kotlin.jetbrains.org](http://kotlin.jetbrains.org) ）提供有关语言的完整详细信息。在这篇文章中，我提供了与里程碑版本相关的一些亮点。
## 盒子里有什么东西

Kotlin以IntelliJ IDEA**的**独立编译器**和**插件的形式出现。

* IntelliJ IDEA插件

Kotlin毕业于官方插件库！
* Kotlin毕业于官方插件库！
* 独立编译器（在这里下载）

见 [入门指南](http://confluence.jetbrains.net/display/Kotlin/Getting+Started) 详细信息。
## 标准库

Kotlin的 [标准库](http://jetbrains.github.com/kotlin/versions/snapshot/apidocs/index.html) 提供了许多有用的功能，包括现有Java API的增强功能。例如，<span id =“more-514”> </span>可以使用集合中的map（）/ filter（）/ etc进行批量数据处理：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val minors = users.filter { it.age < 21 }
```

{% raw %}
<p></p>
{% endraw %}

或者您可以简单地*从java.io.File中读取文本：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val text = file.readText("UTF-8")
```

{% raw %}
<p></p>
{% endraw %}

甚至java.util.concurrent也变得更好：

{% raw %}
<p></p>
{% endraw %}

```kotlin
myReentrantLock.read {
    // read your data
}
```

{% raw %}
<p></p>
{% endraw %}

请参阅标准库API文档 [这里](http://jetbrains.github.com/kotlin/versions/snapshot/apidocs/index.html) 。
## 构建工具

我们已经大大改善了Kotlin的Maven Integration。
首先，Kotlin的魔法文物现在已经发表了 [repository.jetbrains.com](http://repository.jetbrains.com/) 。<BR/>
查找构建Kotlin项目以及混合Java / Kotlin代码的说明 [这里](http://confluence.jetbrains.com/display/Kotlin/Kotlin+Build+Tools#KotlinBuildTools-Maven) 。
您仍然可以使用Kotlin [蚂蚁](http://confluence.jetbrains.com/display/Kotlin/Kotlin+Build+Tools#KotlinBuildTools-Ant) 和 [格里芬](https://github.com/griffon/griffon-kotlin-plugin) ， 当然。
## 什么是新的

这里我想指出一个改进：I​​DEA插件现在做非常丰富的语义突出显示，可以在设置对话框中进行调整：

{% raw %}
<p style="text-align: center"><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012/04/Settings.png"><img alt="" class="alignnone size-medium wp-image-520" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012/04/Settings.png?resize=300%2C292&amp;ssl=1"/></a></p>
{% endraw %}

有关更改的完整列表，请参阅提交历史记录 [github](https://github.com/JetBrains/kotlin/commits/) 和封闭的问题 [YouTrack](http://youtrack.jetbrains.com/issues/KT?q=resolved+date%3A+2012-02-14+..+2012-04-11) 。
的 [上一篇文章](http://blog.jetbrains.com/kotlin/2012/03/kotlin-m1-candidate/) 提供以下功能的一些细节：

* JDK API增强功能
* 扩展功能的代码完成
* KDoc  -  Kotlin的API文档生成器
* GitHub支持
* 注释
* 多行字符串模板
* 简单枚举
* 本地功能
* “Assert not null”operator（!!）
* 字节代码查看器

## 非常感谢

在一个很酷的项目上工作是很有趣的，但与伟大的人一起工作更好。我要感谢JetBrains的团队，JetBrains不在团队中的球员，但仍然帮助我们以及使Kotlin更快的外部贡献者，即：

* James Strachan：标准库和KDoc
* Hiram Chirino，Franck Rasolo，Mark Petrovic，Taro Nagasawa：标准图书馆改进
* Sergey Lukjanov，Stephen Milligan，Oleg Kunov：IDE改进
* Danno Ferrin：JVM后端错误修复

## 有一个漂亮的Kotlin！

