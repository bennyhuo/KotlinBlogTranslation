---
title: "M9 is here!"
date: 2014-10-15 18:38:00
author: Hadi Hariri
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2014/10/m9-is-here/
translator:
translator_url:
---

M9 has arrived and it’s bringing many new features and important changes. We’ve already [highlighted these](http://blog.jetbrains.com/kotlin/2014/10/m9-is-coming/) and [covered others in detail](http://blog.jetbrains.com/kotlin/2014/10/making-platform-interop-even-smoother/) . Let’s dig deeper into some of the other improvements.<br/>
<span id="more-1643"></span>
## Language Changes

<b>NOTE:</b> Some of the changes below are <em>breaking changes</em>, meaning that some code that was compilable with earlier versions will not compile any more, so you’ll need to correct it.
### Platform Types

As we [mentioned before](http://blog.jetbrains.com/kotlin/2014/10/making-platform-interop-even-smoother/) , platform interoperability (i.e. Java and JavaScript interoperability) is among our top priorities, because this is so for our users. <em>Nullability</em> issues when interoperating with Java were one of the biggest complaints we were getting. In a nutshell, the problem is that any reference coming from Java may be <em>null</em>, and Kotlin, being null-safe by design, forced the user to null-check every Java value, or use <em>safe calls</em> (<code>?.</code>) or <em>not-null assertions</em> (<code>!!</code>). Those being very handy features in the pure Kotlin world, tend to turn into a disaster when you have to use them too often in the Kotlin/Java setting. We relied on [external annotations](http://blog.jetbrains.com/kotlin/using-external-annotations) and [KAnnotator](http://blog.jetbrains.com/kotlin/2013/03/kannotator-0-1-is-out/) to mitigate this problem by enhancing Java with extra type information. This approach proves to be too cumbersome and doesn’t work for some cases.
This is why we took a radical approach and made Kotlin’s type system more relaxed when is comes to Java interop: now references coming from Java have specially marked types (we call them “platform types”, because they come from the underlying platform), which are treated specially:

* Kotlin does not enforce null-safety for platfrom types. I.e. for Java values you get Java’s semantics: NPE is now possible for values coming from Java






val s = javaMethod() // s has a platform type
s.foo() // this line may throw NPE, like in Java




12

val s = javaMethod() // s has a platform types.foo() // this line may throw NPE, like in Java
* Platform types can not be mentioned explicitly in Kotlin code, but when the IDE/Compiler shows you type information, they are distinguished by exclamation marks at the end. Examples: String!, ArrayList<Int!>!, (Mutable)Collection<Foo!>!.
* To store platform values, you can either rely on the type inference, or pick Kotlin types (either nullable or not, as you please):






val s = javaMethod() // platform type inferred
val s1: String = javaMethod() // not-null type chosen by the programmer
val s2: String? = javaMethod() // nullable type chosen by the programmer




123

val s = javaMethod() // platform type inferredval s1: String = javaMethod() // not-null type chosen by the programmerval s2: String? = javaMethod() // nullable type chosen by the programmer





When you assign a platform value to a non-null type, Kotlin emits assertions in the byte code so that to make sure that a non-null variable doesn’t hold a null, this keeps most nulls from propagating through the code. So, there may be an assertion error on line 2 in this example, instead of an NPE some time later.
* When you override Java methods, again, you can not mention platform types, so you have to pick some Kotlin types instead:

