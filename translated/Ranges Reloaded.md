---
title: [译]Ranges Reloaded
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

在Kotlin M5中，我们重新设计了一些范围。
范围表达式由具有操作符形式的rangeTo函数形成，它们由in和！in进行补充。范围是针对任何可比类型（Comparable的子类）定义的，但是对于优化的数字原语。以下是使用范围的示例：

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

如果你想以相反的顺序迭代数字怎么办？这很简单。您可以使用标准库中定义的downTo（）函数：

{% raw %}
<p></p>
{% endraw %}

```kotlin
for (i in 4 downTo 1) print(i) // prints "4321"
```

{% raw %}
<p></p>
{% endraw %}

可以用任意步长迭代数字，不等于1？当然，step（）函数会帮助你：

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

图书馆有两个特征：范围<T>和进展<N>。
范围<T>表示数学意义上的间隔，用于可比类型。它有两个端点：开始和结束，它们包含在范围内。主要操作是contains（），通常以运算符中的/！形式使用。
进展<N>表示为数字类型定义的算术级数。它具有开始，结束和非零增量。进展<N>是Iterable <N>的子类型，因此可用于for循环和函数，如map，filter等。第一个元素是start，每个下一个元素等于previous plus increment。过程迭代相当于Java / JavaScript中的索引for循环：

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

对于数字，“..”运算符创建一个对象，它是Range和Progression。 downTo（）和step（）函数的结果总是一个进展。
