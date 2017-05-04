---
title: "[译]Kotlin Eclipse Plugin 0.5.0"
date: 2015-12-01 15:57:00
author: Nikolay Krasko
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/12/kotlin-eclipse-plugin-0-5-0/
translator:
translator_url:
---

这个版本的新功能

* Kotlin Beta 2 支持
* 语义突出
* 重命名重构
* 标记发生
* 提取变量重构
* 导航到 Kotlin 标准库源


{% raw %}
<p><a class="drag" href="http://marketplace.eclipse.org/marketplace-client-intro?mpc_install=2257536" title="Drag to your running Eclipse workspace to install Kotlin Plugin for Eclipse"><img alt="Drag to your running Eclipse workspace to install Kotlin Plugin for Eclipse" data-recalc-dims="1" src="https://i2.wp.com/marketplace.eclipse.org/sites/all/themes/solstice/_themes/solstice_marketplace/public/images/btn-install.png?w=640&amp;ssl=1"/></a></p>
{% endraw %}


{% raw %}
<p><span id="more-3156"></span></p>
{% endraw %}

## 语义突出显示

随着新版本的 Kotlin 插件，使用语义代码突出显示，生活越来越丰富多彩。现在我们与 Java 编辑器共享大多数设置，因此 Kotlin 代码将重用您最喜欢的颜色主题。切换到 Eclipse *黑暗主题*并配置突出显示 [Eclipse 颜色主题](http://eclipsecolorthemes.org/) 还支持插件。
## 改名

我们现在支持*重命名*重构。有一件事情是异常先进的：它可以跨语言工作：Kotlin 声明可以从 Java 和 Kotlin 中的任何用法重命名！相同的重命名 Java 声明
<img data-recalc-dims =“1”onmouseout =“this.src ='https：//i2.wp.com/blog.jetbrains.com/kotlin/files/2015/11/rename.png？w = 640 ';“ onmouseover =“this.src ='https：//d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/11/rename.gif';” src =“https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/11/rename.png?w=640”/>
## 标记发生

默认情况下，为 Kotlin 文件启用自动使用高亮显示在光标下的声明
<img data-recalc-dims =“1”onmouseout =“this.src ='https：//i2.wp.com/blog.jetbrains.com/kotlin/files/2015/11/mark.png？w = 640 ';“ onmouseover =“this.src ='https：//d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/11/mark.gif';” src =“https：//i2.wp.com/blog.jetbrains.com/kotlin/files/2015/11/mark.png?w=640”/>
## 提取变量

现在可以使用*提取局部变量*重构来从所选表达式创建局部变量
<img data-recalc-dims =“1”onmouseout =“this.src ='https：//i1.wp.com/blog.jetbrains.com/kotlin/files/2015/11/extract.png？w = 640 ';“ onmouseover =“this.src ='https：//d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/11/extract.gif';” src =“https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/11/extract.png?w=640”/>
## 导航到 Kotlin 标准库

来自 Kotlin 代码的 Kotlin 标准库的引用现在可以导航。激活*开放宣言*对使用的操作将打开通讯记录文件，并在图书馆的源代码中显示声明。<br/>
<img data-recalc-dims =“1”onmouseout =“this.src ='https：//i0.wp.com/blog.jetbrains.com/kotlin/files/2015/11/navifation.png？w = 640 ';“ onmouseover =“this.src ='https：//d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/11/navigation.gif';” src =“https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/11/navifation.png?w=640”/>
