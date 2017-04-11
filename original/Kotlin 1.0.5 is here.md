---
title: Kotlin 1.0.5 is here
date: 2016-11-08 22:04:00
author: Dmitry Jemerov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2016/11/kotlin-1-0-5-is-here/
---

We’re happy to announce that we’ve just released Kotlin 1.0.5, which continues the series of bugfix and tooling updates for Kotlin 1.0.
We’d like to thank our external contributors whose pull requests were included in this release: Kirill Rakhman, Vladislav Golub, Vsevolod Tolstopyatov, Yoshinori Isogai, takahirom and gitreelike. Thanks to everyone who tried the EAP builds and sent us feedback, too!
The complete list of changes in the release can be found in the changelog. Some of the changes worth highlighting are:
### Loop to Lambda Conversion

The IntelliJ IDEA plugin can now detect many cases where imperative for loops can be rewritten in a more compact and idiomatic manner using standard library functions such as filter and map. As a simple example, the following snippet:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val result = arrayListOf<String>()
for (s in list) {
    if (s.isNotEmpty()) {
        result.add(s)
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

…will be automatically converted to:

{% raw %}
<p></p>
{% endraw %}

```kotlin
val result = list.filter { it.isNotEmpty() }
 
```

{% raw %}
<p></p>
{% endraw %}

To trigger the conversion, put the caret on the for keyword and press Alt-Enter.
### Postfix Code Completion

IntelliJ IDEA’s postfix code completion is now supported for Kotlin, with a large array of templates. Note that the feature depends on platform changes made in IntelliJ IDEA 2016.2 and is therefore unavailable in Android Studio 2.2; it will be supported in newer versions of Android Studio based on newer IntelliJ Platform versions.

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2016/11/1.0.5-postfixCompletion.png?ssl=1" rel="attachment wp-att-4358"><img alt="1-0-5-postfixcompletion" class="alignnone size-full wp-image-4358" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2016/11/1.0.5-postfixCompletion.png?resize=640%2C465&amp;ssl=1"/></a></p>
{% endraw %}

### New Refactorings

The Kotlin plugin now supports “Extract Interface” and “Extract Superclass” refactorings, which were previously only supported only for Java and some other languages, as well as an entirely new refactoring “Introduce Type Parameter”, providing an easy way to change a class or function into a generic one.

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2016/11/1.0.5-extractInterface.png?ssl=1" rel="attachment wp-att-4359"><img alt="1-0-5-extractinterface" class="alignnone size-full wp-image-4359" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2016/11/1.0.5-extractInterface.png?resize=640%2C363&amp;ssl=1"/></a></p>
{% endraw %}

### Android IDE Support Improvements

Kotlin 1.0.5 updates the Kotlin Lint checks to feature parity with Android Studio 2.2’s Java Lint checks, fixing a lot of issues in the process. It also adds a long-awaited feature: “Extract string resource” intention, allowing to move a hard-coded string literal from Kotlin code to a string resource file.

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2016/11/1.0.5-android-extract-string-resource.png?ssl=1" rel="attachment wp-att-4357"><img alt="1-0-5-android-extract-string-resource" class="alignnone size-full wp-image-4357" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2016/11/1.0.5-android-extract-string-resource.png?resize=640%2C188&amp;ssl=1"/></a></p>
{% endraw %}

### JavaScript Support Improvements

Kotlin 1.0.5 adds two major new features to the JavaScript backend:

* The @JsName annotation allows to control the names of JavaScript functions and properties generated from Kotlin code, making it much easier to call Kotlin-compiled code from plain JavaScript;
* Class literals (Foo::class) are now supported. The value of a ::class expression does not implement the full KClass API; it only defines a simpleName property to access the class name.

### How to update

To update the plugin, use Tools | Kotlin | Configure Kotlin Plugin Updates and press the “Check for updates now” button. Also, don’t forget to update the compiler and standard library version in your Maven and Gradle build scripts.
As usual, if you run into any problems with the new release, you’re welcome to ask for help on the forums, on Slack (get an invite here), or to report issues in the issue tracker.
Let’s Kotlin!
