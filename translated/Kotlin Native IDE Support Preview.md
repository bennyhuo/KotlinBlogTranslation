---
title: Kotlin/Native IDE Support Preview
author: Roman Belov
date: 2017-11-04 02:44:00
source_url: https://blog.jetbrains.com/kotlin/2017/11/kotlinnative-ide-support-preview/
tags: 
categories:  官方动态
---

Kotlin / Native是一种全新的技术，可将Kotlin直接编译为机器码，并生成可在没有虚拟机的情况下运行的可执行文件。在KotlinConf 2017上，我们宣布了Kotlin / Native开发工具的预览版本。
虽然我们有与Kotlin合作的IntelliJ IDEA，但Kotlin / Native与Clang和LLDB支持等本土技术相结合。那为什么JetBrains为Kotlin / Native选择CLion，我们的C和C ++的IDE。
要开始使用，请下载并安装CLion 2017.3（请注意，此版本现在处于早期访问预览阶段）。接下来，从JetBrains插件库中安装两个插件。在CLion中，选择“配置”→“插件”→“安装JetBrains插件”然后在那里找到Kotlin和Kotlin / Native插件，并安装它们。不要忘记，这仍然是一个技术预览和错误是可能的，但如果你遇到任何，请报告！

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
