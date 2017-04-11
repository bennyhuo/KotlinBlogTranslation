---
title: [译]Kotlin 1.0 Beta 2 is Out!
date: 2015-11-16 21:01:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/11/kotlin-1-0-beta-2-is-out/
---

我们测试版的第一次更新在这里！我们正在稳定，所以它主要是错误修复和标准库的更改。
## 语言变化

我们现在对类型参数执行单实例继承约束：相同的T不能同时具有List <Int>和List <String>作为其上限。对于类始终被禁止，现在对类型参数也是一样的检查。
智能演员不可能的情况下，诊断有所改善：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class C {
    var x: String? = ""
    fun foo(): String {
        if (x != null) return x // ERROR: smart cast to String is impossible,
                                // because 'x' is a member variable
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

此外，编译器现在足够聪明，可以在特定时点值始终为空时提醒我们：

{% raw %}
<p></p>
{% endraw %}

```kotlin
    var x: Foo? = ...
    if (x != null) return
    x?.bar() // WARNING: bar() will never run, because x is always null here
 
```

{% raw %}
<p></p>
{% endraw %}

## 图书馆更改

我们清理标准库的API。这个时间关系范围最明显的变化。我们打算使用常见的用例，例如“if（x in 1..10）”或“for（i in 1..10）”保持不变，但在引擎盖下进行了一些重命名和层次重构：

* 双重和浮动进度被丢弃
* 字节和短进度已被弃用，字节和短路的..运算符现在返回IntRange
* 范围<T>重命名为ClosedRange <T>，其end属性重命名为endInclusive
* Progression <T>不利于具体的进阶实现：IntProgression，LongProngession，CharProgression
* 开始和结束属性被重命名为第一个和最后一个

然后，字符串的实用程序扩展被推广到可能的情况下与CharSequence一起工作。
filterIsInstance扩展现在需要显式指定其类型参数：

{% raw %}
<p></p>
{% endraw %}

```kotlin
foo(list.filterIsInstance()) // error: what is the type the checks are done for?!
foo(list.filterIsInstance<Bar>()) // OK: we are checking for Bar
 
```

{% raw %}
<p></p>
{% endraw %}

注意：为了减小运行时库的大小（这对Android应用程序尤其重要），我们从标准库中删除了kotlin.dom和kotlin.browser包。它们现在可以作为一个单独的库kotlinx.dom。如果您在项目中使用任何这些软件包，请添加新的库作为依赖关系，并更新代码中的import语句（将kotlin.dom和kotlin.browser更改为kotlinx.dom和kotlinx.browser）。否则，库的API没有改变。
其他变化：

* 添加

MutableLists和Arrays的就地倒置和排序
naturalOrder和reverseOrder比较器
mapNotNull，mapIndexedNotNull，filterIndexed
String.toByte（）
* MutableLists和Arrays的就地倒置和排序
* naturalOrder和reverseOrder比较器
* mapNotNull，mapIndexedNotNull，filterIndexed
* String.toByte（）
* 已弃用（运行代码清理来迁移代码）

功能。发电机
toLinkedList
* 功能。发电机
* toLinkedList
* 掉下来

加入，合并
代表l y
FileTreeWalk.filter，File.recurse，BufferedReader.lines和lineIterator
断言，检查和要求与非懒惰的消息参数
* 加入，合并
* 代表l y
* FileTreeWalk.filter，File.recurse，BufferedReader.lines和lineIterator
* 断言，检查和要求与非懒惰的消息参数

## Dokka

Kotlin项目的新文档生成工具Dokka终于达成了全面的发布。 Dokka支持混合语言项目，并了解Kotlin代码中的KDoc注释和Java代码中的JavaDoc注释。 Dokka具有Gradle，Maven和Ant的插件，因此您可以轻松地将其与项目的构建系统集成。下载Dokka并在Dokka项目网站上找到更多信息。
## IDE更改


* 完成现在适用于Java静态成员和对象成员。只需按Ctrl + Space第二次：

