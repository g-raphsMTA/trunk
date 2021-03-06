
import sys

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from GraphPanel import GraphPanel
from InfoPanel import InfoPanel
from SearchPanel import SearchPanel
from VertexPositionAlg import resetButton
from ColorPopupM import vertexColorButton, backgroundColorButton
from NbhPanel import NbhPanel
from GraphLoader import Root

#loading the LayoutUI specifications
Builder.load_file("LayoutUI.kv")

#Initializing the Test class (Renamed later)
class Toolbar(TabbedPanel):
    
    infoPanel = ObjectProperty(InfoPanel(size_hint=(1, 0.8)))
    searchPanel = ObjectProperty(SearchPanel(size_hint=(1, 1)))
    
    def Initalize(self, graph):
        nbhPanel = NbhPanel()
        
        info = InfoPanel(size_hint=(1, 0.8))
        self.infoPanel = info
        box = BoxLayout(orientation='vertical')
        box.add_widget(info)
        tinybox2 = BoxLayout(size_hint=(1, 0.2))
        box.add_widget(tinybox2)
        tinybox2.add_widget(nbhPanel)
        
        search = SearchPanel(size_hint=(1, 1))
        self.searchPanel = search
        resetBtn = resetButton()
        
        resetBtn.initialize(graph)
        nbhPanel.initialize(graph)
        search.initialize(graph)
        
        gbox = BoxLayout(orientation='vertical')
        gbox.add_widget(search)
        
        tinybox = BoxLayout(size_hint=(1, 0.2))
        tinybox.add_widget(resetBtn)
        
        gbox.add_widget(tinybox)

        self.ids.Node.add_widget(box)
        self.ids.Graph.add_widget(gbox)
        
        

class TabbedPanelApp(App):
    def build(self):
        TabbedPanel.add_widget(btntest)
        return Toolbar()

        
class BuildLayout(App):
    def build(self):
        
        #vvvv Basic Layouts vvvv
        layout = AnchorLayout(anchor_x='center', anchor_y='top')

        TopBarHolder = AnchorLayout(anchor_x='left', anchor_y='top',
                                    size_hint=(1, 0.05))
        RemainingHolder = AnchorLayout(anchor_x='left', anchor_y='bottom')
        ToolBarHolder = AnchorLayout(anchor_x='right', andchor_y='bottom')
        #^^^^ Basic Layouts ^^^^

        #HELP POPUP
        helpWin = Popup(title='Help', content=Label(text='This will be the help window'), size_hint=(None, None), size=(400, 400))

        #this is the top bar
        TopBar = BoxLayout(size_hint=(0.75, 1))
        #vvvv And contents of Top Bar vvvv
        btnOpenFile = Button(text='Open new File')
        root = Root()
        btnOpenFile.bind(on_release=root.show_load)


        
        bgCol = backgroundColorButton(text='background Col')
        vertexCol = vertexColorButton(text='vertex Col')
        btnDisplay = Button(text='Display')

        
        #vvvv this is the Tabbed Box on the right side vvvv
        ToolBar = Toolbar(size_hint=(0.25, 1))
        
        #vvvv and the contents of the Toolbar vvvv

        lblPlaceholder = Label(text='_________')
        
        lblInfo = Label(tet='Info')
        
        
        
        #this is where the graph visualization goes
        graphPanel = GraphPanel(size_hint=(0.75, 0.95))


        #vvvv GraphPanel settings vvvv
        graphPanel.setNamesVisible()
        #^^^^ GraphPanel settings ^^^^ 
   

        #vvvv Adding everything to the UI vvvv
        layout.add_widget(RemainingHolder)
        layout.add_widget(TopBarHolder)
        RemainingHolder.add_widget(graphPanel)
        layout.add_widget(ToolBarHolder)
        
        
        ToolBarHolder.add_widget(ToolBar)

        
        TopBarHolder.add_widget(TopBar)
        TopBar.add_widget(btnOpenFile)
        TopBar.add_widget(bgCol)
        TopBar.add_widget(vertexCol)

        
        ToolBar.Initalize(graphPanel)
        bgCol.initialize(graphPanel)
        vertexCol.initialize(graphPanel)
        root.set_graph(graphPanel)
        
        graphPanel.setDataColector(ToolBar.infoPanel)

        
        
        #^^^^ Adding everything to the UI ^^^^

        
        return layout

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
    app = BuildLayout()
    app.run()

