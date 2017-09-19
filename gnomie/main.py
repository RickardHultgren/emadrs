import kivy
from datetime import datetime, timedelta

kivy.require('1.7.2') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from functools import partial
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.slider import Slider
#from kivy.clock import Clock

from kivy.core.window import Window


mngr = 'madrs'
thedate = thedate=datetime.now().strftime("%Y%m%d")

Builder.load_string('''
<MADRS>:
	name: 'madrs'
	container:container
    ScrollView:
        pos_hint: {'x': 0, 'y': 0}
        size_hint: 1,.85
        size: self.size
        #height: root.theheight
        #height: root.theheight
        StackLayout:
            padding: root.width * 0.02, root.height * 0.02
            spacing: root.width * 0.02, root.height * 0.02            
            size_hint_y: None
            size_hint_x: 1            
            do_scroll_x: False
            do_scroll_y: True
            id: container
''')

#https://stackoverflow.com/questions/18670687/how-i-can-adjust-variable-height-text-property-kivy

#https://www.psy-world.com/madrs.htm

class MADRS(Screen):
	global mngr
	global thedate
	global markedlines
	theheight=NumericProperty()
	def __init__ (self,**kwargs):
		super(MADRS,self).__init__(**kwargs)
		global mngr
		global markedlines
		global thedate

		q1 = Label(
			text='1 - APPAREN SADNESS - Representing despondency, gloom and despair, (more than just ordinary transient low spirits) reflected in speech, facial expression, and posture. Rate by depth and inability to brighten up. ',
			size_hint_y=None, size_hint_x=1)
		q1.bind(width=lambda s, w:
			   s.setter('text_size')(s, (self.width, None)))
		q1.bind(height=q1.setter('texture_size[1]'))
		q1.bind(height=q1.setter('self.minimum_height'))
		

		a1text00 = Label(
			text='Nothing marked                                       ',
			size_hint_y=None)
		a1text00.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a1text00.bind(texture_size=a1text00.setter('size'))
				
		a1text6 = Label(
			text='6. Looks miserable all the time. Extremely despondent.',
			size_hint_y=None)
		a1text6.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a1text6.bind(texture_size=a1text00.setter('texture_size'))
		
		a1text5 = Label(
			text='5.',
			size_hint_y=None)
		a1text5.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a1text5.bind(texture_size=a1text00.setter('texture_size'))

		a1text4 = Label(
			text='4. Appears sad and unhappy most of the time',
			size_hint_y=None)
		a1text4.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a1text4.bind(texture_size=a1text00.setter('texture_size'))

		a1text3 = Label(
			text='3.',
			size_hint_y=None)
		a1text3.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a1text3.bind(texture_size=a1text00.setter('texture_size'))

		a1text2 = Label(
			text='2.',
			size_hint_y=None)
		a1text2.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a1text2.bind(texture_size=a1text00.setter('texture_size'))

		a1text1 = Label(
			text='1.',
			size_hint_y=None)
		a1text1.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a1text1.bind(texture_size=a1text00.setter('texture_size'))

		a1text0 = Label(
			text='0.',
			size_hint_y=None)
		a1text0.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a1text0.bind(texture_size=a1text00.setter('texture_size'))


		a1text = GridLayout(orientation='vertical', cols=1, size_hint_x=.5, padding=0, spacing=0,
		#adjust to content size:
		size_hint_y = None
		)

		a1text.add_widget(a1text6)
		a1text.add_widget(a1text5)
		a1text.add_widget(a1text4)
		a1text.add_widget(a1text3)
		a1text.add_widget(a1text2)
		a1text.add_widget(a1text1)
		a1text.add_widget(a1text0)
		a1text.add_widget(a1text00)
		
		a1slider = Slider(
			size_hint_y=None,
			size_hint_x=.5,
			step=1,
			min=-1,
			max=7,
			id="a1slider",
			orientation='vertical',
			height= 7*(a1text00.height)
			
		)
		a1text.bind(height=a1text.setter('self.minimum_height'))
		#adjust to content size:
		a1slider.bind(height=a1slider.setter('self.minimum_height'))
		#self.container.height=a1text00.height+q1.height
		#self.container.bind(height=2*a1text00.setter('height'))
		
		self.theheight=a1slider.height+q1.height
		self.container.height=self.theheight
		
		self.container.add_widget(q1) 		
		self.container.add_widget(a1slider)
		self.container.add_widget(a1text)

class gnomieApp(App):
	global mngr
	def build(self):
		global mngr
		the_screenmanager = ScreenManager()
		madrs = MADRS(name='madrs')
		#Clock.schedule_interval(homescreen.update, 0.25)
		if mngr=='madrs':
			the_screenmanager.add_widget(madrs)
		return the_screenmanager
		
if __name__ == '__main__':
	gnomieApp().run()

