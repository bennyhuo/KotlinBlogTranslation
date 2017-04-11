---
title: Ranges Reloaded
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

In Kotlin M5 we have redesigned our ranges a little bit.
Range expressions are formed with rangeTo functions that have the operator form of .. which are complemented by in and !in. Range is defined for any comparable type (subclass of Comparable), but for number primitives it is optimized. Here are examples of using ranges:

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

Numerical ranges have extra feature: they can be iterated over. Compiler takes care about converting this in simple analogue of Java’s indexed for-loop, without extra overhead. Examples:

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

What if you want to iterate over numbers in reversed order? It’s simple. You can use downTo() function defined in standard library:

{% raw %}
<p></p>
{% endraw %}

```kotlin
for (i in 4 downTo 1) print(i) // prints "4321"
```

{% raw %}
<p></p>
{% endraw %}

Is it possible to iterate over numbers with arbitrary step, not equal to 1? Sure, step() function will help you:

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

## How it works

There are two traits in the library: Range<T> and Progression<N>.
Range<T> denotes an interval in the mathematical sense, defined for comparable types. It has two endpoints: start and end, which are included in the range. Main operation is contains(), usually used in the form of in/!in operators.
Progression<N> denotes arithmetic progression, defined for number types. It has start, end and non-zero increment. Progression<N> is a subtype of Iterable<N>, so it can be used in for-loops and functions like map, filter, etc. First element is start, every next element equals previous plus increment. Iteration over Progression is equivalent to an indexed for-loop in Java/JavaScript:

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

For numbers, the “..” operator creates an object which is both Range and Progression. Result of downTo() and step() functions is always a Progression.
