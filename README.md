# QStory
This is a QGIS plugin that adds "story" functionality to web maps from qgis2web (and other similar tools)

## Idea
It is possible to include this functionality into other plug-ins, but after some consideration I desided to start from a Unix filosofy and try and build a tool that does One thing, and does it (reasonably) well.

This plug-in is a tool to build the story, not the map. Use any tool you want to build your web map (for now qgis2web is recommended) and then this tool to build the story and "apply" it to the web map.
## Basic functionality
The plugin is pointed to a html-file for the web map. In that it looks for the &lt;/head&gt; and &lt;/body&gt; tags, where it adds some code.

When the story is generated it will save resource files at the web map location, that is called by the code in the html file.
## The plugin principals
The plugin is a simple form to generate the story "pages". It is only the content that is created, the style and apperance in the end result is controled by selecting a "theme". Themes are folders with resource files that can be anything, but at a minimum there should be a "qstory.css" and a "qstory.js" file.

The plugin generates a couple of list variables that is used in a pages.js file to generate the story pages. This generation of the lists is independent of which "theme" that is selected. This means the basic structure is pretty simple and the real power is implemented in the resource files.

This also makes it easier to add and modify themes for the plugin in the future. Initially there will be a very limited number of simple themes, and when the basic functionality is settled you are encouraged to contribute with additional story themes to the project.
## Goals
I will build this plugin first as a protorype, when I have some time over. There's no time goal and progress and end results will depend on the community involvement.

The plugin will only be uploaded to the QGIS repository if there's a possitive response from users.

## Forks
If anyone think you can do this better it's quite OK to "steal" the project and use it in other plug-ins (GPL3 license). Just let me know so I can move on to other experiments...

## Download
You can use the code as a whole, but if you just want to test the plugin as it is right now, you can use the zip-file:
https://github.com/klakar/QStory/raw/master/qstory/qstory.zip
