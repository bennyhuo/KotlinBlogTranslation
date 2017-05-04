---
title: "[译]Kotlin NetBeans plugin beta is out!"
date: 2016-09-19 18:42:00
author: Dmitry Jemerov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2016/09/kotlin-netbeans-plugin-beta-is-out/
translator:
translator_url:
---

今天我们很高兴地介绍 NetBeans IDE 的 Kotlin 插件的第一个 BETA 版本。
主要特点是：

* 建立和运行您的代码

Maven 和 Ant 支持

Java 互操作性

代码突出显示

诊断

代码完成

导航

调试

单元测试

自动导入

标记发生

快速搜索

代码格式
* Maven 和 Ant 支持

Java 互操作性

代码突出显示

诊断

代码完成

导航

调试

单元测试

自动导入

标记发生

快速搜索

代码格式
* Java 互操作性

代码突出显示

诊断

代码完成

导航

调试

单元测试

自动导入

标记发生

快速搜索

代码格式
* 代码突出显示

诊断

代码完成

导航

调试

单元测试

自动导入

标记发生

快速搜索

代码格式
* 诊断

代码完成

导航

调试

单元测试

自动导入

标记发生

快速搜索

代码格式
* 代码完成

导航

调试

单元测试

自动导入

标记发生

快速搜索

代码格式
* 导航

调试

单元测试

自动导入

标记发生

快速搜索

代码格式
* 调试

单元测试

自动导入

标记发生

快速搜索

代码格式
* 单元测试

自动导入

标记发生

快速搜索

代码格式
* 自动导入

标记发生

快速搜索

代码格式
* 标记发生

快速搜索

代码格式
* 快速搜索

代码格式
* 代码格式


{% raw %}
<p><span id="more-4256"></span></p>
{% endraw %}

## 安装

