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
---

我们一直在为Kotlin M9的下一个即将发布的版本而努力，它包含相当多的新功能和一些重要的更改。<span id =“more-1625”> </ span>
## 平台互操作性改进

Kotlin的目标之一一直是利用现有的代码，库和JVM生态系统，并能够混合和匹配Kotlin和Java。使用M9，我们将大大减少摩擦。用于消耗或实现Java编写的API，导出函数作为静态方法，删除冲突以及特征的未知空白类型现在以更直接的方式编译，从而解决了仅支持简单接口的某些代码生成库的问题。
## 增量编译

我们希望Kotlin编译与Java一样快，为此我们引入了增量编译。此优化显着减少编译时间。它还兼容IntelliJ IDEA的自动创建功能，它可以在后台编译代码，因为进行了更改。
## 模块

编译器和IDE现在分享对模块的理解，使其在设计时间和编译时间之间保持一致。完成不再提供不包含在特定模块的依赖关系的库中的符号，从而提高隔离度并减少不必要的外部依赖关系的可能性。现在，<em>内部</ em>可见性修饰符仍将被视为<em> public </ em>。在这方面做出明确的承诺之前，我们仍然需要了解用户体验消费DSL的方式。
## 调试器

通用调试器的改进，可以更好地了解Kotlin生成的代码，为断点和Kotlin特定的构造提供更好的体验。
## 重构和智慧

IntelliJ IDEA的可用性和新功能的改进，包括期待已久的<em>使用创建</ em>，更多意图（快速修复）和代码完成增强功能。现在，<em>提取方法</ em>重构也分析了提取新方法的代码重复，建议用新方法替换这些方法。 Java到Kotlin转换器也得到了很大的改进，提供了将单个或多个文件从Java转换为Kotlin的更好的转换。
## JVM代码生成

对于JVM，代码生成的改进可以减少字节码大小，提高生成代码的性能，更好地兼容Java8运行时的现代HotSpot优化和增强功能内联，这是M9的一些期望。
## JavaScript

对JavaScript平台的支持已经得到改进，几乎所有的语言功能都可以用于定位JavaScript运行时的模块。标准库已经预编译，现在随编译器一起提供，允许编写使用标准函数的JavaScript兼容子集的代码，例如处理收集操作的代码。并且通过一个微小的修改，代码也可以在node.js上运行。
M9即将推出，敬请期待！
