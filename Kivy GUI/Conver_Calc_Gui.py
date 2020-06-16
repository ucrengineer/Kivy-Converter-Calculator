from kivy.config import Config
Config.set('graphics','resizable',0)

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty,ObjectProperty,NumericProperty
import LabelB


Builder.load_string("""

<Option>:
    BoxLayout:
        cols: 2
        rows: 1


        Button:
            text: "Calculator"
            font_size:"20sp"

            
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'calculator'
            
        Button:
            text: "Converter"
            font_size:"20sp"
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'converter'

<Converter>:
    FloatLayout:
        size: 300,300

        

        Spinner:
            id: pressure
            text:"Pressure Units"
            values: ["mpa","psi","atm","bar"]
            pos: 100,540
            size_hint:.15,.1
            on_text: root.on_spinner_select(self.text)
     

        Spinner:
            id: length
            text: "Length Units"
            values:["in","cm","mm",\
                    "micron","nanometer"]
            pos: 100,480
            size_hint: .15,.1
            on_text: root.on_spinner_select(self.text)

        Spinner:
            id: mass
            text: "Mass Units"
            values:["g","oz","lb",\
                    "ml"]
            pos: 100,420
            size_hint: .15,.1
            on_text: root.on_spinner_select(self.text)

        Spinner:
            id: temp
            text: "Temp Units"
            values:["c","k","f"]
            pos: 100,360
            size_hint: .15,.1
            on_text: root.on_spinner_select(self.text)

        Spinner:
            id: time
            text: "Time Units"
            values:["sec","min","hours",\
                    "days"]
            pos: 100,300
            size_hint: .15,.1
            on_text: root.on_spinner_select(self.text)

        Spinner:
            id: hardness
            text: "Hardness"
            values:["vickers","Pa"]
            pos: 100,240
            size_hint: .15,.1
            on_text: root.on_spinner_select(self.text)


        Spinner:
            id: pressure
            text:"Pressure Units"
            values: ["mpa","psi","atm","bar"]
            pos: 575,540
            size_hint:.15,.1
            on_text: root.on_spinner_select2(self.text)
     

        Spinner:
            id: length
            text: "Length Units"
            values:["in","cm","mm",\
                    "micron","nanometer"]
            pos: 575,480
            size_hint: .15,.1
            on_text: root.on_spinner_select2(self.text)

        Spinner:
            id: mass
            text: "Mass Units"
            values:["g","oz","lb",\
                    "ml"]
            pos: 575,420
            size_hint: .15,.1
            on_text: root.on_spinner_select2(self.text)

        Spinner:
            id: temp
            text: "Temp Units"
            values:["c","k","f"]
            pos: 575,360
            size_hint: .15,.1
            on_text: root.on_spinner_select2(self.text)

        Spinner:
            id: time
            text: "Time Units"
            values:["sec","min","hours",\
                    "days"]
            pos: 575,300
            size_hint: .15,.1
            on_text: root.on_spinner_select2(self.text)

        Spinner:
            id: hardness
            text: "Hardness"
            values:["vickers","Pa"]
            pos: 575,240
            size_hint: .15,.1
            on_text: root.on_spinner_select2(self.text)






        
        Button:
            text: "Calculator Screen"
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'calculator'
            size_hint:.5,.25
            pos:400,0
        Button:
            text: "Front Screen"
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'option'
            size_hint:.5,.25

        TextInput:
            id: value
            text:""
            font_size: "25sp"
            size_hint: .15,.1
            pos: 340,400
            on_text: root.grabvalue(self.text)
            

        Button:
            text: "Convert!"
            size_hint: .15,.1
            pos:340,350
            on_press: root.convert(root.value,root.var1,root.var2)
          
        Label:
            text: "Convert " + root.strvalue +" " + root.var1 + " to " + root.var2
            pos: 6,0

        LabelB:
            text: "{}".format(root.solution)
            font_size: "40sp"
            pos: 315,150
            bcolor: 1,0,0,1
            size_hint: .22,.2

<Calculator>:
    GridLayout:
        cols:4
        rows:3

        Button:
            text: "Converter Screen"
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'converter'
            size_hint_y:None
            size_hint_x:None
            width:200
        Label:
            text: "Input Data"
        Label:
            text: "Display Data"
        Button:
            text: "Calculate"
            size_hint_y:None

        Button:
            text: "Front Screen"
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'option'

            
""")

#Create View 
class Option(Screen):
    pass

class Calculator(Screen):
    pass

#View object for Converter
class Converter(Screen):
    #Create Model functions
   var1 = StringProperty()
   var2 = StringProperty()
   value = NumericProperty()
   strvalue = StringProperty()
   value = 1
   solution = NumericProperty()
   
   
   
   
   def on_spinner_select(self,text):
       self.var1 = text

   def on_spinner_select2(self,text):
       self.var2 = text

   def grabvalue(self,value):
       self.value = value
       self.strvalue = value
       
   #Create Logic functions
   def convert(self,value,var1,var2):
       time = {
        'sec':1, 'min':60, 'hours':60**2,'days':60**2*(24)
           }
       pressure = {
           'mpa':1,'psi':.00689476,'atm':.101325,'bar':.1
           }
       length = {'in':1,'cm':.393701,'mm':.0393701,'micron':3.93701e-5,
                 'nanometer':3.93701e-8
           }
       mass = {
           'g':1,'oz':28.3495,'lb':453.592,'ml':1
           }

       hardness = {
           'vickers':1,'Pa':1/9.807
           }

           
      
       try:    
           self.solution = int(value)*time[var1]/time[var2]
       except:
           pass
       try:
           self.solution = int(value)*pressure[var1]/pressure[var2]
       except:
           pass
       try:
           self.solution = int(value)*length[var1]/length[var2]
       except:
           pass
       try:
           self.solution = int(value)*mass[var1]/mass[var2]
       except:
           pass
       try:
           if var1 == 'c' and var2 == 'k':
               self.solution = int(value) + 273.15
           if var1 == 'c' and var2 == 'f':
               self.solution = (int(value)*9/5) + 32
           if var1 == 'k' and var2 == 'c':
               self.solution = int(value) - 273.15
           if var1 == 'k' and var2 == 'f':
               self.solution = (int(value)-273.15)*9/5 + 32
           if var1 == 'f' and var2 == 'k':
               self.solution = (int(value)-32)*5/9 + 273.15       
           if var1 == 'f' and var2 == 'c':
               self.solution = (int(value)-32)*5/9

       except:
           pass
       try:
           self.solution = int(value)*hardness[var1]/hardness[var2]
       except:
           pass
        

      

       

       
      
        
       
       
       
    


#Create the screen manager
sm = ScreenManager()
sm.add_widget(Option(name='option'))
sm.add_widget(Calculator(name='calculator'))
sm.add_widget(Converter(name='converter'))

#Create class for app
class ConvertCulator(App):

    def build(self):
        return sm

#Create Loop
if __name__ == '__main__':
    ConvertCulator().run()
    
