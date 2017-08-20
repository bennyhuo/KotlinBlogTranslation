---
title: Kotlin 1.1.4 is out
author: Dmitry Jemerov
date: 2017-08-15 10:38:00
source_url: https://blog.jetbrains.com/kotlin/2017/08/kotlin-1-1-4-is-out/
tags: 
categories:  官方动态
---

我们很高兴地宣布发布Kotlin 1.1.4，这是Kotlin 1.1的一个新的bug修复和工具更新。此更新：

* 修复了IntelliJ IDEA插件中的主要性能回归
* 添加对包缺省可空性注解的支持
* 改善Java 9的支持
* 添加使用@Parcelize注释生成Android Parcelable实现的初始实验支持
* 添加一个用于JavaScript死代码消除的工具，提高对JS调试和JS单元测试支持的源映射支持
* 生成更高效的字节码
* 为IntelliJ IDEA插件添加了许多新功能

该更新程序与所有版本的IntelliJ IDEA兼容，从2016.2到2017.2以及Android Studio 2.3和3.0 Beta版本。
此版本中的完整更改列表可以在更改日志中找到。

{% raw %}
<p><span id="more-5184"></span></p>
{% endraw %}

我们要感谢我们的外部贡献者，他们的推荐要求包括在这个版本中：Andrius Semionovas，Bill Collins，Derek Alexander，Dimach，Ilya Zorin，Kirill Rakhman，Stuart Kent，takahirom，Toshiaki Kameyama，Vasily Kirichenko，Vitaly Khudobakhshov，Vladimir Koshelev，Yoshinori Isogai，Yuli Fiterman和Zoltan Polgar。
## 包缺省可空性注解

从这个版本开始，Kotlin支持package-default可空性注释（如JSR-305檚@ParametersAreNonnullByDefault和Spring Framework 5.0中引入的@NonNullApi注释）。为了方便迁移，并避免由于使用Java API的更为精确的可空性信息而导致的编译错误，默认情况下，对这些注释的支持已关闭，需要通过将-Xjsr305-annotations = enable命令行选项传递给编译器来启用。要在Gradle构建中启用此功能，请使用freeCompilerArgs选项;在Maven构建中，使用<args>。有关更多信息，请参阅提出的规范。
## Java 9支持

我们将继续推进Java 9的支持。从此版本开始，Kotlin基于module-info.java的信息执行基于模块的可见性检查。现在还支持在JDK 9下运行编译器。
## Android Extensions插件增强功能

Android Extensions插件现在不仅支持活动和片段，还支持自定义视图，甚至支持自定义布局容器（如ViewHolder）。此外，变体现已完全支持。
您可以在KEEP提案中了解有关新功能的更多信息。所有这些都被认为是实验性的，因此您需要在build.gradle文件中打开一个实验标志：

{% raw %}
<p></p>
{% endraw %}

```kotlin
androidExtensions {
    experimental = true
}
 
```

{% raw %}
<p></p>
{% endraw %}

## 包裹支持

Android Extensions插件现在包括一个自动包装实现生成器。声明主构造函数中的序列化属性并添加@Parcelize注释，并且将自动创建writeToParcel（）/ createFromParcel（）方法：

{% raw %}
<p></p>
{% endraw %}

```kotlin
@Parcelize
class User(val firstName: String, val lastName: String) : Parcelable
 
```

{% raw %}
<p></p>
{% endraw %}

包裹发电机也处于实验状态。我们没有与之相关的兼容性保证，欢迎您对API的反馈。有关更多信息，请参阅提出的规范。
## JavaScript死代码消除

Kotlin 1.1.4添加了一个新工具来消除由Kotlin / JS编译器生成的.js文件中的死代码。此工具仅在Gradle版本中受支持;启用，添加应用插件：'kotlin-dce-js'到你的build.gradle。有关详细信息，请参阅文档。
## JavaScript调试

Kotlin 1.1.4改进了对JavaScript源代码生成的支持，从而更容易在浏览器调试器（如Chrome DevTools）中调试JS。有关详细信息，请参阅本教程。
## JavaScript单元测试

此更新扩展了JavaScript单元测试支持，以便与更多种类的库共同使用。有关更多信息和示例项目的链接，请参阅论坛帖子。
## 字节码质量改进

在此更新中，我们为生成的字节码的质量实施了许多改进。命名挂起功能的异常现在源于函数本身，这使得它们的堆栈跟踪器更易于阅读，并且字节码在许多情况下表现更好。
## IntelliJ IDEA插件改进

新版本为IntelliJ IDEA插件带来了许多改进：

* 主要业绩改善
* 新的重构？

现在可以使用带有访问器的属性来重构
* 现在支持重命名标签
* 代码样式设置中有许多新的选项
* 数据流分析支持（分析|分析数据流从/到这里）
* 在项目中配置Kotlin？现在支持使用Gradle Kotlin DSL的项目
* 许多新的检查和quickfixes

## 如何更新

要更新插件，请使用工具| Kotlin |配置Kotlin插件更新，然后按“淐呵呵更新” - 按钮。此外，不要忘记在Maven和Gradle构建脚本中更新编译器和标准库版本。
像往常一样，如果您遇到新版本的任何问题，欢迎您在论坛上，Slack（在这里获得邀请）请求帮助，或者在问题跟踪器中报告问题。
让檚ot！
