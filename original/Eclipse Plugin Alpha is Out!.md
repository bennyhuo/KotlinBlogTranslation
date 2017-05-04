---
title: "Eclipse Plugin Alpha is Out!"
date: 2015-03-31 00:54:00
author: Nikolay Krasko
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/03/eclipse-plugin-alpha-is-out/
translator:
translator_url:
---

Kotlin support in IntelliJ IDEA has always been among our top priorities, but we have been working on Eclipse support as well, and today we are happy to present the first **alpha** result of this effort.
Although it’s only a start and many things will be improved over time, it already features

* Building and Running Your Code
* Java Interoperability
* Code Highlighting
* Debugging
* Navigation
* Basic Code Completion (Ctrl+Space)
* Auto-Import
* Unit Testing

## Installation

To give it a try you will need a clean installation of [Eclipse Luna](https://www.eclipse.org/downloads/) . The Kotlin plugin is available from the <em>Eclipse Marketplace</em>. The easiest way to install the Kotlin plugin is to **drag-and-drop this button into a running Eclipse window**:

{% raw %}
<p><a class="drag" href="http://marketplace.eclipse.org/marketplace-client-intro?mpc_install=2257536" title="Drag to your running Eclipse workspace to install Kotlin Plugin for Eclipse"><img alt="Drag to your running Eclipse workspace to install Kotlin Plugin for Eclipse" data-recalc-dims="1" src="https://i2.wp.com/marketplace.eclipse.org/sites/all/themes/solstice/_themes/solstice_marketplace/public/images/btn-install.png?w=640&amp;ssl=1"/></a><br/>
<span id="more-1945"></span></p>
{% endraw %}

Alternatively, you can use <em>Help -&gt; Eclipse Marketplace…</em> menu, or the following update site:

{% raw %}
<p></p>
{% endraw %}

```kotlin
https://dl.bintray.com/jetbrains/kotlin/eclipse-plugin/last/
```

{% raw %}
<p></p>
{% endraw %}

Our [Tutorial](http://kotlinlang.org/docs/tutorials/getting-started-eclipse.html) describes the installation process in more details.
## Eclipse IDE Support

Here we give a quick overview of the features available in this version.
### Building Your Code

Kotlin compiler is integrated into Eclipse’s build process, as a result you can mix Kotlin and Java freely in one Eclipse project.
You can start by creating a new Kotlin project or adding a Kotlin file to an existing Java project. In either case Java classes are accessible from Kotlin and vice versa.

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/03/New-Kotlin-File-in-Context-Menu.png"><img alt="New Kotlin File in Context Menu" class="alignnone size-full wp-image-1957" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/03/New-Kotlin-File-in-Context-Menu.png?resize=640%2C194&amp;ssl=1"/></a></p>
{% endraw %}

Diagnostics (errors and warnings) reported by Kotlin are displayed in the <em>Problems View</em>:

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/03/skitch.png"><img alt="Problems View in Action" class="alignnone size-full wp-image-1959" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/03/skitch.png?resize=640%2C241&amp;ssl=1"/></a></p>
{% endraw %}

### Editor

The basic editor features such as code highlighting and formatting are supported. Basic code completion is also supported, but it needs further improvements.
<em>Auto-import</em> for unresolved classes both from Java and Kotlin is already there:

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/03/Screenshot-2015-03-30-15.26.27.png"><img alt="Eclipse Auto-Import Feature" class="alignnone size-full wp-image-1965" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/03/Screenshot-2015-03-30-15.26.27.png?resize=393%2C119&amp;ssl=1"/></a></p>
{% endraw %}

Many [quick-fixes](https://github.com/JetBrains/kotlin/tree/master/idea/src/org/jetbrains/kotlin/idea/quickfix) and [intentions](https://github.com/JetBrains/kotlin/tree/master/idea/src/org/jetbrains/kotlin/idea/intentions) would be useful while editing Kotlin sources, and we will gradually add more and more of them. We started with the simple one for replacing `get()` calls with the indexing operator (`[...]`):

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/03/Screenshot-2015-03-30-15.29.20.png"><img alt="Replace 'get' With Index Operator" class="alignnone size-full wp-image-1966" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/03/Screenshot-2015-03-30-15.29.20.png?resize=500%2C83&amp;ssl=1"/></a></p>
{% endraw %}

### Navigation

<em>Open Declaration</em> is the only navigation action that is supported in this release:

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/03/eclipse-references.png"><img alt="Eclipse References" class="alignnone size-full wp-image-1969" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/03/eclipse-references.png?resize=592%2C159&amp;ssl=1"/></a></p>
{% endraw %}

Also, you can navigate to declarations in Kotlin files with <em>Outline View</em> and search for Kotlin files by name in <em>Open Resource</em> window.
### Debugger

With our plugin installed, Eclipse JDT debugger gets initial support for Kotlin. Again, there’s much to be improved, but you can

* Set breakpoints in Kotlin code
* Use Step in/over/out
* View local variables and content of Kotlin objects


{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/03/Screenshot-2015-03-30-16.39.21.png"><img alt="Eclipse Debug" class="alignnone size-full wp-image-1971" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/03/Screenshot-2015-03-30-16.39.21.png?resize=640%2C176&amp;ssl=1"/></a></p>
{% endraw %}

### Unit Testing

If you already have JUnit 3 or JUnit 4 in the classpath, you can write your tests in Kotlin. <em>Run -&gt; Run As -&gt; Kotlin JUnit Test</em> in the main menu starts testing and opens results in the <em>JUnit View</em>.

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/03/Screenshot-2015-03-30-01.39.29.png"><img alt="Eclipse Tests Demonstation" class="alignnone size-full wp-image-1962" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/03/Screenshot-2015-03-30-01.39.29.png?resize=560%2C199&amp;ssl=1"/></a></p>
{% endraw %}


{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/03/Screenshot-2015-03-30-01.39.51.png"><img alt="Eclipse Tests Result" class="alignnone size-full wp-image-1961" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/03/Screenshot-2015-03-30-01.39.51.png?resize=503%2C172&amp;ssl=1"/></a></p>
{% endraw %}

## Feedback Welcome

We could have continued implementing features one by one slowly making the plugin more and more stable and powerful. But instead we decided to show the early alpha hoping for the **feedback**. It is very important for us.
Some issues and feature-requests are already in our [tracker](https://youtrack.jetbrains.com/search/Kotlin%20Eclipse-19206) . Please fill free to add more. Thanks.
Also, this is an open-source project, and we expect it to be even more of a **community effort** than our compiler and IntelliJ Plugin are, so your [Pull Requests](https://github.com/JetBrains/kotlin-eclipse/) are very welcome.
