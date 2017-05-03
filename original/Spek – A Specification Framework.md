---
title: "Spek – A Specification Framework"
date: 2014-02-17 17:20:00
author: Hadi Hariri
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2014/02/speka-specification-framework/
translator:
translator_url:
---

For a while now, a [few](http://twitter.com/orangy) [of](http://twitter.com/jonyzzz) [us](https://plus.google.com/111179551284404865949/about) have been working on a project called Spek, a framework that allows you to write executable specifications. It allows you to write specifications (i.e. tests) in a more human-readable, and what’s more important, descriptive manner, without having to resort to long test names, underscores or regular expressions.

{% raw %}
<p><span id="more-1421"></span></p>
{% endraw %}

It’s now reached its first milestone where it’s suitable enough to start being used on projects and we’re ready for feedback and feature requests! It even has its [own site](http://jetbrains.github.io/spek) .
## A brief introduction

Spek is a Specification Framework. If you’re familiar with Jasmine, Mocha, RSpec or Machine Specifications, then you’ll immediately see the resemblance.

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2014/02/image2.png?resize=554%2C359&amp;ssl=1" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;border: 0px" title="image"/></p>
{% endraw %}

If you’re not familiar, let me briefly explain:

* Given – Establish the context of the test, i.e, Arrange
* On – Execute the action, i.e. Act
* It – Validate the results, i.e. Assert

Spek allows you to have more than one action for the same context. That is for the same <em>given </em>you can have multiple <em>on’s</em>. It also allows you to have more than assertion (<em>it) </em>for the same action.
## Spek is not only for Kotlin

Spek is written in Kotlin. Specifications you write will also be in Kotlin. However, as Kotlin is 100% compatible with Java, you can test new and existing Java code with Spek.
## How do I run it?

IntelliJ IDEA supports Spek, so does TeamCity. There’s also a console runner which outputs Text and HTML (needs improvement).

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2014/02/image3.png?resize=553%2C227&amp;ssl=1" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;border: 0px" title="image"/></p>
{% endraw %}

## Try it

Hoping that you like what you see, head over to the [Spek web site](http://jetbrains.github.io/spek) to find out more. It’s still in “EAP” so the more issues reported, the better. And since it’s OSS (Apache 2) [contributions are more than welcome](http://github.com/jetbrains/spek) .
