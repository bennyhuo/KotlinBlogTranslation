---
title: "Kotlin 1.0 Beta Candidate is Out!"
date: 2015-10-22 16:54:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/10/kotlin-1-0-beta-candidate-is-out/
---

We are happy to present Kotlin <strong>Beta Candidate</strong>. An official 1.0 Beta will be out soon. By now, the binary format is finalized, no major language changes are planned, and only a few changes in the standard library are coming.
In this post we describe the changes since M14, including

* imports from objects,
* new safer collection interfaces,
* inlining for Java constants,
* better support for Java statics,
* and more.

## Language changes

We are rolling out some breaking changes along with new important features.
### Operators and infix functions

Since M14, Kotlin requires the <code>operator</code> modifier on functions that are used for operator overloading. From now on the same is required for infix functions:

{% raw %}
<p></p>
{% endraw %}

```kotlin
operator Foo.plus(other: Foo): Foo { ... }
 
fun testPlus() = Foo() + Foo()
 
infix fun Foo.bar(other: Foo): Foo { ... }
 
fun testInfix() = Foo() bar Foo()
 
```

{% raw %}
<p></p>
{% endraw %}

Now, we have relaxed this requirement for Java functions: <strong>any Java function with a suitable signature can be used as an operator</strong>, but not as infix.
Some operator names have been changed to avoid ambiguities:

* we should now use unaryPlus and unaryMinus instead of just plus and minus for unary functions, i.e. -Foo() is now Foo().unaryMinus();
* for delegated properties, getValue and setValue should be used instead of just get and set.

The <em>Code cleanup</em> action will help you migrate your code.
Also, operator signatures are now checked by the compiler at the declaration site. Some of these checks may be relaxed in the future, but we believe that what we have now is a pretty good starting point.
### Imports from objects

Kotlin now supports importing individual members of objects by name (but not <code>*</code>-imports from objects):

{% raw %}
<p></p>
{% endraw %}

```kotlin
import mypackage.MyObject.foo
 
val test = foo("...")
 
```

{% raw %}
<p></p>
{% endraw %}

In this example we imported all members named <code>foo</code> from the named object <code>mypackage.MyObject</code>.
To import from companion objects of classes, we have to specify their full name:

{% raw %}
<p></p>
{% endraw %}

```kotlin
import mypackage.MyClass.Companion.foo
 
```

{% raw %}
<p></p>
{% endraw %}

### Rich @Deprecated

We have been migrating a lot of code lately <img alt=":)" class="wp-smiley" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1" style="height: 1em; max-height: 1em;"/> So Kotlin’s <code>@Deprecated</code> annotation has become really powerful: not only does it require a message and allow to specify a replacement through <code>ReplaceWith("...")</code>, it also has a <code>level</code> now: <code>WARNING</code>, <code>ERROR</code> or <code>HIDDEN</code>.

* WARNING is default and works as a normal deprecation: there will be warnings at call sites, and the IDE will strike it out,
* ERROR is the same, but a compilation error is reported instead of a warning,
* HIDDEN is what previously was @HiddenDeclaration: it simply makes this declaration invisible to clients at compile time.

### Smart casts for captured local var’s

Smart casts now work even on local <code>var</code>‘s that are captured in lambdas, if they are not mutated in those lambdas:

{% raw %}
<p></p>
{% endraw %}

```kotlin
var a: Any? = ...
 
val mapped = users.map {
    "${it.name}: $a"
}
 
if (a is String) {
    println(a.length) // This works now
}
 
```

{% raw %}
<p></p>
{% endraw %}

### Multiple main() functions in the same package

We can now define a <code>main()</code> function with standard signature in each file (with the exception of <code>@file:JvmMultileClass</code>). This is very useful when experimenting with code:

{% raw %}
<p></p>
{% endraw %}

