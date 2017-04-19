---
title: "Kotlin M2 Candidate"
date: 2012-06-04 08:53:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2012/06/kotlin-m2-candidate/
---

It’s been seven weeks since [Kotlin M1 release](http://blog.jetbrains.com/kotlin/2012/04/kotlin-m1-is-out/) , and I’m happy to invite you to try out a candidate build of <strong>Kotlin M2</strong>! This post gives an overview of the upcoming milestone release along with come usage instructions.
## Thank you, M1!

Our M1 build did a pretty good job: got about [800 downloads](http://plugins.intellij.net/plugin/?id=6954) , and brought extensive feedback in our [forum](http://devnet.jetbrains.com/community/kotlin) and [issue tracker](http://youtrack.jetbrains.net/issues/KT) .
Seems like you have had some fun with it, and we are aiming at even more fun <img alt=":)" class="wp-smiley" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/wp-includes/images/smilies/simple-smile.png?w=640&amp;ssl=1" style="height: 1em; max-height: 1em;"/>
## What’s new


* Little Things
* Language Features
* JavaScript
* Android
* How to Install the Candidate Build


{% raw %}
<p><span id="more-550"></span></p>
{% endraw %}

## Little Things

As usual, it’s been [a lot of bugs fixed](http://youtrack.jetbrains.com/issues/KT?q=resolved+date%3A+2012-04-12+..+2012-06-07) . I’d like to point out that we are working on the IDE performance. It has been somewhat improved in M2, and will get to its real speed by the next milestone.
## Language Features

Kotlin now respects <strong>visibility modifiers</strong>. We have four of them:

* private, protected, public — as usual,
* internal — visible inside a module (that is more than a package).

You can now pass an <strong>array of values to a vararg-function</strong>:

{% raw %}
<p></p>
{% endraw %}

```kotlin
fun printAll(vararg a : String) {
    for (item in a) println(item)
}
 
fun main(args: Array<String>) {
    printAll("one", "two")
    printAll(*args)
}
```

{% raw %}
<p></p>
{% endraw %}

The <strong>spread</strong> operator “converts” an array into a vararg-list. Unlike Java, this does not present any ugly corner-cases.
There will a few more nice things shortly.
## JavaScript Support in the IDE

While you can still play with Kotlin directly in your browser with [Kotlin Web Demo](http://kotlin-demo.jetbrains.com) , there’s now a real IDE for Kotlin compiled to JavaScript.
When you [install the M2 Candidate build of the IntelliJ IDEA plugin](#install) , follow these instructions to try out some Kotlin-to-JS compilation:

* Check out kotlin-js-hello project from github
* Open it as an IntelliJ IDEA project
* Set it up as a Kotlin-JS project
* Select your favorite browser and run. The result will open in the browser.
* Have fun editing the JavaScript file as you like and re-running…

Currently, the API documentation is only being prepared. Meanwhile, you can study Kotlin’s JS APIs [here](https://github.com/JetBrains/kotlin/tree/master/js/js.libraries/src) .
## Android

After fixing some bugs and finding out a lot of interesting stuff (special thanks to [Aleksandro Eterverda](https://github.com/eterverda) ), we are ready to run Kotlin on Android!

{% raw %}
<p style="text-align: center"><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/06/KotlinDroid.png"><img alt="" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2012/06/KotlinDroid.png?resize=250%2C136&amp;ssl=1"/></a></p>
{% endraw %}


* You’ll need Android SDK installed and set up
* IDE support for Android is available in the Open Source version of IntelliJ IDEA
* Install the M2 Candidate build of the IntelliJ IDEA plugin
* For a quick start, check out kotlin-android-hello project from github
* Set up your run configuration, and run the project (step-by-step here)
* Enjoy

Some other Kotlin programs running on Android:

* We are working on porting standard Android samples to Kotlin: kotlin-samples-for-android. Feel free to contribute!
* Vladimir Lichonos assembled a set of useful Kotlin utilities for Android: kotlinAndroidLib

## How to Install the Candidate Build


* Get IntelliJ IDEA (Community or Ultimate) version 11.1.

If you want to separate your work environment from your Kotlin experiments, follow the instructions from here
* If you want to separate your work environment from your Kotlin experiments, follow the instructions from here
* Set up the Integration Build Plugin Repository and install the plugin. Step-by-step instructions here.

## As usual, your feedback is very welcome. Have a nice Kotlin!


{% raw %}
<hr/>
{% endraw %}


{% raw %}
<p> </p>
{% endraw %}

Portions of this page are modifications based on work created and [shared by Google](http://code.google.com/policies.html) and used according to terms described in the [Creative Commons 3.0 Attribution License](http://creativecommons.org/licenses/by/3.0/) .
