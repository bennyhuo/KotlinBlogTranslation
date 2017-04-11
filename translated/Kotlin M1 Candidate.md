---
title: [译]Kotlin M1 Candidate
date: 2012-03-30 14:57:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2012/03/kotlin-m1-candidate/
---

IntelliJ IDEA 11.1最近发布，我们很高兴地宣布Kotlin IDE插件的里程碑式候选版本。这篇文章概述了上个月发生了什么。
## 里程碑候选人构建准备好您的评估

要在IntelliJ IDEA 11.1上安装（免费社区版本），请按照“入门指南”中的说明进行操作。简而言之：

* 使用此插件库：http://www.jetbrains.com/kotlin/eap-plugin-repository/updatePlugins.xml
* 或从这里下载压缩插件。

您可以随时从我们的构建服务器下载每晚的Kotlin版本，或者从源代码自行构建。
现在我们简要介绍一下新的和值得注意的内容。有关以前实现的功能，请参阅此博文。
## 小事情很重要

首先，我们做了很多bug修复，改进和其他重要的事情，很难演示。查看github中的提交历史记录以及YouTrack中的封闭问题。
## 图书馆

随着扩展功能的强大，Kotlin使现有的Java API更好。特别是，我们为JDK集合提供增强功能，以便您可以这样说：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun main(args : Array<String>) {
    val list = arrayList(1, 2, 3)
    val odds = list.filter {it % 2 == 1}
    println(odds.join(", "))
}
```

{% raw %}
<p></p>
{% endraw %}

这里，filter（）和join（）是扩展函数。
实现方面，扩展函数只是静态实用程序函数，如“好老旧”Java的Collecions *，但是使用“receiver.function（）”调用语法，IDE使它们变得更好：有代码完成可以帮助您浏览通过API学习它（就像扩展是正常的类成员一样）：

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Extensions.png"><img alt="" class="alignnone size-medium wp-image-483" data-recalc-dims="1" sizes="(max-width: 259px) 100vw, 259px" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Extensions.png?resize=259%2C300&amp;ssl=1" srcset="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Extensions.png?resize=259%2C300&amp;ssl=1 259w, https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Extensions.png?w=663&amp;ssl=1 663w"/></a></p>
{% endraw %}

您可以导航到库函数的源：

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Navigation-2.png"><img alt="" class="alignnone size-full wp-image-485" data-recalc-dims="1" sizes="(max-width: 501px) 100vw, 501px" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Navigation-2.png?resize=501%2C144&amp;ssl=1" srcset="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Navigation-2.png?resize=300%2C86&amp;ssl=1 300w, https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Navigation-2.png?w=501&amp;ssl=1 501w"/></a></p>
{% endraw %}

看到那里的文档评论：

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/03/println.png"><img alt="" class="alignnone size-full wp-image-486" data-recalc-dims="1" sizes="(max-width: 476px) 100vw, 476px" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/03/println.png?resize=476%2C297&amp;ssl=1" srcset="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/03/println.png?resize=300%2C187&amp;ssl=1 300w, https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/03/println.png?w=476&amp;ssl=1 476w"/></a></p>
{% endraw %}

图书馆文档的HTML版本在这里可用。
## GitHub支持

Kotlin突出显示现在由github支持，包括要点。
## 注释

Kotlin现在支持注释。这是一个依赖于JUnit 4的小例子：

{% raw %}
<p></p>
{% endraw %}

```kotlin
import org.junit.Test as test
import org.junit.Assert.*
 
class Tests {
    test fun simple() {
        assertEquals(42, getTheAnswer())
    }
}
```

{% raw %}
<p></p>
{% endraw %}

在这里阅读更多
## 字符串模板

现在可以使用多行字符串模板，例如：

{% raw %}
<p></p>
{% endraw %}

```kotlin
println("""
  First name: $first
  Last name: $last
  Age: $age
""")
```

{% raw %}
<p></p>
{% endraw %}

## 简单枚举

现在支持简单的枚举类案例。例如：

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Color {
  RED
  GREEN
  BLUE
}
```

{% raw %}
<p></p>
{% endraw %}

## 本地功能

函数可以在其他函数中声明：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun count() : Int {
  fun count(parent : Entity) : Int {
    return 1 + parent.children.sum { count(it) }
  }
  return count(this.root)
}
```

{% raw %}
<p></p>
{% endraw %}

## 可空性

Kotlin现在可以识别@Nullable和@NotNull注释）。如果Java代码说：

{% raw %}
<p></p>
{% endraw %}

```kotlin
@NotNull String foo() {...}
```

{% raw %}
<p></p>
{% endraw %}

Kotlin将trat foo（）返回一个不可为空的String。
添加一个用于将可空值转换为不可空值的短操作符（!!）：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val foo = getSomethingThatMayBeNull()
foo!!.bar() // throw NPE if foo is null, run bar() otherwise
```

{% raw %}
<p></p>
{% endraw %}

## 字节代码公布

点击IDEA窗口右边的Kotlin按钮，然后选择“Bytecode”选项卡。您将看到Kotlin为您的程序生成的字节码！

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Bytecode-1.png"><img alt="" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Bytecode-1.png?resize=640%2C312&amp;ssl=1"/></a></p>
{% endraw %}

## 您的反馈非常受欢迎。有一个漂亮的Kotlin！

