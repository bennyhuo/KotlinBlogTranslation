---
title: Kotlin 1.1.60 is out
author: Dmitry Jemerov
date: 2017-11-13 22:07:00
source_url: https://blog.jetbrains.com/kotlin/2017/11/kotlin-1-1-60-is-out/
tags: 
categories:  官方动态
---

我们很高兴地宣布Kotlin 1.1.60的发布，这是Kotlin 1.1的一个新的错误修正和工具更新。此更新：

* 为Kotlin / JS增量编译添加实验支持
* 向JSR-305自定义可用性注释支持添加新功能
* 在自动Parcelable实现生成器中引入了很多bug修复，并为其提供了IDE支持
* 改进了Gradle增量构建
* 在IntelliJ插件中引入新的检查，性能改进和错误修复

此更新与2016.3至2017.3的所有IntelliJ IDEA版本以及Android Studio 2.3,3.0和3.1 Canary兼容。
此更新的完整列表可以在更新日志中找到。
我们要感谢我们的外部贡献者，他们的提案请求包括在这个版本中：龟井俊明，Kirish Rakhman，Paul Merlin，Raluca Sauciuc，Yoshinori Isogai，Andrey Mischenko，Francesco Vasco，Jonathan Leitschuh，Denis Grachev和pivotal-vladimir。

{% raw %}
<p><span id="more-5441"></span></p>
{% endraw %}

## Kotlin / JS增量编译

Kotlin 1.1.60在Kotlin / JS Gradle项目中引入了增量编译的实验性支持，可以显着减少开发过程中的构建时间，编译一个小的局部变化，而不是一分钟，而非完整的非增量重建。
它在默认情况下是禁用的，应该通过在gradle.properties或local.properties中设置kotlin.incremental.js = true来启用它。
随时尝试一下，并向Kotlin问题跟踪器报告遇到的任何问题。
## JSR-305支持

对JSR-305可空性注释的支持（由Kotlin 1.1.50中的类型限定符昵称和默认扩展）得到了进一步改进，并且在此版本中得到了错误修复。
### 类型限定符默认为所有类型的用法

JSR-305默认类型限定符现在可以指定ElementType.TYPE_USE来影响注释范围内的所有类型用法，包括类型参数，类型参数上限和通配符类型：

{% raw %}
<p></p>
{% endraw %}

```kotlin
@Nonnull(when = When.MAYBE)
@TypeQualifierDefault({ElementType.TYPE_USE})
public @interface NullableApi {
}
 
@NullableApi
interface Foo<T extends Bar> { // Upper bound T : Bar? in Kotlin
    List<String> baz(List<? extends Qux> qux);
    // in Kotlin: fun baz(qux: List<out Qux?>?): List<String?>?
}
 
```

{% raw %}
<p></p>
{% endraw %}

### 自定义可空性标注的迁移状态

提供类型限定符昵称和类型限定符默认注释的图书馆维护者现在可以通过使用@UnderMigration标记注释类型来控制注释的迁移状态。这个注释是在一个新的工件kotlin-annotations-jvm中发布的，应该作为库的一个依赖添加，例如在Gradle中编译“org.jetbrains.kotlin：kotlin-annotations-jvm：1.1.60”。
@UnderMigration（status = ...）值指定编译器如何处理在注释的API用法中检测到的可空性违例，并且可以是MigrationStatus.STRICT，MigrationStatus.WARN和MigrationStatus.IGNORE之一，从而使编译器产生错误，警告或不分别。
注意：MigrationStatus.STRICT现在被认为是实验性的，因为在当前版本中编译的代码没有保证，这个选项对于未来的Kotlin版本仍然是正确的。 Kotlin 1.2.x或Kotlin 1.3中的支票很可能会更加严格。
### 用于迁移状态控制的编译器标志

出于某种原因，需要与图书馆维护人员提供的迁移状态不同的图书馆用户可以通过将编译器标志以下列形式之一传递给可空性检查：

* -Xjsr305 = {strict | warn | ignore}现在只影响所有没有@UnderMigration状态的注释
* -Xjsr305 =迁移中：{strict | warn | ignore}将覆盖所有@UnderMigration注释的行为
* -Xjsr305 = @：{strict | warn | ignore}其中fq.name是特定批注的完全限定名称，用于覆盖迁移状态

严格的模式也是实验性的，对于使用Kotlin 1.1.60编译的源代码，未来的版本不能保证。
这些标志可以合并，例如，-Xjsr305 = ignore -Xjsr305 = under-migration：ignore -Xjsr305=@org.library.MyNullable：warn使编译器忽略所有可空性注释，但忽略org.library.MyNullable并报告警告后者。
## 可支持的支持

本版本修复了Kotlin 1.1.4（参见规范）中提供的实验性自动Parcelable实现生成器中的许多已知问题，并以诊断和快速修复的形式提供了IDE支持，旨在帮助使用@Parcelize。
## Gradle增量构建

使用Kotlin 1.1.60，Gradle项目的测试源代码集中的Kotlin代码在主源发生更改时都会重新编译。
此外，一些错误修复使得最新的检查更加可靠，以确保只要JVM目标，编译器插件配置和其他选项等选项发生更改，就会重新编译代码。
## IntelliJ IDEA插件的改进

新版本在Kotlin IntelliJ IDEA插件中带来了许多改进：

* 新建项目向导，用Kotlin DSL创建一个Gradle项目
* 快速修复在类型不匹配的情况下将Iterable，Sequence和Array转换为对方
* 在使用类型参数时需要快速修复
* 很多错误修复和性能改进

## 如何更新

要更新插件，请使用工具| Kotlin |配置Kotlin插件更新并按下“立即更新”按钮（对于Android Studio 3.1，从插件库的单独通道下载插件）。另外，不要忘了在Maven和Gradle构建脚本中更新编译器和标准库版本。
像往常一样，如果遇到新版本的任何问题，欢迎您在论坛上寻求帮助，在Slack上（在此处获得邀请），或者在问题跟踪器中报告问题。
让科特林！
