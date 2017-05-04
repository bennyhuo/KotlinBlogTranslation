---
title: "Writing Kotlin in the Browser"
date: 2013-10-16 08:00:00
author: Hadi Hariri
tags:
keywords:
categories: 官方动态
reward: false
reward_title: Have a nice Kotlin!
reward_wechat:
reward_alipay:
source_url: https://blog.jetbrains.com/kotlin/2013/10/writing-kotlin-in-the-browser/
translator:
translator_url:
---

Did you know that Kotlin can target JavaScript as well as the JVM? Don’t be too surprised if you didn’t know, as we’ve not been giving it too much coverage, despite already shipping a [successful product](http://blog.jetbrains.com/webide/2012/08/liveedit-plugin-features-in-detail/) that uses this capability. But here’s hoping to change things.<span id="more-1330"></span>
# The Basics – A Simple Project

First step is to set up a new project. When using Kotlin in a project, we have the ability to target either the JVM or JavaScript. If we’re adding a new Kotlin file to an existing project, [Kotlin will prompt us for this](http://blog.jetbrains.com/kotlin/2013/10/how-to-configure-kotlin-in-your-project/) . If we’re starting a new project, we can choose the target during the setup wizard, assuming we’re using IntelliJ IDEA.

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/10/image.png?resize=610%2C499&amp;ssl=1" style="padding-top: 0px; padding-left: 0px; padding-right: 0px; border-width: 0px;"/></p>
{% endraw %}

We also need to add the Kotlin standard library to the project. Clicking on the Create button we’ll be prompted with the location where we want these files copied. By default it copies is to a folder named *script*. And we’ll get to this later on as it’s important.

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/10/image1.png?resize=603%2C157&amp;ssl=1" style="padding-top: 0px; padding-left: 0px; padding-right: 0px; border-width: 0px;"/></p>
{% endraw %}

## Project organization

The resulting structure of the project should be

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/10/image2.png?resize=350%2C196&amp;ssl=1" style="padding-top: 0px; padding-left: 0px; padding-right: 0px; border-width: 0px;"/></p>
{% endraw %}

The project has two files that are added:

* The lib folder contains the header files, as a jar file, which are used during development.
* The script folder contains a single kotlin.js which is the Kotlin runtime library. This is used in production.

All our Kotlin source code should be placed in the *src*folder. Once this is compiled, it will generate some JavaScript files that need to then be shipped along with the *kotlin.js* runtime file.
All other source code, be this external JavaScript libraries or files, CSS and HTML files can be placed anywhere, preferably in the same project to make development easier but not necessarily. For our example we’re going to place this in a folder called *web*and create a series of subfolders to structure our code.

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i0.wp.com/blog.jetbrains.com/kotlin/files/2013/10/image3.png?resize=344%2C259&amp;ssl=1" style="padding-top: 0px; padding-left: 0px; padding-right: 0px; border-width: 0px;"/></p>
{% endraw %}

## Setting up a workflow

When we write Kotlin code,the compiler will generate some JavaScript which needs to be shipped as part of our application. By default, IntelliJ IDEA will output this file and its sourcemap to a folder named *out/production/{project_name}*

{% raw %}
<p><img alt="image" border="0" data-recalc-dims="1" src="https://i2.wp.com/blog.jetbrains.com/kotlin/files/2013/10/image4.png?resize=275%2C154&amp;ssl=1" style="padding-top: 0px; padding-left: 0px; margin: 0px; padding-right: 0px; border-width: 0px;"/></p>
{% endraw %}

During development we need to have an up to date version of these files so ideally we’d like to have these located in our *web/js/app*folder. We can do this in many ways, either using [IntelliJ IDEA artifacts](http://www.jetbrains.com/idea/webhelp/artifact.html) or Maven/Gradle. In our case we’re just going to use an artifact. We can set one up to copy the corresponding files to the desired output location and additional also copy the *kotlin.js* file that was originally copied to the *script*folder to the same location*.
***<span style="font-size: x-small;">*This is a one-time operation so a better alternative is to define the output location of this file directly to our required output folder when setting up the project. We have done it this way to explain things step by step. </span>***
## Interacting with DOM Elements

Now that we have the project layout ready, let’s start writing some code. The most basic thing we can do is manipulate some DOM elements. We can create a simple HTML page (named *index.html*) and place it under the *web*folder
The idea is to now update the value of the input field using Kotlin.  For that we can create a new file called *main*.*kt*and place it under our *src*folder.
## Web-targeted Libraries

Kotlin provides a series of libraries targeted specifically at the web. In our case, since we want to manipulate the DOM, we can import the *js.dom.html*to access the *document* variable. The resulting code would be
which is very straightforward. We’re using the *document.getElementById*to retrieve the DOM element and then setting its value using *setAttribute*. Exactly the same way we’d do it using JavaScript, except here we’re using Kotlin and have the benefit of static typing, among other things.
The standard library already provides support for DOM manipulation, HTML 5 features such as Canvas and Local Storage, as well as wrappers for common libraries such as jQuery. We will be adding more as we go along, and we’ll cover some of them in future posts.
## Running the code

Now that we have the code compiled, we need to actually run it. For this we have to reference both the *kotlin.js*as well as the generated (*basic.js*) file from our *index.html* page.

{% raw %}
<p> </p>
{% endraw %}

The code corresponding to the *main* function will automatically be called when the page is loaded.
Once we load our *index.html*page, we should see the result.

{% raw %}
<p><img alt="image" data-recalc-dims="1" src="https://i1.wp.com/blog.jetbrains.com/kotlin/files/2013/10/image5.png?resize=638%2C283&amp;ssl=1"/></p>
{% endraw %}

## Calling Kotlin from JavaScript

What if we have some code in Kotlin we want to use from JavaScript? For instance, think of scenarios where you need to do some sort of business logic that needs to be repeated both on the client and the server. Well all we need to do is write it and then call it. Here is a simple function written in Kotlin

{% raw %}
<p> </p>
{% endraw %}

This is placed inside the same module as the application and we can call it referencing it by the Kotlin module name*
**<span style="color: #000000;">**This API is not final and will most likely change in the future, and probably will be much more compact.*</span>**
# Next Steps

That’s not all that is possible with Kotlin. One thing we haven’t mentioned is the ability to call JavaScript code from within Kotlin and that is something we’ll be covering in a another post, as this one has already become too long!
If you want to play with Kotlin to JavaScript without having to install anything, you can also try it directly in the [browser](http://kotlin-demo.jetbrains.com) . And as always, give us your feedback!
