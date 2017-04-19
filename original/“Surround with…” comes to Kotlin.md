---
title: "“Surround with…” comes to Kotlin"
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

Great news for fans of Intellij IDEA: “Surroud with…” action is now available for Kotlin!
## What is the “Surround with…” action?

<strong></strong>This action allows you to surround a block of code with <em>if</em>, <em>try</em> or other statements (see [the full list](#full_list) bellow). Simply select a block of code, press <em>Ctrl + Alt + T</em> and choose the template (<em>Cmd + Alt + T</em> for Mac):<span id="more-868"></span>

{% raw %}
<p><img alt="" data-recalc-dims="1" src="https://i0.wp.com/www.evernote.com/shard/s119/sh/30b15c39-ad04-4960-a4ac-63a0c44b7798/15300fa96a0fb6466f48c2abdd2f5f8b/deep/0/surroundwith1.jpg?w=640&amp;ssl=1"/></p>
{% endraw %}

The IDE will add the neccessary code and put the caret at the position that allows you to finish your refactoring:

{% raw %}
<p><img alt="" data-recalc-dims="1" src="https://i0.wp.com/www.evernote.com/shard/s119/sh/7423c1e1-9464-4839-80a5-5c45e5cb981f/ee1a2a5c7f7ba1727f7cd59b3dde48dc/deep/0/surroundwith2.jpg?w=640&amp;ssl=1"/></p>
{% endraw %}

If the surrounded block contains variable declarations that are used after the block, they will be moved out of the block:

{% raw %}
<p><img alt="" data-recalc-dims="1" src="https://i1.wp.com/www.evernote.com/shard/s119/sh/38c06e91-2f1d-4140-9feb-f444b8c73a83/8bf36356ade04ec4ac35fef45dda5187/deep/0/surroundwith3.jpg?w=640&amp;ssl=1"/></p>
{% endraw %}


{% raw %}
<p><img alt="" data-recalc-dims="1" src="https://i1.wp.com/www.evernote.com/shard/s119/sh/07b88a70-2214-45e4-a83b-a798a3902e11/f973c8b777dc6854aefc7c63bd081266/deep/0/surroundwith4.jpg?w=640&amp;ssl=1"/></p>
{% endraw %}


{% raw %}
<p><span class="embed-youtube" style="text-align:center; display: block;"><iframe allowfullscreen="true" class="youtube-player" height="390" src="https://www.youtube.com/embed/Bwuj15P8yOQ?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640"></iframe></span></p>
{% endraw %}

## Function Literal Template

You can surround a block of code like this:

{% raw %}
<p><img alt="" data-recalc-dims="1" src="https://i1.wp.com/www.evernote.com/shard/s119/sh/c6ee3d36-5c3e-4b8c-976d-b9761c190390/af84ab8fcf8d47df3d7a77eff5244452/deep/0/surroundwith5.jpg?w=640&amp;ssl=1"/></p>
{% endraw %}

Use this template if you want to “hide” some variables in the scope of the block, to create a property with function type or a local function and if you want to call any function with function literal as an argument.

{% raw %}
<p><span class="embed-youtube" style="text-align:center; display: block;"><iframe allowfullscreen="true" class="youtube-player" height="390" src="https://www.youtube.com/embed/ufSDvAxo544?version=3&amp;rel=1&amp;fs=1&amp;autohide=2&amp;showsearch=0&amp;showinfo=1&amp;iv_load_policy=1&amp;wmode=transparent" style="border:0;" type="text/html" width="640"></iframe></span></p>
{% endraw %}

## When template

You don’t need to write <em>when </em>expression by hand any more: you can simply select a subject expression, choose “surround with <em>when(expr) {}</em>” and the result will be:

{% raw %}
<p><img alt="" data-recalc-dims="1" src="https://i2.wp.com/www.evernote.com/shard/s119/sh/08db9fde-304e-4226-a261-0a8d6724ebc1/7d45417b3110edfb4091e8dcc03b97c9/deep/0/surroundwith6.jpg?w=640&amp;ssl=1"/></p>
{% endraw %}

## Full list of  “Surround with…” templates

When a block of code is selected:

* if
* if / else
* { }                       – function literal
* try
* try / catch
* try / catch / finally

When an expression is selected:

* !(expr)                – add negation for Boolean
* (expr)                 – surround with parentheses
* “${expr}”           – surround with quotes
* when(expr) {}

## Kotlin M5.1

We release “Surround with…” as a part of Kotlin M5.1 that will be out very soon.
