---
title: "Kotlin M11 is Out!"
date: 2015-03-19 17:27:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/03/kotlin-m11-is-out/
translator:
translator_url:
---

Today we are releasing a new milestone: Kotlin M11, which brings such long-awaited features as <strong>secondary constructors</strong>, a first glimpse of true <strong>reflection</strong> support for Kotlin and much more. <span id="more-1836"></span>
## Language Changes

M11 brings quite a few language changes, some of which are breaking changes and/or deprecation of old ways of doing things in favor of new ones. Some of your code may break, but we’ve done our best to make your transition path as smooth as possible.
### Multiple Constructors

This feature has been most awaited by Android developers, because subclassing standard view classes on Android requires having more than one constructor. Now you can do that:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class MyView : View {
    constructor(context: Context, attrs: AttributeSet, defStyle: Int) : super(context, attrs, defStyle) {
        // ...
    }
 
    constructor(context: Context, attrs: AttributeSet) : this(context, attrs, 0) {}
}
 
```

{% raw %}
<p></p>
{% endraw %}

Please refer to the [user docs](http://kotlinlang.org/docs/reference/classes.html#constructors) and the [spec document](https://github.com/JetBrains/kotlin/blob/master/spec-docs/secondary-constructors.md) for more details.
### Prefixes For Initializer Blocks

Another change, also related to constructors, is prefixing initializer blocks with the soft-keyword <code>init</code>.<br/>
The main reason for this change is that the formerly used syntax (where just curly braces in a class body denoted an initializer block) didn’t work out too well when an initializer followed a property declaration (which is pretty common):

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Foo {
    val bar = baz() // ERROR here
 
    {
        // pre-M11 initializer
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

An error was reported on the call of <code>baz()</code>, because the initializer looks exactly like a trailing lambda passed to it. The only workaround was to put a semicolon after the property initializer, which looks rather unnatural in Kotlin. So, since M11, we require <code>init</code> before the initializer block:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Foo {
    val bar = baz()
 
    init {
        // initializer
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

The old syntax is <strong>deprecated</strong>, i.e. you’ll get a warning, not an error. Also, the IDE provides an Alt+Enter quick-fix action to convert the old syntax to the new one, which has an option to bulk update the whole project.
See [user docs](http://kotlinlang.org/docs/reference/classes.html#constructors) for more details.
### Companion Objects (Class-Objects Rethought)

As you all probably know, Kotlin classes do not have static members. Instead there may be a special singleton <code>object</code> associated with a class, which we used to call “class object” &dash; a rather unfortunate term. So, we somewhat redesigned the concept, and, [with your help](http://blog.jetbrains.com/kotlin/2015/03/follw-up-new-class-object-syntax/) , chose another name for it: <strong>companion object</strong>.
The unfortunate wording was not the only reason for this change. In fact, we redesigned the concept so that it is more uniform with normal objects.
Note that a class can (and always could) have many objects (usual, named singletons) nested into it:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class KotlinClass {
    object Obj1 { ... }
    object Obj2 { ... }
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

Since M11, one of these objects may be declared with the <code>companion</code> modifier, which means that its members can be accessed directly through class name:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class KotlinClass {
    object Obj1 { ... }
    companion object Obj2 { ... }
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

Accessing members of <code>Obj1</code> requires qualification: <code>KotlinClass.Obj1.foo()</code>. For members of <code>Obj2</code> the object name is optional: <code>KotlinClass.foo()</code>.
One last step: the name of a <em>companion object</em> can be omitted (the compiler will use the default name <code>Companion</code> in this case):

{% raw %}
<p></p>
{% endraw %}

```kotlin
class KotlinClass {
    object Obj1 { ... }
    companion object { ... }
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

Now you can still refer to its members though the name of the containing class: <code>KotlinClass.foo()</code>, or through full qualification: <code>KotlinClass.Companion.foo()</code>.
As you can see, unlike what we used to have with <em>class objects</em>, <em>companion objects</em> are completely uniform with normal objects.
Another important benefit is that now every object <em>has a name</em> (again, <code>Companion</code> is used when the name of a <em>companion object</em> is omitted), which enables <strong>writing extension function for companion objects</strong>:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun KotlinClass.Companion.bar() { ... }
 
```

{% raw %}
<p></p>
{% endraw %}

See user docs [here](http://kotlinlang.org/docs/reference/object-declarations.html#companion-objects) .
### Function Expressions

Kotlin has higher-order functions, which means that you can pass a function around as a value. Before M11, there were two ways of obtaining such values: lambda expressions (e.g. <code>{ x -&gt; x + 1 }</code>) and callable references (e.g. <code>MyClass::myFun</code>). M11 introduces a new one, which is very logical, if you think about it:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val f = fun (x: Int): Int { return x + 1 }
 
```

{% raw %}
<p></p>
{% endraw %}

So, you can use a function, in its traditional syntactic form, as a value. See [user docs](http://kotlinlang.org/docs/reference/lambdas.html#function-expressions) and the [spec document](https://github.com/JetBrains/kotlin/blob/master/spec-docs/multi-declarations-in-parameters.md#function-expressions) for more details.
### Lambda Syntax Restricted (for future enrichment)

Among other things, function expressions enable us to make a step toward supporting <em>multi-declarations</em> in parameters of lambdas. The final goal (not implemented yet) is to be able to, say, filter a list of pairs with the syntax like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
pairs.filter { (a, b) -> a != b }
 
```

{% raw %}
<p></p>
{% endraw %}

Here, <code>(a, b)</code> is a [multi-declaration](http://kotlinlang.org/docs/reference/multi-declarations.html) , i.e. <code>a</code> gets the first component of each <code>Pair</code> object, and <code>b</code> gets the second one. Currently, multi-declarations are not supported, but we deprecated some of the syntactic forms of lambdas to drop them in M12 and make the multi-declaration syntax possible.
What is deprecated:

* specifying return types of lambdas, e.g. { (a: Int): Int -> a + 1 }
* specifying receiver types of lambdas: { Int.(a: Int) -> this + a }
* using parentheses around parameter names of lambdas: { (a, b) -> a + b }

Whenever you really need one of these, please switch to using function expressions instead.
The IDE provides a quick-fix that migrates your code automatically.
### Labeled Returns in Lambdas

For a long time there was a restriction on using <code>return</code> expressions in lambdas: a <em>local</em> <code>return</code> was only allowed if the lambda has an explicit return type specified. This was caused by a limitation in the type inference algorithm. Now, the restriction is removed, and we can use local returns freely:

{% raw %}
<p></p>
{% endraw %}

```kotlin
list.map {
    if (it < 10) return@map DEFAULT
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

### Import Semantics Changed

Importing is one of the least-visible language features for IDE users, but it has a great influence on how tools work, and occasionally on the users, too.<br/>
In M11 we made the order of *-imports (also called “on-demand imports”) insignificant, and made some other tweaks that enabled us to implement efficient automatic management of import directives in the IDE.
## Reflection

Implementing Kotlin-specific reflection (rather than making you use Java reflection on Kotlin classes) is a long-running project that has required a lot of work in the compiler. Essentially, we have to factor out a large portion of the compiler and ship it as part of the runtime. This includes: loading Kotlin-specific metadata from the binaries, representing Kotlin symbols as objects (historically, we call them <em>descriptors</em>), loading Java declarations as Kotlin ones (because Kotlin reflection should work on Java objects too) and so on.
At last, we present the first results of this work: the ability to introspect properties, provided through a new kotlin-reflect.jar that ships with the compiler (a lot more functionality will be added soon).
### The New Reflection Jar

We ship <code>kotlin-reflect.jar</code> separately (not as part of <code>kotlin-runtime.jar</code>), because it is rather big at the moment: about 1.8MB. We will look into reducing its size, but it is likely to always be rather substantial, so making everyone always ship it with their applications is not an option (especially for Android developers).
As a consequence, you may need to add this jar to your classpath, if you use property literals (<code>::propertyName</code>). The M11 compiler will yield an error if you don’t, but later this requirement will be relaxed. The IDE will offer you a quick-fix action that adds the jar automatically to your project.
### Class Literals

To obtain a reflection object for a class in Kotlin, use the following syntax:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val c = MyClass::class
 
```

{% raw %}
<p></p>
{% endraw %}

You get an instance of <code>KClass&lt;MyClass&gt;</code>, which you can introspect, e.g. get its properties.
See more in the [user docs](http://kotlinlang.org/docs/reference/reflection.html#class-references) .
### Compatibility with Java Reflection APIs

Kotlin reflection API works both for Kotlin and Java classes, and you can “convert” from Kotlin to Java reflection objects and back. For example, you can say <code>kClass.java</code> and get a <code>java.lang.Class</code> instance, and vice versa: <code>jlClass.kotlin</code> gives you a <code>KClass</code> instance.
## @Nullable and @NotNull in Java

As always, Java interop is a big priority for us, and this time we are improving on the <em>platform types</em> feature we shipped in [M9](http://blog.jetbrains.com/kotlin/2014/10/m9-is-here/) : now the compiler issues warnings on misuse of Java values annotated as <code>@Nullable</code> and <code>@NotNull</code>. This is not as strict as it used to be before M9, but it doesn’t break as often either.
Next step would be to issue Java nullability errors in a safe way (so that an error can always be fixed reasonably), and this is planned for the next milestone.
## Android Extensions

Good news for Android users: M11 brings a useful extension that makes Android development in Kotlin easier.
We all know about <code>findViewById()</code>. It is a notorious source of bugs and unpleasant code which is hard to read and support. In Java the way around this problem is through libraries such as [ButterKnife](http://jakewharton.github.io/butterknife/) and [AndroidAnnotations](http://androidannotations.org) , which rely on [JSR 269](https://jcp.org/aboutJava/communityprocess/mrel/jsr269/index2.html) , but it is a <code>javac</code>-specific API and is not supported in Kotlin (yet).
Since M11, Kotlin has its own solution to the <code>findViewById()</code> problem, which does not require JSR 269: the new <code>kotlin-android-extensions</code> plugin for the Kotlin compiler allows you to access views in a type-safe way with <strong>zero</strong> extra user code (no annotations or other such things) and <strong>no runtime libraries required</strong>.
To use this extension, you need to enable it in your Gradle build and install an extension plugin into your IDE. See more [here](http://kotlinlang.org/docs/tutorials/android-plugin.html) .
## IntelliJ IDEA Support

More improvements and features for IntelliJ IDEA
### Refactorings and Intentions

The following refactorings and intentions are now available:

* Introduce Property
Ability to introduce property and to define whether we want an initializer, a getter or lazy property
* Create from Usage with Java Interop
It is now possible to invoke “Create from usage” on Java types being used in Kotlin files.
* Receiver to Parameter Conversion
A special case of Change Signature refactoring, whereby a parameter can be refactored to a receiver, thus allowing
converting a function that takes a parameter of type T into an extension function of T. It also allows for the reverse, whereby a receiver can be transformed into a parameter.

