---
title: "Anko 0.6 is Released"
date: 2015-04-30 12:31:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/04/anko-0-6-is-released/
translator:
translator_url:
---

Today we are glad to present the new version of [Anko](https://github.com/JetBrains/anko) — a library which facilitates Android application development. We are happy to have received lots of feedback, and some of the changes in [0.6](https://github.com/JetBrains/anko/releases/tag/v0.6) were actually proposed by the community.<br/>
<span id="more-2124"></span>
## WARNING: Package Name Changed

Well, we are sorry. For historical reasons, Anko package name used to be `kotlinx.android.anko`, and we changed it to `org.jetbrains.anko` in 0.6, to be consistent with the Maven artifact name.
## New Listeners

Anko 0.5 introduced partially defined listeners that reduce code verbosity: when we only need to define one method of a multi-methods listener, we do not have to implement the methods we do not care about. Based on your feedback (thanks, [SalomonBrys](https://github.com/SalomonBrys) !) this feature has been redesigned in 0.6:

* Partially defined listeners can be now used outside DSL layouts as well as inside;
* Syntax is easier to understand;
* The logic “under the hood” is simpler.

This is what it looks like now:

{% raw %}
<p></p>
{% endraw %}

```kotlin
editText {
    textChangedListener {
        onTextChanged { text, start, before, count ->
            toast("New text: $text")
        }
    }
}
```

{% raw %}
<p></p>
{% endraw %}

## Configuration Qualifiers [Qualifiers](http://developer.android.com/guide/topics/resources/providing-resources.html#AlternativeResources) are used to support different layouts for different devices, locales etc.
Anko’s DSL now supports the `configuration()` function that specifies qualifiers the layout is meant for:

{% raw %}
<p></p>
{% endraw %}

```kotlin
configuration(screenSize = ScreenSize.LARGE, orientation = Orientation.LANDSCAPE) {
    /*
      This code will be only executed
      if the screen is large and its orientation is landscape
    */
}
```

{% raw %}
<p></p>
{% endraw %}

This code is equivalent to having your XML layout under the `layout-large-land` directory. Technically, it is implemented through checking the specified qualifiers and only executing the code inside the `configuration()` if their values match. Therefore, usages of `configuration()` are not limited to DSL only: for example, you can safely call Android SDK functions which are not present in older versions of system using `configuration(fromSdk = &lt;version&gt;) { /* code  */ }`.
The full list of supported qualifiers is available [here](https://github.com/JetBrains/anko/blob/master/doc/ADVANCED.md#configuration-qualifiers) .
## Custom View Creation

The neatest way of incorporating your own custom views into the DSL is to create your own [builder-like functions](https://github.com/JetBrains/anko/blob/master/doc/ADVANCED.md#extending-anko) , but since it is time-consuming, Anko now supports a quicker way:

{% raw %}
<p></p>
{% endraw %}

```kotlin
frameLayout {
    customView<CustomView> {
        backgroundResource = R.drawable.custom_view_bg
    }.linearLayout(width = matchParent)
}
```

{% raw %}
<p></p>
{% endraw %}

It is implemented via Java Reflection. Though it is slower than the normal DSL functions, it is much easier when you are prototyping.
## appcompat.v7 Views and Properties

We have made an initial step to support `appcompat.v7` Android library. Extension functions for `View` classes in the support package and extension properties for its attributes are added to Anko. [Widget tinting](http://android-developers.blogspot.ru/2014/10/appcompat-v21-material-design-for-pre.html) is not supported yet, we are hoping to implement it in later versions.
## Top-level DSL Functions for Simple Views are Removed

Since it is very unlikely to have a simple non-container view (such as TextView) as the content view of your activities, we removed DSL functions for such views for the `Activity` and `Fragment` receivers. In the unlikely case of needing such a view on the top level, use `UI()` wrapper function:

{% raw %}
<p></p>
{% endraw %}

```kotlin
UI {
    textView(R.string.name)
}
```

{% raw %}
<p></p>
{% endraw %}

## Your Feedback is Welcome

Anko is licensed under Apache Licence 2.0, and the project is [available on Github](https://github.com/JetBrains/anko) .<br/>
Your feedback and pull requests are welcome!
