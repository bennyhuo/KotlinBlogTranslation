---
title: "[译]The Great Syntactic Shift"
date: 2012-01-04 09:38:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2012/01/the-great-syntactic-shift/
translator:
translator_url:
---

随着 Kotlin 的第一次公开预览即将到来（将于 2012 年 1 月 10 日公布，这是**不到一周**从现在开始！），我们正在把一些事情按顺序排列
特别是，我们回顾了语言中提供的语法形式，并决定改变一些。这些更改与旧的语法不兼容，我们已经迁移了所有的测试数据，并将更新 [公开的文件](http://jetbrains.com/kotlin) 不久。
我想指出，这不是这种最后一个变化。Kotlin 还没有发布，直到我们不断收集反馈意见，有时候会发现有些事情需要改变。因此，在 1.0 之前没有向后兼容性保证。我们意识到向后兼容性是多么的重要，但是我们最好能够根据真实人群的需求创建一个非常好的设计。
以下是我们所做的更改的概述
<span id =“more-291”> </span> <br/>
**命名空间已经死了。长期使用套餐。**
*命名空间*的概念演变成如此接近 Java 包的东西，我们决定重命名它。 **名称空间**关键字替换为**包**关键字。另外，不再支持*命名空间块*。
**箭头失去重量**
在**表达式中，功能文字中使用了一个箭头，**使用箭头。某些语言使用“胖箭头”（=>），有些则使用“薄箭头”（ - >）。最初，我们使用了胖子，但是与比较有一些不幸的相互作用，像这样：

{% raw %}
<p></p>
{% endraw %}

```kotlin
  val higherThanY  = {x => y <= x}
```

{% raw %}
<p></p>
{% endraw %}

所以我们决定切换到一个很薄的箭头：

{% raw %}
<p></p>
{% endraw %}

```kotlin
  val higherThanY  = {x -> y <= x}
```

{% raw %}
<p></p>
{% endraw %}

**更易读的功能类型**
在旧的语法中，我们编写了如下的函数类型：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val f : fun(Int) : String
```

{% raw %}
<p></p>
{% endraw %}

这与 Kotlin 的函数声明语法非常接近，似乎完全符合逻辑。不幸的是，随着这个功能开始与他人互动，事情变得更糟：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun max(col : Collection<Int>, compare : fun(Int, Int) : Int) : Int
```

{% raw %}
<p></p>
{% endraw %}

你在冒号迷路了吗？我也是…
因此，我们决定将函数类型语法更改为以下内容：

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun max(col : Collection<Int>, compare : (Int, Int) -> Int) : Int
```

{% raw %}
<p></p>
{% endraw %}

**还有一点**
此外，我们在类型中引入了可选括号，将元组语法更改为与括号化表达式列表区分开来，并进行了一些次要（向后兼容）更改。所有这一切将很快反映在文档中。像往常一样，您的反馈非常受欢迎。
敬请关注，下周二不要错过公告！
