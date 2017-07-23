---
title: Kotlin Future Features Survey Results
date: 2017-06-13 21:24:00
author: Andrey Breslav
tags: 
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/06/kotlin-future-features-survey-results/
translator: pye52 & 睡魔的倦意
translator_url: https://pye52.github.io/ & https://suima0v0.github.io/
---

最近令人激动的事情层出不穷，我们不得不怀着抱歉的心情推迟公布Future Features Survey的结果。但迟到总比不到要好，本篇博客总结了我们在调查中获知的内容。

总的来说，[Future Features Survey](https://blog.jetbrains.com/kotlin/2017/04/kotlin-1-1-event-report/)从四月份开始，一共收到约850份答复。在此我们要感谢所有参与者！

## 调查结果
原始的统计数据（匿名）可在[这里](https://docs.google.com/spreadsheets/d/1eyhyrJPsNWrM6dYqchQzjNs41AQKjz9Xb_WB-zdy8To/edit)获得。

我们的议题有二：

* 提名三个最受你期待的特性
* 提出一项你认为不需要的特性（可选）

你可以在[这里](https://drive.google.com/file/d/0BwAovUlww0CmVmNQTXd4TTdKYUU/view)查看提名features的名单。

我们总共收到852份答复（某些是白卷），其中大多数人都用完了3个实用特性的提名名额，而约有300多人放弃了对不受欢迎特性的提名。

这是汇总的结果（按受欢迎程度排名）：

{% raw %}
<p><iframe frameborder="0" height="637" scrolling="no" seamless="" src="https://docs.google.com/spreadsheets/d/1eyhyrJPsNWrM6dYqchQzjNs41AQKjz9Xb_WB-zdy8To/pubchart?oid=2077021838&amp;format=interactive" width="790"></iframe></p>
{% endraw %}


{% raw %}
<p><span id="more-5025"></span></p>
{% endraw %}

由上图可知，最受欢迎特性的依次为：“Collection literals”, “SAM conversions for Kotlin interfaces”与“Truly immutable data”

而“Private members accessible from tests”似乎最具争议，108票赞同与120票反对。这可以理解，毕竟可测试性设计是被广泛认可的惯例。

但我对“Overloadable operators | and &”的提名结果感到些许困惑，有46票赞成与50票反对，而我看不出这个特性所带来的任何坏处，请在文章评论区分享你这样选择的原因。

这是最不受欢迎特性的排名：

{% raw %}
<p><iframe frameborder="0" height="483.5" scrolling="no" seamless="" src="https://docs.google.com/spreadsheets/d/1eyhyrJPsNWrM6dYqchQzjNs41AQKjz9Xb_WB-zdy8To/pubchart?oid=346107453&amp;format=interactive" width="933"></iframe></p>
{% endraw %}

需要说明的是，“Optional commas”和“Optional trailing commas”本应是两个选项，我们错误地把他们放在了同一个feature中，所以引起了难以解读的结果。

另外我们还忘了在调查中添加“Ternary conditional operator”，在我意识到的时候已经太晚了，很抱歉各位。我们已经明白这个功能会有很大需求，会持续进行研究的。

但最奇怪的是，这次调查的结果与在Kotlin 1.1发布会中进行的调查截然不同：

{% raw %}
<p><iframe frameborder="0" height="580" scrolling="no" seamless="" src="https://docs.google.com/spreadsheets/d/1gR1C69Rcmv2szbQJ-mXrhW7KtU4tPSya93Xq9sfE8Y0/pubchart?oid=2043595044&amp;format=interactive" width="1034"></iframe></p>
{% endraw %}

我怀疑是人们看了上次投票后产生了某些偏见，但这很难确定，也可能是另外的因素，例如线下与线上的参与者本身就具有很大的差异性。

## 结论
已明确方向的三个特性是：

* Collection literals
* SAM conversions for Kotlin interfaces
* Truly immutable data

相比之下其余的features只收到了较少的投票。Truly immutable data饱受期待，但真的很难实现，这里我们没法给予承诺。而另外两项在不久的将来都可以实现，multi-catch看起来也不错。总而言之，我们将在工作计划中重视这次调查的结果。

免责声明：如上所述，我们并没有承诺在特定的时间内完成任何这些功能。我们很关心用户需要什么，但不能预先承诺任何东西。因为在知道这些功能是否确切（并且优雅地）适合这种语言之前，我们都需要进行慎重的设计工作。