```kotlin
// FILE: a.kt
package foo
 
fun main(args: Array<String>) {
    println("a.kt")
}
 
// FILE: b.kt
package foo
 
fun main(args: Array<String>) {
    println("b.kt")
}
 
```

{% raw %}
<p></p>
{% endraw %}

### Varargs and spread operator

To recap: when calling a <code>vararg</code> function, we can use the  [spread operator](https://kotlinlang.org/docs/reference/functions.html#variable-number-of-arguments-varargs)  that converts an array to a vararg:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun foo(vararg args: String) { ... }
 
fun bar(vararg args: String) {
    foo(*args) // spread operator
}
 
```

{% raw %}
<p></p>
{% endraw %}

The semantics of the <em>spread operator</em> have been fixed so that it always guarantees that an array that <code>foo</code> sees will not be modified or observed by the “outside world”. We can assume that a defensive copy is made every time the spread operator is used (in fact, some optimizations may be implemented later to reduce memory traffic).
As a result, authors of Kotlin libraries can rely on the vararg arrays being safe to store without defensive copying.<br/>
<strong>NOTE</strong>: This guarantee is not fulfilled when Kotlin functions are called from java, because no spread operators are used there. This means that if a function is intended to be used from both Java and Kotlin, its contract for Java clients should include a note that the array should be copied before being passed to it.
### “sparam” annotation target has been renamed to “setparam”

To annotate a setter parameter of a property, use <code>setparam</code> use-site target instead of <code>sparam</code>:

{% raw %}
<p></p>
{% endraw %}

```kotlin
@setparam:Inject
var foo: Foo = ...
 
```

{% raw %}
<p></p>
{% endraw %}

### @UnsafeVariance annotation

Sometimes we need to suppress  [declaration-site variance checks](https://kotlinlang.org/docs/reference/generics.html#declaration-site-variance)  in our classes. For example, to make <code>Set.contains</code> typesafe while keeping read-only sets co-variant, we had to do it:

{% raw %}
<p></p>
{% endraw %}

```kotlin
interface Set<out E> : Collection<E> {
    fun contains(element: @UnsafeVariance E): Boolean
}
 
```

{% raw %}
<p></p>
{% endraw %}

This puts some responsibility on the implementor of <code>contains</code>, because with this check suppressed the actual type of <code>element</code> may be anything at all at runtime, but it’s sometimes necessary to achieve convenient signatures. See more on the type-safety of collections below.
So, we introduced the <code>@UnsafeVariance</code> annotation on types for this purpose. It’s been deliberately made long and stands out to warn agains abusing it.
### Miscellaneous checks and restrictions

Many checks were added, some of these restrictions may be lifted later.
<strong>Type parameter declarations</strong>. We decided to restrict the syntax of type parameter declarations so that all such declarations are consistent, so

* fun foo<T>() is deprecated in favor of fun <T> foo():
* All constraints on type parameters should occur either in “where” or inside “<…>”:


{% raw %}
<p></p>
{% endraw %}

```kotlin
fun <T: Any> foo() {} // OK
fun <T> foo() where T: Serializable, T: Comparable<T> {} // OK
 
fun <T: Serializable> foo() where T: Comparable<T> {} // Forbidden
 
```

{% raw %}
<p></p>
{% endraw %}

<strong>Dynamic type checks for arrays</strong>. Array element types are reified in Java, but their Kotlin-specific properties, like nullability, is not. So, we removed the special treatment of arrays that allowed checks like <code>a is Array&lt;String&gt;</code>, and now arrays work as all other generic classes: we can check for <code>a is Array&lt;*&gt;</code> and a cast like <code>a as Array&lt;String&gt;</code> is marked as unchecked. We added a JVM-specific function <code>isArrayOf&lt;T&gt;()</code> that check that a given array can contain elements of type <code>T</code> <em>in Java</em>:

{% raw %}
<p></p>
{% endraw %}

```kotlin
    val a: Any? = ...
 
    if (a is Array<*> && a.isArrayOf<String>()) {
        println((a as Array<String>)[0])
    }
 
```

{% raw %}
<p></p>
{% endraw %}

<strong>Delegated properties</strong>. The conventions for delegated properties now use <code>KProperty&lt;*&gt;</code> instead of <code>PropertyMetadata</code> in <code>getValue</code> and <code>setValue</code>:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun Foo.getValue(thisRef: Bar, property: KProperty<*>): Baz? {
    return myMap[property.name]
}
 
```

{% raw %}
<p></p>
{% endraw %}

<em>Code cleanup</em> will help you migrate.
<strong>Callable references</strong>. Some usages of <code>::</code> are forbidden for now, to be enabled later when we implement bound references. Most notably, <code>::foo</code> should not be used for now when <code>foo</code> is a member of a class. Only <code>MyClass::foo</code> should be used. References to members of objects are also unsupported temporarily (they will work as bound references too). We can use lambdas as a workaround for the time being.
<strong>If-expressions</strong>. We unified the semantics of <code>if</code> and <code>when</code> by requiring an <code>else</code> when <code>if</code> is used as an expression:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val foo = if (cond) bar // ERROR: else is required
 
```

{% raw %}
<p></p>
{% endraw %}

<strong>Nothing-returning functions</strong>. When a function is known to throw an exception or loop forever, it’s return type may be <code>Nothing</code>, which means that it never returns normally. To make the tooling smarter, we require that such functions always have their return type specified explicitly:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun foo() = throw MyException() // Must specify return type explicitly
 
fun bar(): Nothing = throw MyException() // OK
fun baz() { throw MyExcepion() } // OK
fun goo(): Goo { throw MyExcepion() } // OK
 
```

{% raw %}
<p></p>
{% endraw %}

This is now a warning that will be promoted to error after we migrate our code with <em>Code cleanup</em>
<strong>Visibility checks</strong> were restricted so that, for example, a public declaration can not expose a local, private or internal type. Access to internal declarations is checked in the compiler as well as in the IDE;
See more  [here](https://github.com/JetBrains/kotlin/releases/tag/build-1.0.0-beta-1038) .
## Collections

The major change in this version is that we have cleaned up collections and other core APIs so that, for example, <code>size</code> is now a property, and <code>contains</code> is type-safe: it takes <code>E</code> instead of <code>Any?</code>. This has been a major effort to make the library feel like Kotlin while keeping it compatible with Java. There’s quite some compiler magic behind it, but we are pleased with the result.
Example:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val strs = setOf("1", "abc")
 
if (1 in strs) { // 'strs' is a set of strings, can't contain an Int
    println("No!")
}
 
```

{% raw %}
<p></p>
{% endraw %}

Analogous code works in Java, because <code>Set&lt;E&gt;.contains</code> (which <code>in</code> is compiled to) takes <code>Object</code>, not <code>E</code>, the element type of the set. This has proven to be error-prone, so we decided to make Kotlin collection interfaces safer (while keeping full compatibility with Java collections). As a result, our <code>contains</code> takes an <code>E</code>, and the example above is incorrect in Kotlin.
At the moment the Kotlin compiler reports a deprecation warning on <code>in</code> in the example above, because we have provided transitional extension functions in the standard library to help everyone migrate, but soon this will be an error. <em>Code cleanup</em> is our friend here: it will replace <code>1 in strs</code> with <code>strs.containsRaw(1)</code>. <code>containsRaw</code> is a new function in the standard library that we can use when we <em>really need</em> the Java-like behavior: we can check membership of any object in any set by using <code>containsRaw</code>.
Bottomline:

* Collection.contains, Map.get and some other collection methods are now safer;
* We can use containsRaw, getRaw, etc to get the untyped behavior;
* Collection.size, Array.size, String.length, Map.Entry.key etc are now properties;
* List.remove(Int) has been renamed to removeAt(int) to avoid clashes with List<Int>.remove that removes by item, not by index;
* Code cleanup will migrate all the code.

All normal Java collections work without changes: the compiler knows how to find a “property” <code>size</code> on a <code>java.util.ArrayList</code>.
## Java interop

There have been many important changes that concern how Kotlin declarations are visible from Java and vice versa.
### Inlining constants defined in libraries

From now on we inline Java constants (public static final fields of primitive and String types) that come from libraries. This will help Android developers that have been suffering from API incompatibilities:

{% raw %}
<p></p>
{% endraw %}

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) { ... }
 
```

{% raw %}
<p></p>
{% endraw %}

Will now work on any version on Android runtime (used to crash on runtimes younger than Lollipop).
### Smaller runtime

We are only starting there, but the foundation has been laid for the work on reducing the size of the <code>kotlin-runtime</code> library. It is now only 200K smaller than it was in M14, but there are more things we’ll do to make it smaller (and it won’t break compatibility).
### Static methods, fields and classes

Kotlin is now very friendly to Java statics:

* we can use inherited nested classes, static methods and fields from Java classes inside their Kotlin subclasses;
* we can access inherited Java static methods and fields through subclass name: SubClass.SUPER_CLASS_CONSTANT;
* we can access members of companion objects of superclasses from within Kotlin subclasses;
* but the only qualified name a class can be accessed by is its canonical name, i.e. we can’t say SubClass.SupersInnerClass.

This closes many issues we used to have with big inheritance-based frameworks like Android.
### Interface inheritance rules are compatible with Java 8

To make Kotlin future-proof, we added some requirements that comply with the Java 8’s ones, to be able to later compile function bodies in Kotlin interfaces to Java default methods.
In some cases it leads to Kotlin requiring more explicit overrides than before, and, sadly, methods of <code>Any</code> can’t be implemented in interfaces any more (this wouldn’t work in Java 8).
Side note: the default implementations of interface methods are accessible from Java through as static members of <code>MyIntf.DefaultImpls</code>.
### More convenient getter names for booleans

When a property in Kotlin is, for example, named <code>isValid</code>, its Java getter will now be <code>isValid()</code> and not <code>getIsVaild()</code>.
### @JvmField and objects

We have made the strategy for generating pure fields (as opposed to get/set pairs) more predictable: from now on only properties annotated as <code>@JvmField</code>, <code>lateinit</code> or <code>const</code> are exposed as fields to Java clients. Older versions used heuristics and created static fields in objects unconditionally, which is against our initial design goal of having binary-compatibility-friendly APIs by default.
Also, singleton instances are now accessible by the name <code>INSTANCE</code> (instead of <code>INSTANCE$</code>).
We had to prohibit the usage of <code>@JvmField</code> in interfaces, because we can’t guarantee proper initialization semantics for them.
### Int is Serializable

Now the type <code>Int</code> and other basic types are <code>Serializable</code> on the JVM. This should help many frameworks.
### No “package facades”

Classes like <code>KotlinPackage</code> etc are gone. We have finished the transition onto the new class-file layout, and the previously deprecated “package facades” are now removed. Use <code>FileNameKt</code> and/or <code>@file:JvmName</code> (with the optional <code>@file:JvmMultifileClass</code>).
### Internals are now mangled

Since Java doesn’t have <code>internal</code> visibility (yet), we had to mangle the names of <code>internal</code> declarations to avoid unexpected clashes in overrides when we extend a class from another module. Technically, internal members are available to Java clients, but they look ugly, which is the minimal price we could pay for predictability of library evolution.
### Other deprecations and restrictions


* @Synchronized and @Volatile are not applicable for abstract declarations;
* As the final step of getting rid of external annotations, @KotlinSignature is deprecated and will be removed;
* Generic types whose arguments contains Nothing are compiled to raw Java types now, since Java doesn’t have a proper counterpart of `Nothing;

## IDE Changes


* Now Parameter Info works almost everywhere, including brackets, this and super calls

