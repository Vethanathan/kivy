import kivy 
from kivy.uix.boxlayout import BoxLayout 

kivy.require("1.9.1") 
from kivy.uix.button import Button 
from kivy.uix.textinput import TextInput 

from kivy.app import App 

from kivy.uix.label import Label 
  

class MyApp(App):
# layout
    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')
        btn1 = Button(text="OK")
        btn1.bind(on_press=self.buttonClicked)
        
        self.lbl1 = Label(text="test")
        self.lbl1 = Label(text="vyapar_sale and balance , daily_expence income and expence")
        
        self.txt1 = TextInput(text='', multiline=False)
        self.txt2 = TextInput(text='', multiline=False)
        self.txt3 = TextInput(text='', multiline=False)
        self.txt4 = TextInput(text='', multiline=False)
        layout.add_widget(self.txt1)
        layout.add_widget(self.txt2)
        layout.add_widget(self.txt3)
        layout.add_widget(self.txt4)
        layout.add_widget(btn1)
        layout.add_widget(self.lbl1)
        return layout

# button click function
    def buttonClicked(self,btn):
        self.lbl1.text = "Balnce is " + str(  int(self.txt1.text) +    int(self.txt3.text) - int(self.txt2.text) -  int(self.txt4.text  )          )

# run app
if __name__ == "__main__":
    MyApp().run()