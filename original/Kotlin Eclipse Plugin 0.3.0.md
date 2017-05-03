---
title: "Kotlin Eclipse Plugin 0.3.0"
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
translator:
translator_url:
---

We are happy to announce Kotlin Eclipse Plugin version 0.3.0. This release is loaded with new features:

* Kotlin M13 support
* Find references
* Parameter hints
* Select enclosing/next/previous element
* Override/Implement action
* Body conversion intention
* Debugger: Run to cursor
* Debugger: Step into selection
* Better performance


{% raw %}
<p><a class="drag" href="http://marketplace.eclipse.org/marketplace-client-intro?mpc_install=2257536" title="Drag to your running Eclipse workspace to install Kotlin Plugin for Eclipse"><img alt="Drag to your running Eclipse workspace to install Kotlin Plugin for Eclipse" data-recalc-dims="1" src="https://i2.wp.com/marketplace.eclipse.org/sites/all/themes/solstice/_themes/solstice_marketplace/public/images/btn-install.png?w=640&amp;ssl=1"/></a></p>
{% endraw %}


{% raw %}
<p><span id="more-2689"></span></p>
{% endraw %}

## Find References

A very common task in daily activity of any developer is looking up references to a function, property or class all over the project. <em>Find References</em> in 0.3.0 searches through usages of Kotlin declarations in both Java and Kotlin code. And running <em>Find References</em> for a Java declaration reveals usages in Kotlin too! The same <code>Ctrl+Shift+G / ⇧⌘G</code> shortcut works for both languages.

{% raw %}
<p><img data-recalc-dims="1" onmouseout="this.src='https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/09/references_cover_new.png?w=600';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/09/references_new.gif';" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/09/references_cover_new.png?w=600"/></p>
{% endraw %}

## Parameter Hints

Kotlin Eclipse plugin now supports parameter hints. To look up the order of function parameters or their names and types, place the cursor inside the parentheses and press <code>Ctrl+Shift+Space / ⇧⌃Space</code> to see a hint.

{% raw %}
<p><img data-recalc-dims="1" onmouseout="this.src='https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/09/parameters_cover.png?w=480';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/09/parameters.gif';" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/09/parameters_cover.png?w=480"/></p>
{% endraw %}

## Select Enclosing Element

Some IDE features proved to be really addictive, and once accustomed, you will always miss them if they are not present. A good example is a <em>Select Enclosing Element</em>. It’s far more convenient to select “function arguments”,  “statement”, “function body” or “whole class” instead of thinking where should selection begin and end.

{% raw %}
<p><img data-recalc-dims="1" onmouseout="this.src='https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/09/selection_cover_new.png?w=495';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/09/selection_new.gif';" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/09/selection_cover_new.png?w=495"/></p>
{% endraw %}

Please note that <em>Select Next/Previous element</em> actions are also supported for Kotlin.
## Override/Implement Members

Since 0.3.0 Kotlin Eclipse plugin can help in resolving a very frequent “not implemented” error. <em>Quick Fix</em> menu (<code>Ctrl + 1</code> / ⌘1) has an <em>Implement Members</em> item that will generate all missing declarations after selection.

{% raw %}
<p><img data-recalc-dims="1" onmouseout="this.src='https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/09/implement_fix_cover.png?w=450';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/09/implement_fix.gif';" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/09/implement_fix_cover.png?w=450"/></p>
{% endraw %}

It’s also possible to call <em>Override/Implement Members</em> and select methods you want to implement as a separate action from <em>Quick Access</em> (<code>Ctrl + 3</code> / ⌘3).

{% raw %}
<p><img data-recalc-dims="1" onmouseout="this.src='https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/09/implement_override_cover.png?w=530';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/09/implement_override.gif';" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/09/implement_override_cover.png?w=530"/></p>
{% endraw %}

## Body Conversion Quick-Fix

Kotlin allows you to declare methods in a really short way, and now Eclipse can to convert one form to another with a quick fix (<code>Ctrl + 1</code> / ⌘1).

{% raw %}
<p><img data-recalc-dims="1" onmouseout="this.src='https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/09/body_convert_cover_new.png?w=335';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/09/body_convert_new.gif';" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/09/body_convert_cover_new.png?w=335"/></p>
{% endraw %}

## Debugger

Several important debugger features are ready to be tried out.
### Run To Line

While debugging your program it’s a very common task to skip some code and stop the execution an particular line. This is very much like a “one-time breakpoint”, but removing a breakpoint right after hitting it is tedious. This is why debuggers have <em>Run To Line</em> (<code>Ctrl + R</code> / ⌘R) feature which is now also supported for Kotlin code.

{% raw %}
<p><img data-recalc-dims="1" onmouseout="this.src='https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/09/run_to_cursor_cover.png?w=630';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/09/run_to_cursor.gif';" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/09/run_to_cursor_cover.png?w=630"/></p>
{% endraw %}

### Step Into Selection

It’s often not enough to debug in terms on lines. Imagine the situation when there’re several calls in one line and you want to skip two of them but wonder what the third function does. Instead of cycling through <em>Step-Into</em>, <em>Step-Out</em> actions it’s better to hit <em>Step Into Selection</em> (<code>Ctrl + F5</code> / ⌥ F5) action.

{% raw %}
<p><img data-recalc-dims="1" onmouseout="this.src='https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/09/step_into_selection_cover.png?w=580';" onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/09/step_into_selection.gif';" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/09/step_into_selection_cover.png?w=580"/></p>
{% endraw %}

## Performance

This release has a significant boost in performance of build and completion on board.
## Conclusion

While it might seem that we choose features for release at random it’s not exactly so <img alt=":)" class="wp-smiley" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1" style="height: 1em; max-height: 1em;"/> Actually we are gradually addressing problems we have in our project with the [percentage of Kotlin code growing](https://github.com/JetBrains/kotlin-eclipse) and pretty happy with the result.
If you have an idea what feature should be implemented next, please [create an issue](https://youtrack.jetbrains.com/newIssue?project=KT&clearDraft=true&c=Subsystems+Eclipse+Plugin) in our tracker.
Have a nice Kotlin in Eclipse!
