---
title: "Kotlin gets support for S-expressions"
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

Kotlin is always happy to learn from other programming languages, and this is why we decided to support  [S-expressions](http://en.wikipedia.org/wiki/S-expression) , the empowering concept of  [LISP](http://en.wikipedia.org/wiki/Lisp_(programming_language)) .
The main motivation behind this is the compatibility with  [Clojure](http://clojure.org/) , the LISP for the JVM. Clojure is well-known for its solid libraries, particularly the ones used for concurrency and read-only data structures.
To facilitate interoperability with LISP (and Clo<em>j</em>ure libraries in particular), Kotlin now allows expressions like this one:

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

This is only to give you the taste. Now, let’s explain the constructs one-by-one.<span id="more-1505"></span>
## S-expressions explained

First of all, there’s only one new syntactic construct added, namely the S-expression. It has the form

{% raw %}
<p></p>
{% endraw %}

```kotlin
(A B C ...)
```

{% raw %}
<p></p>
{% endraw %}

where A, B, C … may themselves be S-expressions or other Kotlin expressions.
Now, most operations in LISP are written in prefix form, and if you want, you can write addition in this style in Kotlin:

{% raw %}
<p></p>
{% endraw %}

```kotlin
(+ 1 two 3)
```

{% raw %}
<p></p>
{% endraw %}

Note that literals (‘1’, ‘3’) can be mixed with other expressions (e.g. ‘two’).
LISP originally stands for <strong>LIS</strong>t <strong>P</strong>rocessing, so the literals for lists are very important:

{% raw %}
<p></p>
{% endraw %}

```kotlin
(list abc "def" ghi "jkl")
```

{% raw %}
<p></p>
{% endraw %}

This create a list of four objects.
Normal Kotlin functions can be called in the LISP-manner, so to print the list above, we can say:

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

Lambda expressions also have a LISP-form:

{% raw %}
<p></p>
{% endraw %}

```kotlin
(lambda (arg1) (+ 1 arg1 2))
```

{% raw %}
<p></p>
{% endraw %}

And the following code demonstrates closures:

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

## Try it out!

You can find the above examples (and some more)  [here](http://kotlin-demo.jetbrains.com/?publicLink=104074971561017308771-1697121195) . They are runnable, and you can play with the code. <strong>Disclaimer</strong>: it’s only a prototype.
## Limitations

Unfortunately, at this stage our support for S-expressions is somewhat limited. Due to some issues connected with parsing, an S-expression can only be of <strong>odd length</strong>. We are working on removing this limitation.
Also, when defining a named function as an S-expression, its name has to be preceded with a dot (not to be confused with the Dot operator mentioned below):

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

## Dot Operator

Many of you were waiting eagerly for us to release the  [Dot operator](http://blog.jetbrains.com/kotlin/2013/04/the-dot-operator/) . Now it’s implemented, compiler and IDE plugin are downloadable  [here]( https://github.com/JetBrains/kotlin/releases/tag/dot-operator) , thanks to  [jgl87](https://github.com/JetBrains/kotlin/pull/430) .
