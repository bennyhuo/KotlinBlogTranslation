---
title: "The Dot Operator"
date: 2013-04-01 10:00:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2013/04/the-dot-operator/
---

<strong>Warning: this is an April Fools’ post</strong> [Point-free](http://en.wikipedia.org/wiki/Point-free_programming) style is a big trend in modern functional programming: it allows to manipulate functions without mentioning their arguments which makes the code concise and compositional. Here is an example from Wikipedia:

{% raw %}
<p></p>
{% endraw %}

```kotlin
mf = (. map) . (.) . filter
```

{% raw %}
<p></p>
{% endraw %}

This function, written in Haskell, composes a map() function with a filter() function. As you can see, point-free style largely relies on dots.
Kotlin is not a functional language per se, but we are happy to borrow useful features from other languages. So, today I’ll write about dots.<span id="more-1007"></span>
# The Dot

We introduce the <strong>dot</strong> operator in Kotlin. As usual, it works by convention. If there’s a function like this

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun Foo.dot() {
    println("a dot!")
}
```

{% raw %}
<p></p>
{% endraw %}

it will be called whenever there’s a dot (“.”) after an expression of type Foo:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun test(f: Foo) {
    f.foo()
    Foo().bar().baz()
}
```

{% raw %}
<p></p>
{% endraw %}

This function prints “a dot!” twice: once for each dot after a Foo. The bar() function doesn’t return a Foo, so the dot after it doesn’t count.
# Dot Chaining

What if my dot() function returned something, for example, another Foo?

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Foo(val count: Int)
 
fun Foo.dot(): Foo {
    return Foo(count + 1)
}
```

{% raw %}
<p></p>
{% endraw %}

then, of course, it’s result is used to call whatever comes after the dot:

{% raw %}
<p></p>
{% endraw %}

```kotlin
println(Foo(1).count)
```

{% raw %}
<p></p>
{% endraw %}

This prints 2, because the dot() function returned a new Foo with an increased counter.
As you can see, the dot operator gives us a lot of power and addresses most of the issues previously tackled only by [aspect-oriented programming](http://en.wikipedia.org/wiki/Aspect-oriented_programming) .
# Flavors of the Dot

The real power of the dot operator comes in when you declare it with a parameter:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun Any.dot(p: Dot) {
   ...
}
```

{% raw %}
<p></p>
{% endraw %}

The parameter must be of the Dot type, of which there are a few interesting predefined values:

{% raw %}
<p></p>
{% endraw %}

```kotlin
LEFT
RIGHT
TOP
BOTTOM
```

{% raw %}
<p></p>
{% endraw %}

These values correspond, obviously, to the position of the dot:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun test() {
    println(a.b[1..2])
}
```

{% raw %}
<p></p>
{% endraw %}

One might think that in this example dot() is called three times: one for “a.b”, with the argument BOTTOM, then twice for “1..2”: first with LEFT, and then with RIGHT (these are not two BOTTOMs, because “..” is a single  [token](http://en.wikipedia.org/wiki/Token_(parser)#Token)  in Kotlin), but in fact it gets called four times, and the fourth time (in fact it comes first) with TOP as an argument.
I’m sure you already see why: in Kotlin, we never forget to dot out i’s, and that dot counts as well; its position is clearly TOP (we could introduce a separate [tittle](http://en.wikipedia.org/wiki/Tittle) () function, but we found it too inconvenient). Tittles above j’s count just as well, same for dots in ; ! ? etc.
# The Depth of the Dot

You may be wondering what happens if dot() is defined like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun Foo.dot() {
    println(this.count)
}
```

{% raw %}
<p></p>
{% endraw %}

There is a dot after <strong>this</strong>, which has type Foo, in the body of Foo.dot() function itself, so dot() should be called recursively at that point and, seemingly, never terminate. This is called a <em>higher-order dot</em>, and is executed only if there’s a function dot1() defined on Foo. If dot1(), in turn, contains a higher-order dot, then dot2() is called and so on:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun Foo.dot1() {
    println(this.count) // a call to dot2() if that is defined
}
```

{% raw %}
<p></p>
{% endraw %}

This corresponds to Russel’s approach to set theory called [type theory](http://en.wikipedia.org/wiki/Type_theory) (with its notion of a  [class](http://en.wikipedia.org/wiki/Class_(set_theory)) ), which lies the solid foundation for statically-typed object-oriented programming.
# Conclusion

We are planning to support the dot operator very soon. The first version will be restricted to basic ASCII characters such as . : ; ! ? and, of course i, but in the future we plan to expand it to other characters like ё.
<strong>Have a nice Dot!</strong>
