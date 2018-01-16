# coding:utf-8
import kivy
kivy.require('1.7.2') # replace with your current kivy version !
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ListProperty, ObjectProperty, StringProperty, NumericProperty
from kivy.factory import Factory
from kivy.uix.button import Button
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.spinner import Spinner
from kivy.uix.dropdown import DropDown
from kivy.uix.checkbox import CheckBox
from kivy.lang import Builder
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
#from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
from kivy.storage.jsonstore import JsonStore
#from kivy.uix.gridlayout import GridLayout
from functools import partial
#from kivy.uix.treeview import TreeView, TreeViewNode
#from kivy.uix.treeview import TreeViewLabel
#from kivy.uix.scrollview import ScrollView
try:
	from plyer import email
except:
	pass
#Declaration of global variables:
settingdata = JsonStore('settingdata.json')
statuscpy = dict(JsonStore('statusdata.json'))
statusdict = dict()

Builder.load_string('''
<MainScreen>:
    GridLayout:
        row_default_height:root.height / 8
		cols:1
        orientation: 'vertical'
        name: 'mainscreen'
        ActionBar:
            width:root.width
            height:root.height / 8
            background_color:50,125,255,.6
            pos_hint: {'top':1}
            ActionView:
                use_separator: True
                ActionPrevious:
                    title: 'eMADRS'
                    with_previous: False
                ActionGroup:
                    mode: 'spinner'
                    text: 'Menu'
                    ActionButton:
                        text: 'Settings'
                        on_release: root.settings()
    
        ScrollView:
            width:root.width
            height:root.height / 4
            hint_size:1,1/4
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
                id: qbox    
        GridLayout:
            orientation: 'vertical'
            cols:1
            width:root.width
            height:root.height / 4            
            ScrollView:
                size: self.size
                #height: root.theheight
                BoxLayout:
                    padding: root.width * 0.02, root.height * 0.02
                    spacing: root.width * 0.02, root.height * 0.02            
                    size_hint_y: 1
                    size_hint_x: None            
                    do_scroll_x: True
                    do_scroll_y: False
                    id: container
        BoxLayout:
            width:root.width
            height:root.height / 8
            orientation: 'horizontal'
            size_hint: 1, 0.10
            pos_hint: {'x': 0, 'y': 0}
            id:checkboxes
''')  

