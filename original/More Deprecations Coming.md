---
title: "More Deprecations Coming"
date: 2015-04-06 12:55:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/04/more-deprecations-coming/
translator:
translator_url:
---

There are two more items on the language cleanup list: backing-field syntax and static type assertion operator.<span id="more-2040"></span>
## Backing Fields

When you have a property and you don’t implement at least one of its accessors (`get` or `set`) manually, such a property gets a <em>backing field</em>, i.e. a piece of storage holding its value:

{% raw %}
<p></p>
{% endraw %}

```kotlin
var foo: Foo? = null
    set(v) {
        ...
    }
    // default getter is used
 
```

{% raw %}
<p></p>
{% endraw %}

you can access the backing field through the name of the property prefixed with the `$` sign:

{% raw %}
<p></p>
{% endraw %}

```kotlin
$foo = 2
 
```

{% raw %}
<p></p>
{% endraw %}

This may be needed to bypass the custom accessor(s).
This feature is rather rarely used, and also clashes visually with string templates (`"$foo"`, surprisingly, has nothing to do with backing fields), so we want to get rid of it.
In case you really need it, your workaround is <em>backing property</em>:

{% raw %}
<p></p>
{% endraw %}

```kotlin
private var _backing: Foo? = null
var foo: Foo?
    get() = _backing
    set(v) {
        ...
    }
 
```

{% raw %}
<p></p>
{% endraw %}

Since no getters or setters are generated for private properties, the resulting byte code will be exactly the same.
## Static Type Assertions

Another rarely used feature is the following syntax:

{% raw %}
<p></p>
{% endraw %}

```kotlin
foo(bar, null: Baz)
 
```

{% raw %}
<p></p>
{% endraw %}

The type after colon in an expression specifies the <em>expected static type</em> of it, i.e. this is not a cast, but simply an instruction to the compiler to make sure that the static type of this expression is actually “Bar”. The fact that it’s hard to explain has something to do with this being rarely used (I think Kotlin’s test data is the only major client). So, we are withdrawing this syntax, and maybe will make use of it later (possibilities include array/list slices and C-style ternary conditionals).
In case you needed this syntax to disambiguate your overloads, `as` is a good workaround.
