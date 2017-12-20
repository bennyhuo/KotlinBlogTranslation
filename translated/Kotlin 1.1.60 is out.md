---
title: Kotlin 1.1.60 is out
author: Dmitry Jemerov
date: 2017-11-13 22:07:00
source_url: https://blog.jetbrains.com/kotlin/2017/11/kotlin-1-1-60-is-out/
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
tags: 
categories:  官方动态
translator: pye52
translator_url: https://pye52.github.io/ 
---

我们很高兴宣布Kotlin 1.1.60的发布，这是针对Kotlin 1.1一个bug修正和工具更新的新版本。包含以下更新：

* 为Kotlin / JS增量编译添加实验性支持
* 向JSR-305自定义可空注解支持添加新的特性
* 修复Parcelable生成器中的大量bug，并为其提供了IDE的支持
* 改善了Gradle的增量构建
* 在IntelliJ插件中引入新的检查，性能改进和bug修复

此更新与2016.3至2017.3的所有IntelliJ IDEA版本以及Android Studio 2.3,3.0和3.1 Canary兼容。
可以在[更新日志](https://github.com/JetBrains/kotlin/blob/1.1.60/ChangeLog.md)中看到完整的更新列表。
同时要感谢我们的代码贡献者，他们的pr已合并到该版本中：龟井俊明，Kirish Rakhman，Paul Merlin，Raluca Sauciuc，Yoshinori Isogai，Andrey Mischenko，Francesco Vasco，Jonathan Leitschuh，Denis Grachev和pivotal-vladimir。

## Kotlin / JS增量编译

在1.1.60版本中，Kotlin / JS Gradle项目将实验性地支持增量编译，对于微小的局部变更，只需数秒而非几分钟的完整构建，这可以显着减少开发过程中的构建时间。
默认情况下它是禁用的，你可以在`gradle.properties`或`local.properties`中设置`kotlin.incremental.js = true`来启用。
欢迎使用，若遇到任何问题，请向[Kotlin issue tracker](https://youtrack.jetbrains.com/oauth?state=%2Fissues%2FKT)反馈。

## 对JSR-305的支持

在Kotlin 1.1.50 中利用类型限定符别名和默认参数实现的扩展——[JSR-305可空性注解](https://kotlinlang.org/docs/reference/java-interop.html#jsr-305-support)得到了进一步的改善，其中的bug在该版本中得到修复。
### 默认类型限定符注释的用法

现在JSR-305默认类型限定符可以通过`ElementType.Type`来强制被注释的所有类型的用法，及其参数，基类和通配符类型：

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

### 自定义可空注解的迁移状态

提供类型限定符别名和类型限定符默认注释的代码库维护者现在可以通过`@UnderMigration`来控制注释的迁移状态。该注释发布在新的工件`kotlin-annotations-jvm`中，因此需要在gradle中添加一个新的依赖`compile "org.jetbrains.kotlin:kotlin-annotations-jvm:1.1.60`。

`@UnderMigration（status = ...）`(取值范围为：`MigrationStatus.STRICT`、`MigrationStatus.WARN`、`MigrationStatus.IGNORE`)指定编译器在处理被注释的API的错误用法时的行为：报告错误，提示警告或直接忽略。

注意：在当前版本编译的代码中无法保证`MigrationStatus.STRICT`的表现，因此该值当前是实验性的，但在之后的Kotlin版本中会正常作用。 Kotlin 1.2.x或Kotlin 1.3中的检查将很可能更加严格。

### 用于迁移状态控制的编译器标记

出于某种原因，当代码库的用户需要使用与维护者提供的不同的迁移状态时，可以通过将下列其中之一的编译器标记传递给可空性检查：

* `-Xjsr305 = {strict | warn | ignore}`现在只影响没有标记`@UnderMigration`状态的注释
* `-Xjsr305=under-migration:{strict|warn|ignore}`将覆写所有`@UnderMigration`注释的行为
* `-Xjsr305=@<fq.name>:{strict|warn|ignore}`将复写限定名称为fq.name的迁移状态

`strict`模式也是实验性的，无法保证Kotlin 1.1.60所编译的源代码在将来的版本中仍能通过编译。
这些标志可以被合并，例如，`-Xjsr305=ignore -Xjsr305=under-migration:ignore -Xjsr305=@org.library.MyNullable:warn`将使编译器忽略所有可空性注释，以及`org.library.MyNullable`，但后者同时会有一个警告。

## 对Parcelable的支持

本版本修复了Kotlin 1.1.4（参考[标准](https://github.com/Kotlin/KEEP/blob/master/proposals/extensions/android-parcelable.md)）中实验性Parcelable生成器的大量已知问题，并以`diagnostics `和`quick fixes`的形式提供了IDE支持，通过@Parcelize注释以利用该功能。

## Gradle增量构建

在Kotlin 1.1.60下，Gradle项目下`test`代码集中的Kotlin代码会在`main`集发生更改时重新编译。
此外，我们修复了一些bug使得新版的检查更加可靠，以便确保在JVM target，编译器插件配置和其他选项发生改动后，就会重新编译代码。
## IntelliJ IDEA插件的改进

新版本在Kotlin IntelliJ IDEA插件中带来了许多改进：

* 用Kotlin DSL创建一个Gradle项目的新项目向导
* 当类型不匹配时通过quick fix在`Iterable`，`Sequence`和`Array`之间互相转换
* 通过quick fix在类型参数需要时智能指定
* 大量的bug修复及性能改进

## 如何更新

若需要更新插件，请执行Tools | Kotlin | Configure Kotlin Plugin Updates 并点击“Check for updates now”按钮（对于Android Studio 3.1，从[Plug Repository](https://plugins.jetbrains.com/plugin/6954-kotlin)独立的渠道中更新）。同时注意要在Maven和Gradle构建脚本中更新编译器和标准库的版本。
像往常一样，如果在新版本中遇到任何问题，欢迎您在[论坛](https://youtrack.jetbrains.com/oauth?state=%2Fissues%2FKT)上寻求帮助，在Slack上（获取[邀请](http://slack.kotlinlang.org/)），或者在[issue tracker](https://youtrack.jetbrains.com/issues/KT)中报告问题。

请尽情享受Kotlin！