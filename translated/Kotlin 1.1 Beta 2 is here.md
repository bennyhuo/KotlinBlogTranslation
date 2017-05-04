---
title: "[译]Kotlin 1.1 Beta 2 is here"
date: 2017-02-02 23:24:00
author: Dmitry Jemerov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/02/kotlin-1-1-beta-2-is-here/
translator:
translator_url:
---

我们很高兴地宣布 Kotlin 1.1 的第二个测试版。请尝试新版本 - 您的反馈对于确保我们可以提供质量版本至关重要。
自从第一个测试版本开始，我们主要关注稳定性，错误修正以及改进此版本的关键重点领域：协同程序支持和 JavaScript 后端。自 1.1 Beta 版以来的完整列表可以在 [更新日志](https://github.com/JetBrains/kotlin/blob/0e1b61b422bd0d006158d8b68fa34e960853c5c6/ChangeLog.md) 。如果您有兴趣了解 1.1 版本中添加的所有内容，请查看我们的 [什么是新页面](https://kotlinlang.org/docs/reference/whatsnew11.html) 。

{% raw %}
<p><span id="more-4562"></span></p>
{% endraw %}

## 迁移说明

对于 JavaScript 项目，我们更改了标准库的工件名称。而不是`kotlin-js-library`，它现在是`kotlin-stdlib-js`。当您更新到 1.1 beta 2 或更新的版本时，您将需要更新您的 Maven 和 Gradle 脚本。
除此之外，JavaScript 的测试支持类（包`kotlin.test`）现在被打包为单独的工件，就像以前为 Java 版本一样。如果您在 JS 项目中使用 kotlin.test，请在`kotlin-test-js`上添加依赖关系。
Kotlin 标准库中的协同程序 API 已被移至`kotlin.coroutines.experimental`包;如果您在代码中使用了这些 API，则需要更新导入。看到 [安德烈的论坛帖子](https://discuss.kotlinlang.org/t/experimental-status-of-coroutines-in-1-1-and-related-compatibility-concerns/2236) 为了这个变化的背景。
我们还使您的 Gradle 项目中的实验协同程序支持变得更加容易。您可以将以下代码片段添加到 build.gradle 中，而不是编辑 gradle.properties：

{% raw %}
<p></p>
{% endraw %}

```kotlin
kotlin {
    experimental {
        coroutines 'enable'
    }
}
```

{% raw %}
<p></p>
{% endraw %}

如果你正在使用 [kotlinx.corutines 库](https://github.com/kotlin/kotlinx.coroutines) 请更新您的依赖关系到版本`0.6-beta`。该库的早期版本与此 Kotlin 更新不兼容。
## 新功能

我们在此测试版中添加了几个最新功能。这里是最重要的：

* 编译器现在报告一个警告，如果您声明一个扩展名与同一个类的成员具有相同的签名，并且将始终被遮蔽（例如 String.length（））
* 传递给通用功能的成员引用的类型推断现在得到很大的改进（KT-10711）
* 减号运算符现在可以与地图一起使用，返回地图的副本，并删除给定的键。 -  = 操作符可以在可变地图上使用，以从地图中删除给定的键。
* 现在可以使用 KPropertyN.getDelegate（）访问委托属性的委托实例（详见 KT-8384）;
* 意图（由 Kirill Rakhman 贡献）合并两个嵌套 if 语句;
* 支持在启用 Jack 工具链时构建 Android 项目（jackOptions {true}）;
* 意图（由 Kirill Rakhman 贡献）在 Android 应用程序中生成 View 构造函数。

## 源兼容性 Kotlin 1.0

在这次更新中我们非常关注的另一个领域是与 Kotlin 1.0 的源兼容性**。这样，即使您的团队使用 Kotlin 1.0，您也可以尝试使用 Kotlin 1.1，而不用担心通过使用新版本中添加的一些功能来打破构建。
要启用兼容性模式：

* 对于 Maven，Ant 和命令行编译器，将 -language-version 编译器参数设置为 1.0。
* 在 Gradle 构建中，将 kotlinOptions {languageVersion =“1.0”}添加到您的 compileKotlin 任务中。
* 在 IDE 中，在 Kotlin facet 设置或 Settings | 中指定语言版本构建，执行，部署 | 编译器 | Kotlin 编译器

## 如何尝试

**在 Maven / Gradle 中：**将`http://dl.bintray.com/kotlin/kotlin-eap-1.1`添加为构建脚本和项目的存储库;使用`1.1.0-beta-38`作为编译器和标准库的版本号。
**在 IntelliJ IDEA 中：**转到*工具→Kotlin→配置 Kotlin 插件更新*，然后在*更新频道*下拉菜单中选择“Early Access Preview 1.1”下拉列表，然后按*检查更新*。
命令行编译器可以从中下载 [Github 发行页面](https://github.com/JetBrains/kotlin/releases/tag/v1.1-beta2) 。
**<a href="http://try.kotlinlang.org/"> try.kotlinlang.org </a>**。即将推出。
让我们来吧！
