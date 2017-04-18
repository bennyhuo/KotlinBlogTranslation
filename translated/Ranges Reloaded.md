---
title: "[译]Ranges Reloaded"
date: 2013-02-06 14:47:00
author: Evgeny Gerashchenko
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2013/02/ranges-reloaded/
---

在 [Kotlin M5](http://blog.jetbrains.com/kotlin/2013/02/kotlin-m5-is-out/)  我们已经重新设计了我们的范围。<span id =“more-855”> </ span>
范围表达式与具有<tt> rangeTo </ tt>函数形成 [操作员形式](http://confluence.jetbrains.com/display/Kotlin/Operator+overloading#Operatoroverloading-Binaryoperations)  补充 [in和！in](http://confluence.jetbrains.com/display/Kotlin/Operator+overloading#Operatoroverloading-in) 。范围是针对任何可比类型（<code> Comparable </ code>的子类）定义的，但是对于数字原语，它被优化。以下是使用范围的示例：

{% raw %}
<p></p>
{% endraw %}

```kotlin
if (i in 1..10) { // equivalent of 1 <= i && i <= 10
  println(i)
}
 
if (x !in 1.0..3.0) println(x)
 
if (str in "island".."isle") println(str)
// equivalent of "island" <= str && str <= "isle"
```

{% raw %}
<p></p>
{% endraw %}

数值范围有额外的功能：可以迭代。编译器在Java的索引for循环的简单模拟中关心转换，而不需要额外的开销。例子：

{% raw %}
<p></p>
{% endraw %}

```kotlin
for (i in 1..4) print(i) // prints "1234"  
 
for (i in 4..1) print(i) // prints nothing
 
for (x in 1.0..2.0) print("$x ") // prints "1.0 2.0 "
```

{% raw %}
<p></p>
{% endraw %}

如果你想以相反的顺序迭代数字怎么办？这很简单。您可以使用标准库中定义的<tt> downTo（）</ tt>函数：

{% raw %}
<p></p>
{% endraw %}

```kotlin
for (i in 4 downTo 1) print(i) // prints "4321"
```

{% raw %}
<p></p>
{% endraw %}

可以用任意步长迭代数字，不等于1？当然，<tt> step（）</ tt>功能会帮助你：

{% raw %}
<p></p>
{% endraw %}

```kotlin
for (i in 1..4 step 2) print(i) // prints "13"  
 
for (i in 4 downTo 1 step 2) print(i) // prints "42"  
 
for (i in 1.0..2.0 step 0.3) print("$x ") // prints "1.0 1.3 1.6 1.9 "
```

{% raw %}
<p></p>
{% endraw %}

## 怎么运行的

库中有两个特征：<tt> Range＆lt; T＆gt; </ tt>和<tt>进展＆lt; N＆gt; </ tt>。
<tt>范围＆lt; T＆gt; </ tt>表示数学意义上的间隔，用于可比类型。它有两个端点：<tt> start </ tt>和<tt> end </ tt>，它们包含在范围内。主要操作是<tt> contains（）</ tt>，通常在</ tt> / <tt>！中的</ tt>操作符中以<tt>的形式使用。
<tt>进展＆lt; N＆gt; </ tt>表示 [算术进展](http://en.wikipedia.org/wiki/Arithmetic_progression) ，定义为数字类型。它具有<tt> start </ tt>，<tt> end </ tt>和非零<tt>增量</ tt>。 <tt>进展＆lt; N＆gt; </ tt>是<tt> Iterable＆lt; N＆gt; </ tt>的子类型，因此它可以用于for循环和诸如<tt> map </ tt>，<tt > filter </ tt>等等。第一个元素是<tt> start </ tt>，每个下一个元素等于上一个加号<tt>增量</ tt>。在<tt>进化中的迭代</ tt>相当于Java / JavaScript中的索引for循环：

{% raw %}
<p></p>
{% endraw %}

```kotlin
// if increment > 0
for (int i = start; i <= end; i += increment) {
  // ...
}
 
// if increment < 0
for (int i = start; i >= end; i += increment) {
  // ...
}
```

{% raw %}
<p></p>
{% endraw %}

对于数字，“<tt> .. </ tt>”运算符创建一个对象，它们都是<tt> Range </ tt>和<tt> Progression </ tt>。 <tt> downTo（）</ tt>和<tt> step（）</ tt>函数的结果始终是<tt>进度</ tt>。
