---
title: "[译]Kotlin 1.0 Beta 3 is Out!"
date: 2015-12-07 15:45:00
author: Andrey Breslav
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2015/12/kotlin-1-0-beta-3-is-out/
---

我们很高兴提出Kotlin 1.0 Beta的另一个更新。我们正在努力完成标准库，摆脱语言中旧的弃用构造，以及错误修复，性能改进和面向未来的检查。
完整的更改列表可用 [这里](https://youtrack.jetbrains.com/issues/KT?q=%23Major+%23Critical+%23Resolved+-Obsolete+-%7BEclipse+Plugin%7D+resolved+date%3A+2015-11-16+..+2015-11-30) 。<BR/>

看到封闭的问题 [这里](https://youtrack.jetbrains.com/issues/KT?q=%23Major+%23Critical+%23Resolved+-Obsolete+-%7BEclipse+Plugin%7D+resolved+date%3A+2015-11-16+..+2015-11-30) 。<span id =“more-3263”> </ span>
## 图书馆变更

我们正在努力在标准库中使其在1.0之前成为最佳形状。这涉及到一些实验，所以新的抛弃发生，新的功能被添加。我们计划在1.0版本（或RC）中对标准库进行最终的清理：删除所有的deprecations和其他遗留的东西。
这里我们只提供一个亮点 [变化](https://github.com/JetBrains/kotlin/releases/tag/build-1.0.0-beta-3595) ：<code> contains（）</ code>和其他类似的扩展名现在接受集合元素的超类型。

{% raw %}
<p></p>
{% endraw %}

```kotlin
// strs: Collection<String>
// ns: String?
// cs: CharSequence
// i: Int
strs.contains(ns) // accepted now
strs.contains(cs) // accepted now
str.contains(i) // ERROR (in fact, a deprecation warning, but will be an error soon)
 
```

{% raw %}
<p></p>
{% endraw %}

我们发现以前提出的<code> containsRaw </ code>方法是低效的，并且选择使<code> contains（）</ code>更容许，同时保持最初的安全性。请注意，收集界面本身是完整的，所有这些都是通过扩展功能完成的。使用<em>代码清理</ em>来迁移代码。
## 语言变化

来自语言变化的一些亮点，完整列表可用 [这里](https://github.com/JetBrains/kotlin/releases/tag/build-1.0.0-beta-3595) 。<BR/>

许多我们以前不赞成的事情现在已经成为错误。使用<em>代码清理</ em>进行迁移。
### 表达时

这种代码已被证明是有问题的，所以我们决定不赞成这样做：

{% raw %}
<p></p>
{% endraw %}

```kotlin
when {
    foo.isValid(), foo.isReady() -> process(foo)
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

许多人倾向于认为条件“<code> foo.isValid（），foo.isReady（）</ code>”表示<code> foo </ code> <strong> <strong> <strong> <strong> <strong> <strong> >和</ strong>准备好，而实际上逗号是指<em>或</ em>。解决方法很简单：只需使用<code> || </ code>：

{% raw %}
<p></p>
{% endraw %}

```kotlin
when {
    foo.isValid() || foo.isReady() -> process(foo)
    ...
}
 
```

{% raw %}
<p></p>
{% endraw %}

代码清理</ em>将会为您迁移。
### 注释

已经修复了一个错误，阻止我们在注释参数的默认值中使用数组：

{% raw %}
<p></p>
{% endraw %}

```kotlin
annotation class Entry(val value: String)
 
annotation class Example(
        val entries: Array<Entry> = arrayOf(Entry("a"), Entry("b")) // OK now
)
 
```

{% raw %}
<p></p>
{% endraw %}

### 枚举值（）

最近我们将传统的Java的<code> Enum.values（）</ code>更改为一个属性：<code> Enum.values </ code>，但现在我们将这个更改推回，因为有一个不愉快的角落：枚举中的常量可能被命名为<code>值</ code>，然后没有办法访问其中的一个。我们考虑了不同的选项，并决定将<code>值</ code>改回功能是最干净的。
所以，现在不推荐使用<code>值</ code>属性，并且不推荐使用<code> values（）</ code>函数。
### 可见性和范围规则

所以我们正在清理和修正小问题的可见性和范围规定

* 受保护的成员被允许在伴随对象中
* 来自子类的非@JvmStatic保护对象的调用对象被标记为错误（不支持）
* 私有设置器现在已被弃用用于打开的属性
* 本地密封类已弃用（从不可用）
* 覆盖设定器不能削弱可视性
* 内部类不再允许在枚举条目中
* 在lambdas / object literals / local函数中使用未初始化的变量被禁止

## Android扩展

我们合并了IntelliJ IDEA的主要Kotlin插件和Android的</ em> Kotlin扩展插件。后者现在已经过时了，因为它的功能可以从主Kotlin插件获得。
此外，我们还添加了对Android <strong>产品风格</ strong>的支持：现在，来自不同风格的属性可以在不同的包中使用。
例如，如果我们在<code> build.gradle </ code>文件中有两种口味：

{% raw %}
<p></p>
{% endraw %}

```kotlin
productFlavors {
    free {
        versionName "1.0-free"
    }
    pro {
        versionName "1.0-pro"
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

现在，我们可以使用合成属性，不仅可以在<code> main </ code>源代码集中进行布局，还可以为flavor布局使用合成属性：

{% raw %}
<p></p>
{% endraw %}

```kotlin
// Import synthetic properties for the `activity_free.xml` layout in the `free` flavor
import kotlinx.android.synthetic.free.activity_free.versionMarker
 
class FreeActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        ...
 
        setContentView(R.layout.activity_free)
 
        ...
 
        versionMarker.text = "Free version"
    }
}
 
```

{% raw %}
<p></p>
{% endraw %}

请注意，主源集合的所有布局现在位于<code> kotlinx.android.synthetic.main </ code>软件包之下，旧的软件包命名约定已被弃用。
## IDE中的新功能


* Android Extensions插件已被合并到主Kotlin插件中，不再需要单独安装
* 创建新的Gradle项目时，我们添加了选择Kotlin的选项：
* 调试器：stacktrace导航现在支持来自内联函数的堆栈帧。还有一些改进，通过内联函数。
* 添加了三个新的属性初始化快速修复：
* 介绍变量（Ctrl + Alt + V / Cmd + Alt + V）现在支持多声明表达式：
* 还允许在lambda或匿名函数中选择容器进行表达：
* Beta 3支持从字符串模板片段引入Variable / Parameter / Property / Function
* 最后，添加了一个实验功能 - 对IDE中的Kotlin脚本文件（.kts）的基本支持

