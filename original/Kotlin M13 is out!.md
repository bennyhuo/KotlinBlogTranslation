---
title: "Kotlin M13 is out!"
date: 2015-09-16 18:29:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/09/kotlin-m13-is-out/
translator:
translator_url:
---

It’s been a long summer, and we have a lot to tell you about Kotlin M13 (details below):

* Compiler daemon for faster compilation;
* lateinit properties to support dependency injection and other frameworks;
* sealed classes for expressing closed hierarchies;
* Specifying and checking annotation targets;
* Java get/set pairs are now seen as properties in Kotlin;
* Better type safety for Java interop: taking @NotNull annotations into account (see this blog post);
* Modifiers and annotations have been separated syntactically (see this blog post);
* Fully functional reflection on classes, functions and properties;
* Access to internal is now checked outside of a module (details below);
* New .class file layout for top-level functions and properties;
* and more (see below)

## Language changes

We are wrapping up with the language and making necessary changes to finalize the syntax as well as adding small things that are missing for critical use-cases. Some of the changes are breaking, and as usual we do our best to help you migrate.
Note that the 1.0 release which we’re working towards right now will be focused on the JVM support. The JavaScript backend will be included, but it will be considered an experimental feature. Because of that, there are few changes affecting JavaScript in this release. We plan to resume work on JS after the 1.0 release is out.
### Late-init properties

One of the biggest issues when using Kotlin with frameworks that inject values into Java fields (i.e. Dependency Injection, Mocking, Serialization and other frameworks) used to be the inability to have a property of a non-null type that is not initialized in constructor.
Now, we introduce `lateinit` properties:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Example {
    @Inject
    lateinit val foo: Foo
    @Inject
    lateinit var bar: Bar
}
 
```

{% raw %}
<p></p>
{% endraw %}

Both `foo` and `bar` have no initializers, but at the same time declare a non-null type. If we try to read them before they are initialized, an exception will be thrown, but as soon as they are initialized by a DI framework (Guice, Dagger or Spring, for example), they can be read as normal properties.
Such properties can also be used for other use cases (such as JUnit `setUp` initialization). Note that `val`‘s can be marked `lateinit` as well as `var`‘s. Unlike `var`s, they can not be assigned freely in the code, but a framework can inject values into them without obstacles, because the underlying JVM fields are not marked as `final`.
See more in the [language docs](http://kotlinlang.org/docs/reference/properties.html#late-initialized-properties) .
### Sealed classes

Many people ask if Kotlin supports [Algebraic Data Types (ADTs)](https://en.wikipedia.org/wiki/Algebraic_data_type) . The answer has always been: “Yes, ADTs can be expressed as classes in Kotlin, and `when` is practically as good as pattern matching”. Now we have added a bit more type-safety to it: with `sealed` classes we can make sure that all cases are enumerated in `when`:

{% raw %}
<p></p>
{% endraw %}

```kotlin
package pets
 
import pets.Pet.*
 
sealed class Pet(val name: String) {
    class Dog(name: String): Pet(name)
    class Cat(name: String): Pet(name)
}
 
