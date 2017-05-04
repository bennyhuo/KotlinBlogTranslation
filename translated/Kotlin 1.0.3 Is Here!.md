---
title: "[译]Kotlin 1.0.3 Is Here!"
date: 2016-06-30 18:52:00
author: Roman Belov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2016/06/kotlin-1-0-3-is-here/
translator:
translator_url:
---

我们很高兴地介绍 Kotlin 1.0.3**。这个更新不是全新的和闪亮的功能，更多的是关于错误修复，工具改进和性能提升。这就是为什么你会喜欢它😉看看充分 [更改日志](https://github.com/JetBrains/kotlin/blob/1.0.3/ChangeLog.md) 并通过子系统发布统计信息：
<img alt =“Kotlin 1.0.3。修复问题”class =“alignnone size-full wp-image-4043”src =“https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/06/Pasted-image -at-2016_06_28-07_25-PM.png“width =”800“/> <br/>
<span id =“more-4042”> </span> <br/>

具体来说，我们要向我们的贡献者表示感谢，他们的承诺包括在 1.0.3 中 [雅罗斯拉夫·乌兰诺维奇](https://github.com/yarulan) ， [杰克·沃顿](https://github.com/JakeWharton) 和 [基拉里·拉赫曼](https://github.com/cypressious) 。基里尔已经对格式化器进行了十几项改进，并提交了 20 多项提交 - 伟大的工作，基里尔，我们非常感谢。在这里，我们还要感谢我们的 EAP 用户，并对 1.0.3 的预发布版本进行了测试并提供了无价的反馈。
虽然此更新不是功能丰富的，但有几个重要的改进和功能，值得一提：
## 编译器的新功能：


* 新选项 -jdk-home 指定编译代码的 JDK
* 指定 Kotlin 语言版本（-language-version）和目标 Java 版本（-jvm-target）的选项（将在 1.1 中生效，现在添加用于转发兼容性）
* 更有效的字节码（在循环中不再有迭代器，避免使用单元进行不必要的操作）
* 诊断信息的各种改进

## IDE 的新功能


* 自动提供 Java 到 Kotlin 转换，用于从浏览器和 IDE 之外的其他来源复制的 Java 代码

