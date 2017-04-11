---
title: Multiple Inheritance Part 2: Possible directions
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
---

In the previous post in this series we discussed the disadvantages of the inheritance model we initially planned for Kotlin. Today we will talk about alternative designs.
Note that these posts are intended to provoke a discussion, so that we can benefit from your feedback and come up with a better design.
What’s out there
The previous post concluded with the following (incomplete) list of solutions to the problem of multiple inheritance available in other languages:

* Java and C# have classes and interfaces, i.e. multiple interface inheritance and single implementation inheritance;
* Scala has classes and traits that may implement methods and even have state, but their constructors can not have parameters;
* Some other languages, like Fortress, do not allow state in traits;
* <Your favorite language here>

We all know that Java’s approach is rock-solid, but imposes severe limitations on code reuse, so we would like to relax these limitations, but without getting ourselves into trouble. “First degree” of relaxing the limitations would be stateless traits (like in Fortress, and in [1]): no state in traits, no implicit overrides. Or we can trade inheritance of traits off for state and get mixins (like in Ruby). Relaxing the limitations even more we get to Scala’s traits that have state but no parameters for constructors, and one trait may override functions of another. Then we get to CZ’s classes with requires (as presented in [2]). The next step, I guess, would already be unrestricted multiple inheritance, like in C++.
We will skip a thorough analysis of each of these solutions, and just make a remark about state.

State. One important consideration is whether to allow multiple inheritance of state in this or that form. On the one hand, it seems to be very useful, but on the other hand, it imposes problems. One problem was discussed in the previous post under the name of Problem 2:
the implementation of Left assumes it’s initialized with 3, but it may call bar() that is implemented in Right and assumes everything is initialized with 4. This may cause some inconsistent behavior.
Another problem is that having state in a unit of inheritance (a class or trait or mixin) implies having a constructor there, and constructors may have side effects, and it’s important that those come in a predictable order.
Problem 2 is rather elegantly fixed by the Scala’s approach of having no parameters in the trait constructors. Unfortunately, the problem of constructor side-effects still stands: changing inheritance relations between traits (e.g. done by a library-writer) may reorder side-effects of their constructors upon creating a subclass instance (see this comment below). And this problem seems to be inevitable no matter what approach to multiple inheritance of state we choose (I wish someone could prove me wrong here!).
All that said, I’ll explain a design we are currently considering. As mentioned above, the purpose of this text is to start a discussion, so your feedback is very welcome.
The Kotlin way (Attempt #2)
First, I would like to note that at this point, we prefer conservative solutions, so that we could naturally extend them later if the set of features they provide is not enough.
In short, the current design can be described as follows:

* Stateless traits: no properties with backing fields, no constructors,
* that can “require” classes to be present in the set of supertypes of a concrete class that uses the trait,
* with no automatic resolution for overriding conflicts: if a class inherits two implementations of something, it must override this something and provide its own implementation (i.e., choose from the inherited ones, or write its own from scratch, or mix the two).

So, we refrain from having multiple inheritance of state for now. I think it’s OK if we try it this way and consider relaxing the limitations later, if there’s a real demand for that.
Syntax. Now, let’s render this in some syntax. First question here is “Should we still call those stateless guys classes, or have a special term?” They differ from classes by imposing some limitations, and for now it is that they don’t have any state. If there are only classes, the user will fall into the following situation:

* Nothing tells me that this class is special, so
* I add a piece of state, and
* the compiler complains about having no constructor, so
* I simply add a constructor, and
* get errors from some other classes telling me that I broke someone’s supertype lists, so
* it takes some time before I track down the real cause of the error, which is no good.

It would be a lot better if I knew that this class bears some restrictions in the first place, so I wouldn’t make any changes blindly, and if I made a bad change, the compiler would know that I have violated a local restriction, and would complain appropriately. So, it’s better to have traits differ syntactically from unrestricted classes. So, let’s have a keyword trait in front of the declaration, rather than class1.
So, we have classes (state and all, but single inheritance) and traits (no state, no constructor, but multiple inheritance). Traits can declare (“require”, is CZ terms) one superclass, but not initialize it:

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
One other syntactic issue is whether we should have a single homogenous supertype list (like in the example above) or something like Java’s “extends” and “implements” clauses, or even Scala’s “extends Class with Trait1 with Trait2 with Trait3” syntax. The idea of making things explicit speaks for some syntactic separation of a class in the supertype list, for it is privileged in some way, i.e. having something like Java’s “extends” and “implements”, at least. On the other hand, we all know this annoying case in Java, when I turn an interface into an abstract class, and have to change all those subclasses that used to implement the interface, and now must extend the class. The change that could be syntactically local becomes non-local. This is why we’re inclined to have a homogenous supertype list, as in the example above.
Using traits
Now, we prohibit state in traits. It certainly is a significant limitation, but I would like to point out what it is not.
You CAN have properties in your traits. The limitation is that those properties can not have backing fields or initializers, but properties themselves may appear in traits:

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

Our trait declares an abstract property, and the class overrides it with a stateful one. Now, the trait can use the property, and by late binding of calls, if we call foo() on an object of C, we get 239 printed.
You CAN access state in your traits. The previous example shows how you can do it sort of indirectly, by making subclasses override a property you define, but there is another way. Remember that a trait may declare (require) a superclass:

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

In this example, we have a base class A, that defines a concrete property y and initializes it. The trait B extends this class, but does not pass a constructor parameter in, because traits have no initialization code at all. Note that B has access to the property y defined in A. Now, class C extends A and initializes it with 239, and extends B. Extending B is OK because B requires A, and we extend A, all right.
Now, what happens when we call foo() on an instance of C? It prints 478 (239 * 2), because the value of y is obtained from this instance, and the constructor of C has written 239 there.
Now, let’s look at the last example about traits:
How to resolve overriding conflicts. When we declare many types in out supertype list, it may appear that we inherit more than one implementation of the same method. For example:

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

Traits A and B both declare functions foo() and bar(). Both of them implement foo(), but only B implements bar() (bar() is not marked abstract in A, because this is the default for traits, if the function has no body). Now, if we derive a concrete class C from A, we, obviously, have to override bar() and provide an implementation. And if we derive D from A and B, we don’t have to override bar(), because we have inherited only one implementation of it. But we have inherited two implementations of foo(), so the compiler does not know, which one to choose, and forces us to override foo() and say what we want explicitly.
I think, it’s enough for today. Your comments are very welcome, as usual.
References

0. Nathanael Shärli, Stéphane Ducasse, Oscar Nierstrasz, and Andrew Black. Traits: Composable Units of Behavior. ECOOP-2003, pdf preprint.
1. Donna Malayeri and Jonathan Aldrich. CZ: multiple inheritance without diamonds. SIGPLAN Not. 44, 10 (October 2009), 21-40, a pdf preprint.


{% raw %}
<hr/>
{% endraw %}

1 Earlier this post used to say the following:
One good way to do it is to have a qualifier on a class declaration, i.e. trait class instead of just class (we could say just trait, but there are some language extensibility considerations against it, which I do not want to dive into now).
But we have found a simple solution to our language extensibility problem, and the problem does not stand any more.
