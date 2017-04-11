---
title: [译]Kotlin M1 is Out!
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
---

今天我们很高兴地宣布，M1：科特林的第一个里程碑式的发布。
Kotlin的主页（kotlin.jetbrains.org）提供了关于语言的全部细节。在这篇文章中，我提供了与里程碑版本相关的一些亮点。
## 盒子里有什么东西

Kotlin以IntelliJ IDEA独立编译器和插件的形式出现。

* IntelliJ IDEA插件

Kotlin毕业于官方插件库！
* Kotlin毕业于官方插件库！
* 独立编译器（在这里下载）

有关详细信息，请参阅入门指南。
## 标准库

Kotlin的标准库提供了许多有用的功能，包括对现有Java API的增强。例如，它可以使用集合中的map（）/ filter（）/ etc进行批量数据处理：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val minors = users.filter { it.age < 21 }
```

{% raw %}
<p></p>
{% endraw %}

或者您可以从java.io.File中简单地读取文本：

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

请参阅此处的标准库API文档。
## 构建工具

我们已经大大改善了Kotlin的Maven Integration。
首先，Kotlin的maven文物现已发布在repository.jetbrains.com。
查找有关构建Kotlin项目的说明以及Java / Kotlin混合代码。
当然，您仍然可以使用Kotlin与Ant和Griffon。
## 什么是新的

这里我想指出一个改进：I​​DEA插件现在做非常丰富的语义突出显示，可以在设置对话框中进行调整：

{% raw %}
<p style="text-align: center"><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012/04/Settings.png"><img alt="" class="alignnone size-medium wp-image-520" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012/04/Settings.png?resize=300%2C292&amp;ssl=1"/></a></p>
{% endraw %}

有关更改的完整列表，请参阅github中的提交历史记录以及YouTrack中的已关闭问题。
以前的帖子提供了以下功能的一些细节：

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

