---
title: "[译]Kotlin Post-1.0 Roadmap"
date: 2016-04-14 16:34:00
author: Dmitry Jemerov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2016/04/kotlin-post-1-0-roadmap/
---

Kotlin 1.0发布以来已经差不多两个月了，现在团队正在从稳定和错误修复转变为新功能，所以现在是谈谈我们未来计划的好时机。
我们已经发表了 [Android路线图](http://blog.jetbrains.com/kotlin/2016/03/kotlins-android-roadmap/) ，但还有许多其他领域正在应用我们的努力。我们目前的发展主要分为两个部分：

* Kotlin 1.0.x将是一系列版本，其中包含错误修复，工具更新，IDE支持以及其他不影响核心语言的领域。 1.0.x版本将每隔几周定期发布一次。
* Kotlin 1.1将包含主要的新语言功能，以及来自1.0.x分支的所有改进。这将是一个功能驱动的版本，我们不会宣布任何具体的时间框架。

我们来看看每个地区的计划，从大的开始就更详细地看
<span id =“more-3844”> </span>
## 新语言功能

在我们开始谈论具体功能之前，<strong>大声明</strong>：我们在这里谈论的所有内容仍然处于设计阶段，随着我们向前迈进，功能可能会发生巨大变化或完全丢失设计，实施和反馈收集过程。所以，没有保证。
### 异步/等待/收益

现在我们正在设计的最重要的功能就是支持<strong>协同程序</strong>（async / await / yield）。到目前为止，异步/等待模式已经发现了许多不同的语言，包括C＃，Python和Dart，我们也希望在Kotlin中支持这一点。然而，这并不是故事的结尾：我们想将特定的代码执行语义放在库中，而不是编译器中。
编译器将负责将用作协同程序的函数转换为允许挂起并恢复其执行的形式。协调程序的实际执行（初始调用，以及在暂停点之后恢复执行）将由支持库负责。因此，相同的机制将允许我们支持许多不同的模式：生成器（<code> yield </code>），异步执行的函数（<code> async </code> / <code>等待</code>），Go像渠道和goroutines，以及潜在的其他甚至还没有被发明。
请注意，我们仍然在估计实施此功能所需的工作，我们不知道在1.1时间内支持它是否合理，否则将推迟到以后的版本。
### 其他语言功能

我们收到了很多来自Kotlin 1.0的反馈，我们很高兴看到很多请求都要求相同的功能。我们选择了最常见的，并将它们优先考虑为Kotlin 1.1。我们可以肯定的是：

* 数据类层次结构支持将删除许多当前对数据类继承的限制，例如，允许您将一个代数数据类型表示为嵌套在一个密封类中的一系列数据类：
密封类C {

数据类A（val x：X，val y：Y）：C（）{...}

}
* 类型别名将允许为类型（例如，函数类型或具有长签名的通用类型）分配一个简短名称：
typealias MouseEventHandler =（MouseEvent） - > Unit
* 在lambdas中的解析将允许您在作为参数传递给lambda时轻松解压缩数据类实例或支持解构协议的另一对象：
myMap.forEach {（key，value） - > println（key + value）}
* 绑定方法引用将允许创建调用特定对象实例上的方法的方法引用，并且不需要将其作为参数传递：
letters.filter（“abc”:: contains）
* 本地委派属性将允许您将本地变量定义为委派属性：
fun foo（）{val x by lazy {...}}

## Java 8/9支持

从1.0版开始，Kotlin仅针对Java 6。这意味着生成的字节码不会使用Java 7或8中添加的任何功能，而标准库仅暴露了Java 6中存在的API。
在1.0.x和1.1版本以外的版本中，我们计划删除这些限制，并为您选择您要定位的JVM版本。 Java 6还将得到支持，但如果您选择定位Java 8，我们将利用这一点。标准库将允许您使用新的Java 8 API，例如流API，编译器将使用较新的字节码功能，例如对界面中的默认方法的支持。我们还计划在JDK 9发布之前支持Project Jigsaw（JDK 9模块系统）。
## JavaScript支持

当我们开始完成1.0版本时，我们决定暂停JavaScript支持工作，并将JVM作为主要支持的平台发布。现在1.0已经出来了，我们已经恢复了对JS的工作，我们正在朝着我们的目标迈进，让您将应用程序的业务逻辑只写一次，并在后端和用户浏览器中运行。
我们在短期内的主要优先事项是填补缺少的语言功能，并与整个JavaScript基础架构（从对JS模块系统的支持开始）进行更好的整合。我们还计划为大多数主要的JS库利用一大堆强大类型的API定义，这些都是由TypeScript社区积累的。我们将提供一种将这些定义转换为Kotlin代码的工具，让您可以使用来自Kotlin的库，使用完整类型的API，并且在集成上花费的精力很少。
## IDE功能

在IDE空间中，我们目前的优先级如下：

* 框架支持：我们计划扩展IntelliJ IDEA Ultimate提供的Java企业框架支持无与伦比的水平，使其对于Kotlin也同样有效。这将是IntelliJ IDEA和Kotlin插件内并行发生的渐进过程;第一批Spring支持功能已经在Kotlin 1.0.2 EAP中提供。
* 意图和快速修复：在我们看来，IDE的主要角色之一就是教你如何使用这种语言，如果你犯了错误，帮助你恢复速度，提供代码改进建议和自动快速修复。 Kotlin 1.0已经包含了一系列很好的工具，我们将在1.0.x和1.1更新中进行扩展。作为一个例子，我们正在构建可以使用函数（如map和filter）将命令式循环转换为功能样式编写的代码的工具。
* 其他改进：我们的路线图上的其他内容包括新的重构，如Inline方法，更强大和灵活的格式化程序，支持Kotlin代码的图表等。

## 其他工具改进

Android路线图文章已经提到了我们计划在我们的工具中进行的一些改进，例如支持使用Gradle增量编译和支持Android Lint检查。这两个功能都已经在Kotlin 1.0.2 EAP中可用，并且稍后会进一步改进。
## 概要

正如你所看到的，有很多令人兴奋的事情来了，有很多机会参与。停止我们 [闲聊聊天](http://kotlinslackin.herokuapp.com/) 试试看 [EAP构建](https://discuss.kotlinlang.org/c/eap) ，文件 [问题](http://youtrack.jetbrains.com/issues/KT) - Kotlin的未来取决于你，我们的用户，我们总是乐意听到你必须说的话。
