---
title: "What’s new in Standard Library M13 and M14"
date: 2015-09-28 16:56:00
author: ilya.gorbunov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/09/whats-new-in-standard-library-m13-and-m14/
translator:
translator_url:
---

Standard Library continues its evolution:

* Lazy<T> type has been introduced
* More concise syntax for storing properties in a Map
* Final changes in the Char arithmetics
* Plus and minus operations on a collection now depend on its type
* New scope functions: apply and run
* Right-open ranges
* Trimming indents in multiline strings literals
* and more


{% raw %}
<p><span id="more-2759"></span></p>
{% endraw %}

# What’s new in M13

## Lazy

Lazy evaluation is a useful pattern and it was unfair to limit it only to delegated properties. Now there is `Lazy&lt;T&gt;` type right in the `kotlin` package and you can use it in many contexts. You can delegate properties to instances of `Lazy`, which has the `get` extension function to satisfy the delegation convention:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class Poll(val json: Map<String, *>) {
    val messages: List<Message> by lazy {
        // some expensive and not always needed computation
        val field = json.get("messages")
        (field as JSONArray).toList().map {
            Message((it as JSONObject).toMap())
        }
    }
}
```

{% raw %}
<p></p>
{% endraw %}

Unlike `Delegates.lazy`, an semantics of `lazy` is **synchronized** by default.
## Delegating properties to a map

Another common use case is storing values of properties in a map, where names of properties serve as keys. For this case we provide extension functions `get` and `set` on maps to satisfy the delegation convention, allowing to delegate property right to the map, without creating wrapper delegate objects:

{% raw %}
<p></p>
{% endraw %}

```kotlin
import kotlin.properties.*
 
class Poll(val json: Map<String, *>) {
    val timestamp: Long by json
    val utc_timestamp: Long by json
    val error: String by json
}
```

{% raw %}
<p></p>
{% endraw %}

## Observable and vetoable properties

We have fixed a nuisance with observable delegates: the callback handler passed to observable property was called before the property value was changed. Now it is invoked after. It’s worth noting that callbacks are now inlined into these delegates, thus usages of observable and vetoable delegates now cost one object allocation less.
Read more about standard delegates in the [reference](http://kotlinlang.org/docs/reference/delegated-properties.html#standard-delegates) .
## Completing the change of Char arithmetic

In M13 we’re finalizing the semantic changes of arithmetic operations on the `Char` type. Only three arithmetic operations on `Char` are left:

* Char - Int → Char
* Char + Int → Char
* Char - Char → Int

All other binary operations involving `Char` were deprecated in M12 and now are dropped.
## Plus and minus operators for collections

`plus` operation on collections is not new, but it was defined so that its return type and behavior were not intuitive: for example, when adding an element to a set, you would receive a list having that element concatenated to all elements of the set, possibly resulting in that element to be duplicated.<br/>
Now return type of plus operation depends on the type of <em>first</em> operand:

* for Iterable, Collection and List the result is List, and operation is a concatenation
* for Array the result is Array, and operation is concatenation
* for Set the result is Set, and operation is inclusion of element(s) into the resulting set
* for Map the result is Map, and operation is inclusion of key-value pair(s) into the resulting map
* for Sequence the result is Sequence, and operation is lazy concatenation

Also we have introduced `minus` operation. It has the same relation between type of its first operand and its return type, and the following semantics:

* Collection - single_element returns the collection with the single occurrence of that element removed
* Collection - collection_of_elements returns the collection without all the elements contained in another collection.

## New scope functions: apply and run

Prior to M13 there were two so-called <em>scope functions</em> in the Standard Library: `let` and `with`. We call them scope functions, because their only purpose is to modify scope of a function passed as the last parameter. For example, to bring the parameter of scope function to the receiver of function parameter in case of `with`, and vice versa in case of `let`.<br/>
Now you have two more scope functions at your disposal:

* one that passes its receiver to the receiver of its function parameter:
T.run(f: T.() → R): R
We call it run, because it’s a generalization of run without receiver.
* one that applies given Unit-returning function to the receiver and returns the receiver itself:
T.apply(f: T.() → Unit): T

## Constructing open ranges

There was a common request to introduce right-open ranges in Kotlin. We have examined use-cases and found that most of them are involving integer ranges. In case of integers an opened at the end range can be represented with a closed range, whose end value is one less than the corresponding open range’s end.<br/>
To create such ranges you can use newly introduced [until](http://kotlinlang.org/api/latest/jvm/stdlib/kotlin/until.html) function. It returns closed range with values up to the specified end but not including it, so that:
`0 until 20 == 0..19`
## find vs firstOrNull

There were many debates about naming a function that finds the first element matching given predicate in a collection. `find` is easy to explore, but `firstOrNull` is consistent with how this operation is called in LINQ and Reactive Extensions. Prior to M13 `find` was deprecated in favor of `firstOrNull`, but now we’ve decided to “undeprecate” it and leave as a synonym for `firstOrNull`. Also we’ve provided `findLast`, which is a synonym for `lastOrNull`.
## Removing indentation from multiline string literals

A well-known pain with multiline string literals was the formatting: you couldn’t format a code containing these literals well without introducing whitespace into the literal itself.

{% raw %}
<p></p>
{% endraw %}

```kotlin
    val multiline = """First line
Second line
Third line"""
```

{% raw %}
<p></p>
{% endraw %}

Now we provide several functions to strip common whitespace prefix from each line of a string:<br/>
trimIndent, [trimMargin](http://kotlinlang.org/api/latest/jvm/stdlib/kotlin/trim-margin.html) , [replaceIndent](http://kotlinlang.org/api/latest/jvm/stdlib/kotlin/replace-indent.html) , [replaceIndentByMargin](http://kotlinlang.org/api/latest/jvm/stdlib/kotlin/replace-indent-by-margin.html) {% raw %}
<p></p>
{% endraw %}

```kotlin
    // first and last blank lines are removed,
    // and common indentation from other lines is stripped
    val multiline = """
      First line
      Second line
      Third line
    """.trimIndent()
