---
title: [译]Kotlin 1.1 Release Candidate is Here
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
---

截至今天，Kotlin 1.1终于达到了候选人候选人阶段。这意味着我们的大部分开发工作都已经完成，我们对结果感到满意，我们很快将它们作为最终的Kotlin 1.1版本发布。我们已经在内部对此版本进行了大量测试，但现实世界总是比任何测试环境更加多样化，因此我们需要您的帮助。请尝试这个版本，让我们知道你的经验！

{% raw %}
<p><img alt="11RC-01" class="alignnone size-full wp-image-4599" height="251" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/02/11RC-01.png" width="1300"/><br/>
<span id="more-4589"></span></p>
{% endraw %}

发布候选人中唯一的新功能是无需功能 - 即takeIf的对应（在1.1之前添加），但具有倒置的条件。对于错误修复，还有更多，更改日志为您提供了一个完整的列表。除此之外，我们已经在IDE中修复了几个性能问题 - 长期以来的痛点和最近的回归。
## 迁移说明

正如我们前面提到的，预编译版本生成的所有二进制文件都被编译器所禁止：现在需要重新编译1.1-M0x和Beta编译的所有内容。当然，从1.0.x开始的所有代码完全没有重新编译。
到目前为止，您可以从Java 6开始，以任何版本的Java运行Kotlin编译器，但这是即将更改 - 从第一个1.1.x更新开始，编译器将仅在Java 8或9下运行。为您准备迁移，编译器现在会在Java 6或7下运行时发出警告。请注意，这仅影响构建环境;编译代码默认情况下仍然与Java 6兼容，我们没有计划删除对它的支持。
现在不推荐使用.javaClass扩展属性。作为替代，请使用:: class.java。 IDE提供了一个quickfix来更新用途，包括单个和整个项目。
为了减小JavaScript标准库的大小，我们在kotlin.dom和kotlin.dom.build包中弃用了很多帮助函数，我们将在以后的更新中删除它们。
## 如何尝试

在Maven / Gradle中：添加http://dl.bintray.com/kotlin/kotlin-eap-1.1作为构建脚本和项目的存储库;使用1.1.0-rc-91作为编译器和标准库的版本号。
在IntelliJ IDEA：转到工具→Kotlin→配置Kotlin插件更新，然后在更新频道下拉列表中选择“早期访问预览1.1”，然后按检查更新。
在Eclipse中：使用以下更新站点安装该插件
https://dl.bintray.com/jetbrains/kotlin/eclipse-plugin/0.8.0
命令行编译器可以从Github发行页面下载。
在try.kotlinlang.org。
让我们来吧！
