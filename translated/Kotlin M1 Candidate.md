---
title: "[译]Kotlin M1 Candidate"
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

要安装在IntelliJ IDEA 11.1（免费社区版本可用 [这里](http://www.jetbrains.com/idea/) ），请按照说明进行操作 [入门](http://confluence.jetbrains.net/display/Kotlin/Getting+Started) 指南。简而言之：

* 使用此插件库：http://www.jetbrains.com/kotlin/eap-plugin-repository/updatePlugins.xml
* 或从这里下载压缩插件。

您可以随时从我们的夜晚下载Kotlin的每夜建筑物 [构建服务器](http://teamcity.jetbrains.com/viewLog.html?buildId=lastSuccessful&tab=artifacts&buildTypeId=bt345) 或自己建立 [来源](https://github.com/jetbrains/kotlin) 。
现在我们简要介绍一下新的和值得注意的内容。请参阅 [这个博文](http://blog.jetbrains.com/kotlin/2012/01/the-road-ahead/) 对于以前实现的功能。<span id =“more-440”> </ span>
## 小事情很重要

首先，我们做了很多bug修复，改进和其他重要的事情，很难演示。查看提交历史记录 [github](https://github.com/JetBrains/kotlin/commits/) 和封闭的问题 [YouTrack](http://youtrack.jetbrains.com/issues/KT?q=resolved+date%3A+2012-02-14+..+2012-03-31) 。
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
实现方面，扩展函数只是静态实用程序函数，如“好老旧”Java的Collecions *，但是使用“receiver.function（）”调用语法，IDE使它们更好：有<strong>代码完成< / strong>可以帮助您浏览API并学习（就像扩展名是正常的类成员一样）：

{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Extensions.png"><img alt="" class="alignnone size-medium wp-image-483" data-recalc-dims="1" sizes="(max-width: 259px) 100vw, 259px" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Extensions.png?resize=259%2C300&amp;ssl=1" srcset="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Extensions.png?resize=259%2C300&amp;ssl=1 259w, https://i1.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Extensions.png?w=663&amp;ssl=1 663w"/></a></p>
{% endraw %}

您可以导航到库函数的源：

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Navigation-2.png"><img alt="" class="alignnone size-full wp-image-485" data-recalc-dims="1" sizes="(max-width: 501px) 100vw, 501px" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Navigation-2.png?resize=501%2C144&amp;ssl=1" srcset="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Navigation-2.png?resize=300%2C86&amp;ssl=1 300w, https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/03/Navigation-2.png?w=501&amp;ssl=1 501w"/></a></p>
{% endraw %}

并在那里查看<strong> doc评论</ strong>：

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/03/println.png"><img alt="" class="alignnone size-full wp-image-486" data-recalc-dims="1" sizes="(max-width: 476px) 100vw, 476px" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/03/println.png?resize=476%2C297&amp;ssl=1" srcset="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/03/println.png?resize=300%2C187&amp;ssl=1 300w, https://i0.wp.com/blog.jetbrains.com/kotlin/files/2012/03/println.png?w=476&amp;ssl=1 476w"/></a></p>
{% endraw %}

图书馆文档的HTML版本可用 [这里](http://jetbrains.github.com/kotlin/versions/snapshot/apidocs/index.html) 。
## GitHub支持

Kotlin突出显示现在得到支持 [github](https://github.com/JetBrains/kotlin/blob/master/libraries/stdlib/test/CollectionTest.kt) ， 包含 [要旨](https://gist.github.com/2234718) 。
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

阅读更多 [这里](http://confluence.jetbrains.net/display/Kotlin/Annotations) 。
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

简单的例子 [枚举类](http://confluence.jetbrains.net/display/Kotlin/Enum+classes) 现在得到支持。例如：

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

Kotlin现在认识到了 [@Nullable和@NotNull注释](http://www.jetbrains.com/idea/documentation/howto.html) ）。如果Java代码说：

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
短手操作（ [!!](http://confluence.jetbrains.net/display/Kotlin/Null-safety#Null-safety-sure) ）将可空值转换为不可空的值：

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

