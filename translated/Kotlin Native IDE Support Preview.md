---
title: Kotlin/Native IDE Support Preview
author: Roman Belov
date: 2017-11-04 02:44:00
source_url: https://blog.jetbrains.com/kotlin/2017/11/kotlinnative-ide-support-preview/
tags: 
categories:  官方动态
---


Kotlin/Native是一项可以将Kotlin直接编译为机器码的[全新技术](http://kotlinlang.org/docs/reference/native-overview.html)，并且生成不依赖虚拟机即可运行的可执行文件。在KotlinConf 2017上，我们正式发布了Kotlin/Native开发工具的预览版本。

尽管我们使用IntelliJ IDEA来编写Kotlin，但Kotlin/Native结合了如Clang和LLDB等原生技术的支持。因此JetBrains为Kotlin/Native选择了[CLion](https://www.jetbrains.com/clion/)作为C和C++的IDE。  

要开始使用，请下载并安装CLion 2017.3（请注意，此版本现阶段仍处于早期预览阶段）。接下来，从JetBrains插件库中安装两个插件。在CLion设置中，依次选择***配置(Configure) → 插件(Plugins) → 安装JetBrains插件…(Install JetBrains plugin…)***，找到并安装Kotlin和Kotlin/Native插件。请谨记该技术仍然是预览版本，遇到任何错误都有可能，若您在开发中遇到相关问题可及时向我们进行反馈！


{% raw %}
<p><span id="more-5421"></span></p>
{% endraw %}

# 新Kotlin / Native项目

学习新技术需要一个很好的切入点，我们已经为你准备了一个。从CLion创建示例项目，并使用一些简单的代码示例。点击*新建项目* Kotlin / Native Application *，然后选择一个可用样本。 CLion将根据需要自动下载并在计算机上安装本地软件包。
# Code Insight

Kotlin / Native IDE支持基于IntelliJ IDEA常规Kotlin插件。这意味着您拥有所有特定的代码检查，意图，代码完成操作，当然还有可用于Kotlin / Native的重构！
# 调试

CLion插件支持基于LLDB的调试。请注意，这仍处于积极的发展阶段，需要特定的条件（加上一点运气）才能正常工作。请尝试一下，让我们知道它是如何工作的！
# Kotlin /本机测试

CLion插件还支持使用kotlin.test框架编写的运行测试。暂时运行一个测试，需要手动创建一个“运行”菜单下的运行配置（在运行→编辑配置下），在编辑器弹出菜单中创建配置将在以后的更新中被支持。
一旦你运行测试，你会看到一个像这样的一个不错的测试树：
# 什么是下一个？

IDE代码洞察力，测试支持和调试器已经是一个非常坚实的工具集，我们将继续研究这些功能，使您的体验尽可能流畅地公开发布。但是，这并不是我们计划提供的第一个Kotlin / Native IDE支持的稳定版本。我们还将全力支持与本地库的互操作性，并提供诸如文档预览，跨语言导航以及当然还有重构等功能。
有一个不错的Kotlin / Native！
