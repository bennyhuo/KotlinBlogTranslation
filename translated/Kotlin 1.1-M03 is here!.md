---
title: "[译]Kotlin 1.1-M03 is here!"
date: 2016-11-24 12:50:00
author: Ilya Chernikov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2016/11/kotlin-1-1-m03-is-here/
---

我们很高兴地宣布即将到来的Kotlin1.1的第三个里程碑。此版本带来了新的语言功能，以及JavaScript后端，编译器和IDEA插件中的改进和修复。新版本还包括Kotlin 1.0.5中引入的所有工具功能，并与IntelliJ IDEA 2016.3 EAP和Android Studio 2.2和2.3兼容。
与其他里程碑版本一样，我们为新语言和库功能提供<b>无后向兼容性保证</b>。在1.1版本的里程碑版本中引入的任何内容都将在最终1.1版本之前更改</b>。
请分享您关于新功能或您可能遇到的任何问题的反馈，通过此版本 [YouTrack](https://youtrack.jetbrains.com/issues/KT) ， [论坛](https://discuss.kotlinlang.org) 和 [松弛](http://kotlinlang.slack.com/) 。
1.1-M03的完整更新日期可用 [这里](https://github.com/JetBrains/kotlin/blob/1.1-M03/ChangeLog.md) 。

{% raw %}
<p><span id="more-4380"></span></p>
{% endraw %}

## 未使用符号的下划线

现在可以使用下划线而不是lambda的未使用参数的名称：

{% raw %}
<p></p>
{% endraw %}

```kotlin
foo { _, x -> ... }
```

{% raw %}
<p></p>
{% endraw %}

解构声明中的一个未使用的变量名称现在也可以用下划线替代。

{% raw %}
<p></p>
{% endraw %}

```kotlin
val (x, _, z) = expr
```

{% raw %}
<p></p>
{% endraw %}

这两种情况在适当的情况下进行了详细描述 [保持](https://github.com/Kotlin/KEEP/blob/master/proposals/underscore-for-unused-parameters.md) 。
## 数字文字中的下划线

根据Java 8规范，Kotlin现在支持在数字之间使用单个下划线符号的数字文字。例如：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val ONE_MILLION = 1_000_000
```

{% raw %}
<p></p>
{% endraw %}

见 [保持](https://github.com/Kotlin/KEEP/blob/master/proposals/underscores-in-numeric-literals.md) 更多的细节和例子。
## 通用枚举值访问

的支持 [提案](https://github.com/Kotlin/KEEP/blob/master/proposals/generic-values-and-valueof-for-enums.md) 以两种内在功能的形式登陆标准图书馆：

{% raw %}
<p></p>
{% endraw %}

```kotlin
inline fun <reified T : Enum<T>> enumValues(): Array<T>
inline fun <reified T : Enum<T>> enumValueOf(name: String): T
```

{% raw %}
<p></p>
{% endraw %}

它们允许枚举通用枚举类型的值。例如。

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class RGB { RED, GREEN, BLUE }
 
print(enumValues<RGB>().joinToString { it.name }) // prints RED, GREEN, BLUE
```

{% raw %}
<p></p>
{% endraw %}

## 对于类似建筑物的DSL的范围控制

如详细描述的 [保持](https://github.com/Kotlin/KEEP/blob/master/proposals/scope-control-for-implicit-receivers.md) DSL作者在为构建器类构造表达范围限制方面存在问题。例如，对于一些html-builder DSL：

{% raw %}
<p></p>
{% endraw %}

```kotlin
table {
  tr {
    tr {} // PROBLEM: Table.tr() is valid here
  }
}
```

{% raw %}
<p></p>
{% endraw %}

为了解决这个问题，我们添加了<code> @DslMarker </code>注释，允许在这些情况下更准确地控制可见性范围。有关使用示例请参阅 [使用此功能的kotlinx.html库的预览版本](https://github.com/Kotlin/kotlinx.html/tree/dsl-markers) （看到 [HtmlTagMarker](https://github.com/Kotlin/kotlinx.html/blob/dsl-markers/shared/src/main/kotlin/api.kt#L103) 和 [HTMLTag](https://github.com/Kotlin/kotlinx.html/blob/dsl-markers/shared/src/main/kotlin/htmltag.kt#L5) 实现和 [DSL-标记](https://github.com/Kotlin/kotlinx.html/blob/dsl-markers/DSL-markers.md) 预览库使用信息）。
## 标准库统一

不同平台的标准库统一过程正在向前发展。我们已经开始统一1.1-M2中的异常类型，现在在所有平台上都支持一些更常见的类型，可以在<code> kotlin。* </code>包中使用，默认情况下导入。这些包括：

* ArrayList，HashSet，LinkedHashSet，HashMap，LinkedTashMap在kotlin.collections中
* 在kotlin.text中附加和StringBuilder
* 比较器在kotlin.com对比

在JVM上，这些只是来自<code> java.util </code>和<code> java.lang </code>的旧旧类型的typealiases
## JavaScript后端中支持新语言功能

JavaScript后端现在支持与JVM后端兼容的以下Kotlin语言功能：

* 协调程序
* lambda参数中的解析
* 解构声明中未使用的变量名

## JS代码生成改进

JavaScript后端现在可以生成更多的静态可检查代码，这对JS代码处理工具（比如minifier，optimizers，linters等）来说更为友善。
## 如何尝试

<b>在Maven / Gradle中：</b>添加 [http://dl.bintray.com/kotlin/kotlin-eap-1.1](http://dl.bintray.com/kotlin/kotlin-eap-1.1) 作为构建脚本和项目的存储库;使用1.1-M03作为编译器和标准库的版本号。
<b>在IntelliJ IDEA中：</b>转到<i>工具→Kotlin→配置Kotlin插件更新</i>，然后在<i>更新频道</i>下拉列表中选择“早期访问预览1.1”下拉列表，然后按<i>检查更新</i>。
开车去Kotlin！
