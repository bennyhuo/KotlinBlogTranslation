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

在 Kotlin 1.1 中，编译器生成 JavaScript 功能已经达到生产可用状态。当然，编译器支持还不足以解决现实生活中的问题，所以我们继续将 Kotlin 整合到更大的 JavaScript 生态系统中。
今天，我们要介绍两个新项目：一个将 Kotlin 与 npm，webpack 和 karma 集成在一起的 Gradle 插件，以及一个实现了 Kotlin/JVM 后端和基于 React 的 Kotlin/JS 前端的全栈应用程序示例。
## Kotlin 前端插件

[Kotlin 前端插件](https://github.com/Kotlin/kotlin-frontend-plugin)  允许你使用 webpack 构建和部署 Kotlin 前端应用。你可以使用 npm 作为应用的包管理器，插件将负责将依赖的包下载并将其打包到生成的 JS 文件中。该插件还与 Karma 集成，允许你运行应用的测试用例。为了获得最佳的工作流程，该插件支持连续编译和实时预览，确保你的应用在浏览器中始终是最新的。
[README](https://github.com/Kotlin/kotlin-frontend-plugin/blob/master/README.md)  文件给出使用插件的说明，示例目录包含一个 [简单的例子](https://github.com/Kotlin/kotlin-frontend-plugin/tree/master/examples/frontend-only)  显示如何将其应用于真实的项目。
## Kotlin React 例子

 [Thinkter](https://github.com/Kotlin/kotlin-fullstack-sample)  是使用 Kotlin 构建的现代全栈应用程序的一个例子。后端运行在 Jetty 并使用 [Ktor](https://github.com/kotlin/ktor) （由 Kotlin 团队开发的 Kotlin Web 应用程序框架）。前端使用 React; Kotlin 的 React Wrappers 是 [作为项目的一部分提供](https://github.com/Kotlin/kotlin-fullstack-sample/tree/master/frontend/src/org/jetbrains/react) 。欢迎你在项目中使用我们的 React Wrappers，并根据自己的需要进行调整。请注意，我们正在努力在内部开发 React Wrappers，我们正在考虑将它们作为单独的开源库发布。
想要了解 Kotlin React 的代码，可以直接阅读 [应用组件](https://github.com/Kotlin/kotlin-fullstack-sample/blob/master/frontend/src/org/jetbrains/demo/thinkter/NewThoughtComponent.kt) 的源码。
Kotlin 开发团队非常欢迎你们反馈意见！请在 GitHub 上提交问题，逛逛 [论坛](https://discuss.kotlinlang.org/) ，或者加入[Kotlin Slack](http://slack.kotlinlang.org/) 的 #javascript 频道。
