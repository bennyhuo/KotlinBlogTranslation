---
title: "[译]M9 is coming"
date: 2014-10-01 22:10:00
author: Hadi Hariri
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2014/10/m9-is-coming/
translator:
translator_url:
---

我们一直在为 Kotlin M9 的下一个即将发布的版本而努力，它包含相当多的新功能和一些重要的更改。<span id =“more-1625”> </span>
## 平台互操作性改进

Kotlin 的目标之一一直是利用现有的代码，库和 JVM 生态系统，并能够混合和匹配 Kotlin 和 Java。使用 M9，我们将大大减少摩擦。用于消耗或实现 Java 编写的 API，导出函数作为静态方法，删除冲突以及特征的未知空白类型现在以更直接的方式编译，从而解决了仅支持简单接口的某些代码生成库的问题。
## 增量编译

我们希望 Kotlin 编译与 Java 一样快，为此我们引入了增量编译。此优化显着减少编译时间。它还兼容 IntelliJ IDEA 的自动创建功能，它可以在后台编译代码，因为进行了更改。
## 模块

编译器和 IDE 现在分享对模块的理解，使其在设计时间和编译时间之间保持一致。完成不再提供不包含在特定模块的依赖关系的库中的符号，从而提高隔离度并减少不必要的外部依赖关系的可能性。现在，*内部*可见性修饰符仍将被视为*public*。在这方面做出明确的承诺之前，我们仍然需要了解用户体验消费 DSL 的方式。
## 调试器

通用调试器的改进，可以更好地了解 Kotlin 生成的代码，为断点和 Kotlin 特定的构造提供更好的体验。
## 重构和智慧

IntelliJ IDEA 的可用性和新功能的改进，包括期待已久的*使用创建*，更多意图（快速修复）和代码完成增强功能。现在，*提取方法*重构也分析了提取新方法的代码重复，建议用新方法替换这些方法。 Java 到 Kotlin 转换器也得到了很大的改进，提供了将单个或多个文件从 Java 转换为 Kotlin 的更好的转换。
## JVM 代码生成

对于 JVM，代码生成的改进可以减少字节码大小，提高生成代码的性能，更好地兼容 Java8 运行时的现代 HotSpot 优化和增强功能内联，这是 M9 的一些期望。
## JavaScript

对 JavaScript 平台的支持已经得到改进，几乎所有的语言功能都可以用于定位 JavaScript 运行时的模块。标准库已经预编译，现在随编译器一起提供，允许编写使用标准函数的 JavaScript 兼容子集的代码，例如处理收集操作的代码。并且通过一个微小的修改，代码也可以在 node.js 上运行。
M9 即将推出，敬请期待！
