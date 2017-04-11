---
title: [译]Follow-up: New Class Object Syntax
date: 2015-03-14 10:57:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/03/follw-up-new-class-object-syntax/
---

在上一篇文章中，我解释了以前被称为“类对象”的重新设计：它们现在与普通嵌套对象更加统一，名称（名称可以省略，但编译器将使用默认名称），我们可以为其添加扩展名。
该职位的目标之一是收集关于我们提出的术语的反馈意见，即“默认对象”，并且许多人在评论中正确地声明该术语具有缺点：对于“默认实例类”。现在我们正在寻找一个更好的术语，需要更多的反馈...
更新：感谢大家，在您的帮助下，我们选择了伴侣。
我们正在谈论一个修饰符在单词对象前面：

{% raw %}
<p></p>
{% endraw %}

```kotlin
class KotlinClass {
    ??? object {
        fun callMeOnTheClassName() { ... }
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

我们的候选人是：

* 默认对象
* 附加对象
* 伴侣对象
* 清单对象

如果您在评论中分享了有关这些候选人的想法，我们将非常感激。
谢谢！
美国有一个建议是简单地使用命名约定而不是修饰符。这个评论解释了为什么我们决定赞成一个修饰语。还要注意的是，这个惯例比其他公约会更频繁地使用，而另外一些公约将在即将到来的语言设计审查中被重新考虑。