class MainScreen(Screen):
	nownr=0
	currentnr = NumericProperty(nownr)
	qlist=(
	"Här ber vi dig beskriva din sinnesstämning, om du känner dig ledsen, tungsint eller dyster till mods. Tänk efter hur du har känt dig de senaste tre dagarna, om du har skiftat i humöret eller om det har varit i stort sett detsamma hela tiden, och försök särskilt komma ihåg om du har känt dig lättare till sinnes om det har hänt något positivt.",
	"Här ber vi dig markera i vilken utsträckning du haft känslor av inre spänning, olust och ångest eller odefinierad rädsla under de senaste tre dagarna. Tänk särskilt på hur intensiva känslorna varit, och om de kommit och gått eller funnits hela tiden.",
	"Här ber vi Dig beskriva hur bra du sover. Tänk efter hur länge du sovit och hur god sömnen varit under de senaste tre nätterna. Bedömningen skall avse hur du faktiskt sovit, oavsett om du tagit sömnmedel eller ej. Om du sover mer än vanligt, sätt din markering vid 0.",
	"Här ber vi dig ta ställning till hur din aptit är, och tänka efter om den på något sätt skilt sig från vad som är normalt för dig. Om du skulle ha bättre aptit än normalt, markera då det på 0.",
	"Här ber vi dig ta ställning till din förmåga att hålla tankarna samlade och koncentrera dig på olika aktiviteter. Tänk igenom hur du fungerar vid olika sysslor som kräver olika grad av koncentrationsförmåga, t ex läsning av komplicerad text, lätt tidningstext och TV-tittande.",
	"Här ber vid dig försöka värdera din handlingskraft. Frågan gäller om du har lätt eller svårt för att komma igång med sådant du tycker du bör göra, och i vilken utsträckning du måste över vinna ett inre motstånd när du skall ta itu med något.",
	"Här ber vi dig ta ställning till hur du upplever ditt intresse för omvärlden och för andra människor, och för sådana aktiviteter som brukar bereda dig nöje och glädje.",
	"Frågan gäller hur du ser på din egen framtid och hur du uppfattar ditt eget värde. Tänk efter i vilken utsträckning du ger dig självförebråelser, om du plågas av skuldkänslor, och om du oroat dig oftare än vanligt för t ex din ekonomi eller din hälsa.",
	"Frågan gäller din livslust, och om du känt livsleda. Har du tankar på självmord, och i så fall, i vilken utsträckning upplever du detta som en verklig utväg?"
	)
	bttns=(0,0,0,0,0,0,0,0,0)

	def __init__ (self,**kwargs):
		super (MainScreen, self).__init__(**kwargs)
		self.planupdate()
		
	def planupdate(self):
		#for the buttons:
		try:
			self.ids.checkboxes.clear_widgets()
			self.ids.qbox.clear_widgets()
			self.ids.container.clear_widgets()
		except:
			pass
		bigbox=BoxLayout(
			orientation='vertical'
			)
		for i in range(0,6):
			smallbox=BoxLayout(orientation='horizontal')
			chckbx=CheckBox(
				padding=( '100pt', '100pt')
				
				)		
			#???
			smallbox.add_widget(chckbx)
			smallbox.add_widget(Label(text='???'))
			bigbox.add_widget(smallbox)
		self.ids.container.add_widget(bigbox)
		for i in range(0,9):
			newq=Label(size_hint_y=None, size_hint_x=1)
			newq.bind(width=lambda s, w:
				   s.setter('text_size')(s, (self.width, None)))
			newq.bind(height=newq.setter('texture_size[1]'))
			newq.bind(height=newq.setter('self.minimum_height'))			
			newbox=Button(id="box%s"%str(i))
			txt=''
			if self.bttns[i]==1:
				txt="Ø"
			elif self.bttns[i]==0:
				txt="O"
			newbox.text=txt
			if i==self.nownr:
				newbox.background_color= (1.0, 0.0, 0.0, 1.0)
				newq.text=str(self.qlist[i])
				self.ids.qbox.add_widget(newq)
			newbox.bind(on_release=partial(self.chng_bttn, i))
			self.ids.checkboxes.add_widget(newbox)
		#	exec('Gvar%s.loop=True'%(str(i)))
		#	exec('Cvar%s.loop=True'%(str(i)))
		#	exec('Dvar%s.loop=True'%(str(i)))
		pass
	def chng_bttn(self,number, *args):
		self.nownr=number
		self.planupdate()
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
			email.send(recipient=StringProperty(str(settingdata.get('email')['address'])),
				subject=StringProperty('MADRS-S'),
				text=StringProperty('%s'%themessage)
				#,create_chooser=BooleanProperty()
				)
			box.add_widget(Label(text='Email sent to:%s'%settingdata.get('email')['address']))
		except:
			box.add_widget(Label(text='Couldn\'t send e-mail'))
		
		popup2 = Popup(title='Settings', content=box, size_hint=(None, None), size=(400, 400))
		store_btn = Button(text='OK')
		store_btn.bind(on_press = lambda *args: popup2.dismiss())
		box.add_widget(store_btn)
		popup2.open()



class emadrsApp(App):
	def build(self):
		the_screenmanager = ScreenManager()
		#the_screenmanager.transition = FadeTransition()
		mainscreen = MainScreen(name='mainscreen')
		the_screenmanager.add_widget(mainscreen)
		return the_screenmanager
		
if __name__ == '__main__':
	emadrsApp().run()
