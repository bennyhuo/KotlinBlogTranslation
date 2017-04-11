---
title: [译]Kotlin 1.1 Beta Is Here!
date: 2017-01-19 13:51:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/01/kotlin-1-1-beta-is-here/
---

恭喜！今天Kotlin 1.1已经达到了Beta，这意味着

* 现在是时候尝试了，
* 还有时间给我们您的反馈（我们真的需要它！），
* 发布即将到来。


{% raw %}
<p><center><img alt="Kotlin 1.1 Beta" class="alignnone size-full wp-image-4514" height="650" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/01/1.1-Beta-Banner-2-01.png" width="1300"/></center></p>
{% endraw %}

过去一年来，我们对Kotlin感兴趣，并感谢所有用户，贡献者和支持者。特别感谢早期采用新功能的勇气和反馈给我们的EAP版本！

{% raw %}
<p><span id="more-4484"></span></p>
{% endraw %}

## 概述Kotlin 1.1中的内容

Kotlin 1.1的最大消息是

* 完全支持编译JavaScript，和
* JVM，Android和JavaScript上的协调程序。

下面我们再给出一些关于这些细节的细节，但是它们不是1.1的唯一令人兴奋的消息。更多的语言改进和新功能即将到来（我们的新功能页面上有更多详细信息）：

* 类型别名：typealias Action <T> =（T） - > Unit
* 绑定可调用引用：expr :: foo
* 基于getter的类型推断：val myString get（）=“hi”
* 编译器插件

默认情况下打开课程
默认情况下生成无参考构造函数
扩展羊羔在SAM转换
* 默认情况下打开课程
* 默认情况下生成无参考构造函数
* 扩展羊羔在SAM转换
* 数据类的继承
* 密封类的子类在同一个文件中
* 在lambdas中解构：map.forEach {（k，v） - > ...}
* 未使用参数的下划线
* 构建器类DSL的范围控制：@DslMarker
* 提供操作符约定
* 本地委托属性
* Kotlin系列上的JDK 8方法：list.parallelStream（）
* 内联属性
* enumValues（）/ enumValueOf（）用于通用访问枚举
* 数字文字中的下划线：1_000_000

## 弃用

我们弃用我们用于％运算符的不幸名称mod，并将其替换为rem，语义正确，并与现有库（如java.math.BigInteger）一致。弃用警告和工具将引导您完成迁移过程。
## JavaScript

很简单：可以将完整的Kotlin语言编译成JavaScript。这并不意味着我们已将所有的JDK移植到浏览器中：语言和标准库不与JDK结合使用，但您可以在JS上使用Kotlin字符串，集合，序列，数组和其他核心API JVM / Android。
许多流行的JS库将通过类型的头文件（从DefinitelyTyped转换）可用。我们支持所有流行的运行时模块系统的JavaScript以及webpack和其他重要的工具。
我们将在Kotlin 1.2及更高版本中投入大量精力，使JavaScript工具顺利而有用。我们的目标是使Kotlin能够实现愉快的全套堆栈开发。
## 协调程序

老实说，很难过度强调协调程序。未来已经到来，我们坚持下去：我们需要非阻塞异步API来跟上我们正在处理的数据量。我们已经通过回调地狱征服了，但是我们应该更好。我们想简单地按照自然的顺序逻辑编写代码，让编译器为我们指定异步。这是协同程序的关键：异步/等待，生成/产出，非阻塞IO，Rx和更多的带来的挂起功能的单一统一范式。这样的函数（或lambda）表示可以暂停（不阻塞任何线程）并稍后恢复的计算。

{% raw %}
<p></p>
{% endraw %}

```kotlin
future {
    val original = asyncLoadImage("...original...") // creates a Future
    val overlay = asyncLoadImage("...overlay...") // creates a Future
    ...
    // suspend while awaiting the loading of the images
    // then run `applyOverlay(...)` when they are both loaded
    return applyOverlay(original.await(), overlay.await())
}
 
```

{% raw %}
<p></p>
{% endraw %}

协同程序的主要好处是它们的灵活性：

* 语言部分极少
* 一切都可以写成图书馆
* 库完全控制着暂停和恢复计算的所有方面：线程，异常和计算的其他方面是完全可定制的。

我们为有趣的常见用例编写了一组库：kotlinx.coroutines
在这里阅读更多关于协程。
一个重要的说明。凭借所带来的所有好处，Kotlin协同程序是一个相当新的设计，需要大量的战斗测试，才能确定它的100％正确和完整。这就是为什么我们会在“实验性”选择标志下发布。我们不希望语言规则发生变化，但API可能需要在Kotlin 1.2中进行一些调整。

* 命令行：-Xcoroutines = enabled
* Gradle：kotlin.coroutines =在gradle.properties或local.properties中启用
* Maven：<configuration> <args> <arg> -Xcoroutines = enable </ arg> </ args> </ configuration>
* IDE：使用快速修复（Alt + Enter）或修改facet选项（项目结构 - >模块 - >您的模块 - >编译器 - >协程（实验））

## 标准图书馆，工具和框架

Kotlin的标准库正在更新许多有用的实用程序和扩展，包括特定于JDK 7和8的实用程序和扩展。
我们与Gradle的合作导致了gradle-script-kotlin，这意味着您现在可以使用Kotlin脚本为Gradle编写类型安全的构建脚本。
我们现在支持JSR 223，它被Spring框架以及类型安全的DSL和其他的东西所利用。
## 如何尝试

与其他预发行版本一样，我们不会为Kotlin 1.1-Beta提供向后兼容性保证。此外，当我们达到最终RC时，由发行版本生成的所有二进制文件将被编译器禁止：您需要重新编译1.1-M0x和Beta编译的所有内容（1.0.x中的所有代码都是完美的罚款没有重新编译）。
在Maven / Gradle中：添加http://dl.bintray.com/kotlin/kotlin-eap-1.1作为构建脚本和项目的存储库;使用1.1.0-beta-17作为编译器和标准库的版本号。
在IntelliJ IDEA：转到工具→Kotlin→配置Kotlin插件更新，然后在更新频道下拉列表中选择“早期访问预览1.1”，然后按检查更新。
命令行编译器可以从Github发行页面下载。
在try.kotlinlang.org。使用右下角的下拉列表将编译器版本更改为1.1-Beta。
让我们来吧！
