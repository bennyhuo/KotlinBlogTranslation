---
title: [译]Kotlin gets support for S-expressions
date: 2014-04-01 18:33:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2014/04/kotlin-gets-support-for-s-expressions/
---

Kotlin总是乐意从其他编程语言中学习，这就是为什么我们决定支持S表达式，增强LISP的概念。
其背后的主要动机是与Clojure（JVM的LISP）兼容。 Clojure以其实体库而闻名，特别是用于并发和只读数据结构的库。
为了促进与LISP（特别是Clojure库）的互操作性，Kotlin现在允许这样的表达式：

{% raw %}
<p></p>
{% endraw %}

```kotlin
(println (
        (lambda (arg1)
            (+
                "first lambda: "
                arg1
                (lambda (arg2)
                    (+ "second lambda: " arg1 arg2)
                )
            )
        ) foo "bar"
    ))
```

{% raw %}
<p></p>
{% endraw %}

这只是给你的味道。现在，我们一个一个地解释这个结构。
## S表达式解释

首先，只添加一个新的句法结构，即S表达式。它有形式

{% raw %}
<p></p>
{% endraw %}

```kotlin
(A B C ...)
```

{% raw %}
<p></p>
{% endraw %}

其中A，B，C ...可能自己是S表达式或其他Kotlin表达式。
现在，LISP中的大多数操作都是以前缀形式编写的，如果需要，您可以在Kotlin中以此样式写入添加：

{% raw %}
<p></p>
{% endraw %}

```kotlin
(+ 1 two 3)
```

{% raw %}
<p></p>
{% endraw %}

请注意，文字（'1'，'3'）可以与其他表达式（例如“两”）混合。
LISP原来代表LISt Processing，所以列表的文字非常重要：

{% raw %}
<p></p>
{% endraw %}

```kotlin
(list abc "def" ghi "jkl")
```

{% raw %}
<p></p>
{% endraw %}

这将创建一个四个对象的列表。
正常的Kotlin函数可以以LISP方式调用，因此要打印上面的列表，我们可以说：

{% raw %}
<p></p>
{% endraw %}

```kotlin
  (println
       (list abc "def" ghi "jkl")
  )
```

{% raw %}
<p></p>
{% endraw %}

Lambda表达式还具有LISP格式：

{% raw %}
<p></p>
{% endraw %}

```kotlin
(lambda (arg1) (+ 1 arg1 2))
```

{% raw %}
<p></p>
{% endraw %}

以下代码演示了闭包：

{% raw %}
<p></p>
{% endraw %}

```kotlin
    (println (
        (lambda (arg1)
            (+
                "first lambda: "
                arg1
                (lambda (arg2)
                    (+ "second lambda: " arg1 arg2)
                )
            )
        ) foo "bar"
    ))
```

{% raw %}
<p></p>
{% endraw %}

## 试试看！

你可以在这里找到上面的例子（还有一些）。他们是可运行的，你可以玩代码。免责声明：这只是一个原型。
## 限制

不幸的是，在这个阶段我们对S表达式的支持有限。由于与解析相关的一些问题，S表达式只能是奇数长度。我们正在努力消除这个限制。
另外，当将命名函数定义为S表达式时，其名称必须在前面带有一个点（不要与下面提到的点运算符混淆）：

{% raw %}
<p></p>
{% endraw %}

```kotlin
(defun .baz (a, b, c) (+ a b c))<span style="font-size: 16px;"> 
</span>
```

{% raw %}
<p></p>
{% endraw %}

## 点运算符

你们中的许多人正在急切地等待我们释放点运算符。现在实现，编译器和IDE插件可以在这里下载，感谢jgl87。
