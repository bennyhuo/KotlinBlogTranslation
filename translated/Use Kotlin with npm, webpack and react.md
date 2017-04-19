---
title: "[译]Use Kotlin with npm, webpack and react"
date: 2017-04-18 15:23:00
author: Dmitry Jemerov
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2017/04/use-kotlin-with-npm-webpack-and-react/
---

使用Kotlin 1.1，将Kotlin编译器中的JavaScript定位到正式生产就绪状态。当然，编译器支持还不足以解决现实生活中的问题，所以我们继续将Kotlin整合到更大的JavaScript生态系统中。
今天，我们要介绍两个新项目：一个将Kotlin与npm，webpack和karma集成在一起的Gradle插件，以及一个带有Kotlin / JVM后端的完整堆栈应用程序示例，以及使用React构建的Kotlin / JS前端。
## Kotlin前端插件

的 [Kotlin前端插件](https://github.com/Kotlin/kotlin-frontend-plugin) 允许您使用webpack构建和部署Kotlin前端应用程序。您可以使用npm软件包作为应用程序的依赖关系，插件将负责将其下载并将其捆绑到生成的JS文件中。该插件还与Karma集成，允许您运行应用程序的测试。为了获得最佳的工作流程，该插件支持连续编译和热重新加载，确保您始终在浏览器中查看应用程序的最新版本。
的 [读我](https://github.com/Kotlin/kotlin-frontend-plugin/blob/master/README.md) 文件给出使用插件的说明，示例目录包含一个 [简单的例子](https://github.com/Kotlin/kotlin-frontend-plugin/tree/master/examples/frontend-only) 显示如何将其应用于真实的项目。
## Kotlin反应例子 [思考者](https://github.com/Kotlin/kotlin-fullstack-sample) 是Kotlin内置的现代全栈应用程序的一个例子。后端运行在Jetty并使用 [科尔特](https://github.com/kotlin/ktor) ，由Kotlin团队开发的Kotlin Web应用程序框架。前端使用React; Kotlin的一套React包装是 [作为项目的一部分提供](https://github.com/Kotlin/kotlin-fullstack-sample/tree/master/frontend/src/org/jetbrains/react) 。欢迎您在项目中使用包装器，并根据自己的需要进行调整。请注意，我们正在努力在内部开发React包装器，我们正在考虑将它们作为单独的开源库发布。
要查看Kotlin React代码如何，您可以查看 [其中的一个组件](https://github.com/Kotlin/kotlin-fullstack-sample/blob/master/frontend/src/org/jetbrains/demo/thinkter/NewThoughtComponent.kt) 的应用程序。
您对这些版本的反馈非常受欢迎！请在GitHub上提交问题，停止 [论坛](https://discuss.kotlinlang.org/) ，或者加入#javascript频道 [Kotlin松弛](http://slack.kotlinlang.org/) 。