fun Pet.saySomething(): String {
    return when (this) {
        is Dog -> "woof"
        is Cat -> "meow"
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

Note that `else` is not required in the example above: since `Pet` is a sealed class, the compiler knows that it has <em>no subclasses other than `Dog` and `Cat`</em>. So we can be sure that all cases have been checked and `else` is not needed. Incidentally, if you forget to cover some cases, the compiler will report an error and remind you to do it, or resort to `else`.
For now only classes nested into the sealed class can extend it, but we will later relax this restriction and allow subclasses in the same source file.
For more details see the [docs](http://kotlinlang.org/docs/reference/classes.html#sealed-classes) .
### Annotations require “@”

Modifiers and annotations have been separated syntactically (see this [blog post](http://blog.jetbrains.com/kotlin/2015/08/modifiers-vs-annotations/) ) in M13. We now require a `@` for annotations, and all annotation classes are supposed to be named starting with a capital letter (which brings better uniformity with Java).
Thus, library annotations such as `@Throws`, or `@Volatile` are renamed. We also renamed `@platformName` to `@JvmName` and `@platformStatic` to `@JvmStatic`.
Some former annotations have become modifiers:

* data
* inline-related

inline
noinline
crossiniline — instead of former @inlineOption(ONLY_LOCAL_RETURNS)
* inline
* noinline
* crossiniline — instead of former @inlineOption(ONLY_LOCAL_RETURNS)
* tailrec — instead of former @tailRecursive
* external — instead of former @native

This change is transparent for most users since annotations that haven’t changed their names looked like modifiers before.
The old syntax and classes are deprecated.
The [Code Cleanup IDE action](http://blog.jetbrains.com/idea/2014/07/try-intellij-idea-14-eap-138-1283-4-with-code-cleanup-android-studio-beta-features-and-more/) will help you migrate your code.
### Annotation targets and other options

Kotlin now supports the following annotation options (expressed as annotations on annotation classes):

* @Retention – who can see this annotation: RUNTIME (default), BINARY (.class file only) or SOURCE;
* @Target – where the annotation is applicable;
* @MustBeDocumented – a marker that says that this annotation is a part of the API of the annotated element, and must be displayed in the generated documentation;
* @Repeatable – a marker that says that this annotation may be used multiple times on the same element.

See more in the [docs](http://kotlinlang.org/docs/reference/annotations.html#annotation-declaration) .
Additionally, we can now specify an optional target for annotations at use sites:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Example(
    @field:MyFieldAnnotation(...)
    val foo: Foo
)
 
```

{% raw %}
<p></p>
{% endraw %}

<strong>NOTE: this is a breaking change</strong>. Before M13 when we annotated parameters of primary constructors, annotations were written <strong>both</strong> on parameters and fields they are stored in. Now they are only written on one of the following (the first applicable): parameter, property, field. I.e. if the annotation is applicable to both field and parameter, it will only be written on the parameter now. This presents some issues when using Jackson, but there is an easy workaround: use the special [Jackson module for Kotlin](http://mvnrepository.com/artifact/com.fasterxml.jackson.module/jackson-module-kotlin) . And the old way didn’t have one.
Find more information in the [docs](http://kotlinlang.org/docs/reference/annotations.html#annotation-use-site-targets) .
### Visibilities

We have revisited our access modifier/visibility model. From now on:

* private on the top level (outside any class) means “visible only inside this source file”;
* we do not require explicit return types for public declarations any more;
* the default visibility (no modifier) is changed from internal to public,
* we finally enabled the checks that reject usages of internal declarations outside a module.

This may seem controversial that we chose `public` as default visibility. Kotlin being a type-safe language, choosing the safest option, `private`, by default may seem more logical. And we totally realize there are valid arguments in favour of this default. But Kotlin is also a pragmatic language. I’ll try to explain briefly why we believe `public` is the right default.
In real Java code bases (where public/private decisions are taken explicitly), `public` occurs a lot more often than `private` (2.5 to 5 times more often in the code bases that we examined, [including Kotlin compiler and IntelliJ IDEA](https://youtrack.jetbrains.com/issue/KT-3240#comment=27-1110881) ). This means that we’d make people write `public` all over the place to implement their designs, that would make Kotlin a lot more ceremonial, and we’d lose some of the precious ground won from Java in terms of brevity. In our experience explicit `public` breaks the flow of many DSLs and very often — of primary constructors. So we decided to use it by default to keep our code clean.
<strong>NOTE</strong>: `internal` remains supported, but now you need to specify it explicitly.
### Miscellaneous changes


* Support for overloaded callable references: you can now use ::foo even if foo is overloaded, but the right signature can be chosen based on the context;
* Unambiguous super can be used without angle brackets;
* Strict nullability checks for type parameters;
* Functions with no default parameters are preferred in overload resolution (good for API evolution);
* @HiddenDeclaration annotation introduced to hide declarations from clients while keeping them in the binaries (also for smoother API evolution).

## Java interop changes

### Java get/set pairs are now seen as properties

People have been asking for this feature for a long time, and it took us a while to figure it out. Now when we use Java classes that define properties by convention (e.g. `getFoo()` and maybe `setFoo()`), Kotlin automatically defines corresponding extension properties:

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Java:
 
class JBean {
    public Foo getFoo() { return ...; }
    public void setFoo(Foo foo) { ... }
}
 
// Kotlin
 
fun demo(bean: JBean) {
    println(bean.foo) // 'foo' is automatically defined
}
 
```

{% raw %}
<p></p>
{% endraw %}

Access to such properties is optimized so that `bean.foo` compiles to `bean.getFoo()` without any intermediate calls.
### New layout of .class files for top-level declarations

A few months ago we announced [this change](http://blog.jetbrains.com/kotlin/2015/06/improving-java-interop-top-level-functions-and-properties/) and now it’s done:

* By default, each Kotlin source file (e.g. myFile.kt) produces a class file with the same name, capitalized and suffixed with “Kt”: MyFileKt;
* Top-level functions and properties defined in that file are accessible in Java through this class name (instead of the problematic FooPackage);
* Consequently, two files in the same package can not have the same name (or the class files would clash);
* You can specify a @file:JvmName("CustomName") annotation on a source file to change the name of the class;
* Many files can share the same JVM name if they are additionally marked with @file:JvmMultifileClass annotation.

To make this change work, we had to introduce a new resource file that is required to compile Kotlin code against Kotlin binaries. Its name is `META-INF/&lt;module_name&gt;.kotlin_module`. <strong>Make sure these `.kotlin_module` files are not stripped by your packaging process.</strong> Also, make sure that module names do not clash in your project:

* in Maven we use groupId and artifactId for module names, but you can say


{% raw %}
<p></p>
{% endraw %}

```kotlin
<configuration>
    <moduleName>com.example.mymodule</moduleName>
</configuration>
 
```

{% raw %}
<p></p>
{% endraw %}


* in Gradle it’s project name + build task name, to customize:


{% raw %}
<p></p>
{% endraw %}

```kotlin
compileKotlin {
    kotlinOptions.moduleName = "com.example.mymodule"    
}
 
```

{% raw %}
<p></p>
{% endraw %}


* in Ant and command line you should specify module names explicitly:

<kotlinc modulename="com.example.mymodule"/>
$ kotlinc-jvm -module-name com.example.mymodule
* <kotlinc modulename="com.example.mymodule"/>
* $ kotlinc-jvm -module-name com.example.mymodule

More information can be found [here](http://kotlinlang.org/docs/reference/java-interop.html#package-level-functions) .
### Null-safety in Java interop

We first announced this [a while ago](http://blog.jetbrains.com/kotlin/2015/04/upcoming-change-more-null-safety-for-java/) . Now we can use `@NotNull` and `@Nullable` in Java and Kotlin recognizes them so that misuse results in compilation errors rather than warnings.
As a consequence, using Java collections has become a lot safer: we can not put a `null` into an `ArrayList&lt;String&gt;` any more. [Platform types](http://blog.jetbrains.com/kotlin/2014/10/making-platform-interop-even-smoother/) are kept in place, because annotations are often missing and sometimes wrong (violate inheritance rules, for example), so by default no static null-checks are imposed onto Java code.
External annotations are not used either, so we have spared you quite some build configuration.
## Libraries

Kotlin libraries are also being actively developed. M13 brings fully functional reflection library: we can now introspect classes, their members, parameters etc. A separate blog post about this is coming.
The standard library has got many convenient additions including

* + and - for sets and other collections;
* improved delegates for properties.

More on this is a separate post too.
## Tools

<strong>Compiler daemon.</strong> We announced [support for Gradle Daemon](http://blog.jetbrains.com/kotlin/2015/08/gradle-daemon-support-for-faster-compilation/) a while ago and your feedback has been positive: compilation times seem to go down up to a factor of three. We keep working on compilation performance, and since M13 a daemon similar to Gradle’s is used in IntelliJ IDEA as well. This feature is marked “experimental” for now, so you need to tick a box in the <em>Preferences</em> dialog to switch it on:
<p>
  Build, execution, deployment -&gt; Compiler -&gt; Kotlin compiler -&gt; Keep compiler process alive between invocations (experimental)
</p>
<strong>Incremental compilation</strong> is another direction we have taken to improve Kotlin compilation times. M13 brings:

* incremental compilation for inline functions: now if you change a body of an inline function, only classes that use it are recompiled;
* changes to private members do not cause recompilation of other files.

## IDE

The IDE experience has been improved too. For the sake of brevity we highlight only those features that are not easily discovered:

* The IDE suggests name and type of parameters when typing:
(Hint: hover mouse over image to start animation)

