---
title: "[译]Kotlin 1.1 Release Candidate is Here"
date: 2017-02-17 13:37:00
author: Mikhail Glukhikh
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/02/kotlin-1-1-release-candidate-is-here/
translator: ahong222
translator_url: https://github.com/ahong222
---

截至今天，Kotlin 1.1 终于到了候选版本（RC）阶段。这意味着大部分开发工作都已经完成，我们对此结果感到满意，很快就会发布 Kotlin 1.1 正式版。我们已经在内部对此版本进行了大量测试，但现实世界总是比任何测试环境更加多样化，因此我们需要您的帮助。请尝试这个版本，让我们知道您的体验！

{% raw %}
<p><img alt="11RC-01" class="alignnone size-full wp-image-4599" height="251" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/02/11RC-01.png" width="1300"/><br/>
<span id="more-4589"></span></p>
{% endraw %}

候选版本中唯一的新功能是 `takeUnless` 函数，它对应 1.1 之前添加的 [takeIf](https://kotlinlang.org/docs/reference/whatsnew11.html#takeif-and-also)，但判断条件相反。至于错误修复则有很多，完整清单请查看[更新日志](https://github.com/JetBrains/kotlin/blob/1.1-rc/ChangeLog.md)。除此之外，我们还修复了几个 IDE 中的性能问题，包括长期存在和最近回归才出现的。

## 迁移说明
就像我们之前[提到的](https://blog.jetbrains.com/kotlin/2017/01/kotlin-1-1-beta-is-here/)，预发布版本生成的所有二进制文件不能在当前的编译器下使用：您现在**需要重新编译**由 1.1-M0x 和 Beta 编译的所有内容。当然，从 1.0.x 开始的所有代码都不需要重新编译。

在这之前，您可以从 Java 6 开始，以任何版本的 Java 运行 Kotlin 编译器，但这从第一个 1.1.x 更新开始有变化，编译器将仅在 Java 8 或 9 下运行。为您准备迁移，编译器现在会在 Java 6 或 7 下运行时发出警告。请注意，这仅影响构建环境；**编译代码默认情况下仍然与 Java 6 兼容**，我们没有计划删除对它的支持。

现在不推荐使用 `.javaClass` 扩展属性。作为替代，请使用 `::class.java`。IDE 提供了一个 quickfix 来更新写法，单独的修改或者更新整个项目。

为了减小 JavaScript 标准库的大小，我们已经将 `kotlin.dom` 和 `kotlin.dom.build` 包中的大量辅助函数注解为不推荐使用了，然后在将来的更新中删除它们。

## 如何尝鲜
**在 Maven/Gradle 中：** 将 `http://dl.bintray.com/kotlin/kotlin-eap-1.1` 添加为构建脚本和项目的仓库；使用 `1.1.0-rc-91` 作为编译器和标准库的版本号。

**在 IntelliJ IDEA 中：** 点击菜单 *Tools → Kotlin → Configure Kotlin Plugin Updates*，然后在 *Update channel* 的下拉列表中选择 "Early Access Preview 1.1"，接着点击 *Check for updates*。

**在 Eclipse 中：** 从以下更新站点安装插件
`https://dl.bintray.com/jetbrains/kotlin/eclipse-plugin/0.8.0`

**The command-line compiler** 可以从 [Github 发布页面](https://github.com/JetBrains/kotlin/releases/tag/v1.1-rc)下载。
最后，让我们开启 Kotlin 之旅吧！**<a href="http://try.kotlinlang.org/">try.kotlinlang.org</a>**。
