---
title: Kotlin 1.2 EAP（Early Access Program）版本发布
author: Ilya Gorbunov
date: 2017-06-27 21:45:00
source_url: https://blog.jetbrains.com/kotlin/2017/06/early-access-program-for-kotlin-1-2-has-been-started/
tags: EAP
categories:  官方动态
translator: DemoJameson
translator_url: http://www.demojameson.com/
---

我们很高兴地宣布 Kotlin 1.2 EAP 版本开放测试，今天发布了第一个里程碑版本 `1.2-M1`。

此版本默认启用了 1.1.x 版本实验性的语言特性，并且增加了新的在实验特性，以及在标准库中添加了新的 API。

完整的更新日志在[这里](https://github.com/JetBrains/kotlin/blob/1.2-M1/ChangeLog.md)，内容不多。

{% raw %}
<p><span id="more-5090"></span></p>
{% endraw %}

## 语言特性：在注解中使用数组字面量

在这个里程碑版本中值得一提的语言特性是数组字面量，其用法被限制在注解参数中。
之前我们必须使用下面的写法来构建数组：

```kotlin
@CacheConfig(cacheNames = arrayOf("books", "default"))
public class BookRepositoryImpl {
    // ....
}
```

而在 Kotlin 1.2 中，可以使用一对中括号代替 `arrayOf` 函数：

```kotlin
@CacheConfig(cacheNames = ["books", "default"])
public class BookRepositoryImpl {
    // ....
}
```

IDE 将在适当的情况下提示您使用数组字面量这种新语法。

### 参数有默认值的内联函数

直到 1.1.x 版本，我们是无法为内联高阶函数的参数设置默认值的，如下所示的写法并不支持：

```kotlin
inline fun <E> List<E>.printItems(transform: (E) -> String = { it.toString() })
```

想使程序成功编译，要么将函数改为非内联的，要么将函数参数标记为 `noinline`。这两种情况下都无法使函数参数得到内联优化。

而从这个版本开始，Kotlin 支持给内联函数的参数设置默认值了，上面的写法已经支持。

## 标准库 API

此版本采纳了 KEEP 的（Kotlin Evolution and Enhancement Proposals）两条建议，为标准库添加了一些 API。
第一条是 [KEEP-49](https://github.com/Kotlin/KEEP/blob/master/proposals/stdlib/bignumber-operations.md) 引入了 `BigInteger` 和 `BigDecimal` 类型的额外操作和转换扩展，感谢 [Daniil Vodopian](https://github.com/voddan)。
第二条是 [KEEP-11](https://github.com/Kotlin/KEEP/blob/master/proposals/stdlib/window-sliding.md)，它在添加了许多有关集合划分的功能：

* `chunked(size: Int)` 将一个集合划分成给定大小的块的扩展函数
* `windowed(size: Int, step: Int)` 取一个给定大小的窗口，并根据给定的步进沿着集合移动，返回每个窗口元素的子列表
* `pairwise()` 返回集合中元素与相邻后续元素配对后组成的集合

如果您有兴趣请试试这些扩展函数，并告诉我们它们是否适用。

还有一些其他改进，例如 `MutableLis` 的扩展函数 `fill()` 和 `shuffle()` 以及 `List` 的 `shuffled()`，`Regex` 类变为可序列化的。

## JavaScript

在 1.1.2 版本之前，我们推出了的 JS 类型数组支持。 手动启用后会将 Kotlin 基本类型的数组（如 `IntArray`，`DoubleArray`等）转换为 JavaScript 类型的数组。 现在默认启用此支持。

## 预发布版本说明

*请注意，向后兼容性保证并不涵盖预发行版本：特性和 API 可能会在后续版本中更改。 当我们达到最终 RC 版本时，由预发布版本生成的所有二进制文件将被编译器禁止，您将需要重新编译 1.2-Mx 版本编译的所有内容。 当然，由 1.1.x 和更早版本编译的所有代码无需重新编译。*

在这个版本中，如果您编写了内联的 suspend 函数，那么将无法针对旧的运行时进行编译。

## 如何尝试

**在 Maven/Gradle 中**：添加 http://dl.bintray.com/kotlin/kotlin-eap-1.2 作为构建脚本和项目的仓库; 使用 `1.2-M1` 作为编译器插件和标准库的版本号。

**在 IntelliJ IDEA 中**：打开菜单 *Tools → Kotlin → Configure Kotlin Plugin Updates*，然后在 *Update channel* 下拉列表中选择 “Early Access Preview 1.2”，然后点击 *Check for updates* 按钮。

**命令行编译器**：可以从 [Github release 页面](https://github.com/JetBrains/kotlin/releases/tag/v1.2-M1)下载。

**在 [try.kotlinlang.org](https://try.kotlinlang.org/) 上**：使用右下角的下拉列表将编译器版本更改为 `1.2-M1`。
