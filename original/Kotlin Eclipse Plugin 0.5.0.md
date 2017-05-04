---
title: "Kotlin Eclipse Plugin 0.5.0"
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

New in this release

* Kotlin Beta 2 support
* Semantic highlighting
* Rename refactoring
* Mark Occurrences
* Extract Variable refactoring
* Navigation to Kotlin standard library sources


{% raw %}
<p><a class="drag" href="http://marketplace.eclipse.org/marketplace-client-intro?mpc_install=2257536" title="Drag to your running Eclipse workspace to install Kotlin Plugin for Eclipse"><img alt="Drag to your running Eclipse workspace to install Kotlin Plugin for Eclipse" data-recalc-dims="1" src="https://i2.wp.com/marketplace.eclipse.org/sites/all/themes/solstice/_themes/solstice_marketplace/public/images/btn-install.png?w=640&amp;ssl=1"/></a></p>
{% endraw %}


{% raw %}
<p><span id="more-3156"></span></p>
{% endraw %}

## Semantic Highlighting

Life is getting more colourful with a new release of the Kotlin plugin featuring semantic code highlighting. Right now we share most settings with the Java editor, so Kotlin code will reuse your favourite color theme. Switching to the Eclipse *Dark Theme* and configuring highlighting with [Eclipse Color Themes](http://eclipsecolorthemes.org/) plugin is also supported.
## Rename

We now support *Rename* refactoring. One thing unusually advanced about it is that it works across languages: Kotlin declarations can be renamed from any usage, both in Java and Kotlin! Same for renaming Java declarations.<br/>
<img data-recalc-dims="1" onmouseout="this.src='https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/11/rename.png?w=640';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/11/rename.gif';" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/11/rename.png?w=640"/>
## Mark Occurrences

Automatic usages highlighting for the declaration under cursor is now enabled by default for Kotlin files.<br/>
<img data-recalc-dims="1" onmouseout="this.src='https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/11/mark.png?w=640';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/11/mark.gif';" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/11/mark.png?w=640"/>
## Extract Variable

It’s now possible to create local variables from selected expression with *Extract Local Variable* refactoring.<br/>
<img data-recalc-dims="1" onmouseout="this.src='https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/11/extract.png?w=640';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/11/extract.gif';" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/11/extract.png?w=640"/>
## Navigation to Kotlin Standard Library

Reference to Kotlin standard library from Kotlin code are now navigable. Activating *Open Declaration* action on usages will open correspondent file and reveal declaration in the library source code.<br/>
<img data-recalc-dims="1" onmouseout="this.src='https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/11/navifation.png?w=640';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/11/navigation.gif';" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/11/navifation.png?w=640"/>
