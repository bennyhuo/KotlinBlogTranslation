---
title: "[译]The Road Ahead"
date: 2012-01-16 10:10:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2012/01/the-road-ahead/
---

众所周知，我们上周推出了我们的第一个公开发布： [kotlin-demo.jetbrains.com](http://kotlin-demo.jetbrains.com/) 。而当您（7K +独特访问者）正在玩乐时，我们将继续致力于Kotlin编译器，IDE和标准库。在这篇文章中，我将概述我们的计划。 <span id =“more-365”> </ span> <strong> </ strong>
<strong>您今天可以玩的</ strong>
今天你可以已经 [尝试](http://kotlin-demo.jetbrains.com/) Kotlin的许多功能。其中包括：

* 功能文字（封闭）
* 扩展功能和属性
* 特征（接口中的代码）
* 声明网站/使用网站差异
* 一流的代表团
* 混合Java / Kotlin编码

看到 [Kotlin文档](http://jetbrains.com/kotlin) 更多细节。
将事情用于真正的问题揭示了设计的局限性，不一致性和其他缺点，这是<strong>好</ strong>，因为那时我们可以 [修复它们](http://blog.jetbrains.com/kotlin/2012/01/the-great-syntactic-shift/) 。关键是在我们发布1.0版本</ strong>之前，找到并修复几乎所有的东西<strong>。发布后，我们将无法引入向后不兼容的更改，因此修复语言将变得困难。所以，请尝试他们，并在下面的评论中或在...中给我们您的反馈</ strong> [问题追踪器](http://youtrack.jetbrains.net/issues/KT) 。
<strong>什么让我们忙碌</ strong>
<strong> </ strong>目前，我们正在稳定现有功能，并在IDE和语言基础设施（建筑物等）上工作。本月最热门的话题是：

* 模块：module =编译和依赖关系管理单元;
* Ant和Maven集成：使用您最喜欢的构建基础设施;
* 标准库：JDK集合，IO等的实用功能;
* JavaScript后端：原型还是很早，但是它正在改进。

<strong> ToDo </ strong>
当玩Kotlin时，很方便的知道什么还不支持。列表很长，其中一些功能甚至可能会等待2.0：

* 可见性检查：可惜我们没有这些私人，公共等等;
* 本地功能：函数内部的函数可以是非常方便的事情;
* 标记元组（又名记录）：从函数返回很多东西;
* KotlinDoc：像JavaDoc，但是基于Markdown;
* 注释：可定制的元数据以启用编译器扩展;
* 次要建设者：有时你需要多于一个;
* 枚举类（代数数据类型）：像Java枚举，但更好;
* 模式匹配：对象结构的便利条件;
* 内联函数：用于自定义控件结构的零开销闭包;
* 标签：断开并继续外圈;
* 键入别名：缩短长泛型等等;
* 自我类型：永远不要写尴尬的递归泛型;
* 动态类型：互操作性JavaScript和其他动态语言;
* Eclipse插件：Kotlin IDE！= IntelliJ IDEA;
* LLVM后端：将Kotlin编译成本机代码...

即使没有这些东西，你可以有很多的乐趣。尝试使用<strong>扩展功能</ strong>和<strong>关闭</ strong>，<strong> traits </ strong>和<strong>字符串模板</ strong>等等。解决问题（随着时间的推移我们会加入更多）。 [有一个漂亮的Kotlin](http://kotlin-demo.jetbrains.com/) ！
