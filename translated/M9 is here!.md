---
title: [译]M9 is here!
date: 2014-10-15 18:38:00
author: Hadi Hariri
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2014/10/m9-is-here/
---

M9已经到来，它带来了许多新功能和重要变化。我们已经突出了这些，并详细介绍了其他。我们深入了解其他一些改进。
## 语言变化

注意：以下某些更改正在破坏更改，这意味着可以使用早期版本编译的一些代码将不再编译，因此您需要更正它。
### 平台类型

如前所述，平台互操作性（即Java和JavaScript互操作性）是我们的首要任务，因为这对我们的用户来说是如此。与Java进行互操作时的空白问题是我们获得的最大的投诉之一。简而言之，问题是来自Java的任何引用可能都为null，而Kotlin通过设计无效，强制用户对每个Java值进行空值检查，或者使用安全调用（？）或不是null断言（!!）。那些在纯Kotlin世界中非常方便的功能，当您必须在Kotlin / Java设置中经常使用它们时，往往会变成灾难。我们依靠外部注释和KAnnotator通过使用额外的类型信息增强Java来减轻这个问题。这种方法证明是太麻烦了，在某些情况下不起作用。
这就是为什么我们采取了一个激进的方法，并使得Kotlin的类型系统更加轻松，当涉及到Java互操作：现在来自Java的引用有特别标记的类型（我们称之为“平台类型”，因为它们来自底层平台），其中特别处理：

* Kotlin不对平台类型执行零安全性。即对于Java值，您将获得Java的语义：NPE现在可能来自Java的值

