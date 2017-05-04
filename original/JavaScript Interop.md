---
title: "JavaScript Interop"
date: 2014-12-24 09:57:00
author: Hadi Hariri
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2014/12/javascript-interop/
translator:
translator_url:
---

When working with JavaScript, i.e. creating a Kotlin application that compiles down to JavaScript, we often need to interoperate with existing libraries in JavaScript. While Kotlin already provides support for this, we’ve added a few more options in M10 to make interoperability even easier.<br/>
<span id="more-1766"></span>
## Dynamic support

In M10 we’ve added the **dynamic** keyword**[1]** which allows us to declare types as dynamic, permitting certain interoperability which previously could be more cumbersome. For instance, when working with jQuery, up to M10, our only option was to use the strongly typed libraries that Kotlin provides. As for M10 we can now use the dynamic keyword too

{% raw %}
<p></p>
{% endraw %}

```kotlin
jquery.getJSON(KotlinCommitsURL) { commits ->
  val commitsTable = jquery("#kotlin-commits")
  commits.forEach { commit ->
     commitsTable.append("""
                    <tr>
                        <td><a href=${commit.html_url}>${commit.sha.substring(0, 6)}</a></td>
                        <td>${commit.commit.message}</td>
                    </tr>""")
  }
}
```

{% raw %}
<p></p>
{% endraw %}

The code above calls <em>getJSON</em> function on <em>jQuery</em> to return a list of commits from GitHub. The function takes a lambda with a single parameter, which is the actual commits. Each entry in this list is in turn a commit entry with its own fields such as <em>html_url</em> or <em>commit.message</em>.
In the code <em>jQuery, commits</em> and <em>commit</em> are all dynamic, which means that anything we call on these will be resolved at runtime, i.e. by the JavaScript interpreter. This allows for two things:

* Not have to use a strongly-typed library to work with jQuery
* Be able to consume model that hasn’t previously been defined

The second ability is quite useful since it means that we don’t have to create intermediate strongly-typed classes to consume HTTP endpoints.
Of course, we could even use language constructs such as <em>for</em> loops to do the same thing, not only using the <em>forEach</em> extensions function.

{% raw %}
<p></p>
{% endraw %}

```kotlin
jquery.getJSON(KotlinCommitsURL) { commits ->
  val commitsTable = jquery("#kotlin-commits")
  for(commit in commits) {
    commitsTable.append("""
                    <tr>
                        <td><a href=${commit.html_url}>${commit.sha.substring(0, 6)}</a></td>
                        <td>${commit.commit.message}</td>
                    </tr>""")
   }
}
```

{% raw %}
<p></p>
{% endraw %}

In order for this code to work however, we still need to declare <em>jQuery</em> as dynamic, and mark it with the corresponding native equivalent for Kotlin to call

{% raw %}
<p></p>
{% endraw %}

```kotlin
native("$")
val jquery : dynamic = noImpl
```

{% raw %}
<p></p>
{% endraw %}

The <em>noImpl</em> is required since non-nullable variables in Kotlin need initializing, which in this case would be throwing an exception, however this never occurs since it is effectively being compiled down to JavaScript and called on the client-side. The <em>native</em> annotation which already existed pre-M10 is telling Kotlin what the identifier is equivalent to in JavaScript.
### Operators

When declaring dynamic types, certain operators act natively in JavaScript, such as for instance index accessors:

{% raw %}
<p></p>
{% endraw %}

```kotlin
elements: dynamic
// in Kotlin
elements[1]
```

{% raw %}
<p></p>
{% endraw %}

would be compiled to:

{% raw %}
<p></p>
{% endraw %}

```kotlin
elements[i]
```

{% raw %}
<p></p>
{% endraw %}

in JavaScript.
## Inlining JavaScript code

Another feature we added in M10 is the ability to inline some native JavaScript code in Kotlin code. We can do this using the <em>js</em> function:

{% raw %}
<p></p>
{% endraw %}

```kotlin
       jquery.getJSON(KotlinCommitsURL) { commits ->
          js("console.log('Calling JavaScript')")  
          val commitsTable = jquery("#kotlin-commits")
```

{% raw %}
<p></p>
{% endraw %}

The second line inserts <em>console.log(‘Calling JavaScript’)</em> in the output resulting from compilation, interlining JavaScript with Kotlin code.
## Language Injections

M10 also added Language Injection support in IntelliJ IDEA for Kotlin. And while this applies to any string and any language, not just JavaScript, it definitely proves useful when using <em>js</em>, allowing this:

{% raw %}
<p><img alt="js-string" class="aligncenter size-full wp-image-1776" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2014/12/js-string.png?resize=363%2C44&amp;ssl=1"/></p>
{% endraw %}

to look like this:

{% raw %}
<p><img alt="js-injected" class="aligncenter size-full wp-image-1775" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2014/12/js-injected.png?resize=379%2C48&amp;ssl=1"/></p>
{% endraw %}

when injecting JavaScript language:

{% raw %}
<p><img alt="inject-js" class="aligncenter size-full wp-image-1774" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2014/12/inject-js.png?resize=465%2C102&amp;ssl=1"/></p>
{% endraw %}

## Summary

In addition to <em>dynamic</em> and <em>js</em>, we also introduced support for <em>nativeGetter,nativeSetter</em> and <em>nativeInvoke</em> annotations for JavaScript, which we already covered in the [M10 release post](http://blog.jetbrains.com/kotlin/2014/12/m10-is-out/) .
These new features are all provided for better interoperability with JavaScript, but they do not trump any plans to continue to provide strongly-typed support for existing libraries and frameworks in JavaScript.
**[1]**<br/>
“dynamic” is a soft keyword:

* if it occurs in a non-type context, it’s an identifier
* in a type context, when followed by a dot (except for a dot that separates a receiver type from a function/property name) or an angle bracket <, it’s an identifier
* on the left-hand-side of :: in a callable reference: dynamic::foo implies that dynamic there is a normal identifier

