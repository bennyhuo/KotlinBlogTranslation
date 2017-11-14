---
title: Kotlin 1.1.60 is out
author: Dmitry Jemerov
date: 2017-11-13 22:07:00
source_url: https://blog.jetbrains.com/kotlin/2017/11/kotlin-1-1-60-is-out/
tags: 
categories:  官方动态
---

We’re happy to announce the release of Kotlin 1.1.60, a new bugfix and tooling update for Kotlin 1.1. This update:

* Adds experimental support for Kotlin/JS incremental compilation
* Adds new features to JSR-305 custom nullability annotations support
* Brings a lot of bug fixes in the automatic Parcelable implementation generator and provides it with IDE support
* Improves Gradle incremental builds
* Introduces new inspections, performance improvements and bug fixes in the IntelliJ plugin

The update is compatible with all versions of IntelliJ IDEA from 2016.3 until 2017.3, as well as with Android Studio 2.3, 3.0 and 3.1 Canary.
The complete list of changes in this release can be found in the changelog.
We’d like to thank our external contributors whose pull requests were included in this release: Toshiaki Kameyama, Kirill Rakhman, Paul Merlin, Raluca Sauciuc, Yoshinori Isogai, Andrey Mischenko, Francesco Vasco, Jonathan Leitschuh, Denis Grachev, and pivotal-vladimir.

{% raw %}
<p><span id="more-5441"></span></p>
{% endraw %}

## Kotlin/JS Incremental Compilation

Kotlin 1.1.60 introduces experimental support for incremental compilation in Kotlin/JS Gradle projects, which can significantly reduce build times during development, with compilation of a small local change taking seconds instead of a minute for a full non-incremental rebuild.
It is disabled by default and should be enabled by setting kotlin.incremental.js=true in gradle.properties or local.properties.
Feel free to try it out and report any issues you encounter to the Kotlin issue tracker.
## JSR-305 Support

The support for JSR-305 nullability annotations, which was extended by type qualifier nicknames and defaults in Kotlin 1.1.50 , has been further improved and received bug fixes in this release.
### Type qualifier defaults for all type usages

The JSR-305 default type qualifiers can now specify ElementType.TYPE_USE to affect all type usages within the annotated scope, including type arguments, upper bounds of type parameters and wildcard types:

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

### Migration status of custom nullability annotations

Library maintainers who provide type qualifier nickname and type qualifier default annotations can now control the migration status of the annotations by marking the annotation types with @UnderMigration. This annotation is shipped in a new artifact kotlin-annotations-jvm that should be added as a dependency for the library, e.g compile "org.jetbrains.kotlin:kotlin-annotations-jvm:1.1.60" in Gradle.
The @UnderMigration(status = ...) value specifies how the compiler treats nullability violations detected in the annotated API usages and can be one of MigrationStatus.STRICT, MigrationStatus.WARN and MigrationStatus.IGNORE, making the compiler produce errors, warnings or neither respectively.
Note: MigrationStatus.STRICT is now considered experimental in the sense that there are no guarantees for code compiled in current version with this option to be still correct with the future Kotlin versions. It’s very likely that the checks will be more strict in Kotlin 1.2.x or Kotlin 1.3.
### Compiler flags for migration status control

Library users who, for some reason, need a migration status different from that offered by a library maintainer can set up the nullability checks by passing the compiler flags in one of the forms:

* -Xjsr305={strict|warn|ignore} that now only affects all annotations which do not have an @UnderMigration status
* -Xjsr305=under-migration:{strict|warn|ignore} overrides the behavior of all @UnderMigration annotations
* -Xjsr305=@:{strict|warn|ignore} where fq.name is a fully qualified name of a specific annotation to override the migration status

The strict mode is experimental, too, and provides no guarantees for sources compiled with Kotlin 1.1.60 to compile with the future versions.
These flags can be combined, for example, -Xjsr305=ignore -Xjsr305=under-migration:ignore -Xjsr305=@org.library.MyNullable:warn makes the compiler ignore all nullability annotations but org.library.MyNullable and report warnings for the latter.
## Parcelable Support

This release fixes a lot of known issues in the experimental automatic Parcelable implementation generator that was presented in Kotlin 1.1.4 (see the specification) and also provides IDE support in the form of diagnostics and quick fixes aimed to help with using @Parcelize.
## Gradle Incremental Builds

With Kotlin 1.1.60, the Kotlin code in the test source set of a Gradle project is re-compiled incrementally whenever the main sources are changed.
Also, a few bug fixes make the up-to-date checks more reliable to make sure the code is re-compiled whenever such options as JVM target, compiler plugins configuration and others change.
## IntelliJ IDEA Plugin Improvements

The new release brings a lot of improvements in the Kotlin IntelliJ IDEA plugin:

* New project wizard to create a Gradle project with Kotlin DSL
* A quick fix to convert Iterable, Sequence and Array into each other in case of type mismatch
* A quick fix to make a type parameter reified when that is required by its usage
* A lot of bug fixes and performance improvements

## How to update

To update the plugin, use Tools | Kotlin | Configure Kotlin Plugin Updates and press the “Check for updates now” button (for Android Studio 3.1, download the plugin from a separate channel at the Plugin Repository). Also, don’t forget to update the compiler and standard library version in your Maven and Gradle build scripts.
As usual, if you run into any problems with the new release, you’re welcome to ask for help on the forums, on Slack (get an invite here), or to report issues in the issue tracker.
Let’s Kotlin!
