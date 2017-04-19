---
title: "Kotlin Eclipse Plugin 0.7 Is Here!"
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
---

We are happy to present a new release of our plugin for Eclipse IDE. Along with the support for Kotlin <strong>1.0.2</strong> compiler, this update brings very important features and improvements.

{% raw %}
<p><span id="more-3901"></span></p>
{% endraw %}

The code formatting feature was rebuilt in this release. Instead of our first naive implementation we have mostly managed to port the advanced formatter from the Kotlin IntelliJ Idea plugin into Eclipse. This means that [a lot of fixes](https://youtrack.jetbrains.com/issues/KT?q=Formatter%20State:%20Fixed%20Subsystems:%20IDE) are already there and upcoming improvements will be picked up automatically!

{% raw %}
<p><img class="size-full" onmouseout="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/06/fromater.png';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/06/fromater.gif';" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/06/fromater.png"/></p>
{% endraw %}

New line auto-indent also benefitted from this code reuse and now shows far more predictable and smart behaviour.
It was possible to add missing classes imports one-by-one with a quick-fix since 0.1.0 version, and now we’ve improved on that by introducing the <em>Organize Imports</em> feature. It will clean unused imports, add missing imports for classes used in the file and resort them.

{% raw %}
<p><img class="size-full" onmouseout="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/06/organize.png';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/06/organize.gif';" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/06/organize.png" width="800"/></p>
{% endraw %}

Our completion got several fixes in prioritizing variants and is now far more usable. Also not-imported classes are now suggested in completion popup at once and will be inserted together with the corresponding import.

{% raw %}
<p><img class="size-full" onmouseout="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/06/import.png';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/06/import.gif';" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2016/06/import.png" width="800"/></p>
{% endraw %}

Several quick-fixes about missing or illegal modifiers were added:

* It’s now possible to add an open modifier to a declaration which is overridden or subclassed.

