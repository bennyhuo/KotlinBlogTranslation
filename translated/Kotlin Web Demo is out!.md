---
title: [译]Kotlin Web Demo is out!
date: 2012-01-10 19:16:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2012/01/kotlin-web-demo-is-out/
---

自从第一次提交到我们的源代码管理以来，已经有一年多了，我们很高兴地宣布Kotlin的第一个公开预览。
此预览的工作原理如下：

* 您访问http://kotlin-demo.jetbrains.com并在浏览器中加载代码编辑器：
* 你查看例子，修改它们，甚至解决我们的玩具问题示例;
* 您可以在我们服务器上运行的JVM上运行代码，以便您可以使用熟悉的JDK类;
* 或者，您可以将代码编译为JavaScript并在浏览器中运行：

请注意，JavaScript后端是一个pre-alpha版本，因此可能会拒绝编译一些程序。


{% raw %}
<p><span id="more-318"></span></p>
{% endraw %}

实验特点
默认情况下，只有运行程序时才会显示错误突出显示。但是，您可以尝试我们正在尝试的一些功能，并打开“as-you-type”错误突出显示：

如果选择“服务器”，编辑器将开始与我们服务器上托管的类型检查服务进行通信。如果您选择“客户端”，则会将类型检查器作为您的计算机上运行的（相当大的）Applet加载。
“服务器”和“客户端”选项都可以让您完成代码：
请注意，这些功能是实验性的，并可以自由地向我们报告任何问题。
快来了
此演示将进一步开发，让您有更多的乐趣。除此之外，我们还计划添加以下内容：

* 标准库扩展功能，使JDK集合和其他常见API更加愉快（像map（）/ filter（）等））;
* 代码挑战：目前，我们以包含测试数据的代码片段的形式提供了一些示例问题。这将扩展到比赛自动化测试系统。
* 更多示例：总是有更多的炫耀

玩的开心！
