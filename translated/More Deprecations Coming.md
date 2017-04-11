---
title: [译]More Deprecations Coming
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
---

语言清理列表中还有两个项目：后台字段语法和静态类型断言运算符。
## 背景领域

当你有一个属性并且你不手动实现它的至少一个访问者（获取或设置）时，这样的属性将获得一个后备字段，即一个保存其值的存储：

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

您可以通过以$符号为前缀的属性名称访问支持字段：

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
这个功能很少使用，并且还会与字符串模板（“$ foo”，意外的是与支持字段无关）与视觉冲突，所以我们想摆脱它。
如果您真的需要它，您的解决方法是备份属性：

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

一个表达式中的冒号后面的类型指定了它的预期静态类型，即这不是一个转换，而只是一个指令给编译器以确保该表达式的静态类型实际上是“Bar”。很难解释这个事实与这很少使用有关（我认为Kotlin的测试数据是唯一的主要客户）。所以，我们正在撤回这种语法，也许稍后会使用它（可能包括数组/列表切片和C样式三元条件）。
如果你需要这个语法来消除你的重载，这是一个很好的解决方法。
