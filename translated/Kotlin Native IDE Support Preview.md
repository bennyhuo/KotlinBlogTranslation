---
title: Kotlin/Native IDE Support Preview
author: Roman Belov
date: 2017-11-04 02:44:00
source_url: https://blog.jetbrains.com/kotlin/2017/11/kotlinnative-ide-support-preview/
tags: 
categories:  官方动态  
translator: SnakEys  
translator_url: https://github.com/SnakeEys

---


Kotlin/Native是一项可以将Kotlin直接编译为机器码的[全新技术](http://kotlinlang.org/docs/reference/native-overview.html)，并且生成不依赖虚拟机即可运行的可执行文件。在KotlinConf 2017上，我们正式发布了Kotlin/Native开发工具的预览版本。

尽管我们使用IntelliJ IDEA来编写Kotlin，但Kotlin/Native结合了如Clang和LLDB等原生技术的支持。因此JetBrains为Kotlin/Native选择了[CLion](https://www.jetbrains.com/clion/)作为C和C++的IDE。  

要开始使用，请下载并安装[CLion 2017.3](https://www.jetbrains.com/clion/nextversion/)（请注意，此版本现阶段仍处于早期预览阶段）。接下来，从JetBrains[插件库](https://plugins.jetbrains.com/)中安装两个插件。在CLion设置中，依次选择<strong>配置(Configure) → 插件(Plugins) → 安装JetBrains插件…(Install JetBrains plugin…)</strong>，找到并安装Kotlin和Kotlin/Native插件。请谨记该技术仍然是预览版本，遇到任何错误都有可能，若您在开发中遇到相关问题可及时[向我们反馈](https://youtrack.jetbrains.com/issues/KT)！


{% raw %}
<p><span id="more-5421"></span></p>
{% endraw %}

# Kotlin/Native新项目

CLion是学习这门新技术非常好的切入点。从CLion创建示例项目，并使用简单的示例代码。在菜单中依次选择\*新建项目(New Project) → Kotlin/Native应用程序(Kotlin/Native Application)\*，并从列表中选择可用版本。CLion会根据需要自动在计算机上下载并安装本地软件包。 

# 代码内视

Kotlin/Native IDE支持基于IntelliJ IDEA的常规Kotlin插件。这意味着开发者完全拥有特定的代码检查，意图，代码补全等操作，当然还有可用于Kotlin/Native的重构。

# 调试

CLion插件支持基于LLDB的调试。但目前仍处于活跃开发阶段，需要特定的条件（加上一点运气）才能正常运行。尽量尝试并告诉我们是如何运行的！
# Kotlin /本机测试

CLion插件还支持运行使用kotlin.test框架编写的测试。但需要手动创建‘Kotlin/Native测试’的运行配置（<strong><em>运行(Run)→ 编辑配置(Edit Configurations…)</em></strong>），在编辑器弹出菜单中创建配置将在后续的更新中加入。    
运行测试，即可看到如下图中所示的测试树：


# 下一步计划？

IDE代码内视，测试支持以及调试器已经是非常不错的工具集，但我们将继续研究这些功能，让开发者尽可能体验如公开发布版本一样的流畅性。但是，这并不是首个Kotlin/Native IDE支持版本的所有内容，我们还将全力支持与本地库的互操作性，并提供诸如文档预览，跨语言导航，当然还有少不了的重构等功能。

请尽情享受Kotlin/Native！
