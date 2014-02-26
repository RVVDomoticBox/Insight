from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

from kivy.config import Config
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')

class Connexion(Screen):
	def do_login(self, host, port):
		print("host : %s || port : %s" % (host, port) )
		self.manager.current = self.manager.next()

	def resetForm(self):
		self.ids['host'].text = ""
		self.ids['port'].text = ""

class Connected(Screen):
	def disconnect(self):
		self.manager.transition = SlideTransition(direction="right")
		self.manager.current = 'connexion'
		self.manager.get_screen('connexion').resetForm()

class ConnectedApp(App):
	def build(self):
		screen = Connected()
		screen.name = 'connected'
		return screen

class InsightApp(App):
	def build(self):
		manager = ScreenManager()

		# ajout de l'instance de login
		manager.add_widget(Connexion(name='connexion'))

		# ajout de la vue 'connected'
		app = ConnectedApp()
		app.load_kv()
		connectedView = app.build()
		manager.add_widget(connectedView)

		manager.transition = SlideTransition(direction="left")
		return manager


if __name__ == '__main__':
    InsightApp().run()