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
from kivy.graphics import Color, Rectangle
from kivy.storage.jsonstore import JsonStore
try:
	from plyer import email
except:
	pass
from kivy.utils import platform

#https://blog.kivy.org/2014/01/building-a-background-application-on-android-with-kivy/

gnomedata = JsonStore('hello.json')
#MADRSdata = JsonStore('hello.json')
settingdata = JsonStore('hello.json')

settingdata.put('email', address='')

    
    

mngr = 'madrs'
thedate = thedate=datetime.now().strftime("%Y%m%d")

Builder.load_string('''
<Gnome>:
	name: 'gnome'
	container:container
    ActionBar:
        background_color:0,191,255,0.5
        pos_hint: {'top':1}
        ActionView:
            use_separator: True
            ActionPrevious:
                title: 'gnomie'
                with_previous: False
            ActionGroup:
                mode: 'spinner'
                text: 'Menu'
                ActionButton:
                    text: 'gnomie'
                    on_release: app.root.current = 'gnome'
                ActionButton:
                    text: 'MADRS-S'
                    on_release: app.root.current = 'madrs'
                ActionButton:
                    text: 'Settings'
                    on_release: root.settings()
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

<MADRS>:
	name: 'madrs'
	container:container
    ActionBar:
        background_color:0,191,255,0.5
        pos_hint: {'top':1}
        ActionView:
            use_separator: True
            ActionPrevious:
                title: 'gnomie'
                with_previous: False
            ActionGroup:
                mode: 'spinner'
                text: 'Menu'
                ActionButton:
                    text: 'gnomie'
                    on_release: app.root.current = 'gnome'
                ActionButton:
                    text: 'MADRS-S'
                    on_release: app.root.current = 'madrs'
                ActionButton:
                    text: 'Settings'
                    on_release: root.settings()
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

class Gnome(Screen):
	global mngr
	mngr='gnome'
	global thedate
	global markedlines
	theheight=NumericProperty()
	summa = int()
	def __init__ (self,**kwargs):
		super(Gnome,self).__init__(**kwargs)
		global mngr
		global markedlines
		global thedate
###

	
class MADRS(Screen):
	global mngr
	mngr='madrs'
	global thedate
	global markedlines
	theheight=NumericProperty()
	summa = int()
	def __init__ (self,**kwargs):
		super(MADRS,self).__init__(**kwargs)
		global mngr
		global markedlines
		global thedate
###

		q1 = Label(
			text='1 - APPAREN SADNESS - Representing despondency, gloom and despair, (more than just ordinary transient low spirits) reflected in speech, facial expression, and posture. Rate by depth and inability to brighten up. ',
			size_hint_y=None, size_hint_x=1)
		q1.bind(width=lambda s, w:
			   s.setter('text_size')(s, (self.width, None)))
		q1.bind(height=q1.setter('texture_size[1]'))
		q1.bind(height=q1.setter('self.minimum_height'))
		

		a1text00 = Label(
			text='Nothing marked                                             ',
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
			text='2. Looks dispirited but does brighten up without difficulty.',
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
			text='0. No sadness.',
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
			value=-1,
			id="a1slider",
			orientation='vertical',
			height= 7*(a1text00.height)
			
		)
		a1text.bind(height=a1text.setter('self.minimum_height'))
		a1slider.bind(height=a1slider.setter('self.minimum_height'))
		

###



		q2 = Label(
			text='2 - REPORTED SADNESS - Representing reports of depressed mood, regardless of whether it is reflected in appearance or not. Includes low spirits, despondency or the feeling of being beyond help and without hope. Rate according to intensity, duration and the extent to which the mood is reported to be influenced by events.',
			size_hint_y=None, size_hint_x=1)
		q2.bind(width=lambda s, w:
			   s.setter('text_size')(s, (self.width, None)))
		q2.bind(height=q2.setter('texture_size[1]'))
		q2.bind(height=q2.setter('self.minimum_height'))
		

		a2text00 = Label(
			text='Nothing marked                                             ',
			size_hint_y=None)
		a2text00.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a2text00.bind(texture_size=a2text00.setter('size'))
				
		a2text6 = Label(
			text='6. Continuous or unvarying sadness, misery or despondency.',
			size_hint_y=None)
		a2text6.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a2text6.bind(texture_size=a2text00.setter('texture_size'))
		
		a2text5 = Label(
			text='5.',
			size_hint_y=None)
		a2text5.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a2text5.bind(texture_size=a2text00.setter('texture_size'))

		a2text4 = Label(
			text='4. Pervasive feelings of sadness or gloominess. The mood is still influenced by external circumstances. ',
			size_hint_y=None)
		a2text4.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a2text4.bind(texture_size=a2text00.setter('texture_size'))

		a2text3 = Label(
			text='3.',
			size_hint_y=None)
		a2text3.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a2text3.bind(texture_size=a2text00.setter('texture_size'))

		a2text2 = Label(
			text='2. Sad or low but brightens up without difficulty',
			size_hint_y=None)
		a2text2.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a2text2.bind(texture_size=a2text00.setter('texture_size'))

		a2text1 = Label(
			text='1.',
			size_hint_y=None)
		a2text1.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a2text1.bind(texture_size=a2text00.setter('texture_size'))

		a2text0 = Label(
			text='0. Occasional sadness in keeping with the circumstances.',
			size_hint_y=None)
		a2text0.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a2text0.bind(texture_size=a2text00.setter('texture_size'))


		a2text = GridLayout(orientation='vertical', cols=1, size_hint_x=.5, padding=0, spacing=0,
		#adjust to content size:
		size_hint_y = None
		)

		a2text.add_widget(a2text6)
		a2text.add_widget(a2text5)
		a2text.add_widget(a2text4)
		a2text.add_widget(a2text3)
		a2text.add_widget(a2text2)
		a2text.add_widget(a2text1)
		a2text.add_widget(a2text0)
		a2text.add_widget(a2text00)
		
		a2slider = Slider(
			size_hint_y=None,
			size_hint_x=.5,
			step=1,
			min=-1,
			max=7,
			value=-1,
			id="a2slider",
			orientation='vertical',
			height= 7*(a2text00.height)
			
		)
		a2text.bind(height=a2text.setter('self.minimum_height'))
		a2slider.bind(height=a2slider.setter('self.minimum_height'))
		

###


		q3 = Label(
			text='3 - INNER TENSION - Representing feelings of ill-defined discomfort, edginess, inner turmoil, mental tension mounting to either panic, dread or anguish. Rate according to intensity, frequency, duration and the extent of reassurance called for.',
			size_hint_y=None, size_hint_x=1)
		q3.bind(width=lambda s, w:
			   s.setter('text_size')(s, (self.width, None)))
		q3.bind(height=q3.setter('texture_size[1]'))
		q3.bind(height=q3.setter('self.minimum_height'))
		

		a3text00 = Label(
			text='Nothing marked                                             ',
			size_hint_y=None)
		a3text00.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a3text00.bind(texture_size=a3text00.setter('size'))
				
		a3text6 = Label(
			text='6. Unrelenting dread or anguish. Overwhelming panic.',
			size_hint_y=None)
		a3text6.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a3text6.bind(texture_size=a3text00.setter('texture_size'))
		
		a3text5 = Label(
			text='5.',
			size_hint_y=None)
		a3text5.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a3text5.bind(texture_size=a3text00.setter('texture_size'))

		a3text4 = Label(
			text='4. Continuous feelings of inner tension or intermittent panic which the patient can only master with some difficulty.',
			size_hint_y=None)
		a3text4.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a3text4.bind(texture_size=a3text00.setter('texture_size'))

		a3text3 = Label(
			text='3.',
			size_hint_y=None)
		a3text3.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a3text3.bind(texture_size=a3text00.setter('texture_size'))

		a3text2 = Label(
			text='2. Occasional feelings of edginess and ill-defined discomfort.',
			size_hint_y=None)
		a3text2.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a3text2.bind(texture_size=a3text00.setter('texture_size'))

		a3text1 = Label(
			text='1.',
			size_hint_y=None)
		a3text1.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a3text1.bind(texture_size=a3text00.setter('texture_size'))

		a3text0 = Label(
			text='0. Placid. Only fleeting inner tension.',
			size_hint_y=None)
		a3text0.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a3text0.bind(texture_size=a3text00.setter('texture_size'))


		a3text = GridLayout(orientation='vertical', cols=1, size_hint_x=.5, padding=0, spacing=0,
		#adjust to content size:
		size_hint_y = None
		)

		a3text.add_widget(a3text6)
		a3text.add_widget(a3text5)
		a3text.add_widget(a3text4)
		a3text.add_widget(a3text3)
		a3text.add_widget(a3text2)
		a3text.add_widget(a3text1)
		a3text.add_widget(a3text0)
		a3text.add_widget(a3text00)
		
		a3slider = Slider(
			size_hint_y=None,
			size_hint_x=.5,
			step=1,
			min=-1,
			max=7,
			value=-1,
			id="a3slider",
			orientation='vertical',
			height= 7*(a3text00.height)
			
		)
		a3text.bind(height=a3text.setter('self.minimum_height'))
		a3slider.bind(height=a3slider.setter('self.minimum_height'))
		
###


		q4 = Label(
			text='4 - REDUCED SLEEP - Representing the experience of reduced duration or depth of sleep compared to the subject\'s own normal pattern when well.',
			size_hint_y=None, size_hint_x=1)
		q4.bind(width=lambda s, w:
			   s.setter('text_size')(s, (self.width, None)))
		q4.bind(height=q4.setter('texture_size[1]'))
		q4.bind(height=q4.setter('self.minimum_height'))
		

		a4text00 = Label(
			text='Nothing marked                                             ',
			size_hint_y=None)
		a4text00.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a4text00.bind(texture_size=a4text00.setter('size'))
				
		a4text6 = Label(
			text='6. Less than two or three hours sleep.',
			size_hint_y=None)
		a4text6.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a4text6.bind(texture_size=a4text00.setter('texture_size'))
		
		a4text5 = Label(
			text='5.',
			size_hint_y=None)
		a4text5.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a4text5.bind(texture_size=a4text00.setter('texture_size'))

		a4text4 = Label(
			text='4. Sleep reduced or broken by at least two hours.',
			size_hint_y=None)
		a4text4.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a4text4.bind(texture_size=a4text00.setter('texture_size'))

		a4text3 = Label(
			text='3.',
			size_hint_y=None)
		a4text3.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a4text3.bind(texture_size=a4text00.setter('texture_size'))

		a4text2 = Label(
			text='2. Slight difficulty dropping off to sleep or slightly reduced, light or fitful sleep',
			size_hint_y=None)
		a4text2.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a4text2.bind(texture_size=a4text00.setter('texture_size'))

		a4text1 = Label(
			text='1.',
			size_hint_y=None)
		a4text1.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a4text1.bind(texture_size=a4text00.setter('texture_size'))

		a4text0 = Label(
			text='0. Sleeps as usual.',
			size_hint_y=None)
		a4text0.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a4text0.bind(texture_size=a4text00.setter('texture_size'))


		a4text = GridLayout(orientation='vertical', cols=1, size_hint_x=.5, padding=0, spacing=0,
		#adjust to content size:
		size_hint_y = None
		)

		a4text.add_widget(a4text6)
		a4text.add_widget(a4text5)
		a4text.add_widget(a4text4)
		a4text.add_widget(a4text3)
		a4text.add_widget(a4text2)
		a4text.add_widget(a4text1)
		a4text.add_widget(a4text0)
		a4text.add_widget(a4text00)
		
		a4slider = Slider(
			size_hint_y=None,
			size_hint_x=.5,
			step=1,
			min=-1,
			max=7,
			value=-1,
			id="a4slider",
			orientation='vertical',
			height= 7*(a4text00.height)
			
		)
		a4text.bind(height=a4text.setter('self.minimum_height'))
		a4slider.bind(height=a4slider.setter('self.minimum_height'))
		
###


		q5 = Label(
			text='5 - REDUCED APPETITE - Representing the feeling of a loss of appetite compared with when well. Rate by loss of desire for food or the need to force oneself to eat.',
			size_hint_y=None, size_hint_x=1)
		q5.bind(width=lambda s, w:
			   s.setter('text_size')(s, (self.width, None)))
		q5.bind(height=q5.setter('texture_size[1]'))
		q5.bind(height=q5.setter('self.minimum_height'))
		

		a5text00 = Label(
			text='Nothing marked                                             ',
			size_hint_y=None)
		a5text00.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a5text00.bind(texture_size=a5text00.setter('size'))
				
		a5text6 = Label(
			text='6. Needs persuasion to eat at all.',
			size_hint_y=None)
		a5text6.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a5text6.bind(texture_size=a5text00.setter('texture_size'))
		
		a5text5 = Label(
			text='5.',
			size_hint_y=None)
		a5text5.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a5text5.bind(texture_size=a5text00.setter('texture_size'))

		a5text4 = Label(
			text='4. No appetite. Food is tasteless.',
			size_hint_y=None)
		a5text4.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a5text4.bind(texture_size=a5text00.setter('texture_size'))

		a5text3 = Label(
			text='3.',
			size_hint_y=None)
		a5text3.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a5text3.bind(texture_size=a5text00.setter('texture_size'))

		a5text2 = Label(
			text='2. Slightly reduced appetite.',
			size_hint_y=None)
		a5text2.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a5text2.bind(texture_size=a5text00.setter('texture_size'))

		a5text1 = Label(
			text='1.',
			size_hint_y=None)
		a5text1.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a5text1.bind(texture_size=a5text00.setter('texture_size'))

		a5text0 = Label(
			text='0. Normal or increased appetite.',
			size_hint_y=None)
		a5text0.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a5text0.bind(texture_size=a5text00.setter('texture_size'))


		a5text = GridLayout(orientation='vertical', cols=1, size_hint_x=.5, padding=0, spacing=0,
		#adjust to content size:
		size_hint_y = None
		)

		a5text.add_widget(a5text6)
		a5text.add_widget(a5text5)
		a5text.add_widget(a5text4)
		a5text.add_widget(a5text3)
		a5text.add_widget(a5text2)
		a5text.add_widget(a5text1)
		a5text.add_widget(a5text0)
		a5text.add_widget(a5text00)
		
		a5slider = Slider(
			size_hint_y=None,
			size_hint_x=.5,
			step=1,
			min=-1,
			max=7,
			value=-1,
			id="a5slider",
			orientation='vertical',
			height= 7*(a5text00.height)
			
		)
		a5text.bind(height=a5text.setter('self.minimum_height'))
		a5slider.bind(height=a5slider.setter('self.minimum_height'))
		

###


		q6 = Label(
			text='6 - CONCENTRATION DIFFICULTIES - Representing difficulties in collecting one\'s thoughts mounting to incapacitating lack of concentration. Rate according to intensity, frequency, and degree of incapacity produced.',
			size_hint_y=None, size_hint_x=1)
		q6.bind(width=lambda s, w:
			   s.setter('text_size')(s, (self.width, None)))
		q6.bind(height=q6.setter('texture_size[1]'))
		q6.bind(height=q6.setter('self.minimum_height'))
		

		a6text00 = Label(
			text='Nothing marked                                             ',
			size_hint_y=None)
		a6text00.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a6text00.bind(texture_size=a6text00.setter('size'))
				
		a6text6 = Label(
			text='6. Unable to read or converse without great difficulty.',
			size_hint_y=None)
		a6text6.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a6text6.bind(texture_size=a6text00.setter('texture_size'))
		
		a6text5 = Label(
			text='5.',
			size_hint_y=None)
		a6text5.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a6text5.bind(texture_size=a6text00.setter('texture_size'))

		a6text4 = Label(
			text='4. Difficulties in concentrating and sustaining thought which reduces ability to read or hold a conversation.',
			size_hint_y=None)
		a6text4.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a6text4.bind(texture_size=a6text00.setter('texture_size'))

		a6text3 = Label(
			text='3.',
			size_hint_y=None)
		a6text3.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a6text3.bind(texture_size=a6text00.setter('texture_size'))

		a6text2 = Label(
			text='2. Occasional difficulties in collecting one\'s thoughts.',
			size_hint_y=None)
		a6text2.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a6text2.bind(texture_size=a6text00.setter('texture_size'))

		a6text1 = Label(
			text='1.',
			size_hint_y=None)
		a6text1.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a6text1.bind(texture_size=a6text00.setter('texture_size'))

		a6text0 = Label(
			text='0. No difficulties in concentrating.',
			size_hint_y=None)
		a6text0.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a6text0.bind(texture_size=a6text00.setter('texture_size'))


		a6text = GridLayout(orientation='vertical', cols=1, size_hint_x=.5, padding=0, spacing=0,
		#adjust to content size:
		size_hint_y = None
		)

		a6text.add_widget(a6text6)
		a6text.add_widget(a6text5)
		a6text.add_widget(a6text4)
		a6text.add_widget(a6text3)
		a6text.add_widget(a6text2)
		a6text.add_widget(a6text1)
		a6text.add_widget(a6text0)
		a6text.add_widget(a6text00)
		
		a6slider = Slider(
			size_hint_y=None,
			size_hint_x=.5,
			step=1,
			min=-1,
			max=7,
			value=-1,
			id="a6slider",
			orientation='vertical',
			height= 7*(a6text00.height)
			
		)
		a6text.bind(height=a6text.setter('self.minimum_height'))
		a6slider.bind(height=a6slider.setter('self.minimum_height'))
		
###


		q7 = Label(
			text='7 - LASSITUDE - Representing a difficulty getting started or slowness initiating and performing everyday activities.',
			size_hint_y=None, size_hint_x=1)
		q7.bind(width=lambda s, w:
			   s.setter('text_size')(s, (self.width, None)))
		q7.bind(height=q7.setter('texture_size[1]'))
		q7.bind(height=q7.setter('self.minimum_height'))
		

		a7text00 = Label(
			text='Nothing marked                                             ',
			size_hint_y=None)
		a7text00.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a7text00.bind(texture_size=a7text00.setter('size'))
				
		a7text6 = Label(
			text='6. Complete lassitude. Unable to do anything without help.',
			size_hint_y=None)
		a7text6.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a7text6.bind(texture_size=a7text00.setter('texture_size'))
		
		a7text5 = Label(
			text='5.',
			size_hint_y=None)
		a7text5.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a7text5.bind(texture_size=a7text00.setter('texture_size'))

		a7text4 = Label(
			text='4. Difficulties in starting simple routine activities, which are carried out with effort.',
			size_hint_y=None)
		a7text4.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a7text4.bind(texture_size=a7text00.setter('texture_size'))

		a7text3 = Label(
			text='3.',
			size_hint_y=None)
		a7text3.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a7text3.bind(texture_size=a7text00.setter('texture_size'))

		a7text2 = Label(
			text='2. Difficulties in starting activities.',
			size_hint_y=None)
		a7text2.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a7text2.bind(texture_size=a7text00.setter('texture_size'))

		a7text1 = Label(
			text='1.',
			size_hint_y=None)
		a7text1.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a7text1.bind(texture_size=a7text00.setter('texture_size'))

		a7text0 = Label(
			text='0. Hardly any difficulties in getting started. No sluggishness.',
			size_hint_y=None)
		a7text0.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a7text0.bind(texture_size=a7text00.setter('texture_size'))


		a7text = GridLayout(orientation='vertical', cols=1, size_hint_x=.5, padding=0, spacing=0,
		#adjust to content size:
		size_hint_y = None
		)

		a7text.add_widget(a7text6)
		a7text.add_widget(a7text5)
		a7text.add_widget(a7text4)
		a7text.add_widget(a7text3)
		a7text.add_widget(a7text2)
		a7text.add_widget(a7text1)
		a7text.add_widget(a7text0)
		a7text.add_widget(a7text00)
		
		a7slider = Slider(
			size_hint_y=None,
			size_hint_x=.5,
			step=1,
			min=-1,
			max=7,
			value=-1,
			id="a7slider",
			orientation='vertical',
			height= 7*(a7text00.height)
			
		)
		a7text.bind(height=a7text.setter('self.minimum_height'))
		a7slider.bind(height=a7slider.setter('self.minimum_height'))
###


		q8 = Label(
			text='8 - INABILITY TO FEEL - Representing the subjective experience of reduced interest in the surroundings, or activities that normally give pleasure.The ability to react with adequate emotion to circumstances or people is reduced.',
			size_hint_y=None, size_hint_x=1)
		q8.bind(width=lambda s, w:
			   s.setter('text_size')(s, (self.width, None)))
		q8.bind(height=q8.setter('texture_size[1]'))
		q8.bind(height=q8.setter('self.minimum_height'))
		

		a8text00 = Label(
			text='Nothing marked                                             ',
			size_hint_y=None)
		a8text00.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a8text00.bind(texture_size=a8text00.setter('size'))
				
		a8text6 = Label(
			text='6. The experience of being emotionally paralyzed, inability to feel anger, grief or pleasure and a complete or even painful failure to feel for close relatives and friends.',
			size_hint_y=None)
		a8text6.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a8text6.bind(texture_size=a8text00.setter('texture_size'))
		
		a8text5 = Label(
			text='5.',
			size_hint_y=None)
		a8text5.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a8text5.bind(texture_size=a8text00.setter('texture_size'))

		a8text4 = Label(
			text='4. Loss of interest in the surroundings. Loss of feelings for friends and acquaintances.',
			size_hint_y=None)
		a8text4.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a8text4.bind(texture_size=a8text00.setter('texture_size'))

		a8text3 = Label(
			text='3.',
			size_hint_y=None)
		a8text3.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a8text3.bind(texture_size=a8text00.setter('texture_size'))

		a8text2 = Label(
			text='2. Reduced ability to enjoy usual interests.',
			size_hint_y=None)
		a8text2.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a8text2.bind(texture_size=a8text00.setter('texture_size'))

		a8text1 = Label(
			text='1.',
			size_hint_y=None)
		a8text1.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a8text1.bind(texture_size=a8text00.setter('texture_size'))

		a8text0 = Label(
			text='0. Normal interest in the surroundings and in other people.',
			size_hint_y=None)
		a8text0.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a8text0.bind(texture_size=a8text00.setter('texture_size'))


		a8text = GridLayout(orientation='vertical', cols=1, size_hint_x=.5, padding=0, spacing=0,
		#adjust to content size:
		size_hint_y = None
		)

		a8text.add_widget(a8text6)
		a8text.add_widget(a8text5)
		a8text.add_widget(a8text4)
		a8text.add_widget(a8text3)
		a8text.add_widget(a8text2)
		a8text.add_widget(a8text1)
		a8text.add_widget(a8text0)
		a8text.add_widget(a8text00)
		
		a8slider = Slider(
			size_hint_y=None,
			size_hint_x=.5,
			step=1,
			min=-1,
			max=7,
			value=-1,
			id="a8slider",
			orientation='vertical',
			height= 7*(a8text00.height)
			
		)
		a8text.bind(height=a8text.setter('self.minimum_height'))
		a8slider.bind(height=a8slider.setter('self.minimum_height'))
				
###


		q9 = Label(
			text='9 - PESSIMISTIC THOUGHTS - Representing thoughts of guilt, inferiority, self-reproach, sinfulness, remorse and ruin.',
			size_hint_y=None, size_hint_x=1)
		q9.bind(width=lambda s, w:
			   s.setter('text_size')(s, (self.width, None)))
		q9.bind(height=q9.setter('texture_size[1]'))
		q9.bind(height=q9.setter('self.minimum_height'))
		

		a9text00 = Label(
			text='Nothing marked                                             ',
			size_hint_y=None)
		a9text00.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a9text00.bind(texture_size=a9text00.setter('size'))
				
		a9text6 = Label(
			text='6. Delusions of ruin, remorse and unredeemable sin. Self-accusations which are absurd and unshakable.',
			size_hint_y=None)
		a9text6.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a9text6.bind(texture_size=a9text00.setter('texture_size'))
		
		a9text5 = Label(
			text='5.',
			size_hint_y=None)
		a9text5.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a9text5.bind(texture_size=a9text00.setter('texture_size'))

		a9text4 = Label(
			text='4. Persistent self-accusations, or definite but still rational ideas of guilt or sin. Increasingly pessimistic about the future.',
			size_hint_y=None)
		a9text4.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a9text4.bind(texture_size=a9text00.setter('texture_size'))

		a9text3 = Label(
			text='3.',
			size_hint_y=None)
		a9text3.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a9text3.bind(texture_size=a9text00.setter('texture_size'))

		a9text2 = Label(
			text='2. Fluctuating ideas of failure, self-reproach or self-depreciation.',
			size_hint_y=None)
		a9text2.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a9text2.bind(texture_size=a9text00.setter('texture_size'))

		a9text1 = Label(
			text='1.',
			size_hint_y=None)
		a9text1.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a9text1.bind(texture_size=a9text00.setter('texture_size'))

		a9text0 = Label(
			text='0. No pessimistic thoughts.',
			size_hint_y=None)
		a9text0.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a9text0.bind(texture_size=a9text00.setter('texture_size'))


		a9text = GridLayout(orientation='vertical', cols=1, size_hint_x=.5, padding=0, spacing=0,
		#adjust to content size:
		size_hint_y = None
		)

		a9text.add_widget(a9text6)
		a9text.add_widget(a9text5)
		a9text.add_widget(a9text4)
		a9text.add_widget(a9text3)
		a9text.add_widget(a9text2)
		a9text.add_widget(a9text1)
		a9text.add_widget(a9text0)
		a9text.add_widget(a9text00)
		
		a9slider = Slider(
			size_hint_y=None,
			size_hint_x=.5,
			step=1,
			min=-1,
			max=7,
			value=-1,
			id="a9slider",
			orientation='vertical',
			height= 7*(a9text00.height)
			
		)
		a9text.bind(height=a9text.setter('self.minimum_height'))
		a9slider.bind(height=a9slider.setter('self.minimum_height'))
		
###


		q10 = Label(
			text='10 - SUICIDAL THOUGHTS - Representing the feeling that life is not worth living, that a natural death would be welcome, suicidal thoughts, and preparations for suicide. Suicidal attempts should not in themselves influence the rating.',
			size_hint_y=None, size_hint_x=1)
		q10.bind(width=lambda s, w:
			   s.setter('text_size')(s, (self.width, None)))
		q10.bind(height=q10.setter('texture_size[1]'))
		q10.bind(height=q10.setter('self.minimum_height'))
		

		a10text00 = Label(
			text='Nothing marked                                             ',
			size_hint_y=None)
		a10text00.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a10text00.bind(texture_size=a10text00.setter('size'))
				
		a10text6 = Label(
			text='6. Explicit plans for suicide when there is an opportunity. Active preparations for suicide.',
			size_hint_y=None)
		a10text6.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a10text6.bind(texture_size=a10text00.setter('texture_size'))
		
		a10text5 = Label(
			text='5.',
			size_hint_y=None)
		a10text5.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a10text5.bind(texture_size=a10text00.setter('texture_size'))

		a10text4 = Label(
			text='4. Probably better off dead. Suicidal thoughts are common, and suicide is considered as a possible solution, but without specific plans or intention.',
			size_hint_y=None)
		a10text4.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a10text4.bind(texture_size=a10text00.setter('texture_size'))

		a10text3 = Label(
			text='3.',
			size_hint_y=None)
		a10text3.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a10text3.bind(texture_size=a10text00.setter('texture_size'))

		a10text2 = Label(
			text='2. Weary of life. Only fleeting suicidal thoughts.',
			size_hint_y=None)
		a10text2.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a10text2.bind(texture_size=a10text00.setter('texture_size'))

		a10text1 = Label(
			text='1.',
			size_hint_y=None)
		a10text1.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a10text1.bind(texture_size=a10text00.setter('texture_size'))

		a10text0 = Label(
			text='0. Enjoys life or takes it as it comes.',
			size_hint_y=None)
		a10text0.bind(width=lambda s, w:
			   s.setter('text_size')(s, (.5*self.width, None)))
		a10text0.bind(texture_size=a10text00.setter('texture_size'))


		a10text = GridLayout(orientation='vertical', cols=1, size_hint_x=.5, padding=0, spacing=0,
		#adjust to content size:
		size_hint_y = None
		)

		a10text.add_widget(a10text6)
		a10text.add_widget(a10text5)
		a10text.add_widget(a10text4)
		a10text.add_widget(a10text3)
		a10text.add_widget(a10text2)
		a10text.add_widget(a10text1)
		a10text.add_widget(a10text0)
		a10text.add_widget(a10text00)
		
		a10slider = Slider(
			size_hint_y=None,
			size_hint_x=.5,
			step=1,
			min=-1,
			max=7,
			value=-1,
			id="a10slider",
			orientation='vertical',
			height= 6.5*(a10text00.height)
			
		)
		a10text.bind(height=a10text.setter('self.minimum_height'))
		a10slider.bind(height=a10slider.setter('self.minimum_height'))
		

###

		submit_btn=Button(text='Submit',size_hint=(1, None), orientation='vertical', height=.66*q1.height, width=self.width)
		self.theheight=a1slider.height+(.5 * q1.height)+q1.height+(.5 * q1.height)+a2slider.height+(.5 * q1.height)+q2.height+(.5 * q1.height)+a3slider.height+(.5 * q1.height)+q3.height+(.5 * q1.height)+a4slider.height+(.5 * q1.height)+q4.height+(.5 * q1.height)+a5slider.height+(.5 * q1.height)+q5.height+(.5 * q1.height)+a6slider.height+(.5 * q1.height)+q6.height+(.5 * q1.height)+a7slider.height+(.5 * q1.height)+q7.height+(.5 * q1.height)+a8slider.height+(.5 * q1.height)+q8.height+(.5 * q1.height)+a9slider.height+(.5 * q1.height)+q9.height+(.5 * q1.height)+a10slider.height+(.5 * q1.height)+q10.height+(.5 * q1.height)+submit_btn.height
		self.container.height=self.theheight
		
		self.container.add_widget(q1) 		
		self.container.add_widget(a1slider)
		self.container.add_widget(a1text)

		self.container.add_widget(q2) 		
		self.container.add_widget(a2slider)
		self.container.add_widget(a2text)

		self.container.add_widget(q3) 		
		self.container.add_widget(a3slider)
		self.container.add_widget(a3text)

		self.container.add_widget(q4) 		
		self.container.add_widget(a4slider)
		self.container.add_widget(a4text)

		self.container.add_widget(q5) 		
		self.container.add_widget(a5slider)
		self.container.add_widget(a5text)

		self.container.add_widget(q6) 		
		self.container.add_widget(a6slider)
		self.container.add_widget(a6text)

		self.container.add_widget(q7) 		
		self.container.add_widget(a7slider)
		self.container.add_widget(a7text)

		self.container.add_widget(q8) 		
		self.container.add_widget(a8slider)
		self.container.add_widget(a8text)

		self.container.add_widget(q9) 		
		self.container.add_widget(a9slider)
		self.container.add_widget(a9text)

		self.container.add_widget(q10) 		
		self.container.add_widget(a10slider)
		self.container.add_widget(a10text)
				
		self.container.add_widget(BoxLayout(orientation='vertical', height=.66*q1.height,width=self.width, size_hint=(None, None)))
			
		submit_btn.bind(on_press=lambda submit_btn: self.Submit(a1slider.value , a2slider.value , a3slider.value , a4slider.value , a5slider.value , a6slider.value , a7slider.value , a8slider.value , a9slider.value , a10slider.value))
		self.container.add_widget(submit_btn)

	def Submit(self, a1slider , a2slider , a3slider , a4slider , a5slider , a6slider , a7slider , a8slider , a9slider , a10slider):
		if a1slider < 0 or a2slider < 0 or a3slider < 0 or a4slider < 0 or a5slider < 0 or a6slider < 0 or a7slider < 0 or a8slider < 0 or a9slider < 0 or a10slider < 0 :
			box = BoxLayout(orientation='vertical')
			popup1 = Popup(title='', content=box, size_hint=(None, None), size=(400, 400))
			box.add_widget(Label(text='Please fill in all the forms'))
			store_btn = Button(text='OK')
			store_btn.bind(on_press = lambda *args: popup1.dismiss())
			box.add_widget(store_btn)
			popup1.open()
		else:
			self.summa=a1slider + a2slider + a3slider + a4slider + a5slider + a6slider + a7slider + a8slider + a9slider + a10slider
			box = BoxLayout(orientation='vertical')
			popup1 = Popup(title='', content=box, size_hint=(None, None), size=(400, 400))
			if self.summa < 13:
				themessage='Your MADRS-score: %s\nYou probalbly do not have a depression.'%(self.summa)
			if self.summa >= 13 and self.summa <= 19:
				themessage='Your MADRS-score: %s\nYou probalbly have a mild depression.'%(self.summa)
			if self.summa >= 20 and self.summa <= 34:
				themessage='Your MADRS-score: %s\nYou probalbly have a moderate depression.'%(self.summa)
			if self.summa >= 35 :
				themessage='Your MADRS-score: %s\nYou probalbly have a severe depression.'%(self.summa)
			box.add_widget(Label(text=themessage))	
			store_btn = Button(text='OK')
			store_btn.bind(on_press = lambda store_btn: self.send_mail(themessage, popup1))
			box.add_widget(store_btn)
			popup1.open()

	def settings(self):
		box = BoxLayout(orientation='vertical')
		popup1 = Popup(title='Settings', content=box, size_hint=(None, None), size=(400, 400))
		box.add_widget(Label(text='Email-setting:'))
		inpt=TextInput(text=settingdata.get('email')['address'], multiline=False)
		box.add_widget(inpt)
		store_btn = Button(text='OK')
		store_btn.bind(on_release=(lambda store_btn: self.change_mail(inpt.text, popup1)))
		#store_btn.bind(on_press = lambda *args: popup1.dismiss())
		box.add_widget(store_btn)
		popup1.open()

	
	def change_mail(self, theaddress, popup1):
		popup1.dismiss()
		settingdata.put('email', address=theaddress)

	def send_mail(self, themessage, popup1):
		popup1.dismiss()
		box = BoxLayout(orientation='vertical')
		try:
			passemail.send(recipient=StringProperty(settingdata.get('email')['address']),
				subject=StringProperty('MADRS-S'),
				text=StringProperty('%s'%themessage),
				create_chooser=BooleanProperty())
			box.add_widget(Label(text='Email sent to:%s'%settingdata.get('email')['address']))
		except:
			box.add_widget(Label(text='Couldn\'t send e-mail'))
		
		popup2 = Popup(title='Settings', content=box, size_hint=(None, None), size=(400, 400))
		store_btn = Button(text='OK')
		store_btn.bind(on_press = lambda *args: popup2.dismiss())
		box.add_widget(store_btn)
		popup2.open()

		
class gnomieApp(App):
	global mngr
	def build(self):
		if platform == 'android':
			from android import AndroidService
			service = AndroidService('my pong service', 'running')
			service.start('service started')
			self.service = service		
		global mngr
		the_screenmanager = ScreenManager()
		madrs = MADRS(name='madrs')
		gnome = Gnome(name='gnome')
		#Clock.schedule_interval(homescreen.update, 0.25)
		if mngr=='madrs':
			the_screenmanager.add_widget(madrs)
			the_screenmanager.add_widget(gnome)
		if mngr=='gnome':
			the_screenmanager.add_widget(gnome)
			the_screenmanager.add_widget(madrs)
		return the_screenmanager
		
if __name__ == '__main__':
	gnomieApp().run()

