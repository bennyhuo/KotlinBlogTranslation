---
title: Kotlin Future Features Survey Results
author: Andrey Breslav
date: 2017-06-13 21:24:00
source_url: https://blog.jetbrains.com/kotlin/2017/06/kotlin-future-features-survey-results/
tags: 
categories:  官方动态
---

随着所有令人兴奋的最近的事件，我们不得不推迟未来功能调查结果的出版。对于那个很抱歉。比以往更好，本博客总结了我们从调查中学到的内容。
要概述，未来功能调查在四月份进行，约有850份回复。我们要感谢参加调查的所有人！
## 调查结果

调查的原始（匿名）数据可在这里获得。
问题是：

* 最期待的功能1，最期待的功能2，最期待的功能3
* 提名您希望被禁止的一项功能（可选）

您可以在这里查看建议功能的列表。
我们收到了852份答复（其中一些是空白）。大多数人用完了所有三个插槽的积极特征提名，大约300多人跳过了负面提名。
这里是所有结果的总结图（按照有利于特征的提名排序）：

{% raw %}
<p><iframe frameborder="0" height="637" scrolling="no" seamless="" src="https://docs.google.com/spreadsheets/d/1eyhyrJPsNWrM6dYqchQzjNs41AQKjz9Xb_WB-zdy8To/pubchart?oid=2077021838&amp;format=interactive" width="790"></iframe></p>
{% endraw %}


{% raw %}
<p><span id="more-5025"></span></p>
{% endraw %}

所以，这里的喜好是： -  Kotlin接口的AM转换和“不可变数据”？
可以从测试中获得的竞争对手似乎是最有争议的特征：108个人和120个反对者，这是可以理解的，因为设计可测性被广泛认为是一个很好的做法。
我对“可加载运算符”有点困惑和争议：46和50反对，而我在这个功能看到零伤害。请分享你对这篇文章评论的动机。
这里是负面提名图：

{% raw %}
<p><iframe frameborder="0" height="483.5" scrolling="no" seamless="" src="https://docs.google.com/spreadsheets/d/1eyhyrJPsNWrM6dYqchQzjNs41AQKjz9Xb_WB-zdy8To/pubchart?oid=346107453&amp;format=interactive" width="933"></iframe></p>
{% endraw %}

我们不应该把同样的特征（我的错误，对不起）放在“逗号”和“逗号”之间，实际上是两个特征，所以结果难以解释。
另一个错误（在我方面）：我们忘了在调查中包含“三进制条件运算符”，并意识到游戏太晚了。对不起，有些人，我们明白，这个功能有很大的需求，并且会进行研究。
奇怪的是，在Kotlin 1.1发射活动中进行的调查结果却截然不同：

{% raw %}
<p><iframe frameborder="0" height="580" scrolling="no" seamless="" src="https://docs.google.com/spreadsheets/d/1gR1C69Rcmv2szbQJ-mXrhW7KtU4tPSya93Xq9sfE8Y0/pubchart?oid=2043595044&amp;format=interactive" width="1034"></iframe></p>
{% endraw %}

我怀疑结果可能受到人们以前的选票和偏见的事实的影响，但很难确定。其他因素也可能是相关的，例如。聚会上的观众可能与在线调查对象有点不同。
## 结论

有明确的领导：

* 收集文字
* Kotlin接口的SAM转换
* 真正不可变数据

其余的功能明显减少提名。真正不可变的数据是非常可取的，但真的很艰难，所以没有承诺。另外两个在可预见的将来看起来似乎很容易，而且多捕捉看起来好像是一件好事。无论如何，我们将在规划我们的工作时考虑结果。
免责声明：如前所述，我们并没有承诺在特定的时间框架内完成任何这些功能。我们很关心用户需要什么，但可以预先提供任何东西。一方面，在我们甚至知道这些功能是否可以实际地（优雅地）适合这种语言之前，需要进行重要的设计工作。
