---
title: "M10 is out"
date: 2014-12-17 15:02:00
author: Hadi Hariri
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2014/12/m10-is-out/
---

Right before the festivities start, we’ve managed to release the next milestone of Kotlin, adding <strong>dynamic types</strong> and more. Let’s see what M10 brings us. <span id="more-1708"></span>
## Language enhancements

Some improvements in the language, in particular:
### Reified type parameters for inline functions

Before M10, we sometimes wrote code like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun <T> TreeNode.findParentOfType(clazz: Class<T>): T? {
    var p = parent
    while (p != null && !clazz.isInstance(p)) {
        p = p?.parent
    }
    return p as T
}
```

{% raw %}
<p></p>
{% endraw %}

Here, we walk up a tree and use reflection to check if a node has a certain type. It’s all fine, but the call site looks a little messy:

{% raw %}
<p></p>
{% endraw %}

```kotlin
myTree.findParentOfType(javaClass<MyTreeNodeType>())
```

{% raw %}
<p></p>
{% endraw %}

What we actually want is simply <em>pass a type</em> to this function, i.e. call is like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
myTree.findParentOfType<MyTreeNodeType>()
```

{% raw %}
<p></p>
{% endraw %}

But then we’d need <em>reified generics</em> to access that type inside a function, and on the JVM reified generics are expensive…
Fortunately, Kotlin has  [inline functions](http://kotlinlang.org/docs/reference/lambdas.html#inline-functions) , and they now support <strong>reified</strong> type parameters, so we can write something like this:

{% raw %}
<p></p>
{% endraw %}

```kotlin
inline fun <reified T> TreeNode.findParentOfType(): T? {
    var p = parent
    while (p != null && p !is T) {
        p = p?.parent
    }
    return p as T
}
```

{% raw %}
<p></p>
{% endraw %}

We qualified the type parameter with the <strong>reified</strong> modifier, now it’s accessible inside the function, almost as if it were a normal class. Since the function is inlined,  no reflection is needed, normal operators like <strong>!is</strong> are working now. Also, we can call it as mentioned above: <code>myTree.findParentOfType&lt;MyTreeNodeType&gt;()</code>.
Though reflection may not be needed in many cases, we can still use it with a reified type parameter: <code>javaClass<t>()</t></code> gives us access to it:

{% raw %}
<p></p>
{% endraw %}

```kotlin
inline fun methodsOf<reified T>() = javaClass<T>().getMethods()
 
fun main(s: Array<String>) {
  println(methodsOf<String>().joinToString("\n"))
}
```

{% raw %}
<p></p>
{% endraw %}

Normal functions (not marked as <code>inline</code>) can not have reified parameters. A type that does not have a run-time representation (e.g. a non-reified type parameter or a fictitious type like <code>Nothing</code>) can not be used as an argument for a reified type parameter.
This feature is intended to simplify code in frameworks that traditionally rely on reflection, and our internal experiments show that it’s working well.
### Checks for declaration-site variance

Kotlin has  [declaration-site variance](http://kotlinlang.org/docs/reference/generics.html#declaration-site-variance)  from the very beginning, but the correspondent checks have been missing from the compiler for a long time. Now they are put in their place: the compiler complains if we declare a type parameter as <strong>in</strong> or <strong>out</strong>, but misuse it in the class body:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class C<out T> {
  fun foo(t: T) {} // ERROR
}
```

{% raw %}
<p></p>
{% endraw %}

In this example, since T is declared as <strong>out</strong> (i.e. the class is <em>covariant</em> in T), we are not allowed to take it as a parameter to the <code>foo()</code> function, we can only return it.
Note that a <strong>private</strong> declaration is allowed to violate variance restrictions, for example:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class C<out T>(t: T) {
    private var foo: T = t
}
```

{% raw %}
<p></p>
{% endraw %}

Although <code>foo</code>‘s setter takes T as as an argument, and thus violates the <strong>out</strong> restriction on it, the compiler allows this and makes sure that only <em>the same instance</em> of <code>C</code> has access to <code>foo</code>. This means that the following function in <code>C</code> would not compile:

{% raw %}
<p></p>
{% endraw %}

```kotlin
// inside the class C
private fun copyTo(other: C<T>) {
    other.foo = foo // ERROR: Can not access foo in another instance of C
}
```

{% raw %}
<p></p>
{% endraw %}

This is a <strong>breaking change</strong>: some code that compiled previously may break, but not fixing it is likely to result in run-time exceptions anyways, so the compiler errors will be of some value to you <img alt=":)" class="wp-smiley" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1" style="height: 1em; max-height: 1em;"/>
### Type inference supports use-site variance

Type argument inference has been improved to accommodate  [use-site variance](http://kotlinlang.org/docs/reference/generics.html#type-projections)  more comfortably. Now you can call a generic function, e.g. <code>reverseInPlace()</code> on a projected type, such as <code>Array&lt;out Number&gt;</code>:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun example(a: Array<out Number>) {
    a.reverseInPlace()
}
```

{% raw %}
<p></p>
{% endraw %}

where <code>reverseInPlace</code> is defined as follows:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun <T> Array<T>.reverseInPlace() {
    fun (i in 0..size() / 2) {
        val tmp = this[i]
        this[i] = this[size - i - 1]
        this[size - i - 1] = tmp
    }
}
```

{% raw %}
<p></p>
{% endraw %}

The underlying mechanism was proposed initially by Ross Tate in his  [paper on “Mixed-Site Variance”](http://www.cs.cornell.edu/~ross/publications/mixedsite/) .
### Varargs translated to projected arrays

Another <strong>breaking change</strong> comes in the form of a fix to a obscure, but sometimes  [rather](https://youtrack.jetbrains.com/issue/KT-5534)   [annoying](https://youtrack.jetbrains.com/issue/KT-2163)  issue: when we have a function that takes a vararg of <code>String?</code>, we really want to be able to pass an array of <code>String</code> to it, don’t we? Before M10 it was impossible, because vararg of T were compiled to <code>Array&lt;T&gt;</code>, now they are compiled to <code>Array&lt;out T&gt;</code>, and the following code works:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun takeVararg(vararg strings: String?) { ... }
 
val strs = array("a", "b", "c")
takeVararg(*strs)
```

{% raw %}
<p></p>
{% endraw %}

## JavaScript improvements and changes

JavaScript gets an important update in this version with support for dynamic types.
### Dynamic support

Sometimes the best way to talk to dynamic languages is dynamically. This is why we’ve introduced the soft keyword <em>dynamic</em> which allows us to declare types as dynamic. Currently this is only supported when targeting JavaScript, not the JVM.
When interoperating with JavaScript we can now have functions take as parameters, or return, a dynamic type

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun interopJS(obj: dynamic): dynamic {
   ...
   return "any type"
}
```

{% raw %}
<p></p>
{% endraw %}

We’ll cover dynamic in more details along with usage scenarios and limitations in a separate blog post. For technicalities see the  [spec document](https://github.com/JetBrains/kotlin/blob/master/spec-docs/dynamic-types.md) .
### New Annotations

We’ve added a series of annotations to make JavaScript interop easier, in particular <em>nativeInvoke, nativeGetter</em> and <em>nativeSetter</em>.
If a function <code>bar</code> is annotated with <code>nativeInvoke</code>, its calls <code>foo.bar()</code> are translated to <code>foo()</code> in JavaScript. For example:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Foo {
   nativeInvoke
   fun invoke(a: Int) {}
}
 
val f = Foo()
f(1) // translates to f(1), not f.invoke(1)
f.invoke(1) // also translates to f(1)
```

{% raw %}
<p></p>
{% endraw %}

Much the same way, we can use <em>nativeGetter</em> and <em>nativeSetter</em> to get index-access available in JavaScript:

{% raw %}
<p></p>
{% endraw %}

```kotlin
native("Array")
class JsArray<T> {
   nativeGetter
   fun get(i: Int): T = noImpl
   nativeSetter
   fun set(i: Int, v: T): Unit = noImpl
}
```

{% raw %}
<p></p>
{% endraw %}

Without <code>native*</code> annotations, calls to <code>get</code> and <code>set</code> (including those done by convention, e.g. <code>a[i] = j</code> is the same as <code>a.set(i, j)</code>) are translated to <code>a.get(...)</code> and <code>a.set(...)</code>, but with the annotations placed as above, they are translated to square brackets operator in JavaScript:

{% raw %}
<p></p>
{% endraw %}

```kotlin
a[0] // translates to a[0], not a.get(0)
a.get("first") // translates to a["first"]
a[2] = 3 // translates to a[2] = 3
```

{% raw %}
<p></p>
{% endraw %}

We can use these annotations in the following cases:

* non-extension member functions of native declarations,
* top-level extension functions.

### Kotlin.js output – breaking change

Previously, when creating a new project, the kotlin.js runtime would be created in a folder named <em>scripts</em>. As of M10, this file is created on first compilation and is placed in the output folder (defaults to <em>out</em>). This provides for a much easier deployment scenario as library and project output is now located under the same root folder.
### New no-stdlib option to kotlin-js compiler – breaking change

We now provide a command line option for the kotlin-js compiler, namely <em>no-stdlib</em>. Without specifying this option, the compiler uses the bundled standard library. This is a change of behaviour from M9.
### js code

We can now output JavaScript code directly inside Kotlin code

{% raw %}
<p></p>
{% endraw %}

```kotlin
js("var value = document.getElementById('item')")
```

{% raw %}
<p></p>
{% endraw %}

which takes the code provided as parameter and injects it directly into the AST JavaScript code that the compiler generates.
As you can see, we’ve added a lot of new improvements for JavaScript in this release and we’ll cover these in more detail in a separate post.
## Java Interop

### [platformStatic] for properties

Now, we can mark properties as <code>[platformStatic]</code> so that their accessors become visible from Java as static methods.
### Static fields in objects

Properties on any object now produce static fields so that they can easily be consumed from Java even without the need to decorate them with <em>platformStatic</em> annotations.
### JNI and [native]

Kotlin now supports JNI via <code>[native]</code> annotation, defined in <code>kotlin.jvm</code> package (see the spec document  [here](https://github.com/JetBrains/kotlin/blob/master/spec-docs/jvm-native-flag-support.md) .). To declare a native method, simply put the annotation on it:

{% raw %}
<p></p>
{% endraw %}

```kotlin
import kotlin.jvm.*
import kotlin.platform.*
 
class NativeExample {
    native fun foo() // native method
 
    class object {
        platformStatic native fun bar() // static native method
    }
}
```

{% raw %}
<p></p>
{% endraw %}

Here’s an  [example](https://github.com/ligee/kotlin-ndk-samples/blob/master/hello-jni/src/com/example/hellojni/HelloJni.kt)  of using native declarations with Android and NDK.
## IntelliJ IDEA improvements

Some more improvements in the IntelliJ IDEA area, including:
### Incremental compilation in mixed projects

We’ve enhanced incremental compilation and with M10 it now supports dependencies between Kotlin and Java code. Now when you change your Java code, the relevant parts of your Kotlin code are re-compiled. As a reminder, incremental compilation is activated under the Kotlin Compiler options.
### HotSwap fixed in debugger

Now, when we recompile Kotlin code while debugging it, it gets smoothly re-loaded into the debugee process.
### Evaluate Expression: Completion improvements

During debug sessions, when evaluating expressions, casts are automatically added as needed. For instance when downcasting from <em>Any</em> to a specific type.

{% raw %}
<p><img alt="Completion Casts" class="aligncenter size-full wp-image-1716" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2014/12/completion.png?resize=564%2C126&amp;ssl=1"/></p>
{% endraw %}

### Copy reference

We can now obtain the complete reference for any Kotlin symbol, much like we do with  [IntelliJ IDEA in Java code](https://www.jetbrains.com/idea/help/cutting-copying-and-pasting.html) 

{% raw %}
<p><img alt="Copy Reference" class="aligncenter size-full wp-image-1711" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2014/12/copy-reference-no-retina.png?resize=457%2C269&amp;ssl=1"/></p>
{% endraw %}

### Create from usage for classes and packages

Create from usage is now available for classes and packages, which contributes significantly to a TDD workflow. Even if you’re not doing TDD, it does minimize friction of creating new elements.

{% raw %}
<p><img alt="Create Class from Usage" class="aligncenter size-full wp-image-1713" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2014/12/create-class.png?resize=421%2C108&amp;ssl=1"/></p>
{% endraw %}

### Generics in change signature

The Change Signature refactoring now supports generics in cases where a base class function is promoted to use generics. In essence, in the following scenario

{% raw %}
<p></p>
{% endraw %}

```kotlin
open class Base<T> {
    open fun baseMethod<K>(t: T, k: K) {}
}
 
class Derived<X>: Base<List<X>> {
    override fun baseMethod<Y>(a: List<X>, b: Y) {}
}
```

{% raw %}
<p></p>
{% endraw %}

If the signature of <em>Base.baseMethod</em> is changed to <em>baseMethod&lt;T&gt;(t: List&lt;T&gt;, k: K?)</em> then the signature of <em>Derived.baseMethod</em> is appropriately changed to <em>&gt;baseMethod&lt;Y&gt;(a: List&lt;Y&gt;, b: List&lt;X&gt;?)</em>
### Completion improvements

Completions items ordering has been improved, immediate members are now highlighted. Smart completion now finds inheritors of expected types. Completion performance severely improved.
### Runnable objects

Now you can run an object that declared a <code>[platformStatic]</code> main function, for the IDE:

{% raw %}
<p></p>
{% endraw %}

```kotlin
import kotlin.platform.*
 
object Hello {
    platformStatic fun main(args: Array<String>) {
        println("Hello")
    }
}
```

{% raw %}
<p></p>
{% endraw %}

Just right-click the object and select <em>Run …</em>
### Code Coverage highlighting in the Editor

If you run Kotlin code with coverage, the Editor now marks covered and uncovered lines for you (available in IntelliJ IDEA 14 only).
### JavaScript project configuration

The IDE plugin can now automatically configure Maven projects to work with Kotlin/JS. Also, if you have an outdated version of Kotlin’s runtime library, the IDE will ask you to update it, and you can now chose to use a library located in the plugin distribution, instead of copying one into your project.
## Summary

To install M10, update the plugin in your IntelliJ IDEA 14 (or earlier versions), and as always you can find the plugin in our plugin repository. You can also download the standalone compiler from the  [release page](https://github.com/JetBrains/kotlin/releases/tag/build-0.10.4) .
