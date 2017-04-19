---
title: "[译]More changes: Enum Syntax, Another Deprecation and More"
date: 2015-04-07 13:34:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/04/more-changes-enum-syntax-and-one-deprecation-and-more/
---


{% raw %}
<p><a name="enum-syntax"></a></p>
{% endraw %}

## 枚举语法

目前，与非平凡构造函数的枚举的语法有点怪异：

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Message(val str: String) {
    ERROR : Message("This is an error")
    WARNING : Message("This is a friendly warning")
    DEBUG : Message("Ignore this")
}
 
```

{% raw %}
<p></p>
{% endraw %}


{% raw %}
<p><span id="more-2042"></span></p>
{% endraw %}

我们真的希望使它更好，例如这样的：

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Message(val str: String) {
    ERROR("This is an error")
    WARNING("This is a friendly warning")
    DEBUG("Ignore this")
}
 
```

{% raw %}
<p></p>
{% endraw %}

现在有一些技术性，即枚举可以有其他成员：

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Example(...) {
    A(...)
    B(...)
 
    fun foo() { ... }
}
 
```

{% raw %}
<p></p>
{% endraw %}

问题是可以将<code> A </ code>和<code> B </ code>解析为<code> foo（）</ code>上的注释。所以我们在这里有一些选择。
我们倾向于在条目和其他成员之间放置一个分隔符：

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Example(...) {
    A(...)
    B(...)
    ; // this is mandatory
 
    fun foo() { ... }
}
 
```

{% raw %}
<p></p>
{% endraw %}

只有当一些成员遵循分号时才需要分号。
其他选项包括要求对成员的所有注释进行转义（也可能是修饰符）：

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Example(...) {
    A(...)
    B(...)
 
    @inject fun foo() { ... }
}
 
```

{% raw %}
<p></p>
{% endraw %}

这与普通课程，特质等有些不一致
或者我们可以使用（soft-）关键字对enum条目进行前缀：

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Example {
    entry A
    entry B
}
 
```

{% raw %}
<p></p>
{% endraw %}

这看起来太冗长了
另一个问题是我们如何自己注释枚举条目。需要逃脱看起来合理：

{% raw %}
<p></p>
{% endraw %}

```kotlin
enum class Example {
    @Ann1 A
    @Ann2(...) B    
}
 
```

{% raw %}
<p></p>
{% endraw %}

其他选项包括

* 需要枚举文字之间的逗号（像Java一样）
* 需要在枚举文字之间设置换行符并允许在同一行上使用未转义的注释

我们还没有决定哪一种方式。

{% raw %}
<p><a name="break-continue"></a></p>
{% endraw %}

## 禁止在表达式中断/继续

当</ code> -expressions作为</ code> -entry跳转到下一个<code>时，我们计划在<code>中实现<code> continue </ code>。它还没有实现，但是当我们添加代码时，我们希望您的代码保持不变，因此暂时在<code>中禁止在<code>中使用<code>继续</ code>，而不使用指向的标签循环：

{% raw %}
<p></p>
{% endraw %}

```kotlin
loop@
for (...) {
    when (...) {
        ... -> if (...) continue@loop else ... // OK
        ... -> if (...) continue // ERROR
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

我们还禁止<code>中的<code> break </ code> </ code>。虽然还没有决定是否要允许它，但似乎更好的设计是保持<code> break </ code>和<code> continue </ code>对称。
注意：当</ code>在“停止匹配并跳出外部”（如Java和C中的<code> switch </ code>）中时，<code> break </ code>的简单解释，但是<code>当</ code>经常返回一个值时，如果我们突破它，这将是未知的。

{% raw %}
<p><a name="interfaces"></a></p>
{% endraw %}

## 将特征重命名为接口

那么我们很久以前就选择了这些名字，现在我们在Kotlin中所说的“特质”并不是一个特质，就像现在的Java接口一样，所以我们不想使用<code> trait < / code>关键字，并在M12中引入<code> interface </ code>。
反馈请求：让火焰开始<img alt =“:)”class =“wp-smiley”data-recalc-dims =“1”src =“https://i2.wp.com/blog.jetbrains.com/ kotlin / wp-includes / images / smilies / simple-smile.png？w = 640＆amp; ssl = 1“style =”height：1em; max-height：1em“
