---
title: "[译]Spek – A Specification Framework"
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
---

一会儿现在，a [很少](http://twitter.com/orangy) [的](http://twitter.com/jonyzzz) [我们](https://plus.google.com/111179551284404865949/about) 一直在开发一个名为Spek的项目，这个框架允许您编写可执行规范。它允许您以更人性化的方式编写规范（即测试），而且更重要的是描述性的方式，而无需使用长测试名称，下划线或正则表达式。

{% raw %}
<p><span id="more-1421"></span></p>
{% endraw %}

现在已经达到了其第一个里程碑，它足够适合开始在项目中使用，我们准备好反馈和功能要求！它甚至有它的 [自己的网站](http://jetbrains.github.io/spek) 。
## 简要介绍

Spek是一个规范框架。如果您熟悉茉莉花，摩卡，RSpec或机器规格，那么您将立即看到相似之处。

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2014/02/image2.png?resize=554%2C359&amp;ssl=1" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;border: 0px" title="image"/></p>
{% endraw %}

如果你不熟悉，请简单解释一下：

* 给定 - 建立测试的上下文，即排列
* 开 - 执行动作，即Act
* 它 - 验证结果，即Assert

Spek允许您在相同的上下文中拥有多个动作。这是针对相同的<em> </ em>，您可以拥有多个<em>的<em>。它也允许你对同一个动作有更多的断言（<em>它）</ em>。
## 斯派克不仅仅是Kotlin

斯派克写在Kotlin。您写的规格也将在Kotlin。但是，由于Kotlin与Java完全兼容，您可以使用Spek测试新的和现有的Java代码。
## 如何运行？

IntelliJ IDEA支持Spek，TeamCity也是如此。还有一个控制台运行器，输出文本和HTML（需要改进）。

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2014/02/image3.png?resize=553%2C227&amp;ssl=1" style="padding-top: 0px;padding-left: 0px;padding-right: 0px;border: 0px" title="image"/></p>
{% endraw %}

## 尝试一下

希望你喜欢你看到的，转过身来 [Spek网站](http://jetbrains.github.io/spek) 了解更多。它仍然在“EAP”，所以报告的问题越多越好。而且由于它是OSS（Apache 2） [贡献不止一个](http://github.com/jetbrains/spek) 。
