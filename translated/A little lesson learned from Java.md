---
title: "[译]A little lesson learned from Java"
date: 2011-11-13 07:21:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2011/11/a-little-lesson-learned-from-java/
---

关于好书，语言设计和JIT编译的一篇文章，其中一个bug变成了另一个而不是后面的...
</ em>
最近我开始看一本优秀的书 [“Java™拼图”](http://www.javapuzzlers.com/) Joshua Bloch和Neal Gafter提供了Java的“陷阱，陷阱和角落案例”，即使您认为他们做的事情真的没有的程序。我的想法是看Kotlin排除或修复了多少益智游戏。我看过前24个项目，其中15个在Kotlin修复，超过60％。
一些益智游戏无法解决，与世界其他地区的兼容性没有严重的影响。例如，关于IEEE-745浮点数的大多数棘手的事情。但是其他一些，虽然在Kotlin尚未修复，但可能会被修复。一个特别的例子是Puzzler 26“In the Loop”：

{% raw %}
<p></p>
{% endraw %}

```kotlin
/**
* Bloch, Joshua; Gafter, Neal (2005-06-24).
* Java™ Puzzlers: Traps, Pitfalls, and Corner Cases (p. 57).
* Pearson Education (USA). Kindle Edition.
*/
public class InTheLoop {
    public static final int END = Integer.MAX_VALUE;
    public static final int START = END - 100;
 
    public static void main(String[] args) {
        int count = 0;
        for (int i = START; i <= END; i++)
            count++;
        System.out.println(count);
    }
}
```

{% raw %}
<p></p>
{% endraw %}

不要再进一步阅读，直到你确定这个程序打印出来为止。<img alt =“:)”class =“wp-smiley”data-recalc-dims =“1”src =“https://i2.wp.com/blog .jetbrains.com / kotlin / wp-includes / images / smilies / simple-smile.png？w = 640＆amp; ssl = 1“style =”height：1em; max-height：1em“
<span id =“more-247”> </ span> <br/>
因为变量'i'的类型为<strong> int </ strong>，并且ANY <strong> int </ strong>小于或等于Integer.MAX_INT，此程序不会打印任何东西，只需循环即可。
现在，如果我写在Kotlin：

{% raw %}
<p></p>
{% endraw %}

```kotlin
val end = Integer.MAX_VALUE
val start = end - 100
var count = 0
for (i in start..end)
  count++
println(count)
```

{% raw %}
<p></p>
{% endraw %}

它不循环。并打印“101”，这是迭代范围的大小...
这是你想的那一点：“他没有说这个难题还没有被Kotlin固定吗？”是的，我做了。
这个Kotlin程序应该永远循环。而且没有。叹。我已经打开了“新问题”对话框 [跟踪器](http://youtrack.jetbrains.net/issues/KT)  当我太好奇了，看看编译器发出的代码。你知道吗？我没发现什么坏事用Java编写（我今天是你诚实的反编译器），它看起来像这样：

{% raw %}
<p></p>
{% endraw %}

```kotlin
    int end = Integer.MAX_VALUE;
    int start = end - 100;
    int count = 0;
    for (int i = start; i <= end; i++)
       count++;
    System.out.println("count = " + count);
```

{% raw %}
<p></p>
{% endraw %}

并且此终止并打印“101”。那是我真的很困惑的地方
经过一些实验，我发现使变量'end'<strong> final </ strong>使得程序永远循环。 “它必须是JIT”，而且我是对的，当使用“java -Xint”运行时，此代码永远循环，Kotlin代码也循环使用。
怎么来的？那我运行一个64位的JVM。最有可能的是，JIT优化器使循环变量为64位，因为寄存器是这么大的，或者这样的东西，它不会溢出，只是变成Integer.MAX_VALUE + 1。
叹。我关闭了我们的“新问题”对话框，并打开了HotSpot的一个...（有些技术性阻止我现在完成报告过程，但是我会在星期一做）。
现在，我们可以从这个</ strong>中学到什么教训？我不认为我可以从JIT错误中学到很多东西。错误发生 - 这是这里的教训，我想。
但最初的益智游戏呢？我在高中教帕斯卡，一件我非常喜欢这种语言的是<strong> </ strong>循环，总是在这里终止。我们在Kotlin中不能拥有相同的，因为通常<strong> </ strong>使用可能具有任意逻辑的迭代器。但是我们可以做的是保证一系列数字上的<strong>迭代总是终止</ strong>。
BTW，如果一个范围只是一个数字的列表，循环将终止，对吗？所以<strong> IS </ strong> a [错误](http://youtrack.jetbrains.net/issue/KT-492)  在Kotlin编译器毕竟。 <img alt =“:)”class =“wp-smiley”data-recalc-dims =“1”src =“https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images /smilies/simple-smile.png?w=640&amp;ssl=1“style =”height：1em; max-height：1em;“/>
