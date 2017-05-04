---
title: "Announcing Anko for Android"
date: 2015-04-08 16:20:00
author: Hadi Hariri
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/04/announcing-anko-for-android/
translator:
translator_url:
---

We’re excited to announce a library we’ve been working on for Android development, which, among other things allows the creation of Application Interfaces in a type-safe and dynamic way using a DSL.
## A Sample Taste

Here is a small example describing some of Anko’s possibilities. Imagine we need to create a simple sign-up form consisting of an `EditText` for a username and a “Sign up” `Button`. The code for this, using Anko would be:

{% raw %}
<p></p>
{% endraw %}

```kotlin
import kotlinx.android.anko.*
 
class MainActivity : Activity() {
 
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
 
        verticalLayout {
            padding = dip(16)
            textView("Username:") {
                textSize = 18f
            }.layoutParams { verticalMargin = dip(4) }
 
            val login = editText()
 
            button("Sign up") {
                textSize = 20f
                onClick { login(login.text) }
            }.layoutParams { topMargin = dip(8) }
        }
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}


{% raw %}
<p><span id="more-1999"></span></p>
{% endraw %}

Anko makes extensive use of Kotlin’s [extension functions and properties](http://kotlinlang.org/docs/reference/extensions.html) arranged into [type-safe builders](http://kotlinlang.org/docs/reference/type-safe-builders.html) to describe the user interface. In return, we get conciseness and type-safety at compile time.
Of course, we can also see a preview during design time using the Anko Preview plugin, available for both IntelliJ IDEA and Android Studio:

{% raw %}
<p><img alt="Anko Designer" class="aligncenter size-full wp-image-2007" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/04/Screen-Shot-2015-04-02-at-00.33.22.png?resize=640%2C481&amp;ssl=1"/></p>
{% endraw %}

If we now want to add another text input widget, for instance an email, we could probably create another  pair of `textView()` and `editText()` function calls. However, a nicer approach would be to extract the corresponding DSL fragment into a new function:

{% raw %}
<p></p>
{% endraw %}

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
 
    verticalLayout {
        padding = dip(16)
        val login = inputField("Username")
        val email = inputField("E-mail")
 
        button("Sign up") {
            textSize = 20f
            onClick { login(login.text) }
        }.layoutParams { topMargin = dip(8) }
    }
}
 
fun _LinearLayout.inputField(name: String): TextView {
    textView("$name:") {
        textSize = 18f
    }.layoutParams { verticalMargin = dip(4) }
    return editText()
}
 
```

{% raw %}
<p></p>
{% endraw %}

Any additional inputs only require a single function call.
End result of the form would be:

{% raw %}
<p><img alt="Anko result form" class="aligncenter size-full wp-image-2009" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/04/layout-2015-04-02-014006.png?resize=384%2C640&amp;ssl=1"/></p>
{% endraw %}

### Partially defined listeners

Anko is very helpful when you are using Android listeners with lots of methods. Consider the following code written that does not use Anko:

{% raw %}
<p></p>
{% endraw %}

```kotlin
seekBar.setOnSeekBarChangeListener(object: OnSeekBarChangeListener {
  override fun onProgressChanged(seekBar: SeekBar, progress: Int, fromUser: Boolean) {
    // Something
  }
  override fun onStartTrackingTouch(seekBar: SeekBar?) {
    // Just an empty method
  }
  override fun onStopTrackingTouch(seekBar: SeekBar) {
    // Another empty method
  }
})
 
```

{% raw %}
<p></p>
{% endraw %}

Here’s the version using Anko:

{% raw %}
<p></p>
{% endraw %}

```kotlin
seekBar {
  onProgressChanged { (seekBar, progress, fromUser) ->
    // Something
  }
}
 
```

{% raw %}
<p></p>
{% endraw %}

Methods that have empty bodies no longer require, well, empty implementations. Also, if setting `onProgressChanged()` and `onStartTrackingTouch()` for the same View, these two “partially defined” listeners will be merged.
## More than a DSL

Anko is not just a DSL but a library which facilitates Android development in different areas. It has many methods covering dialogs, asynchronous tasks, services, intents and even SQLite database access.
For instance, if you want to start a new `Activity`:

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Without Anko
val intent = Intent(this, javaClass<MyActivity>())
intent.putExtra("id", 5)
startActivity(intent)
 
// With Anko
startActivity<MyActivity>("id" to 5)
 
```

{% raw %}
<p></p>
{% endraw %}

Or activate vibrator:

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Without Anko
val vibrator = getSystemService(Context.VIBRATOR_SERVICE) as Vibrator
vibrator.vibrate(500)
 
// With Anko
vibrator.vibrate(500)
 
```

{% raw %}
<p></p>
{% endraw %}

Or even send a toast message:

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Without Anko
Toast.makeText(this, "Download is complete!", Toast.LENGTH_SHORT).show()
 
// With Anko
toast("Download is complete!")
 
```

{% raw %}
<p></p>
{% endraw %}

### Existing code support

You can keep your old classes written in Java. Moreover, if you still want (or have) to write a Kotlin activity class and inflate an XML layout for some reason, you can use `View` properties and listener helpers which would make things easier:

{% raw %}
<p></p>
{% endraw %}

```kotlin
name.hint = "Enter your name"
name.onClick { /* do something */ }
 
```

{% raw %}
<p></p>
{% endraw %}

## Benefits of Anko

Hopefully you can see that Anko offers a series of benefits, in particular:

* Everything is in one place. Instead of splitting layouts into static (XML) and dynamic parts and then trying to tie them together, we can just write everything we want using Kotlin. Compile-time type checking is a sweet bonus.
* Anko can make our code more concise and readable.
* It allows for easy re-use. We can just extract a part of the DSL into a function and use it multiple times.

## Give it a try!

Anko is still in alpha stage but we want to release early to get your feedback, so please give it a try. We’ve made it as simple as possible to do so. It’s all published on Maven Central, and if you’re using Gradle, you can easily add the required dependencies to the `build.gradle` file:

{% raw %}
<p></p>
{% endraw %}

```kotlin
dependencies {
  compile 'org.jetbrains.anko:anko:0.5-15'
}
 
```

{% raw %}
<p></p>
{% endraw %}

The Anko Preview plugin is available both for IntelliJ IDEA and Android Studio. You can [download](https://plugins.jetbrains.com/plugin/7734) it directly from the Plugin Repository.
There are binaries targeting both raw Android (SDK version 15, Ice Cream Sandwich) and Android with a support-v4 package.
Also, last but not least, much like everything related to Kotlin, Anko is fully Open Source. The repository is on [GitHub](https://github.com/JetBrains/anko) and as always, contributions are welcome!
