---
title: "[译]Kotlin Eclipse Plugin 0.7 Is Here!"
date: 2016-06-03 17:48:00
author: Nikolay Krasko
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2016/06/kotlin-eclipse-plugin-0-7-is-here/
translator:
translator_url:
---

我们很高兴为Eclipse IDE提供一个新版本的插件。除了支持Kotlin **1.0.2**编译器，此更新带来非常重要的功能和改进。

{% raw %}
<p><span id="more-3901"></span></p>
{% endraw %}

该版本中重新编写了代码格式化功能。而不是我们的第一个天真的实现，我们主要设法将高级格式化程序从Kotlin IntelliJ Idea插件移植到Eclipse中。这意味着 [很多修复](https://youtrack.jetbrains.com/issues/KT?q=Formatter%20State:%20Fixed%20Subsystems:%20IDE) 已经在那里，即将到来的改进将自动获取！

{% raw %}
<p><img class="size-full" onmouseout="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/06/fromater.png';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/06/fromater.gif';" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/06/fromater.png"/></p>
{% endraw %}

新线自动缩进也从这个代码重用中受益，现在显示出更加可预测和聪明的行为。
可以添加缺少的类，从0.1.0版本逐个导入一个快速修复，现在我们通过引入<em>组织导入</em>功能进行了改进。它将清理未使用的导入，为文件中使用的类添加缺少的导入，并使用它们。

{% raw %}
<p><img class="size-full" onmouseout="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/06/organize.png';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/06/organize.gif';" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/06/organize.png" width="800"/></p>
{% endraw %}

我们的完成在确定变体的优先级方面有几个修正，现在可用性更高。此外，还可以立即在完成弹出窗口中建议未导入的类，并将与相应的导入一起插入。

{% raw %}
<p><img class="size-full" onmouseout="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/06/import.png';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/06/import.gif';" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/06/import.png" width="800"/></p>
{% endraw %}

添加了关于缺少或非法修饰符的几个快速修复：

* 现在可以向被覆盖或子类化的声明添加一个open修饰符。

