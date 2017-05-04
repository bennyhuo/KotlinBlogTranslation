---
title: "Kotlin M12 is out!"
date: 2015-05-29 16:28:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/05/kotlin-m12-is-out/
translator:
translator_url:
---

We are happy to present Kotlin M12, bringing some rather important changes and new features:

* New syntax for annotations and enums
* More convenient semantics of function types
* Better smart casts
* kapt for Java Annotation Processing support
* Multiple IDE features
* and more…

## Language

Many of the changes introduced to the language and core libraries are deprecations. Use [“Code Cleanup…” action](http://blog.jetbrains.com/idea/2014/07/try-intellij-idea-14-eap-138-1283-4-with-code-cleanup-android-studio-beta-features-and-more/) to fix all warnings in your project automatically.
### Annotations: New Syntax

As we [mentioned before](http://blog.jetbrains.com/kotlin/2015/04/upcoming-change-syntax-for-annotations) , we decided to reserve square brackets for some more productive future uses, and make annotation syntax more familiar to Java users. So, since M12, we write <code>@Foo(args)</code> instead of <code>[Foo(args)]</code>. More details can be found [here](http://kotlinlang.org/docs/reference/annotations.html) (even more — in the [spec document](https://github.com/JetBrains/kotlin/blob/spec-at-based-annotations/spec-docs/at-based-annotation-syntax.md) ).
Note that <code>@</code> is <strong>not required</strong> in most cases. Normally we write annotations without any escaping:

{% raw %}
<p></p>
{% endraw %}

```kotlin
data class Foo // `data` is an annotation
 
```

{% raw %}
<p></p>
{% endraw %}

The old syntax based on <code>[...]</code> is <em>deprecated</em>, so the compiler will issue warnings on your code. To fix these warnings, press Alt+Enter and run a quick fix (individual or for the whole project). The aforementioned “Code Cleanup…” action also works for the whole project.
### Label Syntax Changed

Since M12 <code>@name</code> is an annotation, but it had a meaning before, i.e. it was a [label](http://kotlinlang.org/docs/reference/returns.html#break-and-continue-labels) . We had to find some other syntax for labels, and now they are declared with <code>@</code> at the end:

{% raw %}
<p></p>
{% endraw %}

```kotlin
loop@ for (i in 1..100) {
  for (j in 1..100) {
    if (...)
      break@loop
  }
}
 
```

{% raw %}
<p></p>
{% endraw %}

So, <code>loop@</code> <em>declares</em> a label, and <code>break@loop</code> <em>uses</em> it.
### Class Literals in Annotations

Before M12, annotations in Kotlin were allowed to use <code>java.lang.Class</code>, for example:

{% raw %}
<p></p>
{% endraw %}

```kotlin
annotation class handledBy(val handlerClass: Class<out Handler>)
 
// Usage
handledBy(javaClass<MyHandler>())
class MyEvent {...}
 
```

{% raw %}
<p></p>
{% endraw %}

Now, using Java-specific classes is deprecated in Kotlin annotations, and we need to use Kotlin’s own model: <code>kotlin.reflect.KClass</code> instead of <code>java.lang.Class</code> and <code>Foo::class</code> instead of <code>javaClass&lt;Foo&gt;()</code>:

{% raw %}
<p></p>
{% endraw %}

```kotlin
annotation class handledBy(val handlerClass: KClass<out Handler>)
 
// Usage
handledBy(MyHandler::class)
class MyEvent {...}
 
```

{% raw %}
<p></p>
{% endraw %}

Note that Kotlin sees Java annotations as if they referred to <code>KClass</code> instead of <code>java.lang.Class</code>:

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Java
@interface JavaAnnotation {
    Class<?> value();
}
 
```

{% raw %}
<p></p>
{% endraw %}


{% raw %}
<p></p>
{% endraw %}

```kotlin
// Kotlin
 
fun introspect(jann: JavaAnnotation) {
    val theClass = jann.value // the type of this expression is KClass<*>
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

Now, when we need to turn a <code>KClass</code> into a <code>java.lang.Class</code>, we can call <code>.java</code> on it, e.g. <code>Foo::class.java</code> or <code>jann.value.java</code>.
### Annotated Primary Constructors

We decided to make primary constructor syntax more regular, and now the <em>full form</em> of the primary constructor includes the <code>constructor</code> keyword:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class PrivateConstructor private constructor (val x: Int) {
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

The full form is <strong>only needed when we want to annotate</strong> a primary constructor or add a modifier. In most cases, the old familiar syntax still works:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class MyClass(val x: Int) {
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

### Traits Are Now Interfaces

As our traits are rather limited anyways, and Java’s interfaces are pretty much the same thing, we have deprecated the <code>trait</code> keyword, so please use <code>interface</code> instead.
As usual, quick fixes and “Cleanup Code…” will help you along.
### Enum Classes: New Syntax

The [new syntax for enums](http://kotlinlang.org/docs/reference/enum-classes.html) is very close to what Java has. Enum entries should now be separated with commas:

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Foo {
    A, B, C
}
 
```

{% raw %}
<p></p>
{% endraw %}

Now, when you declare a member of an <code>enum</code> class, it must go after all entries, and there must be a semicolon after the last entry:

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class FooWithMember {
    FOO,
    BAR,
    BAZ;
 
    fun doIt() { ... }
}
 
```

{% raw %}
<p></p>
{% endraw %}

Lastly, when <code>enum</code> has a constructor, you can call it by simply passing the arguments next to the name of the entry:

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Color(val rgb: Int) {
  RED(0xFF0000),
  GREEN(0x00FF00),
  BLUE(0x0000FF)
  // no members => semicolon is not needed here
}
 
```

{% raw %}
<p></p>
{% endraw %}

The old syntax is deprecated.
### Function Types Reformed

We unified function types and extension function types, so that now they can often be used interchangeably. For example, we can pass <code>String::length</code> where a function <code>'(String) -&gt; Int'</code> is expected.

{% raw %}
<p></p>
{% endraw %}

```kotlin
// map() expects `(String) -> Int`
// argument has type `String.() -> Int`
strings.map(String::length)
 
```

{% raw %}
<p></p>
{% endraw %}

More details in [this post](http://blog.jetbrains.com/kotlin/2015/04/upcoming-change-function-types-reform) .
If you used Kotlin’s function classes (e.g. <code>kotlin.Function1</code>) in your Java code, you will need to make adjustments to it, because from now on these classes reside in the <code>kotlin.jvm.functions</code> package. You can migrate all your Java code by running “Cleanup Code…” with the “Usage of deprecated function classes in Java” inspection.
### Smart Casts Made Even Smarter

A long awaited feature: Kotlin can now smart-cast local <code>var</code>‘s:

{% raw %}
<p></p>
{% endraw %}

```kotlin
var foo = bar()
 
if (foo != null) {
    foo.baz() // no error here
}
 
```

{% raw %}
<p></p>
{% endraw %}

Of course, the smart cast only works when the compiler knows that no modification could possibly have happened since the relevant check was made. Note that loops often times distort this picture (due to some technical reasons we can not use a fully-fledged data flow analysis for smart casts), so when a <code>var</code> is mutated in a loop, smart casts may not work.
Usages of public and protected immutable <code>val</code>‘s in the same module can also be smart-cast now:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class C(public val d: D?)
 
fun foo(c: C) {
    if (c.d != null) {
        c.d.foo() // c.d has been smart-cast here
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

### Inlining and Non-Local Returns Supported for Function Expressions [Function expressions](http://kotlinlang.org/docs/reference/lambdas.html#function-expressions) introduced in M11 are now supported in inline calls:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun test(list: List<Foo?>) {
    val mapped = list.map(fun (item) = item?.toString() ?: return@test) // non-local return
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

### Deprecations and Dropped Features

M12 removes some previously deprecated features:

* class object is dropped in favor of companion object;
* init is now required in front of anonymous initializer blocks.

Some more features were deprecated:

* break and continue in when;
* interfaces that extend classes;
* covariant supertype specialization;
* static type assertions.

Use quick-fixes and “Cleanup Code…” to migrate your programs.
## Java Interop

### jvmOverloads

Kotlin has default arguments that dramatically reduce the needs in overloads, but Java clients can not benefit from this feature directly.<br/>
In M12 we have added an annotation <code>jvmOverloads</code> that tells the compiler to generate N+1 overloads for a Kotlin function that has N default parameters.<br/>
For example,

{% raw %}
<p></p>
{% endraw %}

```kotlin
jvmOverloads fun f(a: String, b: Int = 0, c: String = "abc") {
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

will generate

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Java
void f(String a, int b, String c)
void f(String a, int b)
void f(String a)
 
```

{% raw %}
<p></p>
{% endraw %}

### Source Maps for Better Debugging (JSR-45)

We can now step through bodies of inlined function, thanks to source mapping tables emitted by the compiler into generated class files.
Some technical notes: every class file has line numbers assigned to instructions. For inlined function bodies we assign line numbers beyond the actual end of file (e.g. if the file has 50 lines, inlined code has line numbers starting with 51), and these “virtual” numbers are mapped to actual sources of the inlined code that possibly reside in other files. The standard JVM debugger understands the source mappings and can step through the appropriate files and lines. The only caveat is that exception stack traces may sometimes contain line numbers beyond the end of file. We are looking for a solution to this problem.
### Java Annotations: Argument Ordering

In Java, annotations are interfaces and their parameters are methods of those interfaces. Thus, the ordering of the parameters is insignificant, and the call site can not rely on it. This is why Java requires that all arguments but one (named <code>value</code>) are passed as named.
While annotations declared in Kotlin have proper constructors that admit positioned parameters and even varargs, we can not rely on Java annotations in this respect, so from now on the following applies to Java annotations:

* only the parameter named value can be passed without a name,
* only the parameter named value can be a vararg (and automatically becomes one, if it is an array in Java),
* all other parameters can not be passed as positional.

## JavaScript

JavaScript back-end is catching up with the JVM one. M12 adds support for

* Inlining works between modules
* Reified parameters
* Function expressions
* Secondary constructors

## Tools

### kapt: Annotation Processing (JSR-269)

As mentioned earlier in [this post](http://blog.jetbrains.com/kotlin/2015/05/kapt-annotation-processing-for-kotlin/) , M12 adds initial support for Annotation Processing, so that frameworks like Dagger 2 work with Kotlin now. The main limitation of the current implementation is that Kotlin code can not refer to any declarations generated by the annotation processors (so, for Dagger you need to write at least one small class in Java).
We are going to fix this limitation in the future by generating stubs for classes emitted by the Kotlin compiler. Details in the [aforementioned post](http://blog.jetbrains.com/kotlin/2015/05/kapt-annotation-processing-for-kotlin/) .
### Gradle: JUnit Support for Android

Kotlin Gradle plugin for Android now supports JUnit tests. All we need to do is follow [the standard procedure for Java](http://tools.android.com/tech-docs/unit-testing-support#TOC-Setting-up-Android-Studio) , but now we can write our tests in Kotlin.
### Quasar Support

Some of the recent changes in Kotlin enabled a great addition to our ecosystem: now [Quasar](http://docs.paralleluniverse.co/quasar/) provides fibers (lightweight threads), Go-like channels, Erlang-like actors, and other asynchronous tools for Kotlin! See the announcement [here](http://blog.paralleluniverse.co/2015/05/29/quasar-pulsar-0-7-0/) .
## Standard APIs Changed

M12 adds new functionality to the standard library:

* new utilities in kotlin.io package
* new text utilities
* regular expressions API unified across JVM and JS
* new collection utilities
* MIN_VALUE and MAX_VALUE available for all numeric types for both JVM and JS

As we are working on the Kotlin standard library, some things get changed and/or deprecated. Use quick fixes and the “Cleanup Code…” action to migrate your code. (Please make sure that you have attached the sources of the standard library to your project.)
The full list of changes is available [here](https://quip.com/Cy9IAkZtvmjm) .
## IntelliJ IDEA Plugin

Kotlin IDE now supports the standard <strong>Introduce Parameter</strong> refactoring that turns an expression selected inside a function into a parameter:

{% raw %}
<p><img class="aligncenter" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/05/parameter.png?fit=640%2C120&amp;ssl=1"/></p>
{% endraw %}

Additionally, <strong>Introduce Lambda Parameter</strong> is available to extract a piece of code as a function value:

{% raw %}
<p><img class="aligncenter" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/05/lambda.png?fit=640%2C120&amp;ssl=1"/></p>
{% endraw %}

<strong>Rename</strong> has an option to rename related declarations (variables, subclasses etc) as well:

{% raw %}
<p><img class="aligncenter" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/05/rename.png?fit=640%2C85&amp;ssl=1"/></p>
{% endraw %}

As we are adding a lot of deprecations lately, the IDE now supports <code>ReplaceWith</code> quick-fix: there’s an (optional) extra parameter to the <code>deprecated</code> annotation, where we can specify an expression to replace a deprecated call:

{% raw %}
<p><img class="aligncenter" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2015/05/replace-with.png?fit=640%2C230&amp;ssl=1"/></p>
{% endraw %}

There is an intention action to add <code>ReplaceWith</code> to user’s deprecated declarations.
Some more changes:

* New Debugger Features

Evaluate expression for local functions
Field Watch Points (only for properties with backing field)
* Evaluate expression for local functions
* Field Watch Points (only for properties with backing field)
* Change Package Intention
* Highlighting exit points of functions
* Gutter Marks for recursive calls
* Unused receiver parameter inspection
* Code style settings for imports (e.g. we can now always import specified packages with ‘*’)
* Java2Kotlin Converter now offers to update usages in other files
* Typing ‘!’ when completion list is open inserts negated call (e.g. !foo.isEmpty())
* Intention actions to change visibility modifiers
* Intention actions have much better scope of availability now
* Quick-fix to add parameters from the base class when the superclass’ constructor has parameters

## Things That Haven’t Made It (Yet)

We are still working on some of the changes we announced earlier, such as [More Null-safety for Java](http://blog.jetbrains.com/kotlin/2015/04/upcoming-change-more-null-safety-for-java/) . Will roll them out as soon as they are ready.
## More Announcements Coming

There will be some more M12-related material published in the nearest future. Stay tuned!
