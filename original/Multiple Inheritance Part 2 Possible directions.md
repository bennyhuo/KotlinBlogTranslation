---
title: "Multiple Inheritance Part 2: Possible directions"
date: 2011-08-31 16:21:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2011/08/multiple-inheritance-part-2-possible-directions/
translator:
translator_url:
---

In the [previous post in this series](http://blog.jetbrains.com/kotlin/2011/08/multiple-inheritance-part-1-problems-with-the-existing-design/) we discussed the disadvantages of [the inheritance model we initially planned for Kotlin](http://confluence.jetbrains.net/pages/viewpage.action?pageId=41484416) . Today we will talk about alternative designs.
Note that these posts are intended to provoke a discussion, so that we can benefit from your feedback and come up with a better design.
<strong>What’s out there</strong>
The previous post concluded with the following (incomplete) list of solutions to the problem of multiple inheritance available in other languages:

* Java and C# have classes and interfaces, i.e. multiple interface inheritance and single implementation inheritance;
* Scala has classes and traits that may implement methods and even have state, but their constructors can not have parameters;
* Some other languages, like Fortress, do not allow state in traits;
* <Your favorite language here>

We all know that Java’s approach is rock-solid, but imposes severe limitations on code reuse, so we would like to relax these limitations, but without getting ourselves into trouble. “First degree” of relaxing the limitations would be <strong>stateless traits</strong> (like in Fortress, and in  [[1]](#Traits) ): no state in traits, no implicit overrides. Or we can trade inheritance of traits off for state and get mixins (like in Ruby). Relaxing the limitations even more we get to <strong>Scala’s traits</strong> that have state but no parameters for constructors, and one trait may override functions of another. Then we get to CZ’s classes with <strong>requires</strong> (as presented in  [[2]](#CZ) ). The next step, I guess, would already be unrestricted multiple inheritance, like in C++.
We will skip a thorough analysis of each of these solutions, and just make a remark about state.<br/>
<span id="more-115"></span><br/>
<strong>State.</strong> One important consideration is whether to allow <strong>multiple inheritance of state</strong> in this or that form. On the one hand, it seems to be very useful, but on the other hand, it imposes problems. One problem was discussed in [the previous post](http://blog.jetbrains.com/kotlin/2011/08/multiple-inheritance-part-1-problems-with-the-existing-design/#Problem2) under the name of <strong>Problem 2</strong>:
<p>the implementation of Left assumes it’s initialized with 3, but it may call bar() that is implemented in Right and assumes everything is initialized with 4. This may cause some inconsistent behavior.</p>
Another problem is that having state in a unit of inheritance (a class or trait or mixin) implies having a constructor there, and constructors may have side effects, and it’s important that those come in a <strong>predictable order</strong>.
<strong>Problem 2</strong> is rather elegantly fixed by the Scala’s approach of having no parameters in the trait constructors. Unfortunately, the problem of constructor side-effects still stands: changing inheritance relations between traits (e.g. done by a library-writer) may reorder side-effects of their constructors upon creating a subclass instance (see [this comment below](#comment-110) ). And this problem seems to be inevitable no matter what approach to multiple inheritance of state we choose (I wish someone could prove me wrong here!).
All that said, I’ll explain a design we are currently considering. As mentioned above, the purpose of this text is to start a discussion, so your feedback is very welcome.
<strong>The Kotlin way (Attempt #2)</strong>
First, I would like to note that at this point, we prefer <em>conservative solutions</em>, so that we could naturally extend them later if the set of features they provide is not enough.
In short, the current design can be described as follows:

* Stateless traits: no properties with backing fields, no constructors,
* that can “require” classes to be present in the set of supertypes of a concrete class that uses the trait,
* with no automatic resolution for overriding conflicts: if a class inherits two implementations of something, it must override this something and provide its own implementation (i.e., choose from the inherited ones, or write its own from scratch, or mix the two).

So, we refrain from having multiple inheritance of state <em>for now</em>. I think it’s OK if we try it this way and consider relaxing the limitations later, <em>if there’s a real demand for that</em>.
<strong>Syntax.</strong> Now, let’s render this in some syntax. First question here is “Should we still call those stateless guys classes, or have a special term?” They differ from classes by imposing some limitations, and for now it is that they don’t have any state. If there are only classes, the user will fall into the following situation:

* Nothing tells me that this class is special, so
* I add a piece of state, and
* the compiler complains about having no constructor, so
* I simply add a constructor, and
* get errors from some other classes telling me that I broke someone’s supertype lists, so
* it takes some time before I track down the real cause of the error, which is no good.

It would be a lot better if I knew that this class bears some restrictions in the first place, so I wouldn’t make any changes blindly, and if I made a bad change, the compiler would know that I have violated a local restriction, and would complain appropriately. So, it’s better to have traits differ syntactically from unrestricted classes. So, let’s have a keyword <strong>trait</strong> in front of the declaration, rather than <strong>class</strong><sup><a href="#Footnote1">1</a></sup>.
So, we have classes (state and all, but single inheritance) and traits (no state, no constructor, but multiple inheritance). Traits can declare (“require”, is CZ terms) one super<em>class</em>, but not initialize it:

{% raw %}
<p></p>
{% endraw %}

```kotlin
open class MyClass() {
  fun foo() { ... }
}
 
trait MyTrait : MyClass { // MyClass is not initialized
  fun bar() {
    foo() // calls foo() from MyClass
  }
}
 
class Child : MyClass(), MyTrait { // MyClass is initialized
}
 
class ChildErr : MyTrait { // ERROR: MyClass must be a supertype
}
```

{% raw %}
<p></p>
{% endraw %}

This allows traits to use members of a base class without interfering with the initialization logic.
One other syntactic issue is whether we should have a single homogenous supertype list (like in the example above) or something like Java’s “extends” and “implements” clauses, or even Scala’s “extends Class with Trait1 with Trait2 with Trait3” syntax. The idea of making things explicit speaks for some syntactic separation of a class in the supertype list, for it is privileged in some way, i.e. having something like Java’s “extends” and “implements”, at least. On the other hand, we all know this annoying case in Java, when I turn an interface into an abstract class, and have to change all those subclasses that used to <em>implement</em> the interface, and now must <em>extend</em> the class. The change that could be syntactically local becomes non-local. This is why we’re inclined to have a homogenous supertype list, as in the example above.
<strong>Using traits</strong>
Now, we prohibit state in traits. It certainly is a significant limitation, but I would like to point out what it is not.
<strong>You CAN have properties in your traits.</strong> The limitation is that those properties can not have backing fields or initializers, but properties themselves may appear in traits:

{% raw %}
<p></p>
{% endraw %}

```kotlin
trait Trait {
  val property : Int // abstract
 
  fun foo() {
    print(property)
  }
}
 
class C() : Trait {
  override val property : Int = 239
}
```

{% raw %}
<p></p>
{% endraw %}

Our trait declares an <strong>abstract</strong> property, and the class overrides it with a stateful one. Now, the trait can use the property, and by late binding of calls, if we call foo() on an object of C, we get 239 printed.
<strong>You CAN access state in your traits.</strong> The previous example shows how you can do it sort of indirectly, by making subclasses override a property you define, but there is another way. Remember that a trait may declare (require) a superclass:

{% raw %}
<p></p>
{% endraw %}

```kotlin
open class A(x : Int) {
  val y = x * 2
}
 
trait B : A {
  fun foo() {
    print(y)
  }
}
 
class C() : A(239), B {}
```

{% raw %}
<p></p>
{% endraw %}

In this example, we have a base class A, that defines a concrete property y and initializes it. The trait B extends this class, but does not pass a constructor parameter in, because traits have no initialization code at all. Note that B has access to the property y defined in A. Now, class C extends A and initializes it with 239, and extends B. Extending B is OK because B requires A, and we extend A, all right.<br/>
Now, what happens when we call foo() on an instance of C? It prints 478 (239 * 2), because the value of y is obtained from this instance, and the constructor of C has written 239 there.
Now, let’s look at the last example about traits:
<strong>How to resolve overriding conflicts.</strong> When we declare many types in out supertype list, it may appear that we inherit more than one implementation of the same method. For example:

{% raw %}
<p></p>
{% endraw %}

```kotlin
trait A {
  fun foo() { print("A") }
  fun bar()
}
 
trait B {
  fun foo() {print("B")}
  fun bar() {print("bar")}
}
 
class C() : A {
  override fun bar() { print("bar") }
}
 
class D() : A, B {
  override fun foo() {
    super<A>.foo()
    super<B>.foo()
  }
}
```

{% raw %}
<p></p>
{% endraw %}

Traits A and B both declare functions foo() and bar(). Both of them implement foo(), but only B implements bar() (bar() is not marked <strong>abstract</strong> in A, because this is the default for traits, if the function has no body). Now, if we derive a concrete class C from A, we, obviously, have to override bar() and provide an implementation. And if we derive D from A and B, we don’t have to override bar(), because we have inherited only one implementation of it. But we have inherited <em>two</em> implementations of foo(), so the compiler does not know, which one to choose, and forces us to override foo() and say what we want explicitly.
I think, it’s enough for today. Your comments are very welcome, as usual.
<strong>References</strong>

0. Nathanael Shärli, Stéphane Ducasse, Oscar Nierstrasz, and Andrew Black. Traits: Composable Units of Behavior. ECOOP-2003, pdf preprint.
1. Donna Malayeri and Jonathan Aldrich. CZ: multiple inheritance without diamonds. SIGPLAN Not. 44, 10 (October 2009), 21-40, a pdf preprint.


{% raw %}
<hr/>
{% endraw %}

1 Earlier this post used to say the following:
<p>One good way to do it is to have a qualifier on a class declaration, i.e. <strong>trait class</strong> instead of just <strong>class</strong> (we could say just <strong>trait</strong>, but there are some language extensibility considerations against it, which I do not want to dive into now).</p>
But we have found a simple solution to our language extensibility problem, and the problem does not stand any more.
