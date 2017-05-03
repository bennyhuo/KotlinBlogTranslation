---
title: "[译]Kotlin Evolves: How to Keep Your Code Up"
date: 2015-06-17 16:46:00
author: ilya.gorbunov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/06/kotlin-evolves-how-to-keep-your-code-up/
---

Kotlin正在进行定稿，作为此过程的一部分，我们将<strong>清理</strong>：修改语言及其库。最大的变化是在 [M12](http://blog.jetbrains.com/kotlin/2015/05/kotlin-m12-is-out/) ，但还有更多的来临。要点是在我们发布1.0之前执行所有必要的突破性更改，以便我们可以在发布后保持语言和库<strong>向后兼容</strong>。
诀窍是我们，我们自己和你，我们的用户已经有相当多的代码写在Kotlin，我们不希望所有的代码在每次更新中都无所作为（一些破坏是不可避免的，不幸的是，但我们是做我们最好的）。以用户友好的方式进行更改的一般方案是“deprecate-release-remove”，例如：

* 在M12中，我们弃用了相当多的语言结构和库类/函数，
* 那么我们发布了M12，所以每当你使用这些被删除的语言和库功能时，编译器会发出警告，
* 在下一个里程碑中，我们将完全删除这些不推荐的内容，因此编译器将发出错误而不是警告。

所以，如果你的代码中有任何不赞成的警告，那么现在只需要适当的时间去除它们</strong>：下一个主要的更新将会使所有的代码变红，你的构建会中断。
## 摆脱弃用警告

如上所述，有两种弃用警告：语言弃用和库弃用。为了摆脱他们，我们提供几个选择
<span id =“more-2358”> </span>
### 快速修复

使用<em>快速修复</em>，当您按下<code> Alt + Enter </code>时，您可以修复弃用警告：将出现可用选项，可在整个项目中修复单个警告或所有此类警告。不推荐的语言结构和库函数将被更新的版本替代。
请注意，要快速修复在库函数上正常工作，<strong>标准库的来源必须附加到您的项目</strong>。
### 项目范围代码清理

当您已经找到已弃用的用法时，快速修复很好，但是由于我们最近已经弃用了很多东西，因此查找每个用户可能不是一个可行的选择。在这种情况下，您可以使用IDE操作批量应用这些修补程序“<em> Analyze |代码清理</em>“。
我们提供名为“<em>使用冗余或不推荐使用的语法或废弃符号</em>”的检查。在清理期间，此检查自动替代过时语言功能或不必要的详细代码结构的使用，并使用紧凑和最新的语法，以及已弃用的符号的用法以及其提出的替换。
### 手动重写

在极少数情况下，一些不推荐的用法不能自动固定。这些包括语言结构和库符号的使用，将在没有替代方法的情况下被删除，或者不会在不破坏代码的情况下被重写，或者当有几种重写代码的选项时，需要明确的选择。
<strong>底线</strong>。如何准备好Kotlin M13：<br/>
 - 安装Kotlin M12（确保您安装了M12的最新更新），<br/> <br/>
 - 通过上述手段去除废弃警告。
## 在M13中肯定会放弃哪个API

我们想分享一些关于API的计划，放弃M13。这并不是将会被删除的详尽清单。
### 流

Kotlin流的大问题是它们与Java 8中的流冲突（通过名称），我们不能依赖Java 8流，因为Kotlin也针对早期的JDK（认为Android）。因此，在M11中引入序列而不是流，并且流将被丢弃。
### 迭代器工具

迭代器和一些迭代器类的实用函数已被弃用，有利于M8中的流，但现在也不推荐流，因此这种功能的最终继承者是<code> Sequence </code>。
### 顺序实现

我们在实现序列操作所需的标准库中有一堆序列实现，例如，<code> sequence.filter {predicate} </code>的<code> FilteringSequence </code>，<code> TransformingSequence </code > for <code> sequence.map {transform} </code>等等。这些实现类在图书馆的公共API中没有任何意义，所以我们已经在M12中弃用它们，并将它们在M13中隐藏（或者从用户的角度来看）:)。
### String.split和String.replaceFirst

在M12之前，我们对从JDK继承的字符串进行了扩展方法：<code> split </code>，<code> replaceAll </code> / <code> replaceFirst </code>，<code> matches </code>。他们都有共同之处在于它们采用字符串参数并将其解释为正则表达式。这种方法有两个缺点。
首先，它需要编译到底层的<code> Pattern </code>，这在紧密循环中使用时可能具有性能意义。这将详细解释一个名为的文章 [“Java的String.split（）和replace（）”的隐藏的邪恶](http://chrononsystems.com/blog/hidden-evils-of-javas-stringsplit-and-stringr) 。我们希望尽可能的避免在将来写下名为“Kotlin的某些东西的隐藏的罪恶”的文章，所以我们像往常一样决定明确表达，并引入这些功能的重载，这些函数采用了<code> Regex </code >作为预期正则表达式的参数。
其次，它使得很难引入一个负载字符串并将其解释为文字。我们不得不在M12中引入这样的重载，用于<code> split </code>和<code> replaceFirst </code>，我们必须分别命名为<code> splitBy </code>和<code> replaceFirstLiteral </code>。但是，一旦我们删除M13中原来的弃用重载，我们将把这些新方法重命名为<code> split </code>和<code> replaceFirst </code>（当然我们会把<code > splitBy </code>和<code> replaceFirstLiteral </code>已弃用，并在其<code>已弃用的</code>注释中提供替换。
还值得注意的是，<code> split </code>方法的返回类型已更改：它现在返回一个<code> List＆lt; String＆gt; </code>而不是<code> Array＆lt; String＆gt; </code >，并且最终改变其关于删除空子串的行为。按照最不高兴的原则，我们从这个不合适的责任中减轻了<code> split </code>，现在不需要<code> split（regex：String）</code>，我们应该说<code> split（regex.toRegex （））。dropLastWhile {it.isEmpty（）} .toTypedArray（）</code>。 IDE将帮助您迁移。
## 结论

我们将在标准库中进行更多更改，但是我们已经介绍了代码清理和快速修复。在发布之前，对于每个Kotlin里程碑，如上所述执行代码清理将使您的代码保持最新。
