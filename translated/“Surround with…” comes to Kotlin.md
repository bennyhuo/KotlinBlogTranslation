---
title: "[译]“Surround with…” comes to Kotlin"
date: 2013-02-26 09:20:00
author: Natalia Ukhorskaya
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2013/02/surround-with-comes-to-kotlin/
---

对于Intellij IDEA的球迷来说，好消息：“Surroud with ...”动作现在可用于Kotlin！
## 什么是“Surround with ...”动作？

<strong> </strong>此操作允许您使用<em>环绕一个代码块，如果</em>，<em>尝试</em>或其他语句（请参阅 [完整列表](#full_list) 下面）。只需选择一个代码块，按<em> Ctrl + Alt + T </em>，然后选择适用于Mac的模板（<em> Cmd + Alt + T </em>）：<span id =“more-868” > </span>

{% raw %}
<p><img alt="" data-recalc-dims="1" src="https://i0.wp.com/www.evernote.com/shard/s119/sh/30b15c39-ad04-4960-a4ac-63a0c44b7798/15300fa96a0fb6466f48c2abdd2f5f8b/deep/0/surroundwith1.jpg?w=640&amp;ssl=1"/></p>
{% endraw %}

IDE将添加必要的代码，并将插入符号放在允许您完成重构的位置：

{% raw %}
<p><img alt="" data-recalc-dims="1" src="https://i0.wp.com/www.evernote.com/shard/s119/sh/7423c1e1-9464-4839-80a5-5c45e5cb981f/ee1a2a5c7f7ba1727f7cd59b3dde48dc/deep/0/surroundwith2.jpg?w=640&amp;ssl=1"/></p>
{% endraw %}

如果被包含的块包含在块之后使用的变量声明，则它们将被移出该块：

{% raw %}
<p><img alt="" data-recalc-dims="1" src="https://i1.wp.com/www.evernote.com/shard/s119/sh/38c06e91-2f1d-4140-9feb-f444b8c73a83/8bf36356ade04ec4ac35fef45dda5187/deep/0/surroundwith3.jpg?w=640&amp;ssl=1"/></p>
{% endraw %}


{% raw %}
<p><img alt="" data-recalc-dims="1" src="https://i1.wp.com/www.evernote.com/shard/s119/sh/07b88a70-2214-45e4-a83b-a798a3902e11/f973c8b777dc6854aefc7c63bd081266/deep/0/surroundwith4.jpg?w=640&amp;ssl=1"/></p>
{% endraw %}


{% raw %}
<p><span class="embed-youtube" style="text-align:center; display: block;"><iframe allowfullscreen="true" class="youtube-player" height="390" src="https://www.youtube.com/embed/Bwuj15P8yOQ?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640"></iframe></span></p>
{% endraw %}

## 功能文字模板

你可以围绕一个这样的代码块：

{% raw %}
<p><img alt="" data-recalc-dims="1" src="https://i1.wp.com/www.evernote.com/shard/s119/sh/c6ee3d36-5c3e-4b8c-976d-b9761c190390/af84ab8fcf8d47df3d7a77eff5244452/deep/0/surroundwith5.jpg?w=640&amp;ssl=1"/></p>
{% endraw %}

如果要“隐藏”块范围内的某些变量，使用此模板创建具有函数类型或本地函数的属性，并且要使用函数文字作为参数调用任何函数。

{% raw %}
<p><span class="embed-youtube" style="text-align:center; display: block;"><iframe allowfullscreen="true" class="youtube-player" height="390" src="https://www.youtube.com/embed/ufSDvAxo544?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640"></iframe></span></p>
{% endraw %}

## 当模板

您不需要手写</em>表达手段：您可以简单地选择主题表达式，当（expr）{} </em>“选择”使用<em>环绕“，结果将会：

{% raw %}
<p><img alt="" data-recalc-dims="1" src="https://i2.wp.com/www.evernote.com/shard/s119/sh/08db9fde-304e-4226-a261-0a8d6724ebc1/7d45417b3110edfb4091e8dcc03b97c9/deep/0/surroundwith6.jpg?w=640&amp;ssl=1"/></p>
{% endraw %}

## “Surround with ...”模板的完整列表

当选择代码块时：

* 如果
* 如果别的
* {}  - 函数文字
* 尝试
* 试着抓
* try / catch / finally

当选择表达式时：

* ！（expr） - 为布尔值添加否定
* （expr） - 用括号括起来
* “$ {expr}” - 用引号括起来
* when（expr）{}

## Kotlin M5.1

作为Kotlin M5.1的一部分，我们将尽快发布“Surround with ...”。
