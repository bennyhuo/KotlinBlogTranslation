---
title: "A little lesson learned from Java"
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
translator:
translator_url:
---

*A post about good books, language design and JIT compilation, in which one bug turns into another and than back…<br/>*
Recently I started looking through an excellent book [“Java™ Puzzlers”](http://www.javapuzzlers.com/) , where Joshua Bloch and Neal Gafter provide a list of Java’s “Traps, Pitfalls, and Corner Cases”, i.e. programs that make you think they do what they really don’t. My idea is to see how many of the puzzlers are ruled out or fixed by Kotlin. I’ve looked through the first 24 items, and 15 of them are fixed in Kotlin, which is over 60%.
Some of the puzzlers can’t be fixed without severe implications on compatibility with the rest of the world. For example, most of the tricky things about IEEE-745 floating-point numbers. But some other ones, though not fixed in Kotlin yet, may be fixed. One particular example is Puzzler 26 “In the Loop”:

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

Don’t read further until you figure what this program prints <img alt=":)" class="wp-smiley" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1" style="height: 1em; max-height: 1em;"/>
<span id="more-247"></span><br/>
This program prints nothing and simply loops forever, because variable ‘i’ is of type **int**, and ANY **int** is less or equal than Integer.MAX_INT.
Now, if I write this in Kotlin:

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

It does NOT loop. And prints “101”, which is the size of the range of iteration…
This is the point where you think: “Didn’t he say that this puzzler is not yet fixed by Kotlin?” Yes, I did.
This Kotlin program SHOULD loop forever. And it does not. Sigh. I have already opened the “New issue” dialog in our [tracker](http://youtrack.jetbrains.net/issues/KT) when I got too curious and looked at the code our compiler emits. You know what? I found nothing bad there. Written in Java (I am your honest decompiler today), it would look like this:

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

And this TERMINATES and prints “101”. That’s where I really got puzzled.
After some experimentation, I discovered that making variable ‘end’ **final** makes the program loop forever. “It must be JIT, ” — I though, and was right: when run with “java -Xint”, this code loops forever, and so does the Kotlin code.
How come? Well, I run a 64-bit JVM. Most likely, JIT optimizer makes the loop variable 64-bit, because registers are this big, or something like this, and it does not overflow, but just becomes Integer.MAX_VALUE + 1.
Sigh. I closed our “New issue” dialog, and opened the HotSpot’s one… (Some technicalities prevent me from finishing the reporting process right now, but I will do it on Monday).
Now, **what lesson can we learn from this**? I don’t think I can learn much from hitting a JIT bug. Bugs happen — that’s the lesson here, I think.
But what about the initial puzzler? I teach Pascal at a high school, and one thing I really like about this language is that a **for** loop ALWAYS TERMINATES there. We cannot have the same in Kotlin, because in general **for** uses an iterator that may have arbitrary logic in it. But what we can do is guarantee that **iteration over a range of numbers always terminates**.
BTW, if a range was just a list of numbers, the loops would terminate, right? So it **IS** a [bug](http://youtrack.jetbrains.net/issue/KT-492) in the Kotlin compiler, after all. <img alt=":)" class="wp-smiley" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1" style="height: 1em; max-height: 1em;"/>
