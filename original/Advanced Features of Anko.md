---
title: "Advanced Features of Anko"
date: 2015-05-06 10:34:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/05/advanced-features-of-anko/
translator:
translator_url:
---

Last week we published [a new version](http://blog.jetbrains.com/kotlin/2015/04/anko-0-6-is-released/) of Anko. While the main purpose of this library is creating layouts though a DSL, even the users of XML layouts can benefit from it. Today we are going to talk about such “ambivalent” features of Anko.<span id="more-2135"></span>
## Intent Helpers

The common way of starting a new `Activity` is to create an `Intent`, maybe put some parameters into it, and finally pass the created `Intent` to the `startActivity()` method of a `Context`.

{% raw %}
<p></p>
{% endraw %}

```kotlin
val intent = Intent(this, javaClass<SomeActivity>())
intent.putExtra("id", 5)
intent.putExtra("name", "John")
startActivity(intent)
 
```

{% raw %}
<p></p>
{% endraw %}

With Anko we can do this in exactly one line of code:

{% raw %}
<p></p>
{% endraw %}

```kotlin
startActivity<SomeActivity>("id" to 5, "name" to "John")
 
```

{% raw %}
<p></p>
{% endraw %}

`startActivity()` function accepts key-value pairs that will be passed as `Intent` extra parameters. Another function, `startActivityForResult()` with similar semantics is also available.
Please refer to the [Intent Builder Functions](https://github.com/JetBrains/anko/blob/master/doc/ADVANCED.md#intent-builder-functions) reference section for more information.
## Popular Intent Shorthands

Almost every application has code that loads a page in the default web browser or opens a new email screen using Android intents, so there are helper functions for this in Anko:

{% raw %}
<p></p>
{% endraw %}

```kotlin
browse("http://somewebsite.org (http://somewebsite.org/)")
email("admin@domain.net (mailto:admin@domain.net)", "Here I am!", "Message text")
 
```

{% raw %}
<p></p>
{% endraw %}

Other useful intents are described under the [Useful Intent Callers](https://github.com/JetBrains/anko/blob/master/doc/ADVANCED.md#useful-intent-callers) reference section.
## Alert Dialogs

Anko provides a declarative way of creating alert dialogs with text messages, lists, progress bars and even with your own DSL layout.
For a simple text alert with a couple of buttons at the bottom, all you need is:

{% raw %}
<p></p>
{% endraw %}

```kotlin
alert("Order", "Do you want to order this item?") {
    positiveButton("Yes") { processAnOrder() }
    negativeButton("No") { }
}.show()
 
```

{% raw %}
<p></p>
{% endraw %}

There is a function that creates and shows a list dialog:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val flowers = listOf("Chrysanthemum", "Rose", "Hyacinth")
selector("What is your favorite flower?", flowers) { i ->
    toast("So your favorite flower is ${flowers[i]}, right?")
}
 
```

{% raw %}
<p></p>
{% endraw %}

Both indeterminate and basic progress dialogs are supported:

{% raw %}
<p></p>
{% endraw %}

```kotlin
progressDialog("Please wait a minute.", "Downloading…")
indeterminateProgressDialog("Fetching the data…")
 
```

{% raw %}
<p></p>
{% endraw %}

Also, as mentioned above, you can use Anko’s DSL in dialogs to create a custom layout:

{% raw %}
<p></p>
{% endraw %}

```kotlin
alert {
    customView {
        verticalLayout {
            val familyName = editText {
                hint = "Family name"
            }
            val firstName = editText {
                hint = "First name"
             }
             positiveButton("Register") { register(familyName.text, firstName.text) }
         }
    }
}.show()
 
```

{% raw %}
<p></p>
{% endraw %}

## Services

Android system services, such as `WifiManager`, `LocationManager` or `Vibrator`, are available in Anko through extension properties for the `Context`:

{% raw %}
<p></p>
{% endraw %}

```kotlin
if (!wifiManager.isWifiEnabled()) {
    vibrator.vibrate(200)
    toast("Wifi is disabled. Please turn on!")
}
 
```

{% raw %}
<p></p>
{% endraw %}

## Asynchronous Tasks

Probably the most popular way to execute code in the background is to subclass an `AsyncTask`. But, despite of its popularity, it is inconvenient in many ways. Anko has several functions which practically do the same but are easier to use.
`async() {...}` function executes code inside `{}` under the `ThreadExecutor`. You can use the default one or pass your own.

{% raw %}
<p></p>
{% endraw %}

```kotlin
async(someExecutor) { // omit the parameter to use the default executor
// This code will be executed in background
}
 
```

{% raw %}
<p></p>
{% endraw %}

If you want to go back to the UI thread inside `async()`, you can use `uiThread()` function.

{% raw %}
<p></p>
{% endraw %}

```kotlin
async {
    // Do some work
    uiThread {
        toast("The work is done!")
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

`uiThread()` has a special semantics inside `async()`: `async()` does not hold a `Context` instance but only a `WeakReference` to it, so even if lambda execution never finishes, the `Context` instance will not leak.

{% raw %}
<p></p>
{% endraw %}

```kotlin
async {
    uiThread {
        /* Safe version. This code won't be executed
            if the underlying Context is gone. */
    }
    ctx.uiThread {
    /* Here we are calling the `uiThread`
        extension function for Context directly,
        so we are holding a reference to it. */
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

## Logging

Android SDK provides the `android.util.Log` class which consists of a few logging methods. Usage is straightforward but the methods require passing a tag argument, and the actual log message must be a `String`. You can get rid of this by using the `AnkoLogger` trait:

{% raw %}
<p></p>
{% endraw %}

```kotlin
class SomeActivity : Activity(), AnkoLogger {
    fun someMethod() {
        info("Info message")
        debug(42) // .toString() method will be called automatically
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

The default tag name is a class name (`SomeActivity` in this case), but you can easily change it by overriding the `loggerTag` property of `AnkoLogger`.
Each method has two versions: plain and “lazy” (lambda will be executed only if `Log.isLoggable(tag, Log.INFO)` is `true`).

{% raw %}
<p></p>
{% endraw %}

```kotlin
info("String " + "concatenation")
info { "String " + "concatenation" }
 
```

{% raw %}
<p></p>
{% endraw %}

You can read more about logging in the [Logging](https://github.com/JetBrains/anko/blob/master/doc/ADVANCED.md#logging) reference section.
## Conclusion

To try `Anko`, follow [these instructions](https://github.com/JetBrains/anko#using-with-gradle) .
And as usual, your feedback is very welcome.
