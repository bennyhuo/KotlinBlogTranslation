---
title: "Multiple Inheritance Part 1: Problems with the existing design"
date: 2011-08-23 12:59:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2011/08/multiple-inheritance-part-1-problems-with-the-existing-design/
translator:
translator_url:
---

I’m back from my vacation, and it’s time to get to one one the biggest issues pointed out in the feedback we received during conference presentations and in the comments to the docs. I’m talking about inheritance.
I plan to write a series of posts on this topic. These posts are intended to provoke a discussion, so that we can benefit from your feedback and come up with a better design.
This is the first post in the series, and I discuss the design we [presented in July 2011](http://confluence.jetbrains.net/download/attachments/40702623/JVMLS_workshop_2011.pdf?version=1&modificationDate=1311201781543) . It features the following approach to inheritance:

* there were no interfaces, only classes;
* each class could have multiple superclasses;
* if some non-abstract member (property or method) was inherited from two of the supertypes, the compiler required the user to override it and specify manually what code to run.

(For more details, see our [wiki](http://confluence.jetbrains.net/pages/viewpage.action?pageId=41484416) as of July 20th 2011.)
This is, basically, the infamous **multiple inheritance** story, and we remember from the C++ times that it is sort of bad. Let’s look closer.
**It’s all about initialization**
Let’s a look at the following example:

{% raw %}
<p></p>
{% endraw %}

```kotlin
abstract class Base(x : Int) { ... }
 
open class Left(x : Int) : Base(x) { ... }
open class Right(x : Int) : Base(x) { ... }
 
class Child : Left(3), Right(4) { ... }
```

{% raw %}
<p></p>
{% endraw %}

So, we have a [diamond](http://en.wikipedia.org/wiki/Diamond_problem) : Base at the top, Left and Right on the sides, and Child at the bottom. One thing looks suspicious here: Child initializes its superclasses passing different numbers two them: 3 to Left and 4 to right. Now, they, in turn, initialize Base with those numbers… What is Base initialized with?

{% raw %}
<p><span id="more-74"></span></p>
{% endraw %}

Actually, there are two “instances” of Base created: one, initialized with 3, is hidden inside Left(3), and another, initialized with 4 — inside Right(4). I.e. it works like non-virtual inheritance in C++. (On the Java platform, we implemented it by delegation, which is invisible for the user.)
Now, what happens when you call a function that is defined in Base? For example, let’s say that Base defines two abstract functions:

{% raw %}
<p></p>
{% endraw %}

```kotlin
abstract class Base(x : Int) {
  fun foo()
  fun bar()
}
```

{% raw %}
<p></p>
{% endraw %}

Now, let Left override foo() and Right override Bar:

{% raw %}
<p></p>
{% endraw %}

```kotlin
open class Left(x : Int) : Base(x) {
  override fun foo() { print(x) }
}
open class Right(x : Int) : Base(x) {
  override fun bar() { print(x) }
}
```

{% raw %}
<p></p>
{% endraw %}

In this case Child inherits two <em>declarations</em> of foo() and two <em>declarations</em> bar(), but at the same time it inherits <em>only one implementation</em> for each of these functions, so it’s OK, the behavior is determined. So, when we say

{% raw %}
<p></p>
{% endraw %}

```kotlin
val c = Child(0)
c.foo()
c.bar()
```

{% raw %}
<p></p>
{% endraw %}

The output is

{% raw %}
<p></p>
{% endraw %}

```kotlin
3
4
```

{% raw %}
<p></p>
{% endraw %}

Because foo() was called for Left, and bar() was called for Right.
If Child inherited more <em>than one implementation</em> of, say, foo(), the compiler would have complained until we override foo() in Child and specify the behavior explicitly. So, we are guaranteed to have no ambiguity when calling functions of Child.
So far, so good, but there still is something wrong with this approach…
**Problem 1:** the constructor for Base is called twice whenever we create an instance of Child. It’s bad because if it has side-effects, they are duplicated, and the author of the Child class may not know about it, because someone change the inheritance graph turning it into a diamond that was not there before.
<br/>
**Problem 2:** the implementation of Left assumes it’s initialized with 3, but it may call bar() that is implemented in Right and assumes everything is initialized with 4. This may cause some inconsistent behavior.
**Problem 3:** being implemented by delegation, deep hierarchies will degrade performance by having long delegation chains.
**(Im)Possible ways of fixing it**
Now, how can we fix our design? C++ copes with **Problems 1** and **3** by having [virtual inheritance](http://en.wikipedia.org/wiki/Virtual_inheritance) . On the Java platform and with separate compilation in mind, I do not think we can get rid of delegation when a class <em>inherits state</em> from two sources, so the **Problem 3** stands for us anyway. And having two flavors of inheritance is no good, as we learned from C++…
Virtual inheritance does not fix **Problem 2**: being initialized differently, parts of the inherited implementation may make inconsistent assumptions about the overall state of the object. This problem seems intractable in the general case, but let’s be accurate and make sure it really is.
We could try to guarantee that everything is initialized consistently. In the general case, when we pass arbitrary expressions to Left and Right, there’s no way to be sure they yield same results, even if they are textually the same. Then, we could impose some constraints here. For example: only allow to pass compile-time constants or immutable variables to superclass constructors. In this case the compiler could examine the whole class hierarchy and make sure every base class is initialized consistently. There is a problem, though: if one of the superclasses change its initialization logic even slightly, subclasses may become inconsistent, so this will be a big evolution problem, for example, for libraries.
And, of course, it would be too restrictive to impose those constraints on all classes. So we end up with two flavors of classes…
Well, it seems that “there are only classes (i.e. no interfaces or alike)” approach did not work out. Now, it’s time to consider other approaches.
**What’s out there**
Different languages manage multiple inheritance differently, and I summarize some of the approaches here.

* Java and C# have classes and interfaces, i.e. multiple interface inheritance and single implementation inheritance;
* Scala has classes and traits that may implement methods and even have state, but their constructors can not have parameters;
* Some other languages, like Fortress, do not allow state in traits;
* <Your favorite language here>

In the [next post](http://blog.jetbrains.com/kotlin/2011/08/multiple-inheritance-part-2-possible-directions/) of this series we will discuss the options in detail.
And now it’s time for your comments. They are very welcome.
