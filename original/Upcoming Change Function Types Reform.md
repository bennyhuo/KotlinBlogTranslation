---
title: "Upcoming Change: Function Types Reform"
date: 2015-04-09 14:26:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/04/upcoming-change-function-types-reform/
translator:
translator_url:
---

Kotlin M12 will likely bring another change that is crucial for implementing a useful reflection library for Kotlin. In short, we are going to unify `FunctionX` and `ExtensionFunctionX` to be represented in the same way at runtime, but it will not affect our ability to create [type-safe builders](http://kotlinlang.org/docs/reference/type-safe-builders.html) and other DSL-like constructs.<span id="more-2062"></span>
## Why

Currently, there are 23*2 = 46 class files related to `FunctionX` in the `kotlin` package `kotlin-runtime.jar` and 46 more class files related to `ExtensionFunctionX` (`X` being a number between 0 and 22). This is a lot of class files already, but there are 46*3 = 138 more class files in the `kotlin.reflect` package (`KFunctionX`, `KMemberFunctionX`, `KExtensionFunctionX`), which is way over the top <img alt=":)" class="wp-smiley" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1" style="height: 1em; max-height: 1em;"/>
So, for one thing, we really need to **reduce the number of class files** in `kotlin-runtime.jar`.
Then, at the moment `ExtensionFunctionX` types are not related to `FunctionX` types, and we can not say `listOfStrings.map(String::length)`, because the argument has type `String.() -&gt; Int`, but `map()` expects `(String) -&gt; Int`, which is sad, annoying and inconvenient.
So, we want to make extension functions **coercible to normal functions** (with an extra parameter).
While we are at it, we would also like to **allow functions with more than 22 parameters**, theoretically any number of parameters (in practice 255 on JVM).
An important constraint here is that **implementing Kotlin functions in Java** must remain easy: Java 8 lambdas should work and in earlier versions of Java `new Function2() { ... }` with only `invoke()` method in the body should be enough.
## How

All 230 function class files will be replaced by a single interface [Function](https://github.com/JetBrains/kotlin/blob/spec-function-types/spec-docs/function-types.md#function-trait) which will represent all functions at runtime (+ we will keep 23 interfaces `kotlin.jvm.FunctionX` to facilitate easy creation of Kotlin functions in Java). A total win of over 200 class files.
Now, function values (“`(A) -&gt; B`“) and extension function values (“`A.() -&gt; B`“) will be represented by the same type at runtime, which will allow using them almost interchangeably. The static type system will only distinguish arities (e.g. the compiler will create fictitious “classes” `FunctionX` for any X, which will exist at compile time only and will never be emitted as class files).
Since the compile-time types will not be exactly the same as runtime types, several tweaks in operators like `is` and `as` are required, but they will not affect the cases that are not statically known to involve function types.
The <em>syntactic distinction</em> between function- and extension function types will be preserved (through desugaring `A.() -&gt; B` to an annotated function type): when a lambda is type-checked against an expected type which is an extension function, type inference adds a `this`-receiver to its signature, and for a normal function it adds a parameter instead:

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Normal function:
fun call(callback: (Foo) -> Unit) { // callback has type `Function1<Foo, Unit>
    ...
}
 
// argument is a lambda with a normal parameter
call { foo -> println(foo) }
 
// Extension function
fun builder(body: Foo.() -> Unit) { // body has type `@extension Function1<Foo, Unit>`
  ...
}
 
// argument is an extension lambda: no parameters, but `this` is available
builder {
    this.bar() // `this` has type Foo
}
```

{% raw %}
<p></p>
{% endraw %}

## Consequences

These changes will make reflection on functions possible (i.e. `KClass` will finally have `getFunctions()`), and using function objects will be more intuitive.
**You won’t need to change anything in your code** unless you referenced `ExtensionFunctionX` types directly (by saying, e.g. `ExtensionFucntion0&lt;Foo, Unit&gt;`).
For more details, see this [spec document](https://github.com/JetBrains/kotlin/pull/636/files) (you can comment on the source, or press “View” for rendered markdown).
