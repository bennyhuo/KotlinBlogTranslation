---
title: "[译]Kotlin 1.1 Beta Is Here!"
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
translator:
translator_url:
---

恭喜！今天 Kotlin 1.1 已经达到了 Beta，这意味着

* 现在是时候尝试了，
* 还有时间给我们您的反馈（我们真的需要它！），
* 发布即将到来。


{% raw %}
<p><center><img alt="Kotlin 1.1 Beta" class="alignnone size-full wp-image-4514" height="650" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/01/1.1-Beta-Banner-2-01.png" width="1300"/></center></p>
{% endraw %}

过去一年来，我们对 Kotlin 感兴趣，并感谢所有用户，贡献者和支持者。特别感谢早期采用新功能的勇气和反馈给我们的 EAP 版本！

{% raw %}
<p><span id="more-4484"></span></p>
{% endraw %}

## 概述 Kotlin 1.1 中的内容

Kotlin 1.1 的最大消息是

* 完全支持编译 JavaScript，和
* JVM，Android 和 JavaScript 上的协调程序。

下面我们再给出一些关于这些细节的细节，但是它们不是 1.1 的唯一令人兴奋的消息。更多的语言改进和新功能即将到来（我们可以获得更多的细节 [什么是新的](https://kotlinlang.org/docs/reference/whatsnew11.html) 页）：

* 类型别名：typealias Action <T> =（T） - > Unit
* 绑定可调用引用：expr :: foo
* 基于 getter 的类型推断：val myString get（）=“hi”
* 编译器插件
* 默认情况下打开课程
默认情况下生成无参考构造函数
扩展羊羔在 SAM 转换
* 默认情况下打开课程
* 默认情况下生成无参考构造函数
* 扩展羊羔在 SAM 转换
* 数据类的继承
* 密封类的子类在同一个文件中
* 在 lambdas 中解构：map.forEach {（k，v） - > ...}
* 未使用参数的下划线
* 构建器类 DSL 的范围控制：@DslMarker
* 提供操作符约定
* 本地委托属性
* Kotlin 系列上的 JDK 8 方法：list.parallelStream（）
* 内联属性
* enumValues（）/ enumValueOf（）用于通用访问枚举
* 数字文字中的下划线：1_000_000

## 弃用

我们弃用了我们用于`％`运算符的不幸的名称`mod`，并将其替换为语法正确的＆code＆remot = 例如`java.math.BigInteger`。弃用警告和工具将引导您完成迁移过程。
## JavaScript

很简单：可以将完整的 Kotlin 语言编译成 JavaScript。这并不意味着我们已将所有的 JDK 移植到浏览器中：语言和标准库不与 JDK 结合使用，但您可以在 JS 上使用 Kotlin 字符串，集合，序列，数组和其他核心 API JVM / Android。
许多流行的 JS 库将通过类型的头文件（从 [绝对命令](https://github.com/DefinitelyTyped/DefinitelyTyped) ）。我们支持所有流行的运行时模块系统的 JavaScript 以及 [网络包](https://webpack.github.io/) 和其他重要工具。
我们将在 Kotlin 1.2 及更高版本中投入大量精力，使 JavaScript 工具顺利而有用。我们的目标是使 Kotlin 能够实现愉快的全套堆栈开发。
## 协调程序

老实说，很难过度强调协调程序。未来已经到来，我们坚持下去：我们需要非阻塞异步 API 来跟上我们正在处理的数据量。我们已经通过回调地狱征服了，但是我们应该更好。我们想简单地按照自然的顺序编写代码逻辑，让编译器为我们指定不同步。这是协同程序的关键：异步/等待，生成/收益，非阻塞 IO，Rx 和更多的带来在*挂起功能的单一统一范例*。这样的函数（或 lambda）表示可以暂停（不阻塞任何线程）并稍后恢复的计算。

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

我们为有趣的常见用例写了一套图书馆： [kotlinx.coroutines](https://github.com/Kotlin/kotlinx.coroutines) [阅读更多关于协程](https://github.com/Kotlin/kotlin-coroutines/blob/master/kotlin-coroutines-informal.md) 这里。
**重要的注释**。凭借所带来的所有好处，Kotlin 协同程序是一个相当新的设计，需要大量的战斗测试，才能确定它的 100％正确和完整。这就是为什么我们会在“实验性”选择标志下发布。我们不希望语言规则发生变化，但 API 可能需要在 Kotlin 1.2 中进行一些调整。

* 命令行：-Xcoroutines = enabled
* Gradle：kotlin.coroutines = 在 gradle.properties 或 local.properties 中启用
* Maven：<configuration> <args> <arg> -Xcoroutines = enable </arg> </args> </configuration>
* IDE：使用快速修复（Alt + Enter）或修改 facet 选项（项目结构 - >模块 - >您的模块 - >编译器 - >协程（实验））

## 标准图书馆，工具和框架

Kotlin 的标准库正在更新 [许多有用的实用程序](https://kotlinlang.org/docs/reference/whatsnew11.html#standard-library) 和扩展包括特定于 JDK 7 和 8 的扩展。
我们的合作 [毕业](https://blog.gradle.org/kotlin-meets-gradle) 已经导致了 gradle-script-kotlin，这意味着您现在可以使用 Kotlin 脚本编写 Gradle 的类型安全的构建脚本。
我们现在支持 JSR 223 [Spring 框架](https://spring.io/blog/2017/01/04/introducing-kotlin-support-in-spring-framework-5-0) 以及类型安全的 DSL 和其他事情。
## 如何尝试

与其他预发行版本一样，我们为 Kotlin 1.1-Beta 提供了**无后向兼容性保证**。此外，当我们达到最终 RC 时，由发行版本生成的所有二进制文件将被编译器禁止：您需要重新编译 1.1-M0x 和 Beta 编译的所有内容（1.0.x 中的所有代码都是完美的罚款没有重新编译）。
**在 Maven / Gradle 中：**添加 [http://dl.bintray.com/kotlin/kotlin-eap-1.1](http://dl.bintray.com/kotlin/kotlin-eap-1.1) 作为构建脚本和项目的存储库;使用`1.1.0-beta-17`作为编译器和标准库的版本号。
**在 IntelliJ IDEA 中：**转到*工具→Kotlin→配置 Kotlin 插件更新*，然后在*更新频道*下拉菜单中选择“Early Access Preview 1.1”下拉列表，然后按*检查更新*。
命令行编译器可以从中下载 [Github 发行页面](https://github.com/JetBrains/kotlin/releases/tag/v1.1-beta) 。
**<a href="http://try.kotlinlang.org/"> try.kotlinlang.org </a>**。使用右下角的下拉列表将编译器版本更改为 1.1-Beta。
让我们来吧！
