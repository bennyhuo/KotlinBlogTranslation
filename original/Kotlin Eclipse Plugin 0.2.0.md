---
title: Kotlin Eclipse Plugin 0.2.0
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

# Kotlin Eclipse Plugin 0.2.0

Today we are happy to present a new version of Kotlin plugin for Eclipse. This release includes the following features:

* Update to Kotlin M12
* Java to Kotlin converter
* Navigation to Kotlin sources from Java
* Kotlin syntax highlighting in Compare View


{% raw %}
<p><span id="more-2339"></span></p>
{% endraw %}

## Kotlin M12

Starting from this release, Eclipse plugin supports Kotlin M12. All existing projects will start using it automatically and new projects will be configured to use it from the beginning. Please take a look at the list of changes and deprecations in the language, as some code will probably need to be updated.
## Convert Java Code to Kotlin

In this release we continue to improve interaction between Java and Kotlin in Eclipse IDE.
Now it’s possible to try Kotlin in an existing project by converting Java files to Kotlin from IDE in the way our online demo can do it. Nice thing about conversion in the IDE is the ability to convert several files at once. Action is called Convert Java to Kotlin and can be found in the context menu in the Package Explorer view:

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/06/conversion.png"><img alt="conversion" class="alignnone size-full wp-image-2340" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/06/conversion.png?resize=640%2C403&amp;ssl=1"/></a></p>
{% endraw %}

If the file created trough conversion happens to be the first Kotlin file in the project, the IDE will also configure the Kotlin Nature and suggest to add Kotlin runtime library to the class path.
There are some known issues with formatting of resulting code but this will be improved in one of next releases.
## Navigate from Java Code to Kotlin

Now you can easily navigate from Java to Kotlin classes and functions with Open Declaration (Ctrl+Click or F3).

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/06/navigation.png"><img alt="navigation" class="alignnone size-full wp-image-2341" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/06/navigation.png?resize=640%2C191&amp;ssl=1"/></a></p>
{% endraw %}

## Highlighting for File Comparison

Finally, this update enables Kotlin syntax highlighting in the Compare view. This was immediately considered to be a major feature after the first code review of Kotlin code

{% raw %}
<p> <a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/06/screenshot3.png"><img alt="screenshot3" class="alignnone size-full wp-image-2342" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/06/screenshot3.png?resize=640%2C253&amp;ssl=1"/></a></p>
{% endraw %}

## Feedback

Install this release by drag-and-drop’ing this button to Eclipse:

{% raw %}
<p><a class="drag" href="http://marketplace.eclipse.org/marketplace-client-intro?mpc_install=2257536" title="Drag to your running Eclipse workspace to install Kotlin Plugin for Eclipse"><img alt="Drag to your running Eclipse workspace to install Kotlin Plugin for Eclipse" data-recalc-dims="1" src="https://i2.wp.com/marketplace.eclipse.org/sites/all/themes/solstice/_themes/solstice_marketplace/public/images/btn-install.png?w=640&amp;ssl=1"/></a></p>
{% endraw %}

Your feedback and pull requests are welcome!
