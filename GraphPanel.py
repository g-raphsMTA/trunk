from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty
from Edge import Edge
from Vertex import Vertex
from kivy.lang import Builder
Builder.load_file('GraphPanel.kv')

class GraphPanel(Widget):

    currentVertex = ObjectProperty( None )
    listOfVertices = ObjectProperty( [] )
    listOfEdges = ObjectProperty( [] )
    currentEdge = 0

  #  def __init__(self, numVertices):
   #     for x in range(0, numVertices):
    #        vertex = Vertex()
     #       vertex.setAlpha(0)
         #   self.add_widget(vertex)
      #      self.listOfVertices.append(vertex)
      #  print(len(self.listOfVertices))

    def newGraph(self, numVertices):
        for x in range(0, numVertices):
            vertex = Vertex()
            self.listOfVertices.append(vertex)
            self.add_widget(vertex)
        
    def modifyVertex(self, vertexNo, name):
        pass

    def modifyVertex(self, vertexNo, name, info):
        pass

    def setVertexPosition(self, vertexNo, x, y):
        self.listOfVertices[vertexNo].setPosition(x,y)
        self.listOfVertices[vertexNo].setAlpha(1)

    def addEdge(self, vertexFromIndex, vertexToIndex, weight):
        edge = Edge()
        self.add_widget(edge)
        edge.setVertices(self.listOfVertices[vertexFromIndex], self.listOfVertices[vertexToIndex])
        self.listOfEdges.append(edge)
        self.listOfVertices[vertexFromIndex].addOutgoingEdge(self.currentEdge)
        self.listOfVertices[vertexToIndex].addIncomingEdge(self.currentEdge)
        self.currentEdge = self.currentEdge + 1
        
    
  #  def addVertexArray(self, vertexArray):
   #     for vertex in vertexArray:
    #        self.listOfVertices.append(vertex)
     #       self.add_widget(vertex)

 #   def addEdgeArray(self, edgeArray):
  #      for edge in edgeArray:
   #         self.listOfEdges.append(edge)
    #        self.add_widget(edge)

    def on_touch_down(self, touch):
        for vertex in self.listOfVertices:
            if vertex.collide_point(touch.x, touch.y):
                self.currentVertex = vertex
                break
            
    def ont_touch_up(self, touch):
        self.currentVertex = ObjectProperty(None)
        
    def on_touch_move(self, touch):
        if self.currentVertex != None:
          # self.currentVertex.setPosition(touch.x, touch.y)
            
            for e in self.currentVertex.getIncomingEdgeIndexes():
                self.listOfEdges[e].changeToCoordinates(touch.x, touch.y)
                
            for e in self.currentVertex.getOutgoingEdgeIndexes():
                self.listOfEdges[e].changeFromCoordinates(touch.x, touch.y)


class GraphPanelApp(App):
    def build(self):
        graphPanel = GraphPanel()
        graphPanel.newGraph(3)
        graphPanel.setVertexPosition(0, 100, 100)
        graphPanel.setVertexPosition(1, 200, 200)
        graphPanel.setVertexPosition(2,300, 100)
        graphPanel.addEdge(0, 1, 4)
        graphPanel.addEdge(1, 2, 5)
        
       # vertex1 = Vertex(pos = (100,100), radius = 25)
  #      vertex2 = Vertex(pos = (200,200), radius = 25)
   #     vertex3 = Vertex(pos = (300,100), radius = 25)
    #    edge1 = Edge()
     #   edge2 = Edge()
      #  edge1.setVertices(vertex1, vertex2)
       # edge2.setVertices(vertex2, vertex3)
    #    edge1.changeFromCoordinates(0,0)
     #   edge2.changeToCoordinates(500,100)
    #    vArray = [vertex1, vertex2, vertex3]
    #    eArray = [edge1, edge2]

    #    print(vertex2.getEdgeInc())
     #   graphPanel.addVertexArray(vArray)
       # graphPanel.addEdgeArray(eArray)
        
        return graphPanel

if __name__ == '__main__':
    GraphPanelApp().run()