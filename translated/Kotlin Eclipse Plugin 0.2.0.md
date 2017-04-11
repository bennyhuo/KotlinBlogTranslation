---
title: [译]Kotlin Eclipse Plugin 0.2.0
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
---

# Kotlin Eclipse插件0.2.0

今天我们很高兴为Eclipse提供一个新版本的Kotlin插件。此版本包括以下功能：

* 更新到Kotlin M12
* Java到Kotlin转换器
* 从Java导航到Kotlin源
* 比较视图中的Kotlin语法突出显示


{% raw %}
<p><span id="more-2339"></span></p>
{% endraw %}

## Kotlin M12

从这个版本开始，Eclipse插件支持Kotlin M12。所有现有项目将自动开始使用，新项目将从头开始配置使用。请查看语言中的更改和弃用列表，因为一些代码可能需要更新。
## 将Java代码转换为Kotlin

在此版本中，我们将继续改进Eclipse IDE中Java和Kotlin之间的交互。
现在可以通过将Java文件从IDE转换为Kotlin，以我们的在线演示的方式，在现有项目中尝试Kotlin。在IDE中转换的好东西是能够一次转换多个文件。 Action被称为将Java转换为Kotlin，可以在Package Explorer视图的上下文菜单中找到：

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/06/conversion.png"><img alt="conversion" class="alignnone size-full wp-image-2340" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/06/conversion.png?resize=640%2C403&amp;ssl=1"/></a></p>
{% endraw %}

如果文件创建的槽转换恰好是项目中的第一个Kotlin文件，IDE也将配置Kotlin Nature，并建议将Kotlin运行时库添加到类路径。
有一些已知的问题，格式化的结果代码，但这将在下一个版本之一改进。
## 从Java代码导航到Kotlin

现在您可以轻松地从Java导航到Kotlin类和功能与打开声明（Ctrl +单击或F3）。

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/06/navigation.png"><img alt="navigation" class="alignnone size-full wp-image-2341" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/06/navigation.png?resize=640%2C191&amp;ssl=1"/></a></p>
{% endraw %}

## 突出显示文件比较

最后，此更新使得比较视图​​中的Kotlin语法高亮显示。在Kotlin代码的第一次代码审查之后，这被立即被认为是一个主要功能

{% raw %}
<p> <a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/06/screenshot3.png"><img alt="screenshot3" class="alignnone size-full wp-image-2342" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/06/screenshot3.png?resize=640%2C253&amp;ssl=1"/></a></p>
{% endraw %}

## 反馈

通过将此按钮拖放到Eclipse来安装此版本：

{% raw %}
<p><a class="drag" href="http://marketplace.eclipse.org/marketplace-client-intro?mpc_install=2257536" title="Drag to your running Eclipse workspace to install Kotlin Plugin for Eclipse"><img alt="Drag to your running Eclipse workspace to install Kotlin Plugin for Eclipse" data-recalc-dims="1" src="https://i2.wp.com/marketplace.eclipse.org/sites/all/themes/solstice/_themes/solstice_marketplace/public/images/btn-install.png?w=640&amp;ssl=1"/></a></p>
{% endraw %}

欢迎您的反馈和拉动请求！
