---
title: "[译]Kotlin Eclipse Plugin 0.2.0"
date: 2015-06-10 21:26:00
author: Nikolay Krasko
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/06/kotlin-eclipse-plugin-0-2-0-2/
translator:
translator_url:
---

# Kotlin Eclipse 插件 0.2.0

今天我们很高兴为 Eclipse 提供一个新版本的 Kotlin 插件。此版本包括以下功能：

* 更新到 Kotlin M12
* Java 到 Kotlin 转换器
* 从 Java 导航到 Kotlin 源
* 比较视图中的 Kotlin 语法突出显示


{% raw %}
<p><span id="more-2339"></span></p>
{% endraw %}

## Kotlin M12

从此版本开始，Eclipse 插件支持 [Kotlin M12](http://blog.jetbrains.com/kotlin/2015/05/kotlin-m12-is-out/) 。所有现有项目将自动开始使用，新项目将从头开始配置使用。请看一下列表 [更改和弃用](https://github.com/JetBrains/kotlin/releases/tag/build-0.12.200) 在语言中，因为一些代码可能需要更新。
## 将 Java 代码转换为 Kotlin

在此版本中，我们将继续改进 Eclipse IDE 中 Java 和 Kotlin 之间的交互。
现在可以通过将 Java 文件从 IDE 转换为 Kotlin，在现有的项目中尝试 Kotlin [在线演示](http://try.kotlinlang.org/) 可以做到。在 IDE 中转换的好东西是能够一次转换多个文件。 Action 被称为*将 Java 转换为 Kotlin*，可以在*包资源管理器*视图的上下文菜单中找到：

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/06/conversion.png"><img alt="conversion" class="alignnone size-full wp-image-2340" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/06/conversion.png?resize=640%2C403&amp;ssl=1"/></a></p>
{% endraw %}

如果文件创建的槽转换恰好是项目中的第一个 Kotlin 文件，IDE 也将配置 Kotlin Nature，并建议将 Kotlin 运行时库添加到类路径。
有一些已知的问题，格式化的结果代码，但这将在下一个版本之一改进。
## 从 Java 代码导航到 Kotlin

现在，您可以使用*Open Declaration*（Ctrl + Click 或 F3）轻松地从 Java 导航到 Kotlin 类和函数。

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/06/navigation.png"><img alt="navigation" class="alignnone size-full wp-image-2341" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/06/navigation.png?resize=640%2C191&amp;ssl=1"/></a></p>
{% endraw %}

## 突出显示文件比较

最后，此更新可在*比较*视图中启用 Kotlin 语法高亮显示。在 Kotlin 代码<img alt =“:)”class =“wp-smiley”data-recalc-dims =“1”src =“https：// i2 的第一个代码审查后，这被立即被认为是主要功能。 wp.​​com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1“style =”height：1em; max-height：1em;“/>

{% raw %}
<p> <a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/06/screenshot3.png"><img alt="screenshot3" class="alignnone size-full wp-image-2342" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/06/screenshot3.png?resize=640%2C253&amp;ssl=1"/></a></p>
{% endraw %}

## 反馈

通过将此按钮拖放到 Eclipse 来安装此版本：

{% raw %}
<p><a class="drag" href="http://marketplace.eclipse.org/marketplace-client-intro?mpc_install=2257536" title="Drag to your running Eclipse workspace to install Kotlin Plugin for Eclipse"><img alt="Drag to your running Eclipse workspace to install Kotlin Plugin for Eclipse" data-recalc-dims="1" src="https://i2.wp.com/marketplace.eclipse.org/sites/all/themes/solstice/_themes/solstice_marketplace/public/images/btn-install.png?w=640&amp;ssl=1"/></a></p>
{% endraw %}

您的**反馈**和 [拉请求](https://github.com/JetBrains/kotlin-eclipse) 受欢迎的！
