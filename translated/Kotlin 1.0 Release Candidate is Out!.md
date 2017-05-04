---
title: "[译]Kotlin 1.0 Release Candidate is Out!"
date: 2016-02-04 18:39:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2016/02/kotlin-1-0-release-candidate-is-out/
translator:
translator_url:
---

最后，Kotlin已经毕业了Beta，我们很高兴地介绍了Release Candidate Build！
**注意**：就像我们一样 [早些时候宣布](http://blog.jetbrains.com/kotlin/2015/12/kotlin-1-0-beta-4-is-out/) ，**RC需要重新编译所有代码**，以确保没有使用旧版本编译的代码（即使您使用的是EAP版本，请重新编译）。
这篇博客文章概述了自Beta 4以来所做的更改。库更改是此版本中最大的。另外，一些错误已经修复。完整的更改列表可用 [这里](https://github.com/JetBrains/kotlin/releases/tag/build-1.0.0-rc-1036) 。

{% raw %}
<p><img alt="Kotlin 1.0 RC" class="alignnone size-full wp-image-3485" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2016/02/RC-Banner.png?resize=640%2C330&amp;ssl=1"/></p>
{% endraw %}

<em>请参阅有关<a href="https://news.ycombinator.com/item?id=11034273">黑客新闻</a>和<a href =“https://www.reddit.com的讨论/ r / programming / comments / 445jih / jvm_languages_news_kotlin_10_release_candidate_is /“> Reddit </a> </em>。

{% raw %}
<p><span id="more-3453"></span></p>
{% endraw %}

## 语言

首先，像以前承诺的那样，已经有一个清理：

* 所有先前已弃用的语言结构现在都是错误，而不是警告。
* 以前在字节码中生成的所有不推荐的声明（如接口等中的静态字段）已被删除。

大多数其他语言的变化是微小的调整和错误修复。下面给出了一些亮点。查看完整列表 [这里](https://github.com/JetBrains/kotlin/releases/tag/build-1.0.0-rc-1036) 。
### 委托字段的注释

现在支持新的`@delegate：`注释目标（use-site）。例如，要将委托对象标记为`@Transient`，我们可以说：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Example {
    @delegate:Transient
    val foo by Lazy { ... }
}
```

{% raw %}
<p></p>
{% endraw %}

在字节码中，保留代表的字段将被注释。
### 键入检查使用地点差异

我们修复了一些与使用场所差异（类型预测）相关的烦人的错误。因此，编译器可能会在您的代码中找到一些以前错过的错误

例如，在以下情况下：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val ints = mutableListOf(1, 2, 3)
val strs = mutableListOf("abc", "def")
val comps: MutableList<out Comparable<*>> = ints
comps.addAll(strs) // ?! Adding strings to a list of ints
```

{% raw %}
<p></p>
{% endraw %}

此代码被错误地接受，并在最后一行拒绝了消息：

{% raw %}
<p></p>
{% endraw %}

```kotlin
Projected type MutableList<out Comparable<*>> restricts the use of addAll()
```

{% raw %}
<p></p>
{% endraw %}

## Java互操作性

从Java的get / set对派生的合成属性的一些改进：

* 这样的声明（以及SAM转换的方法）现在与成员一样解决;
* 为返回值的Java设置器添加了支持。

支持从各种流行的库（例如`javax.annotations`，Android SDK等）中的`@ Nullable / @ NotNull`注释添加。

EAP用户报告：
<p>

  被认可的Android注释以很好的方式打破了我的很多代码

</p>
并突出显示错误修复：

* 私有的顶级Kotlin类现在被编译为package-private Java类
* 私人类的成员不能从非私有内联函数访问

## 标准库


* 库代码重新排列成更细粒度的包（不需要更改源）
* 一些功能已经内联了
* 许多内联函数（大多数是一行内容）不能再从Java代码调用。这将有助于我们在将来减少运行时库的大小。
* 所有旧的弃用已被删除
* Map.getOrElse（）和Map.getOrPut（）现在将与空值相关联的键视为缺失。
* mutableListOf，mutableSetOf，mutableMapOf添加到构建可变集合。
* toMutableList而不是toArrayList。后者已被弃用
* 添加关联和关联以帮助构建地图（而不是toMap / toMapBy）
* 比较器和比较相关功能被移动到kotlin.comparisons包（默认情况下不导入）

更多变化 [这里](https://github.com/JetBrains/kotlin/releases/tag/build-1.0.0-rc-1036) ## 


模具

要以更为惯用的方式在Gradle中启用Android Extensions，我们现在说：

{% raw %}
<p></p>
{% endraw %}

```kotlin
apply plugin: 'kotlin-android-extensions'
```

{% raw %}
<p></p>
{% endraw %}

在`build.gradle`文件（每个项目单独）。
旧的方式不再工作，并打印修复说明到输出。
## IDE更改


* 意图使用解构声明使用循环替换地图条目的迭代
* 检查和quickfix清理冗余可见性修饰符
* 检查替换'assert'调用检查变量不为空！或？：错误（...）
* 如果没有为相应模块配置Kotlin运行时，则在IDE中打开.kt文件时显示“Kotlin未配置”通知
* Action来生成toString（）方法
* 支持通过主构造函数实现成员参数
* 参数信息弹出窗口用于显示类型参数
* 完成根据当前文件中的未解析标识符提供名称变体
* Quickfix用于在表达式中添加缺少的分支
* 支持将嵌套类移动到上级或另一顶级类
* @Suppress现在可以用于IDE检查

## 安装说明

对于IntelliJ IDEA的用户，自动更新可能无法在IDE中运行，因此您需要下载插件并从zip文件安装：

* 在这里下载
* 转到首选项|插件并点击从磁盘安装插件...

抱歉给你带来不便。
## 敬请关注

最后一个版本即将到来，同时有一个很棒的Kotlin！ <img alt =“:)”class =“wp-smiley”data-recalc-dims =“1”src =“https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images /smilies/simple-smile.png?w=640&amp;ssl=1“style =”height：1em; max-height：1em;“/>
</p>请参阅<a href="https://news.ycombinator.com/item?id=11034273">黑客新闻</a>和<a href =“https://www.reddit.com/r/编程/评论/ 445jih / jvm_languages_news_kotlin_10_release_candidate_is /“> Reddit </a> </em>。