要尝试一下，您将需要安装 NetBeans 8.1。 Kotlin 插件的 beta 版本可从 [NetBeans 插件门户](http://plugins.netbeans.org/plugin/68590/kotlin) 。
安装过程：

0. 下载 Kotlin 插件

启动 NetBeans IDE

从主菜单中选择“工具”，然后选择“插件”

切换到“已下载”选项卡

在“已下载”选项卡上，单击“添加插件...”按钮

在文件选择器中，导航到具有下载插件的文件夹。选择 NBM 文件，然后单击确定。该插件将显示在要安装的插件列表中。

在“插件”对话框中单击“安装”按钮

单击下一步完成安装向导，同意许可条款并单击安装按钮。=== 启动 NetBeans IDE

从主菜单中选择“工具”，然后选择“插件”

切换到“已下载”选项卡

在“已下载”选项卡上，单击“添加插件...”按钮

在文件选择器中，导航到具有下载插件的文件夹。选择 NBM 文件，然后单击确定。该插件将显示在要安装的插件列表中。

在“插件”对话框中单击“安装”按钮

通过单击下一步完成安装向导，同意许可条款并单击安装按钮。=== 从主菜单中选择工具，然后选择插件

切换到“已下载”选项卡

在“已下载”选项卡上，单击“添加插件...”按钮

在文件选择器中，导航到具有下载插件的文件夹。选择 NBM 文件，然后单击确定。该插件将显示在要安装的插件列表中。

在“插件”对话框中单击“安装”按钮

单击下一步完成安装向导，同意许可条款，然后单击安装按钮。=== 切换到已下载的选项卡

在“已下载”选项卡上，单击“添加插件...”按钮

在文件选择器中，导航到具有下载插件的文件夹。选择 NBM 文件，然后单击确定。该插件将显示在要安装的插件列表中。

在“插件”对话框中单击“安装”按钮

通过单击下一步完成安装向导，同意许可条款并单击安装按钮。=== 在“已下载”选项卡上，单击“添加插件...”按钮

在文件选择器中，导航到具有下载插件的文件夹。选择 NBM 文件，然后单击确定。该插件将显示在要安装的插件列表中。

在“插件”对话框中单击“安装”按钮

通过单击下一步完成安装向导，同意许可条款并单击安装按钮。=== 在文件选择器中，导航到具有下载插件的文件夹。选择 NBM 文件，然后单击确定。该插件将显示在要安装的插件列表中。

在“插件”对话框中单击“安装”按钮

通过单击下一步完成安装向导，同意许可条款并单击安装按钮。=== 在插件对话框中单击安装按钮

通过单击下一步完成安装向导，同意许可条款并单击安装按钮。=== 通过单击下一步完成安装向导，同意许可条款并单击安装按钮。

## 在 NetBeans 中使用 Kotlin

要在 NetBeans 中开始使用 Kotlin，您可以创建一个新的 Java 项目（基于 Maven 或 Ant 的）或打开现有的 Java 项目。您可以自由混合 Java 和 Kotlin，Java 类可从 Kotlin 访问，反之亦然。当时插件支持 Kotlin 1.0.3。
以下是功能的快速概述。
### 诊断


{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2016/09/diagnostics.png?ssl=1" rel="attachment wp-att-4262"><img alt="diagnostics" class="alignnone size-full wp-image-4262" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2016/09/diagnostics.png?resize=640%2C223&amp;ssl=1"/></a></p>
{% endraw %}

### 代码完成


{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2016/09/completion.png?ssl=1" rel="attachment wp-att-4260"><img alt="completion" class="alignnone size-full wp-image-4260" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2016/09/completion.png?resize=640%2C297&amp;ssl=1"/></a></p>
{% endraw %}

### 导航

从 Kotlin 到 Kotlin：

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2016/09/navigationK2K.png?ssl=1" rel="attachment wp-att-4266"><img alt="navigationk2k" class="alignnone size-full wp-image-4266" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2016/09/navigationK2K.png?resize=640%2C160&amp;ssl=1"/></a></p>
{% endraw %}

从 Kotlin 到 Java：

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2016/09/navigationK2J.png?ssl=1" rel="attachment wp-att-4265"><img alt="navigationk2j" class="alignnone size-full wp-image-4265" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2016/09/navigationK2J.png?resize=640%2C213&amp;ssl=1"/></a></p>
{% endraw %}

从 Java 到 Kotlin：

{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2016/09/navigationJ2K.png?ssl=1" rel="attachment wp-att-4264"><img alt="navigationj2k" class="alignnone size-full wp-image-4264" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2016/09/navigationJ2K.png?resize=640%2C212&amp;ssl=1"/></a></p>
{% endraw %}

### 调试

您可以

* 设置断点

使用进/出/结束

查看局部变量和 Kotlin 对象的内容
* 使用进/出/结束

查看局部变量和 Kotlin 对象的内容
* 查看局部变量和 Kotlin 对象的内容


{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2016/09/debugging.png?ssl=1" rel="attachment wp-att-4261"><img alt="debugging" class="alignnone size-full wp-image-4261" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2016/09/debugging.png?resize=640%2C486&amp;ssl=1"/></a></p>
{% endraw %}

### 单元测试

要在 Kotlin 中编写测试，您应该在项目的类路径中具有 JUnit。

{% raw %}
<p><a href="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2016/09/junit.png?ssl=1" rel="attachment wp-att-4263"><img alt="junit" class="alignnone size-full wp-image-4263" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2016/09/junit.png?resize=640%2C348&amp;ssl=1"/></a></p>
{% endraw %}

### 自动导入


{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2016/09/autoImport.png?ssl=1" rel="attachment wp-att-4259"><img alt="autoimport" class="alignnone size-full wp-image-4259" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2016/09/autoImport.png?resize=640%2C192&amp;ssl=1"/></a></p>
{% endraw %}

### 标记发生


{% raw %}
<p><a href="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2016/09/occurrences.png?ssl=1" rel="attachment wp-att-4267"><img alt="occurrences" class="alignnone wp-image-4267" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2016/09/occurrences.png?resize=325%2C114&amp;ssl=1"/></a></p>
{% endraw %}

### 快速搜索


{% raw %}
<p><a href="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2016/09/quickSearch.png?ssl=1" rel="attachment wp-att-4268"><img alt="quicksearch" class="alignnone size-full wp-image-4268" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2016/09/quickSearch.png?resize=640%2C118&amp;ssl=1"/></a></p>
{% endraw %}

### 反馈欢迎

您的反馈非常重要。随意添加问题和功能请求 [插件问题跟踪器](https://github.com/Baratynskiy/kotlin-netbeans/issues) 。
就像 Kotlin 本身一样，NetBeans 插件是一个开源项目，所以您的贡献可以帮助它更快地发展。
