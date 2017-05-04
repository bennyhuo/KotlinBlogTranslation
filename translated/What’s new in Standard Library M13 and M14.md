---
title: "[译]What’s new in Standard Library M13 and M14"
date: 2015-09-28 16:56:00
author: ilya.gorbunov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/09/whats-new-in-standard-library-m13-and-m14/
translator:
translator_url:
---

标准图书馆继续发展：

* Lazy <T>类型已经被引入
* 在Map中存储属性的更简洁的语法
* Char算术的最终变化
* 集合上的加减操作现在取决于其类型
* 新作用域功能：应用和运行
* 右开口范围
* 修剪多行字符串中的缩进
* 和更多


{% raw %}
<p><span id="more-2759"></span></p>
{% endraw %}

# M13的新功能

## 懒

懒惰评估是一种有用的模式，将其仅限于委托的属性是不公平的。现在，在<code> kotlin </code>包中有<code> Lazy＆lt; T＆gt; </code>类型，您可以在许多上下文中使用它。您可以将属性委派给<code> Lazy </code>的实例，该实例具有<code> get </code>扩展功能以满足委派惯例：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Poll(val json: Map<String, *>) {
    val messages: List<Message> by lazy {
        // some expensive and not always needed computation
        val field = json.get("messages")
        (field as JSONArray).toList().map {
            Message((it as JSONObject).toMap())
        }
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

与<code> Delegates.lazy </code>不同，默认情况下，<code> lazy </code>的语义为<strong> synchronized </strong>。
## 将属性委派给地图

另一个常见的用例是将属性的值存储在地图中，其中属性的名称用作键。对于这种情况，我们在地图上提供扩展函数<code> get </code>和<code> set </code>以满足委派约定，允许将属性委托给地图，而不创建包装器委托对象：

{% raw %}
<p></p>
{% endraw %}

```kotlin
import kotlin.properties.*
 
class Poll(val json: Map<String, *>) {
    val timestamp: Long by json
    val utc_timestamp: Long by json
    val error: String by json
}
 
```

{% raw %}
<p></p>
{% endraw %}

## 可观察和否定性质

我们已经修复了可观察的代理的麻烦：传递给observable属性的回调处理程序在属性值更改之前被调用。现在它被调用了。值得注意的是，这些代表现在已经回调了回调，因此可观察和否决代表的使用现在可以减少一个对象分配。
了解更多有关标准代理的信息 [参考](http://kotlinlang.org/docs/reference/delegated-properties.html#standard-delegates) 。
## 完成Char算术的更改

在M13中，我们正在确定<code> Char </code>类型的算术运算的语义变化。仅剩下<code> Char </code>的三个算术运算：

* Char  -  Int→Char
* Char + Int→Char
* Char  -  Char→Int

涉及<code> Char </code>的所有其他二进制操作在M12中已被弃用，现在已被删除。
## 加和减运算符集合

集合上的<code> plus </code>操作不是新的，但是它被定义为使其返回类型和行为不直观：例如，当向元素添加元素时，您将收到具有该元素连接的列表对于集合的所有元素，可能导致该元素被重复
现在返回的加号类型取决于<em>第一个</em>操作数的类型：

* 对于Iterable，Collection和List，结果是List，操作是一个级联
* 对于Array，结果是Array，并且操作是连接
* 对于设置结果为Set，并且操作将元素包含到生成的集合中
* 对于Map，结果是Map，并且操作将键值对包含在生成的映射中
* 对于Sequence，结果是Sequence，操作是惰性连接

我们也引入了<code>减去</code>操作。它的第一个操作数的类型与其返回类型之间具有相同的关系以及以下语义：

* 集合 -  single_element返回集合，删除该元素的一次出现
* Collection  -  collection_of_elements返回集合，而不包含另一集合中的所有元素。

## 新作用域功能：应用和运行

在M13之前，标准库中有两个所谓的<scope>函数</em>：<code> let </code>和<code>与</code>。我们称之为范围函数，因为它们的唯一目的是修改作为最后一个参数传递的函数的作用域。例如，在<code>与</code>的情况下，将scope函数的参数带到函数参数的接收方，反之亦然，在<code> let </code>的情况下。
现在，您还可以使用另外两个示波器功能：

* 一个将其接收器传递给其功能参数的接收器：
T.run（f：T.（）→R）：R
我们称之为运行，因为它是没有接收器运行的泛化。
* 一个将给定的单位返回功能应用于接收器并返回接收器本身：
T.apply（f：T.（）→Unit）：T

## 构建开放范围

有一个共同的要求，在Kotlin推出正确的范围。我们检查了用例，发现它们大多数都涉及整数范围。在整数的情况下，在结束范围内打开可以用闭合范围表示，其结束值比相应的开放范围的结束小一个。
要创建这样的范围，您可以使用新引入 [直到](http://kotlinlang.org/api/latest/jvm/stdlib/kotlin/until.html) 功能。它返回闭合范围，其值直到指定的结尾，但不包括它，因此：
<code> 0 until 20 == 0..19 </code>
## 找到vs firstOrNull

有一些关于命名一个函数的争论，这个函数找到了一个集合中匹配给定谓词的第一个元素。 <code> find </code>很容易探索，但是<code> firstOrNull </code>与LINQ和Reactive Extensions中如何调用此操作是一致的。在M13 <code> find </code>之前，已经弃用了<code> firstOrNull </code>，但是现在我们已经决定“不废弃”它，并作为<code> firstOrNull </code>的同义词。另外我们提供了<code> findLast </code>，这是<code> lastOrNull </code>的同义词。
## 从多行字符串文字中删除缩进

多行字符串文字的着名疼痛是格式化：您不能格式化包含这些文字的代码，而不会将空格引入文字本身。

{% raw %}
<p></p>
{% endraw %}

```kotlin
    val multiline = """First line
Second line
Third line"""
 
```

{% raw %}
<p></p>
{% endraw %}

现在我们提供了几个函数来从字符串的每一行去除公共空格前缀：<br/>
trimIndent， [trimMargin](http://kotlinlang.org/api/latest/jvm/stdlib/kotlin/trim-margin.html) ， [replaceIndent](http://kotlinlang.org/api/latest/jvm/stdlib/kotlin/replace-indent.html) ， [replaceIndentByMargin](http://kotlinlang.org/api/latest/jvm/stdlib/kotlin/replace-indent-by-margin.html) {% raw %}
<p></p>
{% endraw %}

```kotlin
    // first and last blank lines are removed,
    // and common indentation from other lines is stripped
    val multiline = """
      First line
      Second line
      Third line
    """.trimIndent()
 
```

{% raw %}
<p></p>
{% endraw %}

## 


丢弃已弃用的API

在M13中，我们删除了一些以前不推荐使用的API：流，迭代器的扩展方法，<code> FunctionalList </code>，<code> FunctionalQueue </code>和<code> StringTemplate </code>。
完整的更改列表可用 [这里](https://quip.com/I4BbAdzPTzCx) 。
# M14计划

## 在包装零件之间分配顶层功能

正如我们宣布的那样 [早些时候](http://blog.jetbrains.com/kotlin/2015/06/improving-java-interop-top-level-functions-and-properties/) 我们正在改变顶层函数和属性如何映射到编译代码中的类文件。在下一个里程碑中，标准库中的所有顶级内容将分布在相应的包装部件之间。我们将保留包含所有顶级函数的<code> KotlinPackage </code> facade类，但将来它将被废弃和删除。
请注意，这些更改仅影响Java代码中顶级Kotlin成员的使用。将提供IDE中的检查来迁移这些用法。
## 接下来会下降什么

我们还在清理标准库中不推荐使用的API，下面是我们下一个里程碑的内容：

* 大小，空和notEmpty扩展属性;
* 扩展makeString和appendString;
* 从提供的元素构造数组和集合的方法：array，intArray，arrayList，hashMap等

## kotlin-swing和kotlin-jdbc状态

有两个实验库：kotlin-swing和kotlin-jdbc。我们不会将它们运送到Maven Central存储库。发布到Maven的最新版本将针对M14进行编译。
如果您依赖这些库，可以自由地分叉源代码并在本地编译。我们从Kotlin代码库将它们从Kotlin项目组织下的GitHub中分离出来，

* github.com/kotlin-projects/kotlin-jdbc
* github.com/kotlin-projects/kotlin-swing

