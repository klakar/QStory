# -*- coding: utf-8 -*-
"""
/***************************************************************************
 QStory
                                 A QGIS plugin
 Build a story upon a Web Map
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2019-08-10
        git sha              : $Format:%H$
        copyright            : (C) 2019 by Klas Karlsson
        email                : klas.karlsson@geosupportsystem.se
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication, Qt, QByteArray
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QFileDialog
# Initialize Qt resources from file resources.py
from .resources import *

# Import the code for the DockWidget
from .qstory_dockwidget import QStoryDockWidget
import os.path
from math import log, exp
import json
from distutils.dir_util import copy_tree

# Import functions from QGIS
from qgis.utils import iface
from qgis.core import QgsCoordinateReferenceSystem, QgsCoordinateTransform, QgsProject, QgsPointXY


#------------------------------------------------------------------------
# QStory global variables
qstory_header = []          # Content for the story header div-tag
qstory_body = []            # Content for the story body div-tag
qstory_location = []        # Map location lon,lat string for the story page
qstory_zoom = []            # Map zoom level integer for the story page
current_index = 0           # Currently active page index in the widget
themes_dir = []             # Folder in the plugin dir for story themes
first_run = True            # Some things should only run once on start...

#------------------------------------------------------------------------


class QStory:
    """QGIS Plugin Implementation."""

    
    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface

        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)

        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'QStory_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&QGIS Story Builder')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'QStory')
        self.toolbar.setObjectName(u'QStory')

        #print "** INITIALIZING QStory"

        self.pluginIsActive = False
        self.dockwidget = None


    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('QStory', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToWebMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action


    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/qstory/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'QStory'),
            callback=self.run,
            parent=self.iface.mainWindow())

    #--------------------------------------------------------------------------

    def onClosePlugin(self):
        """Cleanup necessary items here when plugin dockwidget is closed"""

        #print "** CLOSING QStory"

        # disconnects
        self.dockwidget.closingPlugin.disconnect(self.onClosePlugin)

        # remove this statement if dockwidget is to remain
        # for reuse if plugin is reopened
        # Commented next statement since it causes QGIS crashe
        # when closing the docked window:
        # self.dockwidget = None

        self.pluginIsActive = False


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""

        #print "** UNLOAD QStory"

        for action in self.actions:
            self.iface.removePluginWebMenu(
                self.tr(u'&QGIS Story Builder'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar
    
    #--------------------------------------------------------------------------
    # QStory initiate functions
    
    def qstory_initiate(self):
        
        # Use Global variables
        global qstory_header
        global qstory_body
        global qstory_location
        global qstory_zoom
        global current_index
        global themes_dir
        current_index = 0
        qstory_header.clear()
        qstory_body.clear()
        qstory_location.clear()
        qstory_zoom.clear()

        # Set the global variable for the themes directory
        current_dir = os.path.dirname(os.path.realpath(__file__))
        themes_dir = os.path.join(current_dir, 'themes')

        # Get the selectable themes from the themes folder
        self.get_themes()

        # Initial Preview "help" text
        help_text = '<h3>QStory</h3><p>Here there will be some simple "Get Started" text...</p>'
        # Credits
        help_text += '<div style="font-size: 10pt;text-decoration: underline; font-weight: bold;">Credits</div>'
        help_text += '<div style="font-size: 8pt;">Icons made by <a href="https://www.flaticon.com/authors/google" title="Google">Google</a> from <a href="https://www.flaticon.com/"             title="Flaticon">www.flaticon.com</a> is licensed by <a href="http://creativecommons.org/licenses/by/3.0/"             title="Creative Commons BY 3.0" target="_blank">CC 3.0 BY</a></div>'
        self.dockwidget.web_view.setHtml(help_text)

        # Set first story page
        self.dockwidget.cmb_page.clear()
        self.dockwidget.cmb_page.addItem('1')
        
        qstory_header.insert(0, 'First Page')
        qstory_body.insert(0, '<p>This is a simple story</p><p>Replace <b>this</b> text with your content.</p>')
        qstory_location.insert(0, '14,45')
        qstory_zoom.insert(0, 4)

        # Update the widget
        if not first_run:
            self.update_page(0)

        

    #--------------------------------------------------------------------------
    # QStory Helper functions

    # Get all the themes from the themes folder (in the plugin directory)
    def get_themes(self):
        self.dockwidget.cmb_theme.clear()
        for f in os.listdir(themes_dir):
            self.dockwidget.cmb_theme.addItem(f)

    # Delete the current page and decrease the page numbers
    def delete_page(self):

        # Use Global variables
        global qstory_header
        global qstory_body
        global qstory_location
        global qstory_zoom
        global current_index
        
        # Remove current index from all lists
        qstory_header.pop(current_index)
        qstory_body.pop(current_index)
        qstory_location.pop(current_index)
        qstory_zoom.pop(current_index)

        # Remove last page number from page selector
        self.dockwidget.cmb_page.removeItem(self.dockwidget.cmb_page.count()-1)

        # Update the page form
        if self.dockwidget.cmb_page.count() == current_index:
            current_index -= 1
            if current_index == -1:
                self.qstory_initiate()
        self.update_page(current_index)



    # Add a new page after the current and increase the page numbers
    def add_page(self):

        # Use Global variables
        global qstory_header
        global qstory_body
        global qstory_location
        global qstory_zoom
        
        number_of_pages = self.dockwidget.cmb_page.count()      # How many items in the page combo box
        new_page = current_index + 1                            # Index for the new page is current index + 1
        # Add a page number at the end of the selector list
        new_page_number = number_of_pages + 1
        self.dockwidget.cmb_page.addItem(str(new_page_number))

        # Insert the page in the lists
        qstory_header.insert(new_page, 'New Title')
        qstory_body.insert(new_page, 'New Content')
        ccX, ccY, ccZ = self.canvas_center()
        qstory_location.insert(new_page, '%s,%s' % (str(ccX), str(ccY)))
        qstory_zoom.insert(new_page, ccZ)

        # Show the new page
        self.update_page(new_page)
        
    # Canvas center in lon,lat,zoom
    def canvas_center(self):
        center = iface.mapCanvas().center()
        canvasCrs = iface.mapCanvas().mapSettings().destinationCrs()
        qstoryCrs = QgsCoordinateReferenceSystem(4326)
        transform = QgsCoordinateTransform(canvasCrs, qstoryCrs, QgsProject.instance())
        canvas_X, canvas_Y = transform.transform(center.x(), center.y())
        canvas_scale = iface.mapCanvas().scale()
        canvas_zoom = round(log(591657550.500000 /(canvas_scale/2))/log(2))
        return canvas_X, canvas_Y, canvas_zoom


    # Update the current page with the list content for selected page number
    def update_page(self, page_index):
        global current_index
        
        # First save the current content to the lists
        if current_index != page_index:
            qstory_header[current_index] = self.dockwidget.txt_title.text()
            qstory_body[current_index] = self.dockwidget.txt_body.toPlainText()
            qstory_location[current_index] = self.dockwidget.txt_center.text()
            qstory_zoom[current_index] = self.dockwidget.spin_zoom.value()
        
        # Then get and update the form with selected content
        self.dockwidget.txt_title.setText(qstory_header[page_index])
        self.dockwidget.txt_body.setPlainText(qstory_body[page_index])
        self.dockwidget.txt_center.setText(qstory_location[page_index])
        self.dockwidget.cmb_page.setCurrentIndex(page_index)
        self.dockwidget.spin_zoom.setValue(qstory_zoom[page_index])
        current_index = page_index
        
        # Update the map canvas to the current location and zoom level
        self.set_center()

        # Update button status
        self.update_status(current_index)

        # Update preview
        self.story_content_tab()

    # Update button and forms active/disable depending on current index
    def update_status(self, page_index):
        if self.dockwidget.cmb_page.count() >= 2:
            self.dockwidget.btn_next.setEnabled(True)
            self.dockwidget.btn_previous.setEnabled(True)
        if current_index == 0:
            self.dockwidget.btn_previous.setEnabled(False)
        if current_index == self.dockwidget.cmb_page.count()-1:
            self.dockwidget.btn_next.setEnabled(False)

    # Generate a story JS variable for export and save-file
    def generate_output(self):
        
        # Create a local variable to hold the generated JS string
        export_content = [qstory_header, qstory_body, qstory_location, qstory_zoom]
        return export_content

    # Convert coordinate from srsCrs to dstCrs
    def set_center(self):           #Set the canvas center and scale to approximate page location and zoom level.
        location_X, location_Y = [float(c) for c in self.dockwidget.txt_center.text().split(',')]
        center = QgsPointXY(location_X, location_Y)
        canvasCrs = iface.mapCanvas().mapSettings().destinationCrs()
        qstoryCrs = QgsCoordinateReferenceSystem(4326)
        transform = QgsCoordinateTransform(qstoryCrs, canvasCrs, QgsProject.instance())
        canvas_X, canvas_Y = transform.transform(center.x(), center.y())
        iface.mapCanvas().setCenter(QgsPointXY(canvas_X, canvas_Y))
        canvas_scale = (591657550.500000 * 2) / (exp(log(2) * int(self.dockwidget.spin_zoom.value())))
        iface.mapCanvas().zoomScale(canvas_scale)

    # Copy Theme folder to web site folder
    def copy_2_web(self):
        # Create the paths to the web and selected themes dir and copy the content from themes to web (creating the qstory folder)
        web_dir = os.path.join(os.path.dirname(self.dockwidget.html_file.filePath()), 'qstory')
        selected_theme = os.path.join(themes_dir, self.dockwidget.cmb_theme.currentText())
        print(web_dir)
        print(selected_theme)
        copy_tree(selected_theme, web_dir)

    # Generate the story JS and save it to "pages.js" in the web folder (in the qstory folder)
    def generate_storyjs(self):
        # Generate the JS content
        js_content = 'var story_title = %s;\n' % (str(qstory_header))
        js_content += 'var story_content = %s;\n' % (str(qstory_body))
        js_content += 'var story_location = ['        # Break apart the strings in location to a new list of float lists. I.E. [[0,0], [0,0]]
        for single_location in qstory_location:
            js_content += '%s, ' % (str([float(i) for i in single_location.split(',')]))
        js_content = js_content[:-2] + '];\n'    # Remove last comma and blank space from loop above
        js_content += 'var story_zoom = %s;\n' % (str(qstory_zoom))
        # Get the web qstory path
        web_dir = os.path.join(os.path.dirname(self.dockwidget.html_file.filePath()), 'qstory')
        try:
            os.mkdir(web_dir)
        except:
            print('qstory directory already exist...')
        # Create the pages.js file and write the content to it
        pages_file = open(os.path.join(web_dir, 'pages.js'), 'w')
        pages_file.write(js_content)
        pages_file.close()
        

    #--------------------------------------------------------------------------
    # Here are most "first call" functions for the QStory dock widgetfrom qgis.utils import iface


    def story_generate(self):
        # Start by updating all and move to the first page
        self.update_page(0)

        # Test if the selected file is valid
        # Copy Themes folder to web map folder under name "qstory"
        self.copy_2_web()
        # Generate pages.js file in the new folder
        self.generate_storyjs()
        # Add reference to css and JS in the web map start file
        style_add = '<link rel="stylesheet" href="./qstory/qstory.css"></head>'
        js_add = '<div id="story"><div id="story_header">Title</div><div id="story_body"></div><div id="story_footer"></div></div><script src="./qstory/pages.js"></script><script src="./qstory/qstory.js"></script></body>'
        # Read the web file
        web_file = open(self.dockwidget.html_file.filePath(), 'r')
        web_content = web_file.read()
        web_file.close()
        print(web_content)
        if web_content.find(style_add):     # If the link to qstory.css exist, do nothing. Otherwise continue...
            web_content = web_content.replace('</head>', style_add)
            web_content = web_content.replace('</body>', js_add)
            # Save the new content to the qstory.htm copy of the web file
            story_file = open(os.path.join(os.path.dirname(self.dockwidget.html_file.filePath()), 'qstory.htm'),'w')
            story_file.write(web_content)
            story_file.close()
        """
        The above if statement will not create a new htm file if the file used as a source already have
        the links and placeholders in it. If it have a slightly different string, the new ones will be added anyway.
        If the filename for the source is the same (qstory.htm) the old file will be overritten with the new content.
        """


    def story_content_tab(self):    # Check if the second (preview) tab is active, and in that case update preview of the story page
        # Get the template CSS file from the themes folder
        css_file = open(os.path.join(themes_dir, self.dockwidget.cmb_theme.currentText(),'qstory.css'), 'r')
        css_code = css_file.read()
        css_file.close()
        if self.dockwidget.tab_widget.currentIndex() == 1:
            html = '<style>' + css_code + '</style>'
            html += '<div id="story"><div id="story_header">' + self.dockwidget.txt_title.text() + '</div>'
            html += '<div id="story_body">' + self.dockwidget.txt_body.toPlainText() + '</div></div>' 
            self.dockwidget.web_view.setHtml(html)

    def get_selected(self):         # Change story page to the one selected in the page combo box
        self.update_page(self.dockwidget.cmb_page.currentIndex())

    def next_page(self):            # Go to next story page
        self.update_page(current_index + 1)

    def previous_page(self):        # Go to previous story page
        self.update_page(current_index - 1)

    def get_center(self):           #Get the center coordinate from the canvas, transform it to wgs-84 and estimate zoom level from scale.
        ccX, ccY, ccZ = self.canvas_center()
        self.dockwidget.txt_center.setText('%s,%s' % (str(round(ccX,4)), str(round(ccY,4))))
        self.dockwidget.spin_zoom.setValue(ccZ)

    def save_story(self):
        # Create file
        filename = QFileDialog.getSaveFileName(None, 'Save Story As...','Once_Upon_A_Time.qstory', 'QStory FIles (*.qstory);; QStory Files (*.qstory)')
        # Open file and save generated content to it.
        if filename[0] != '':          # Don't save if dialog is cancelled
            file = open(filename[0], 'w')
            json.dump(self.generate_output(), file)
            file.close()

    def open_story(self):
        # Use global variables
        global qstory_header
        global qstory_body
        global qstory_location
        global qstory_zoom

        current_index = 0
        qstory_header.clear()
        qstory_body.clear()
        qstory_location.clear()
        qstory_zoom.clear()

        # Open a QStory file (basically a textfile with JSON syntax)
        filename = QFileDialog.getOpenFileName(None, 'Open a Story File...', '', 'QStory FIles (*.qstory);; QStory Files (*.qstory)')
        # Read the content and put it into a list with all rows
        if filename[0] != '':
            file = open(filename[0], 'r')
            qstory_header, qstory_body, qstory_location, qstory_zoom = json.load(file)
            file.close()
            
        # Update number of story pages
        self.dockwidget.cmb_page.clear()
        for number in range(1, len(qstory_header) + 1):        # The range function does not include the "end" number. This is why +1
            self.dockwidget.cmb_page.addItem(str(number))
         
        # Update the story pages
        self.update_page(0)

 
    #--------------------------------------------------------------------------

    def run(self):
        """Run method that loads and starts the plugin"""

        if not self.pluginIsActive:
            global current_index

            self.pluginIsActive = True

            #print "** STARTING QStory"

            # dockwidget may not exist if:
            #    first run of plugin
            #    removed on close (see self.onClosePlugin method)
            if self.dockwidget == None:
                # Create the dockwidget (after translation) and keep reference
                self.dockwidget = QStoryDockWidget()

            # connect to provide cleanup on closing of dockwidget
            self.dockwidget.closingPlugin.connect(self.onClosePlugin)

            # show the dockwidget
            # TODO: fix to allow choice of dock location
            self.iface.addDockWidget(Qt.RightDockWidgetArea, self.dockwidget)
            self.dockwidget.show()

            # Initiate the dockwidget
            self.qstory_initiate()

            # Catch events when buttons clicked in panel
            # Each must have corresponding def name():
            self.dockwidget.btn_open.clicked.connect(self.open_story)
            self.dockwidget.btn_save.clicked.connect(self.save_story)
            self.dockwidget.btn_delete.clicked.connect(self.delete_page)
            self.dockwidget.btn_previous.clicked.connect(self.previous_page)
            self.dockwidget.btn_next.clicked.connect(self.next_page)
            self.dockwidget.btn_new.clicked.connect(self.add_page)
            self.dockwidget.btn_center.clicked.connect(self.get_center)
            self.dockwidget.btn_generate.clicked.connect(self.story_generate)
            self.dockwidget.tab_widget.currentChanged.connect(self.story_content_tab)
            self.dockwidget.cmb_page.activated[str].connect(self.get_selected)
            self.dockwidget.cmb_theme.activated[str].connect(self.story_content_tab)
