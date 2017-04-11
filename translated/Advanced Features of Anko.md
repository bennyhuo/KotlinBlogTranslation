---
title: [译]Advanced Features of Anko
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
---

上周我们发布了一个新版本的安科。虽然该库的主要目的是通过DSL创建布局，但即使是XML布局的用户也可以从中受益。今天我们要谈论安科的这种“矛盾”特征。
## 意向助手

启动一个新的Activity的常见方法是创建一个Intent，也许把一些参数放入它，最后将创建的Intent传递给Context的startActivity（）方法。

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

有了安科，我们可以在一行代码中做到这一点：

{% raw %}
<p></p>
{% endraw %}

```kotlin
startActivity<SomeActivity>("id" to 5, "name" to "John")
 
```

{% raw %}
<p></p>
{% endraw %}

startActivity（）函数接受将作为Intent额外参数传递的键值对。另一个函数startActivityForResult（）具有类似的语义也是可用的。
有关详细信息，请参阅Intent Builder函数参考部分。
## 热门意图

几乎每个应用程序都有代码，在默认的Web浏览器中加载一个页面，或者使用Android Intent打开一个新的电子邮件屏幕，所以在Anko中有一些辅助功能：

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

其他有用的意图描述在有用意图调用者参考部分。
## 警报对话框

Anko提供了一种声明性的方式来创建带有短信，列表，进度条，甚至使用您自己的DSL布局的警报对话。
对于一个简单的文本警报，底部有几个按钮，您只需要：

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

有一个功能可以创建和显示列表对话框：

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

支持不确定和基本的进度对话框：

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

另外，如上所述，您可以在对话框中使用Anko的DSL来创建自定义布局：

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

## 服务

Android系统服务，例如WifiManager，LocationManager或Vibrator，可通过上下文的扩展属性在Anko中获得：

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

## 异步任务

可能在后台执行代码最流行的方法是将AsyncTask子类化。但是，尽管它受欢迎，但在许多方面都是不方便的。安科有几个功能，实际上做同样但更容易使用。
async（）{...}函数在ThreadExecutor下的{}中执行代码。您可以使用默认的或通过自己的。

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

如果你想回到async（）中的UI线程，你可以使用uiThread（）函数。

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

uiThread（）在async（）中有一个特殊的语义：async（）不包含一个Context实例，而只包含一个WeakReference，所以即使lambda执行永远不会完成，Context实例也不会泄漏。

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

## 记录

Android SDK提供了由几个记录方法组成的android.util.Log类。用法很简单，但是这些方法需要传递一个tag参数，实际的日志消息必须是一个String。您可以通过使用AnkoLogger trait来摆脱这一点：

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

默认的标签名称是一个类名（在这种情况下为SomeActivity），但您可以通过覆盖AnkoLogger的loggerTag属性轻松更改它。
每个方法都有两个版本：plain和“lazy”（只有Log.isLoggable（tag，Log.INFO）为true），才会执行lambda。

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

您可以阅读有关登录“日志参考”部分的更多信息。
## 结论

尝试安科，按照这些说明。
像往常一样，您的反馈非常受欢迎。
