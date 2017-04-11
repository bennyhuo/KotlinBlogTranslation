---
title: [译]Upcoming Change: More Null-safety for Java
date: 2015-04-10 15:34:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/04/upcoming-change-more-null-safety-for-java/
---

我们结合零安全和Java互操作的战斗已经很久了：

* 我们开始处理所有的Java引用类型为可空，这太不方便了;
* 然后我们使用外部注释来指定可空性，创建了KAnnotator，但是在版本控制时整个事情太脆弱了，有时候用户无法做到所需要的（特别是在继承时）。
* 在M9中，我们抛弃了注释（暂时），并介绍了平台类型，现在可以做任何事情，但是我们失去了（一些）类型安全;
* 在M11中，我们开始通过在Java可空性限制被违反的情况下发出警告来带回注释的有用方面。

现在，我们正计划再做一个步骤，并结合平台类型使用注释，以尽可能地恢复类型安全。
## 概述

详细信息在本规范文档中描述，但总体思路如下：每当我们在Java中遇到可空性注释时，它们都不会与其周围的任何内容相冲突（如超类型中的重写声明），我们使用精确的类型。例如：

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Java
 
class Foo {
    @Nullable String bar(@NotNull String baz) {...}
}
 
// Kotlin
 
foo.bar(nullableString ?: "default")?.length()
 
```

{% raw %}
<p></p>
{% endraw %}

在最后一行，编译器要求我们处理需要非空值的bar（）的参数（所以我们使用“elvis”来提供一个默认值），并且结果为空（我们使用安全的呼叫来保护NPE）。如果我们忽略了任何一个，那么这将是一个编译错误。
## 冲突

似乎我们只是把我们以前放弃的东西（并对此感到高兴），但这不是这样。细节是相当涉及的，但总而言之，与平台类型之前所引入的巨大差异在于您不能拥有同时接受ArrayList <String>和ArrayList <String？>的类型，并导致当我们需要将从Java获得的东西重新提供给另一个Java方法时，需要痛苦的解决方法。是的，如果不是泛型，几乎没有什么会改变，但泛型总是让编译器的作者的世界更加光明
另一件改变的是我们如何处理超越签名的冲突：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Super {
    String foo(String bar) { ... }
}
 
class Sub extends Super {
    @Override
    String foo(@NotNull String bar) { ... }
}
 
```

{% raw %}
<p></p>
{% endraw %}

当我们将未注释的Java类型视为可空时，在上面的示例中，Kotlin只能看到两个不相关的方法：foo（String？）和foo（String）具有不兼容的类型签名。
还有更多的可能的冲突来源，其中大多数在注释中实际上是不一致的，但是用户不断在他们的代码中使用它们，我们必须能够使用它们。所以，每当我们遇到冲突，我们只是坚持平台类型。 M11中引入的警告保留在这种情况下，因此该代码不会以奇怪的方式打破，但是我们尽力让您了解可能的运行时问题。
请注意，在Java中，任何保留未注释的内容仍然包含平台类型，包括Java 8之前的所有通用类型参数。
## 哪些注释？

Kotlin编译器支持的实际注释集可能是可配置的，但无论如何，我们将支持以下内容：

* 我们一直使用的org.jetbrains.annotation
* android.support.annotation
* javax.annotation（和来自FindBugs的）
* javax.validation.constraints
* lombok
* org.eclipse.jdt.annotation
* org.checkerframework.checker.nullness.qual

## 结论

我们希望在M12之后，Java的空值战斗将会结束。不过请继续关注
