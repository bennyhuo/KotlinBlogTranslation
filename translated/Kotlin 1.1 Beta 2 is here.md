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
---

我们很高兴地宣布Kotlin 1.1的第二个测试版。请尝试新版本 - 您的反馈对于确保我们可以提供质量版本至关重要。
自从第一个测试版本开始，我们主要关注稳定性，错误修正以及改进此版本的关键重点领域：协同程序支持和JavaScript后端。自1.1 Beta版以来的完整列表可以在 [更新日志](https://github.com/JetBrains/kotlin/blob/0e1b61b422bd0d006158d8b68fa34e960853c5c6/ChangeLog.md) 。如果您有兴趣了解1.1版本中添加的所有内容，请查看我们的 [什么是新页面](https://kotlinlang.org/docs/reference/whatsnew11.html) 。

{% raw %}
<p><span id="more-4562"></span></p>
{% endraw %}

## 迁移说明

对于JavaScript项目，我们更改了标准库的工件名称。而不是<code> kotlin-js-library </ code>，它现在是<code> kotlin-stdlib-js </ code>。当您更新到1.1 beta 2或更新的版本时，您将需要更新您的Maven和Gradle脚本。
除此之外，JavaScript的测试支持类（包<code> kotlin.test </ code>）现在被打包为单独的工件，就像以前为Java版本一样。如果您在JS项目中使用kotlin.test，请在<code> kotlin-test-js </ code>上添加依赖关系。
Kotlin标准库中的协同程序API已被移至<code> kotlin.coroutines.experimental </ code>包;如果您在代码中使用了这些API，则需要更新导入。看到 [安德烈的论坛帖子](https://discuss.kotlinlang.org/t/experimental-status-of-coroutines-in-1-1-and-related-compatibility-concerns/2236) 为了这个变化的背景。
我们还使您的Gradle项目中的实验协同程序支持变得更加容易。您可以将以下代码片段添加到build.gradle中，而不是编辑gradle.properties：

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

如果你正在使用 [kotlinx.corutines库](https://github.com/kotlin/kotlinx.coroutines) 请更新您的依赖关系到版本<code> 0.6-beta </ code>。该库的早期版本与此Kotlin更新不兼容。
## 新功能

我们在此测试版中添加了几个最新功能。这里是最重要的：

* 编译器现在报告一个警告，如果您声明一个扩展名与同一个类的成员具有相同的签名，并且将始终被遮蔽（例如String.length（））
* 传递给通用功能的成员引用的类型推断现在得到很大的改进（KT-10711）
* 减号运算符现在可以与地图一起使用，返回地图的副本，并删除给定的键。 -  =操作符可以在可变地图上使用，以从地图中删除给定的键。
* 现在可以使用KPropertyN.getDelegate（）访问委托属性的委托实例（详见KT-8384）;
* 意图（由Kirill Rakhman贡献）合并两个嵌套if语句;
* 支持在启用Jack工具链时构建Android项目（jackOptions {true}）;
* 意图（由Kirill Rakhman贡献）在Android应用程序中生成View构造函数。

## 源兼容性Kotlin 1.0

在这次更新中我们非常关注的另一个领域是与Kotlin 1.0的源兼容性</ strong>。这样，即使您的团队使用Kotlin 1.0，您也可以尝试使用Kotlin 1.1，而不用担心通过使用新版本中添加的一些功能来打破构建。
要启用兼容性模式：

* 对于Maven，Ant和命令行编译器，将-language-version编译器参数设置为1.0。
* 在Gradle构建中，将kotlinOptions {languageVersion =“1.0”}添加到您的compileKotlin任务中。
* 在IDE中，在Kotlin facet设置或Settings |中指定语言版本构建，执行，部署|编译器| Kotlin编译器

## 如何尝试

<strong>在Maven / Gradle中：</ strong>将<code> http://dl.bintray.com/kotlin/kotlin-eap-1.1 </ code>添加为构建脚本和项目的存储库;使用<code> 1.1.0-beta-38 </ code>作为编译器和标准库的版本号。
<strong>在IntelliJ IDEA中：</ strong>转到<em>工具→Kotlin→配置Kotlin插件更新</ em>，然后在<em>更新频道</ em>下拉菜单中选择“Early Access Preview 1.1”下拉列表，然后按<em>检查更新</ em>。
命令行编译器可以从中下载 [Github发行页面](https://github.com/JetBrains/kotlin/releases/tag/v1.1-beta2) 。
<strong> <a href="http://try.kotlinlang.org/"> try.kotlinlang.org </a> </ strong>。即将推出。
让我们来吧！
