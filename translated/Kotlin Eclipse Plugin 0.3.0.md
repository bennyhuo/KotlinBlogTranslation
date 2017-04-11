---
title: [译]Kotlin Eclipse Plugin 0.3.0
date: 2015-09-24 18:58:00
author: Nikolay Krasko
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/09/kotlin-eclipse-plugin-0-3-0/
---

我们很高兴地宣布Kotlin Eclipse插件版本0.3.0。此版本加载了新功能：

* Kotlin M13支持
* 查找参考
* 参数提示
* 选择封闭/下一个/上一个元素
* 覆盖/实施动作
* 身体转换意图
* 调试器：运行到光标
* 调试器：逐步选择
* 更好的表现


{% raw %}
<p><a class="drag" href="http://marketplace.eclipse.org/marketplace-client-intro?mpc_install=2257536" title="Drag to your running Eclipse workspace to install Kotlin Plugin for Eclipse"><img alt="Drag to your running Eclipse workspace to install Kotlin Plugin for Eclipse" data-recalc-dims="1" src="https://i2.wp.com/marketplace.eclipse.org/sites/all/themes/solstice/_themes/solstice_marketplace/public/images/btn-install.png?w=640&amp;ssl=1"/></a></p>
{% endraw %}


{% raw %}
<p><span id="more-2689"></span></p>
{% endraw %}

## 查找参考

任何开发人员日常活动中非常常见的任务是查找对整个项目中的函数，属性或类的引用。通过使用Java和Kotlin代码中的Kotlin声明，在0.3.0搜索中查找参考。并且运行Java声明的查找引用也揭示了在Kotlin中的用法！相同的Ctrl + Shift + G /⇧⌘G快捷方式适用于两种语言。

{% raw %}
<p><img data-recalc-dims="1" onmouseout="this.src='https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/09/references_cover_new.png?w=600';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/09/references_new.gif';" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/09/references_cover_new.png?w=600"/></p>
{% endraw %}

## 参数提示

Kotlin Eclipse插件现在支持参数提示。要查找功能参数或其名称和类型的顺序，请将光标放在括号内，然后按Ctrl + Shift + Space /⇧^Space查看提示。

{% raw %}
<p><img data-recalc-dims="1" onmouseout="this.src='https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/09/parameters_cover.png?w=480';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/09/parameters.gif';" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/09/parameters_cover.png?w=480"/></p>
{% endraw %}

## 选择封闭元素

一些IDE功能被证明是真的上瘾，一旦习惯了，如果不存在，你总是会想念他们。一个很好的例子是选择封闭元素。选择“功能参数”，“语句”，“功能体”或“全班”更方便，而不是考虑选择开始和结束。

{% raw %}
<p><img data-recalc-dims="1" onmouseout="this.src='https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/09/selection_cover_new.png?w=495';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/09/selection_new.gif';" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/09/selection_cover_new.png?w=495"/></p>
{% endraw %}

请注意，Kotlin还支持选择下一个/上一个元素操作。
## 覆盖/实施成员

由于0.3.0 Kotlin Eclipse插件可以帮助解决非常频繁的“未实现”错误。快速修复菜单（Ctrl + 1 /⌘1）有一个实现成员项目，将在选择后生成所有缺少的声明。

{% raw %}
<p><img data-recalc-dims="1" onmouseout="this.src='https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/09/implement_fix_cover.png?w=450';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/09/implement_fix.gif';" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/09/implement_fix_cover.png?w=450"/></p>
{% endraw %}

也可以调用“覆盖/实现成员”，并从快速访问（Ctrl + 3 /⌘3）中选择要实现的方法作为单独的操作。

{% raw %}
<p><img data-recalc-dims="1" onmouseout="this.src='https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/09/implement_override_cover.png?w=530';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/09/implement_override.gif';" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/09/implement_override_cover.png?w=530"/></p>
{% endraw %}

## 身体转换快速修复

Kotlin允许您以一种很简单的方式声明方法，现在Eclipse可以通过快速修复（Ctrl + 1 /⌘1）将一个窗体转换为另一个窗体。

{% raw %}
<p><img data-recalc-dims="1" onmouseout="this.src='https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/09/body_convert_cover_new.png?w=335';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/09/body_convert_new.gif';" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/09/body_convert_cover_new.png?w=335"/></p>
{% endraw %}

## 调试器

几个重要的调试器功能已经准备好尝试了。
### 跑到线

在调试程序时，跳过一些代码并停止执行特定行是一个非常常见的任务。这非常像“一次性断点”，但是在击中之后删除断点是乏味的。这就是为什么调试器有运行到行（Ctrl + R /⌘R）功能，现在也支持Kotlin代码。

{% raw %}
<p><img data-recalc-dims="1" onmouseout="this.src='https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/09/run_to_cursor_cover.png?w=630';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/09/run_to_cursor.gif';" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/09/run_to_cursor_cover.png?w=630"/></p>
{% endraw %}

### 步入选择

在线上调试通常还不够。想象一下，一行中有几个电话的情况，你想跳过其中两个，但是想知道第三个功能是什么。而不是单步进入Step-Into，Step-Out动作最好是点击Step Into Selection（Ctrl + F5 / F5）操作。

{% raw %}
<p><img data-recalc-dims="1" onmouseout="this.src='https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/09/step_into_selection_cover.png?w=580';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/09/step_into_selection.gif';" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/09/step_into_selection_cover.png?w=580"/></p>
{% endraw %}

## 性能

此版本在船上构建和完成的性能有显着提升。
## 结论

虽然我们可能会随机选择要发布的功能，但并不完全如此。实际上，我们逐渐解决了我们在项目中遇到的问题，Kotlin代码的增长百分比和结果令人高兴。
如果您有一个想法下一步应该实现哪些功能，请在我们的跟踪器中创建一个问题。
在Eclipse中有一个漂亮的Kotlin！
