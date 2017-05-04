---
title: "[译]Kotlin 1.0.2 is Here"
date: 2016-05-13 13:36:00
author: Dmitry Jemerov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2016/05/kotlin-1-0-2-is-here/
translator:
translator_url:
---

我们很高兴地宣布发布 Kotlin 1.0.2，这是 Kotlin 的第二个修补程序和工具更新。除编译器和语言错误修复外，Kotlin 1.0.2 还为 IDE 和构建工具添加了许多主要功能。
### Gradle 和 IDE 中的增量编译

新版本继续开展 Kotlin 增量编译支持工作，加快开发过程中的周转时间。默认情况下，IDE 中的增量编译（以前标记为实验）已被启用。此外，期待已久的对 Gradle 构建**中的增量编译的支持现在已经存在。
要为 Gradle 启用增量编译，您需要将**kotlin.incremental**属性设置为 true（例如，通过将`kotlin.incremental = true`添加到`在项目的根目录中的 gradle.properties`文件）。
### Android Lint Checks

Kotlin 1.0.2 引入了针对 Kotlin 代码的**Android Lint 检查**的支持，确保正确检测到您所定位的 Android 版本中不支持使用 API​​的问题。

{% raw %}
<p><span id="more-3865"></span></p>
{% endraw %}

Kotlin 1.0.2 支持的检查对应于 Android Studio 1.5 支持的检查;在下一个版本的 Kotlin 将支持在 Android Studio 2.0 中添加或改进的支票。此外，当前版本仅在 IDE 内运行 Lint 检查 Kotlin 代码（作为即时代码检查的一部分，或通过 Analyze | Inspect Code 在批处理模式下）。在下一个版本中将支持从命令行运行检查。
### 紧凑型标准库

与 Android 开发人员相关的其他一些改进是标准库的大小已经减少了约 1500 种方法（从大约 6600 到 5100）。即使在这个变化之前，图书馆也是 [小于 Kotlin 的主要竞争对手](https://github.com/SidneyXu/AndroidDemoIn4Languages) 现在情况更好了。当然，图书馆仍然是完全二进制兼容的。
### Java 7/8 支持库

作为在 Kotlin 1.1 中引入完全支持之前的更好的 Java 7/8 支持的临时解决方法，我们现在提供支持库，将 Java 7 和 8（例如 Stream API）中添加的 API 作为 Kotlin 标准的扩展功能图书馆类。见 [论坛帖子](https://discuss.kotlinlang.org/t/jdk7-8-features-in-kotlin-1-0/1625) 有关使用库的说明。
### IntelliJ IDEA 插件功能

IntelliJ IDEA 插件已经获得了一些主要的新功能：

* 对于 Android Studio 的用户，现在有可能在 Kotlin 中创建一个新的活动;
* 对于 IntelliJ IDEA Ultimate 的用户，现在已经初步支持 Spring Framework，包括检查，线标记，SpEL 语言注入支持，生成依赖关系的操作等等;
* 已经添加了一些检查和快速修复，例如突出显示可以是 val 的 vars 的检查;
* 改进了 Gradle 集成，调试器，格式化，重构等插件领域。

### JavaScript 支持

我们已经恢复了对我们的 JavaScript 后端的工作，而在定位 JavaScript 时，1.0.2 版填补了语言功能支持中剩余的大部分空白。新支持的功能包括嵌套课程，本地课程，本地语言中的非本地返回，不安全的转换等。
### Maven 原型

我们现在提供一个 Maven 原型来轻松创建 Kotlin 项目。使用“新项目 | Maven | 在 IntelliJ IDEA 或以下命令行中，从 Archetype 创建...“

{% raw %}
<p></p>
{% endraw %}

```kotlin
mvn archetype:generate -Dfilter=org.jetbrains.kotlin:
```

{% raw %}
<p></p>
{% endraw %}

### Dokka 0.9.8

与 Kotlin 1.0.2 一起，我们发布了一个新版本 [Dokka](https://github.com/kotlin/dokka) ，Kotlin 文档生成工具。如果您在项目中使用 Dokka，则需要与 Kotlin 一起升级 Dokka，因为较旧的 Dokka 版本与 Kotlin 1.0.2 不兼容。 Dokka 0.9.8 的新功能包括：

* Android Gradle 插件，用于生成 Android 库和应用程序的文档;
* 支持在 Maven 插件中生成 javadoc jar 文件。

### 结论

您可以看到编译器，标准库和其中的工具的修补程序和更改的完整列表 [更新日志](https://github.com/JetBrains/kotlin/blob/1.0.2/ChangeLog.md) 。
在发布工作的同时，我们收到了很多有用的反馈意见 [早期访问预览版本](https://discuss.kotlinlang.org/t/kotlin-1-0-2-eap/1581) 。我们非常感谢所有提供反馈的人，欢迎您加入 EAP 计划，以备将来更新。
像往常一样，如果您遇到新版本的任何问题，欢迎您提供帮助 [论坛](https://discuss.kotlinlang.org/) ，在 Slack（获得邀请） [这里](http://kotlinslackin.herokuapp.com/) ），或报告中的问题 [问题追踪器](https://youtrack.jetbrains.com/issues/KT) 。
