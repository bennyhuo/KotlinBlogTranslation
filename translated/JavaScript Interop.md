---
title: "[译]JavaScript Interop"
date: 2014-12-24 09:57:00
author: Hadi Hariri
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2014/12/javascript-interop/
translator:
translator_url:
---

当使用 JavaScript，即创建一个可编译为 JavaScript 的 Kotlin 应用程序时，我们经常需要与 JavaScript 中的现有库进行互操作。虽然 Kotlin 已经为此提供了支持，但我们在 M10 中添加了更多的选项，使互操作性更加容易
<span id =“more-1766”> </span>
## 动态支持

在 M10 中，我们添加了**动态**关键字**[1]**，这样我们可以将类型声明为动态的，允许某些互操作性以前可能更麻烦。例如，当使用 jQuery，直到 M10，我们唯一的选择是使用 Kotlin 提供的强类库。至于 M10，我们现在也可以使用动态关键字

{% raw %}
<p></p>
{% endraw %}

```kotlin
jquery.getJSON(KotlinCommitsURL) { commits ->
  val commitsTable = jquery("#kotlin-commits")
  commits.forEach { commit ->
     commitsTable.append("""
                    <tr>
                        <td><a href=${commit.html_url}>${commit.sha.substring(0, 6)}</a></td>
                        <td>${commit.commit.message}</td>
                    </tr>""")
  }
}
```

{% raw %}
<p></p>
{% endraw %}

上述代码调用*jQuery*上的*getJSON*函数返回 GitHub 提交的列表。该函数使用带有单个参数的 lambda，即实际的提交。此列表中的每个条目依次是提交条目，其中包含自己的字段，例如*html_url*或*commit.message*。
在代码*jQuery 中，提交*和*提交*都是动态的，这意味着我们调用这些的任何东西都将在运行时被解析，即 JavaScript 解释器。这允许两件事情：

* 不必使用强类型的库来处理 jQuery
* 能够消耗以前未定义的模型

第二个功能是非常有用的，因为这意味着我们不必创建中间强类型的类来消耗 HTTP 端点。
当然，我们甚至可以使用诸如**循环的语言结构来做同样的事情，不仅使用*forEach*扩展功能。

{% raw %}
<p></p>
{% endraw %}

```kotlin
jquery.getJSON(KotlinCommitsURL) { commits ->
  val commitsTable = jquery("#kotlin-commits")
  for(commit in commits) {
    commitsTable.append("""
                    <tr>
                        <td><a href=${commit.html_url}>${commit.sha.substring(0, 6)}</a></td>
                        <td>${commit.commit.message}</td>
                    </tr>""")
   }
}
```

{% raw %}
<p></p>
{% endraw %}

为了使此代码工作，我们仍然需要将 jQuery*声明为动态的，并将其与 Kotlin 的相应本机等价物进行标记

{% raw %}
<p></p>
{% endraw %}

```kotlin
native("$")
val jquery : dynamic = noImpl
```

{% raw %}
<p></p>
{% endraw %}

需要*noImpl*，因为 Kotlin 中的不可为空的变量需要初始化，在这种情况下会引发异常，但是这并不会发生，因为它被有效地编译成 JavaScript 并在客户机上调用 - 侧。已经存在于 M10 之前的*本机*注释告诉 Kotlin JavaScript 中的标识符相当于什么。
### 经营者

当声明动态类型时，某些操作符在 JavaScript 中本地运行，例如索引访问器：

{% raw %}
<p></p>
{% endraw %}

```kotlin
elements: dynamic
// in Kotlin
elements[1]
```

{% raw %}
<p></p>
{% endraw %}

将编译为：

{% raw %}
<p></p>
{% endraw %}

```kotlin
elements[i]
```

{% raw %}
<p></p>
{% endraw %}

在 JavaScript 中。
## 内联 JavaScript 代码

在 M10 中添加的另一个功能是可以在 Kotlin 代码中嵌入一些本机 JavaScript 代码。我们可以使用*js*函数：

{% raw %}
<p></p>
{% endraw %}

```kotlin
       jquery.getJSON(KotlinCommitsURL) { commits ->
          js("console.log('Calling JavaScript')")  
          val commitsTable = jquery("#kotlin-commits")
```

{% raw %}
<p></p>
{% endraw %}

第二行在由编译产生的输出中插入</u> console.log（'Calling JavaScript'）*，将 JavaScript 与 Kotlin 代码相结合。
## 语言注入

M10 还在 IntelliJ IDEA for Kotlin 中添加了语言注入支持。虽然这适用于任何字符串和任何语言，而不仅仅是 JavaScript，但是当使用*js*时，它肯定是有用的，允许这样做：

{% raw %}
<p><img alt="js-string" class="aligncenter size-full wp-image-1776" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2014/12/js-string.png?resize=363%2C44&amp;ssl=1"/></p>
{% endraw %}

看起来像这样：

{% raw %}
<p><img alt="js-injected" class="aligncenter size-full wp-image-1775" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2014/12/js-injected.png?resize=379%2C48&amp;ssl=1"/></p>
{% endraw %}

注入 JavaScript 语言时：

{% raw %}
<p><img alt="inject-js" class="aligncenter size-full wp-image-1774" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2014/12/inject-js.png?resize=465%2C102&amp;ssl=1"/></p>
{% endraw %}

## 概要

除了*动态*和*js*之外，我们还引入了对 JavaScript 的 nativeGetter，nativeSetter*和*nativeInvoke*注释的支持，我们已经覆盖了 [M10 发布帖子](http://blog.jetbrains.com/kotlin/2014/12/m10-is-out/) 。
这些新功能都提供了与 JavaScript 的更好的互操作性，但是他们并没有争取继续为 JavaScript 中的现有库和框架提供强类型的支持。
**[1]** <br/>
“动态”是一个软关键字：

* 如果它发生在非类型上下文中，则它是一个标识符
* 在类型上下文中，当后面跟着一个点（除了将接收器类型与函数/属性名称分开的点除外）或一个尖括号<，它是一个标识符
* 在左侧的::在一个可调参考中：dynamic :: foo 意味着动态有一个正常的标识符

