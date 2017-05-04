---
title: "[译]More Deprecations Coming"
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

语言清理列表中还有两个项目：后台字段语法和静态类型断言运算符。<span id =“more-2040”> </span>
## 背景领域

当你有一个属性并且你不手动实现它的至少一个访问器（`get`或`set`）时，这样一个属性得到一个< em>，即一个保存其值的存储器：

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

您可以通过前缀为`$`符号的属性名称访问备份字段：

{% raw %}
<p></p>
{% endraw %}

```kotlin
$foo = 2
```

{% raw %}
<p></p>
{% endraw %}

这可能需要绕过自定义访问器。
这个功能很少使用，并且与字符串模板（`“$ foo”`）的视觉冲突，令人惊讶的是，与支持字段无关），所以我们想要摆脱它。
如果您真的需要它，您的解决方法是支持属性</em>：

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

由于不为私有属性生成getter或setter，所以产生的字节代码将是完全相同的。
## 静态类型断言

另一个很少使用的功能是以下语法：

{% raw %}
<p></p>
{% endraw %}

```kotlin
foo(bar, null: Baz)
```

{% raw %}
<p></p>
{% endraw %}

表达式中冒号后面的类型指定了<em>预期的静态类型</em>，即这不是一个转换，而只是一个指令给编译器以确保该表达式的静态类型实际上是“Bar “。很难解释这个事实与这很少使用有关（我认为Kotlin的测试数据是唯一的主要客户）。所以，我们正在撤回这种语法，也许稍后会使用它（可能包括数组/列表切片和C样式三元条件）。
如果您需要这种语法来消除您的重载错误，`作为`是一个很好的解决方法。
