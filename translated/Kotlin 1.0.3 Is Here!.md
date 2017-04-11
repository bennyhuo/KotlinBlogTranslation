---
title: [译]Kotlin 1.0.3 Is Here!
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
---

我们很高兴呈现Kotlin 1.0.3。这个更新不是全新的和闪亮的功能，更多的是关于错误修复，工具改进和性能提升。这就是为什么你会喜欢它😉看看完整的更改日志和问题统计子系统：
具体来说，我们要向我们的贡献者表示感谢，他们的承诺包括在1.0.3中，即Yaroslav Ulanovych，Jake Wharton和Kirill Rakhman。基里尔已经对格式化器进行了十几项改进，并提交了20多项提交 - 伟大的工作，基里尔，我们非常感谢。在这里，我们还要感谢我们的EAP用户，并对1.0.3的预发布版本进行了测试并提供了无价的反馈。
虽然此更新不是功能丰富的，但有几个重要的改进和功能，值得一提：
## 编译器的新功能：


* 新选项-jdk-home指定编译代码的JDK
* 指定Kotlin语言版本（-language-version）和目标Java版本（-jvm-target）的选项（将在1.1中生效，现在添加用于转发兼容性）
* 更有效的字节码（在循环中不再有迭代器，避免使用单元进行不必要的操作）
* 诊断信息的各种改进

## IDE的新功能


* 自动提供Java到Kotlin转换，用于从浏览器和IDE之外的其他来源复制的Java代码

