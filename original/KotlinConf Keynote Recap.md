---
title: KotlinConf Keynote Recap
author: Dmitry Jemerov
date: 2017-11-02 20:51:00
source_url: https://blog.jetbrains.com/kotlin/2017/11/kotlinconf-keynote-recap/
tags: 
categories:  官方动态
---

Today is a great day for the Kotlin community. KotlinConf, the inaugural Kotlin conference, opens today, and we’re really impressed that around 1200 attendees from all over the world have joined us in San Francisco. During the conference keynote, Andrey Breslav, the lead designer of Kotlin, has announced a few major developments around Kotlin, and now we’re sharing the news with everyone else.
# Kotlin 1.2 RC

The first major announcement from the keynote is the release of Kotlin 1.2 Release Candidate. The new features in this release include the experimental support for multiplatform projects, allowing you to share code between modules targeting the JVM and JavaScript, as well as several language improvements, including support for array literals in annotations. For more information about the new features in 1.2, please check out the Kotlin 1.2 Beta announcement blog post.
The compiler now rejects binaries compiled with earlier pre-release versions of Kotlin 1.2; you’ll need to recompile them with this release. Code compiled with Kotlin 1.0.x or 1.1.x is, of course, fully compatible with this release of the compiler.
Even though coroutines are still labeled as an experimental feature, we’d like to clarify the exact meaning of this status. Coroutines are fully ready to be used in production, we’re using them in our own development, and we’re not aware of any major issues with the implementation. The reason why we keep the experimental status is that it gives us the ability to iterate on the design. Note that, even if we do make changes to the API, the current API will remain supported, even though it will be marked as deprecated, and we will provide the necessary migration tools. According to our current plans, the experimental status of coroutines will be removed in Kotlin 1.3.
Now is the time when we ask for your help. Even though we’ve done a lot of testing of this release internally and with other teams at JetBrains, the real world is far more varied than what we have access to. Therefore, please — give Kotlin 1.2 RC a try on your own projects, and let us know if you run into any issues. Your help is essential in ensuring a smooth final release.
Tell everyone to go try it

{% raw %}
<p><span id="more-5407"></span></p>
{% endraw %}

# Kotlin/Native iOS Support

The next big news we’ve announced is support for iOS development with Kotlin/Native, released as part of Kotlin/Native 0.4. This support is still in its early days, but it’s there, and it’s a major step on our path of enabling Kotlin development on all platforms.
To show what’s possible, we wrote two apps and published them to the App Store:

* The Spinner app (GitHub) is a simple game built using OpenGL. It runs on both iOS and Android (play store link), and most of the code is shared between the two versions. The iOS version has several additional features such as Game Center integration.
* The KotlinConf app (GitHub) shows you the schedule of this conference, and has a fully native iOS UI built with UIKit.

Both of the sample apps are open-source, and you can use them as a template to build your own cross-platform mobile apps in pure Kotlin.
# Kotlin/Native IDE Support

Of course, you need an IDE to be productive with any language, and starting today, Kotlin/Native has IDE support too.
We’re now releasing an initial preview version of the Kotlin/Native plugin for CLion, our C/C++ IDE. The plugin supports CMake as the build system. It includes the full set of code editing features from the Kotlin plugin for IntelliJ IDEA, as well as initial support for project creation, testing and debugging.

{% raw %}
<p><a href="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/11/clion-debugger.png" rel="attachment wp-att-5414"><img alt="clion-debugger" class="alignnone size-full wp-image-5414" height="612" src="https://d3nmt5vlzunoa1.cloudfront.net/kotlin/files/2017/11/clion-debugger.png" width="1600"/></a></p>
{% endraw %}

To try the plugin, install CLion 2017.3 EAP and search for “Kotlin/Native” in the JetBrains plugins list.
In the coming days, we will publish a separate blog post with more details on the plugin and its features. And of course, the CLion plugin is only one step in our story for Kotlin IDE support; stay tuned for further announcements next year!
# Ktor 0.9

Server-side development is also a key part of our multiplatform story. And now we’re announcing our own take on this part: the 0.9 release of Ktor, an awesome asynchronous coroutine-based Web framework built from the ground up in Kotlin.
Ktor is already being used in a number of projects both inside JetBrains and in the community, and now we’re confident that it’s a solid foundation for building very high-performance Web applications. Check out the quick start guides at ktor.io, try it out and let us know what you think so we can make it even better for 1.0 release.
# Creating Modern Web Apps with React and Kotlin

For Web front-end development with Kotlin, the biggest news for today is the release of official Kotlin wrappers for React.js, as well as  create-react-kotlin-app, a toolbox for creating modern web applications in Kotlin using React.js. With create-react-kotlin-app you can generate and immediately start working on client-side apps without worrying about the project setup and build configuration, using the benefits of a statically typed language and the power of the JavaScript ecosystem.
To get started, run npm install -g create-react-kotlin-app and have a look at the Getting started guide.
# Multiplatform Projects Demo

To show how all of the pieces in our multiplatform story fit together, we’ve built an app using all the latest bits of our technology stack: the KotlinConf app. It consists of the following components:

* Backend using Ktor;
* Browser app using React.js and the Kotlin React wrappers;
* Android app using Anko and Android Architecture Components;
* iOS app (mentioned above) using UIKit.

The backend, browser app and Android app share code using the Kotlin multiplatform project technology. For asynchronous programming, all components use coroutines. For exchanging the data between the server and the client, we use the brand new kotlinx.serialization library.
You’ll find the source code of the app a treasure trove of techniques that you will also be able to use in your own work.
# Learning Kotlin

With all the buzz around Kotlin, there will be more and more people interested in learning the language. To make this easier, we’ve released a new version of the EduTools plugin, allowing to learn Kotlin by solving interactive exercises in your favorite IDE. The new version adds support for Android Studio (previously only IntelliJ IDEA was supported), and includes new UI for building your own courses.
# Future Directions

As for the future evolution of the language, our main goal at this time is to enable better and broader code reuse between the platforms supported by Kotlin. We plan to extend the set of libraries available on all platforms with the same API to include I/O, networking, serialization, date handling and more.
In the compiler, our main focus for 1.3 will remain on internal changes, and not on externally visible language features. The internal changes will enable better performance, improved type inference, generation of more efficient code for all target platforms, as well as the much better responsiveness of the IDE plugins. We hope we’ll still be able to sweeten the release with some nice new language features, but we’re not making any promises at this time.
Let’s Kotlin!
