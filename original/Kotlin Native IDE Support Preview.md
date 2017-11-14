---
title: Kotlin/Native IDE Support Preview
author: Roman Belov
date: 2017-11-04 02:44:00
source_url: https://blog.jetbrains.com/kotlin/2017/11/kotlinnative-ide-support-preview/
tags: 
categories:  官方动态
---

Kotlin/Native is a brand new technology that compiles Kotlin directly to machine code and produces executables that can run without a virtual machine. At KotlinConf 2017, we announced a preview release of development tools for Kotlin/Native.
While we have IntelliJ IDEA for working with Kotlin, Kotlin/Native integrates with technologies from the native world such as Clang and LLDB support. That’s why JetBrains’ choice for Kotlin/Native is CLion, our IDE for C and C++.
To get started, download and install CLion 2017.3 (note that this version is at the early access preview stage for now). Next, install two plugins from the JetBrains Plugin Repository. In CLion, choose Configure → Plugins → Install JetBrains plugin…, then find Kotlin and Kotlin/Native plugins there, and install them. Don’t forget this is still a technology preview and bugs are possible, but if you encounter any, please report them!

{% raw %}
<p><span id="more-5421"></span></p>
{% endraw %}

# New Kotlin/Native Project

Learning a new technology requires a good entry point, and we’ve already prepared one for you. Create sample projects right from CLion and play with some simple code examples. Click *New Project → Kotlin/Native Application *and select one of the available samples. CLion will automatically download and install native packages on your computer as needed.
# Code Insight

Kotlin/Native IDE support is based on the regular Kotlin plugin for IntelliJ IDEA. This means that you have all the specific code inspections, intentions, code completion actions and of course refactorings already available for Kotlin/Native!
# Debugging

The CLion plugin supports debugging, based on LLDB. Note this is still under active development and requires specific conditions (plus a bit of luck) to get working. Please do try it and let us know how it works for you!
# Kotlin/Native Tests

The CLion plugin also supports running tests written using the kotlin.test framework. For the time being, to run a test, you need to create a ‘Kotlin/Native Test’ run configuration (under Run → Edit Configurations…) manually. Creating configurations from the editor popup menu will be supported in future updates.
Once you run the tests, you will see a nice test tree like this one:
# What’s Next?

IDE code insight, testing support, and a debugger are already a pretty solid tool-set, and we’ll continue to polish these features to make your experience as smooth as possible for the public release. However, it’s not everything we plan to offer with the first stable release of Kotlin/Native IDE support. We are also going to fully support interoperability with native libraries, with features such as documentation preview, cross-language navigation and, of course, refactorings.
Have a nice Kotlin/Native!
