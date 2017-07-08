---
title: Early access program for Kotlin 1.2 has been started
author: Ilya Gorbunov
date: 2017-06-27 21:45:00
source_url: https://blog.jetbrains.com/kotlin/2017/06/early-access-program-for-kotlin-1-2-has-been-started/
tags: 
categories:  官方动态
---

我们很高兴地宣布Kotlin 1.2的早期访问计划的开始：今天是其第一个里程碑版本1.2-M1。
此版本默认使用1.1.x版本以前在实验1.2语言版本设置下可用的新语言功能。在标准库中也可以预览新的API。
更新日志中可以找到完整的，但并不是这么大的更改列表。

{% raw %}
<p><span id="more-5090"></span></p>
{% endraw %}

## 语言特征：注释中的数组文字

在这个里程碑中提出的单一的显着语言特征是数组文字，其用法被限制为注释参数。
之前一个人不得不写下如下的内容来指定数组：

{% raw %}
<p></p>
{% endraw %}

```kotlin
@CacheConfig(cacheNames = arrayOf("books", "default"))
public class BookRepositoryImpl {
    // ....
}
 
```

{% raw %}
<p></p>
{% endraw %}

在Kotlin 1.2中，可以使用一个文字代替arrayOf函数：

{% raw %}
<p></p>
{% endraw %}

```kotlin
@CacheConfig(cacheNames = ["books", "default"])
public class BookRepositoryImpl {
    // ....
}
 
```

{% raw %}
<p></p>
{% endraw %}

IDE检查将建议您在适当的情况下使用收集文字的新语法。
### 具有可选功能参数的内联功能

直到现在，不可能使用可选的功能参数声明一个内联的高阶函数，如下所示：

{% raw %}
<p></p>
{% endraw %}

```kotlin
inline fun <E> List<E>.printItems(transform: (E) -> String = { it.toString() })
 
```

{% raw %}
<p></p>
{% endraw %}

一个人不得不使函数本身非内联或将功能参数标记为noinline。在任何一种情况下，都击败功能参数内联的目的。
现在完全支持这种情况。
## 标准库API

此版本针对标准库API提供了两个KEEP（Kotlin Evolution和增强建议）。
第一个是KEEP-49引入了BigInteger和BigDecimal类型的额外操作和转换扩展，我们对此感谢Daniil Vodopian。
第二个是KEEP-11，它涵盖了与分区集合和序列有关的一些功能：

* chunked（size：Int）扩展功能将集合分成给定大小的块;
* 窗口（大小：Int，step：Int）获取给定大小的窗口，并沿着集合移动，给定步骤返回落入每个窗口的元素的子列表;
* pairwise（）扩展返回集合中的所有后续对。

如果您有兴趣并告诉我们，是否适合您的用例，请尝试这些扩展。
还有一些其他增强功能，例如MutableList的fill（）和shuffle（）扩展以及List的shuffled（），Regex类也可以串行化。
## JavaScript的

在1.1.2版本之前，我们介绍了选择性加入JS类型的阵列支持。启用后，将Kotlin原始数组（如IntArray，DoubleArray等）转换为JavaScript类型的数组。现在，不再需要选择加入，因为默认情况下启用此支持。
## 预发行说明

请注意，向后兼容性保证不涵盖预发行版本：功能和API可能会在后续版本中更改。当我们达到最终RC时，由发行版本生成的所有二进制文件将被编译器取代：您需要重新编译1.2 x编译的所有内容。
  但是，由1.1.x和更早版本编译的所有代码完全没有重新编译。
在这个版本中，如果您创建内联挂起功能，您可以在旧的运行时编译。
## 如何尝试

在Maven / Gradle中：添加http://dl.bintray.com/kotlin/kotlin-eap-1.2作为构建脚本和项目的存储库;使用1.2-M1作为编译器插件和标准库的版本号。
在IntelliJ IDEA：转到工具鈫？Kotlin鈫？配置Kotlin插件更新，然后在更新频道下拉列表中选择“访问预览1.2”，然后按检查更新。
命令行编译器可以从Github发行页面下载。
在try.kotlinlang.org上：使用右下角的下拉列表将编译器版本更改为1.2鈥1。
