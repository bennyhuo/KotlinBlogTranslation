---
title: "[译]Advanced Features of Anko"
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
translator:
translator_url:
---

上周我们发表了 [一个新版本](http://blog.jetbrains.com/kotlin/2015/04/anko-0-6-is-released/) 的安科。虽然该库的主要目的是通过DSL创建布局，但即使是XML布局的用户也可以从中受益。今天我们来谈谈Anko的这种“矛盾”的特征。<span id =“more-2135”> </span>
## 意向助手

启动新的`Activity`的常见方法是创建一个`Intent`，可能会把一些参数放入它，最后将创建的`Intent`传递给`上下文`的`startActivity（）`方法。

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

`startActivity（）`函数接受将作为`Intent`附加参数传递的键值对。另一个功能，即具有类似语义的`startActivityForResult（）`也是可用的。
请参考 [意图生成器函数](https://github.com/JetBrains/anko/blob/master/doc/ADVANCED.md#intent-builder-functions) 参考部分了解更多信息。
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

其他有用的意图描述在 [有意义的来电者](https://github.com/JetBrains/anko/blob/master/doc/ADVANCED.md#useful-intent-callers) 参考部分
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

通过`上下文`的扩展属性可以在Anko中提供Android系统服务，例如`WifiManager`，`LocationManager`或`Vibrator` ：

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

可能在后台执行代码最流行的方法是将`AsyncTask`子类化。但是，尽管它受欢迎，但在许多方面都是不方便的。安科有几个功能，实际上做同样但更容易使用。
`async（）{...}`功能在`ThreadExecutor`下的`{}`中执行代码。您可以使用默认的或通过自己的。

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

如果你想回到`async（）`中的UI线程，你可以使用`uiThread（）`函数。

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

`uiThread（）`在`async（）`中有一个特殊的语义：`async（）`不保存`Context`实例，只有一个`WeakReference`，所以即使lambda执行永远不会完成，`Context`实例也不会泄漏。

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

Android SDK提供了由几种记录方法组成的`android.util.Log`类。用法很简单，但是这些方法需要传递一个tag参数，实际的日志消息必须是一个`String`。您可以通过使用`AnkoLogger` trait来摆脱这一点：

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

默认标签名称是一个类名（在这种情况下为`SomeActivity`），但您可以通过覆盖`AnkoLogger`的`loggerTag`属性轻松更改它。
每个方法有两个版本：plain和“lazy”（只有当`Log.isLoggable（tag，Log.INFO）`是`true`）时，将会执行lambda。

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

您可以阅读更多关于登录的信息 [记录](https://github.com/JetBrains/anko/blob/master/doc/ADVANCED.md#logging) 参考部分。
## 结论

要尝试`Anko`，请遵循 [这些说明](https://github.com/JetBrains/anko#using-with-gradle) 。
像往常一样，您的反馈非常受欢迎。
