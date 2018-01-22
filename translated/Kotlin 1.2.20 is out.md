---
title: Kotlin 1.2.20 is out
author: Dmitry Jemerov
date: 2018-01-17 14:54:00
tags: 
categories:  官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2018/01/kotlin-1-2-20-is-out/
translator: pye52
translator_url: https://pye52.github.io/
---

我们很高兴地宣布Kotlin 1.2.20的发布，这是Kotlin 1.2一个bug修复和工具更新的版本。包含了以下更新：

* 增加对Gradle构建缓存的支持
* 针对Android增量编译和Kotlin / Java混合项目的改进
* 为新的Kotlin规范指引提供IDE支持
* 编辑器会为隐式参数和lambdas的返回值添加内嵌式的提示
* JavaScript DCE Gradle的任务将支持开发模式
* IntelliJ插件中引入新的检查方案，性能改进和bug修复

该更新兼容2017.1至2017.3版本的IntelliJ IDEA，以及Android Studio 3.0和3.1 Canary。
更新内容的完整列表可以在[更新日志](inspections)中找到。
我们要感谢这些第三方贡献者，他们的请求被包括在这个版本中：龟山俊明（多达46个贡献！），Yoshinori Isogai，Kenji Tomita，Kirill Rakhman，Sergey Ryabov，Alexey Belkov，Michal Bendowski AdamMc331 Andre Perkins Andrey Mischenko Artem Zinnatullin Chris Povirk Denis Vnukov Dereck Bridie Ilya Zorin Jake Wharton Joscha Alisch Kartik Patodi AJ Alt Ramon Wirsch Vladimir Kasatkin Yusuke Hosonuma a2kaido scache。

## 编译性能的改进

我们仍继续重点关注编译的性能表现，在该版本中我们主要提供了Gradle插件相关的改进。
第一个改进是支持[Gradle构建的缓存](https://guides.gradle.org/using-build-cache/)。如果你使用的是Gradle 4.3或更高版本，并且已开启了缓存（这不是默认开启的，需要配置`--build-cache`或`org.gradle.caching = true`），插件会复用前一次Kotlin编译任务的结果。假设你构建了`master`分支，然后切换到另一个分支，再次构建，并切换回`master`分支，那么代码将不会被重新编译。`master`之前的结果将会被复用。
默认情况下，Kotlin注释处理器的构建缓存是关闭的，因为Gradle无法精确跟踪注释处理器的依赖关系，所以它可能会错误地重用之前执行的注释处理器结果。若无论如何都要启用缓存，请将以下该行添加到build配置：

```kotlin
kapt {
    useBuildCache = true
}
```

第二个改进是[更精准地跟踪Java文件中的变动](https://youtrack.jetbrains.com/issue/KT-17621)，从而在Java中的变更不影响到Kotlin代码时避免Kotlin重新编译。这个功能目前处于实验中。若要启用它，请将以该行添加到你的gradle.properties文件中：

```kotlin
kotlin.incremental.usePreciseJavaTracking=true
```

最后，Android的XML布局文件改动不再引起所有Kotlin代码的重新编译; 由Kotlin Android扩展（`kotlinx.android.synthetic.*`）生成的属性引用文件则会被重新编译。
## Kotlin规范指引

我们最近发布了一个新的官方[Kotlin规范指引](http://kotlinlang.org/docs/reference/coding-conventions.html)，包括了Kotlin代码的格式以及语言和库的特性的习惯用法。从这个版本开始，格式化器将完全支持新的规范指引。IntelliJ IDEA同样可以检测到不符合规范的地方，并能通过quick fixes更正。
新的规范指引所建议的格式与Kotlin插件以前使用的默认格式不同。为了避免不必要的格式更改，需要你明确应用新的规范。打开 Settings | Editor | Code Style | Kotlin然后选择“Set from…”链接以便选择代码样式。

<a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2018/01/1.2.20-codestyle.png?ssl=1" rel="attachment wp-att-5701"><img alt="Kotlin code style settings" class="alignnone size-full wp-image-5701" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2018/01/1.2.20-codestyle.png?resize=640%2C353&amp;ssl=1"/></a>

## IntelliJ IDEA插件的改进

新版本插件为lambdas的隐式参数以及从lambda的返回值增加了内嵌提示。以下截图展示了两个功能的实际效果

<a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2018/01/1.2.20-inlayhints.png?ssl=1" rel="attachment wp-att-5702"><img alt="Kotlin inlay hints" class="alignnone size-full wp-image-5702" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2018/01/1.2.20-inlayhints.png?resize=640%2C213&amp;ssl=1"/></a>

## JavaScript DCE开发模式

JavaScript dead code elimination （DCE）插件用于减少Kotlin输出到JavaScript编译器的代码体积。 因为DCE进程需要额外的时间，而且这个输出的体积在开发中是无关紧要的，所以现在可以禁用[DCE插件](https://youtrack.jetbrains.com/issue/KT-20210)。通过下面的选项来实现：

```kotlin
runDceKotlinJs.dceOptions.devMode = true
```

## 如何更新

若要更新插件，请打开Tools | Kotlin | Configure Kotlin Plugin Updates然后选择"Check for updates now"按钮。请注意同样需要在Maven和Gradle构建脚本中更新编译器和标准库版本。
一如既往，如果在新版本中遇到任何问题，欢迎你在[论坛](https://discuss.kotlinlang.org/)上或者在Slack上（在[这里](slack.kotlinlang.org)获得邀请）求助，或者向[问题跟踪器](https://youtrack.jetbrains.com/issues/KT)报告。
请尽情享受Kotlin!