```

{% raw %}
<p></p>
{% endraw %}

## Dropping deprecated API

In M13 we have dropped some of previously deprecated APIs: streams, extension methods for iterators, `FunctionalList`, `FunctionalQueue` and `StringTemplate`.
The full list of changes is available [here](https://quip.com/I4BbAdzPTzCx) .
# Plans for M14

## Distributing top-level functions between package parts

As we have announced [earlier](http://blog.jetbrains.com/kotlin/2015/06/improving-java-interop-top-level-functions-and-properties/) we’re changing the way how top-level functions and properties are mapped to class files in compiled code. In the next milestone all the top-level stuff in Standard Library is going to be distributed between corresponding package parts. We’ll keep the `KotlinPackage` facade class that contains all top-level functions, but it will be deprecated and removed in the future.
Note that these changes only affect usages of top-level Kotlin members from Java code. An inspection in the IDE will be provided to migrate these usages.
## What’s going to be dropped next

We’re still in the process of cleaning up deprecated APIs from the Standard Library and here is the list of what we are going to drop in the next milestone:

* size, empty and notEmpty extension properties;
* extensions makeString and appendString;
* methods to construct arrays and collections from provided elements: array, intArray, arrayList, hashMap, etc.

## kotlin-swing and kotlin-jdbc status

There were two experimental libraries: kotlin-swing and kotlin-jdbc. We’re not going to ship them anymore to the Maven Central repository. Last versions published to Maven would be compiled against M14.
If you depend on these libraries feel free to fork their source code and compile them locally. We have extracted them from the Kotlin codebase into separate repositories on GitHub under kotlin-projects organization:

* github.com/kotlin-projects/kotlin-jdbc
* github.com/kotlin-projects/kotlin-swing

