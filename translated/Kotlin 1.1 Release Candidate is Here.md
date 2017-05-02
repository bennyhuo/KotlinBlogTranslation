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

截至今天，Kotlin 1.1终于到了候选版本(RC)阶段。这意味着我们的大部分开发工作都已经完成，我们对结果感到满意，我们很快将它们作为最终的Kotlin 1.1版本发布。我们已经在内部对此版本进行了大量测试，但现实世界总是比任何测试环境更加多样化，因此我们需要您的帮助。请尝试这个版本，让我们知道你的经验！

{% raw %}
<p><img alt="11RC-01" class="alignnone size-full wp-image-4599" height="251" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/02/11RC-01.png" width="1300"/><br/>
<span id="more-4589"></span></p>
{% endraw %}

候选版本中唯一的新功能是<code> takeUnless </ code>函数 - 它对应在1.1之前添加的 [takeIf](https://kotlinlang.org/docs/reference/whatsnew11.html#takeif-and-also) ，但判断条件相反。对于错误修复，还有更多，完整清单请查看 [更新日志](https://github.com/JetBrains/kotlin/blob/1.1-rc/ChangeLog.md) 。除此之外，我们已经在IDE中修复了几个性能问题 - 包含有长期存在和最近回归出的问题。
## 迁移说明

就像我们之前 [提到的](https://blog.jetbrains.com/kotlin/2017/01/kotlin-1-1-beta-is-here/) ，由发行版本生成的所有二进制文件都被编译器所禁止：您现在需要重新编译</ b>由1.1-M0x和Beta编译的所有内容。当然，从1.0.x开始的所有代码都不需要重新编译。
在这之前，您可以从Java 6开始，以任何版本的Java运行Kotlin编译器，但这从第一个1.1.x更新开始有变化，编译器将仅在Java 8或9下运行。为您准备迁移，编译器现在会在Java 6或7下运行时发出警告。请注意，这仅影响构建环境; <b>编译代码默认情况下仍然与Java 6兼容，我们没有计划删除对它的支持。
现在不推荐使用<code> .javaClass </ code>扩展属性。作为替代，请使用<code> :: class.java </ code>。 IDE提供了一个quickfix来更新所有使用，包括单个和整个项目。
为了减小JavaScript标准库的大小，我们已经在<code> kotlin.dom </ code>和<code> kotlin.dom.build </ code>包中有大量帮助函数不推荐使用了，而在将来的更新中可能会删除它们。
## 如何尝鲜

<b>在Maven / Gradle中：</ b>将<code> http://dl.bintray.com/kotlin/kotlin-eap-1.1 </ code>添加为构建脚本和项目的仓库;使用<code> 1.1.0-rc-91 </ code>作为编译器和标准库的版本号。
<b>在IntelliJ IDEA中：</ b>转到<i>Tools→Kotlin→Configure Kotlin Plugin Updates</ i>，然后在<i>Update channel</ i>后的下拉列表中选择“Early Access Preview 1.1”下拉列表，然后按<i>Check for updates</ i>。
<strong>在Eclipse中</ strong>：从以下更新站点安装插件
<code> https://dl.bintray.com/jetbrains/kotlin/eclipse-plugin/0.8.0 </ code>
<strong>The command-line compiler</ strong>可以从 [Github发行页面](https://github.com/JetBrains/kotlin/releases/tag/v1.1-rc) 下载。
最后，让我们开启Kotlin之旅吧！<b> <a href="http://try.kotlinlang.org/"> try.kotlinlang.org </a> </ b>。