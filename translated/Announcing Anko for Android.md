---
title: "[译]Announcing Anko for Android"
date: 2015-04-08 16:20:00
author: Hadi Hariri
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/04/announcing-anko-for-android/
---

我们很高兴地宣布，我们一直致力于Android开发的图书馆，其中除了别的以外，还可以使用DSL以类型安全和动态的方式创建应用程序界面。
## 样品味道

这是一个简单的例子，描述安科的一些可能性。想象一下，我们需要创建一个简单的注册表单，包括用户名和<注册> <code>按钮</ code>的<code> EditText </ code>。使用安科的代码是：

{% raw %}
<p></p>
{% endraw %}

```kotlin
import kotlinx.android.anko.*
 
class MainActivity : Activity() {
 
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
 
        verticalLayout {
            padding = dip(16)
            textView("Username:") {
                textSize = 18f
            }.layoutParams { verticalMargin = dip(4) }
 
            val login = editText()
 
            button("Sign up") {
                textSize = 20f
                onClick { login(login.text) }
            }.layoutParams { topMargin = dip(8) }
        }
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}


{% raw %}
<p><span id="more-1999"></span></p>
{% endraw %}

安科广泛使用Kotlin [扩展功能和属性](http://kotlinlang.org/docs/reference/extensions.html)  安排进去 [类型安全的建设者](http://kotlinlang.org/docs/reference/type-safe-builders.html)  来描述用户界面。作为回报，我们在编译时得到简洁和类型安全。
当然，我们还可以在设计时使用Anko Preview插件来查看预览，这些插件适用于IntelliJ IDEA和Android Studio：

{% raw %}
<p><img alt="Anko Designer" class="aligncenter size-full wp-image-2007" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/04/Screen-Shot-2015-04-02-at-00.33.22.png?resize=640%2C481&amp;ssl=1"/></p>
{% endraw %}

如果我们现在想添加另一个文本输入小部件，例如电子邮件，我们可能会创建另一对<code> textView（）</ code>和<code> editText（）</ code>函数调用。然而，更好的方法是将相应的DSL片段提取为新的功能：

{% raw %}
<p></p>
{% endraw %}

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
 
    verticalLayout {
        padding = dip(16)
        val login = inputField("Username")
        val email = inputField("E-mail")
 
        button("Sign up") {
            textSize = 20f
            onClick { login(login.text) }
        }.layoutParams { topMargin = dip(8) }
    }
}
 
fun _LinearLayout.inputField(name: String): TextView {
    textView("$name:") {
        textSize = 18f
    }.layoutParams { verticalMargin = dip(4) }
    return editText()
}
 
```

{% raw %}
<p></p>
{% endraw %}

任何额外的输入只需要单个函数调用。
表格的最终结果是：

{% raw %}
<p><img alt="Anko result form" class="aligncenter size-full wp-image-2009" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2015/04/layout-2015-04-02-014006.png?resize=384%2C640&amp;ssl=1"/></p>
{% endraw %}

### 部分定义的听众

当您使用Android侦听器的方法很多时，安科非常有用。考虑下面写的不使用安科的代码：

{% raw %}
<p></p>
{% endraw %}

```kotlin
seekBar.setOnSeekBarChangeListener(object: OnSeekBarChangeListener {
  override fun onProgressChanged(seekBar: SeekBar, progress: Int, fromUser: Boolean) {
    // Something
  }
  override fun onStartTrackingTouch(seekBar: SeekBar?) {
    // Just an empty method
  }
  override fun onStopTrackingTouch(seekBar: SeekBar) {
    // Another empty method
  }
})
 
```

{% raw %}
<p></p>
{% endraw %}

这是使用安科的版本：

{% raw %}
<p></p>
{% endraw %}

```kotlin
seekBar {
  onProgressChanged { (seekBar, progress, fromUser) ->
    // Something
  }
}
 
```

{% raw %}
<p></p>
{% endraw %}

具有空体的方法不再需要空的实现。另外，如果为相同的View设置<code> onProgressChanged（）</ code>和onStartTrackingTouch（）</ code>，这两个“部分定义”的监听器将被合并。
## 不止一个DSL

安科不仅仅是一个DSL，而是一个促进Android开发在不同领域的图书馆。它有许多方法涵盖对话框，异步任务，服务，意图甚至SQLite数据库访问。
例如，如果要启动新的<code>活动</ code>：

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Without Anko
val intent = Intent(this, javaClass<MyActivity>())
intent.putExtra("id", 5)
startActivity(intent)
 
// With Anko
startActivity<MyActivity>("id" to 5)
 
```

{% raw %}
<p></p>
{% endraw %}

或激活振动器：

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Without Anko
val vibrator = getSystemService(Context.VIBRATOR_SERVICE) as Vibrator
vibrator.vibrate(500)
 
// With Anko
vibrator.vibrate(500)
 
```

{% raw %}
<p></p>
{% endraw %}

或者甚至发送吐司信息：

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Without Anko
Toast.makeText(this, "Download is complete!", Toast.LENGTH_SHORT).show()
 
// With Anko
toast("Download is complete!")
 
```

{% raw %}
<p></p>
{% endraw %}

### 现有代码支持

你可以用Java编写你的旧类。此外，如果您仍然希望（或有）编写Kotlin活动类并由于某种原因夸大XML布局，则可以使用<code> View </ code>属性和监听器助手，这将使事情变得更容易：

{% raw %}
<p></p>
{% endraw %}

```kotlin
name.hint = "Enter your name"
name.onClick { /* do something */ }
 
```

{% raw %}
<p></p>
{% endraw %}

## 安科的好处

希望你能看到安科提供了一系列的好处，特别是：

* 一切都在一个地方。而不是将布局分解成静态（XML）和动态部分，然后尝试将它们绑定在一起，我们可以使用Kotlin编写我们想要的所有内容。编译时类型检查是一个甜蜜的奖励。
* 安科可以使我们的代码更简洁易读。
* 它允许轻松重复使用。我们可以将DSL的一部分提取成功能并多次使用。

## 试一试！

安科还处于阿尔法阶段，但是我们希望尽快发布您的反馈意见，所以请试试。我们尽可能简单地做到这一点。它全部发布在Maven Central上，如果您使用Gradle，您可以轻松地将所需的依赖项添加到<code> build.gradle </ code>文件中：

{% raw %}
<p></p>
{% endraw %}

```kotlin
dependencies {
  compile 'org.jetbrains.anko:anko:0.5-15'
}
 
```

{% raw %}
<p></p>
{% endraw %}

Anko Preview插件可用于IntelliJ IDEA和Android Studio。您可以 [下载](https://plugins.jetbrains.com/plugin/7734)  它直接从插件存储库。
有二进制文件针对的是原始Android（SDK版本15，Ice Cream Sandwich）和Android，支持v4软件包。
此外，最后但并非最不重要的是，与Kotlin相关的所有内容，Anko都是完全开源的。存储库已打开 [GitHub](https://github.com/JetBrains/anko)  和往常一样，欢迎贡献！
