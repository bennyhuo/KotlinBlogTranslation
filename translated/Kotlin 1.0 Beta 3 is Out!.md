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

我们很高兴发布了Kotlin 1.0 Beta的另一个更新。我们正在努力完善标准库，抛弃了过时已久的设计结构，同时修复了bugs，改进性能和为下一个版本作准备。
完整的更新历史在 [这里](https://youtrack.jetbrains.com/issues/KT?q=%23Major+%23Critical+%23Resolved+-Obsolete+-%7BEclipse+Plugin%7D+resolved+date%3A+2015-11-16+..+2015-11-30) 。

最新的issue在 [这里](https://youtrack.jetbrains.com/issues/KT?q=%23Major+%23Critical+%23Resolved+-Obsolete+-%7BEclipse+Plugin%7D+resolved+date%3A+2015-11-16+..+2015-11-30) 。
## Library变更

我们努力在1.0版本到来之前让标准库变得更加完美。这意味着进行一些尝试，所以会有新的部分被弃用，有新的函数被添加。我们计划在1.0版本（或RC）中对标准库进行一次最后的清理：删除所有已过时和其他遗留的东西。
这里我们只关心一个需要注意的[变化](https://github.com/JetBrains/kotlin/releases/tag/build-1.0.0-beta-3595)：现在`contains()`和其他类似的扩展方法接受集合元素的父类型。

```kotlin
// strs: Collection<String>
// ns: String?
// cs: CharSequence
// i: Int
strs.contains(ns) // accepted now
strs.contains(cs) // accepted now
str.contains(i) // ERROR (in fact, a deprecation warning, but will be an error soon)
 
```

我们发现以前建议的`containsRaw`方法比较低效，使用`contains()`更加合适，同时保证了兼容性。请注意，集合接口本身是完整的，所有这些都是通过扩展功能完成的。请使用*Code Cleanup*来迁移代码。
## 语言变化

一些需要注意的语言变化，完整列表在[这里](https://github.com/JetBrains/kotlin/releases/tag/build-1.0.0-beta-3595) 。

许多我们以前不推荐的实现现在会报错。请使用*Code Cleanup*进行迁移。
### When表达式

这种代码已被证明是有问题的，所以我们决定弃用它：

```kotlin
when {
    foo.isValid(), foo.isReady() -> process(foo)
    ...
}
 
```

许多人倾向于认为条件“ foo.isValid(), foo.isReady()”表示 `foo.isValid() == true and foo.isReady() == true`，而实际上逗号是指**or**。解决方法很简单：只需使用**||**:

```kotlin
when {
    foo.isValid() || foo.isReady() -> process(foo)
    ...
}
 
```

*Code Cleanup*会自动迁移。
### 注释

一个bug已被修复，现在我们可以在注解的参数中使用默认值：

```kotlin
annotation class Entry(val value: String)
 
annotation class Example(
        val entries: Array<Entry> = arrayOf(Entry("a"), Entry("b")) // OK now
)
```

### 枚举值()

最近我们将传统的Java的`Enum.values()`更改为一个属性：`Enum.values `，但现在我们将回滚这个更改，因为有一个没有注意到的角落：枚举中的常量可能被命名为`values`，然后便没有办法访问其中的任何一个。我们考虑了不同的方案，最后决定将`values`改回函数是最干净的。
所以，现在不推荐使用`values`属性，也不推荐使用` values()`函数。
### 可见性和作用域

我们正在清理和修正小问题的可见性和作用域

* companion objects中允许protected成员
* 子类调用非@JvmStatic的protected对象将被标记为错误（不支持）
* 对于open属性，私有setters现在已被标记为过时
* local sealed class已弃用（从不可用）
* 重写的setter不能降低可见性
* 枚举类中不再允许存在内部类
* lambdas / object literals / local函数中禁止使用未初始化的变量

## Android扩展

我们合并了IntelliJ IDEA的主要Kotlin插件和Android的*Kotlin*扩展插件。后者现在已经过时了，因为它的功能可以从Kotlin插件获取。
此外，我们还添加了对Android **productFlavors**的支持：现在，来自不同flavors的属性可以在不同的包中使用。
例如，我们可以在` build.gradle`文件中存在两种flavors：

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

现在，我们不仅可以在**main source set**中的布局使用合成属性，还可以在flavor布局使用合成属性：

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

请注意，**main source set**的所有布局现在位于`kotlinx.android.synthetic.main`包之下，旧的包命名约定已被弃用。
## IDE中的新功能


* Android Extensions插件已被合并到Kotlin插件中，不再需要单独安装
* 创建新的Gradle项目时，我们添加了选择Kotlin的选项：
* 调试器：stacktrace导航功能现在支持跟踪内联函数的堆栈帧。同时对内联函数的步进调试功能进行了一系列的改进。
  <img src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/12/init.png?w=640"onmouseover="this.src='https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2015/12/init.gif';"onmouseout="this.src='https://i0.wp.com/blog.jetbrains.com/kotlin/files/2015/12/init.png?w=640';" width="640" height="172">
* 添加了三个快速初始化新属性的*Quick Fixes*：
* **Introduce Variable**（Ctrl + Alt + V / Cmd + Alt + V）现在支持**结构声明(multi-declarations)**：
* 同时**Introduce Variable**还能使用于lambda或匿名函数中：
* Beta 3开始支持从字符串模板中使用Variable / Parameter / Property / Function
* 最后，添加了一个实验功能 - 对IDE中的Kotlin脚本文件（.kts）的基本支持

