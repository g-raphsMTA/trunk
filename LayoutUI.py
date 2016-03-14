
import sys

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder
from GraphPanel import GraphPanel

Builder.load_file("LayoutUI.kv")
#loading the graph capabilities kv file.
Builder.load_file("GraphPanel.kv")

class Test(TabbedPanel):
    pass
        
class BuildLayout(App):
    def build(self):
        layout = AnchorLayout(anchor_x='center', anchor_y='top')

        TopBarHolder = AnchorLayout(anchor_x='left', anchor_y='top',
                                    size_hint=(1, 0.05))
        RemainingHolder = AnchorLayout(anchor_x='left', anchor_y='bottom')
        ToolBarHolder = AnchorLayout(anchor_x='right', andchor_y='bottom')
        
        TopBar = BoxLayout(size_hint=(0.75, 1))

        #this is where the graph visualization goes
        graphPanel = GraphPanel(size_hint=(0.75, 0.95))
        
        ToolBar = Test(size_hint=(0.25, 1))

        btntest = Button(text='topBar')

        #~~~~~~~~~~~
        graphPanel.newGraph(4)
        graphPanel.setVertexPosition(0, 100, 100)
        graphPanel.setVertexPosition(1, 200, 200)
        graphPanel.setVertexPosition(2, 300, 100)
        graphPanel.setVertexPosition(3, 200, 300)
        graphPanel.addEdge(0, 1, 4)
        graphPanel.addEdge(1, 2, 5)
        graphPanel.addEdge(2, 1, 6)
        graphPanel.addEdge(1, 3, 7)
        graphPanel.addEdge(0, 3, 8)

        graphPanel.listOfVertices[1].setRadius(10)
        graphPanel.listOfVertices[0].setRGB(1,0,0)
        graphPanel.listOfVertices[2].setName("Hello")
        graphPanel.setNamesVisible()

        #~~~~~~~~~~~
   
       
        layout.add_widget(TopBarHolder)
        layout.add_widget(RemainingHolder)
        layout.add_widget(ToolBarHolder)
        
        
        
        ToolBarHolder.add_widget(ToolBar)
        TopBarHolder.add_widget(TopBar)
        TopBar.add_widget(btntest)
        RemainingHolder.add_widget(graphPanel)
        
        return layout

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":
    app = BuildLayout()
    app.run()