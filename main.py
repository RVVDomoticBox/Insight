# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

from kivy.uix.label import Label
from kivy.animation import Animation


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

class MainMenu(Screen):
	def disconnect(self):
		self.manager.transition = SlideTransition(direction="right")
		self.manager.current = 'connexion'
		self.manager.get_screen('connexion').resetForm()

	def go_to(self, list):
		self.manager.transition = SlideTransition(direction="left")
		self.manager.current = 'lists'
		self.manager.get_screen('lists').load(list)

class SubView(Screen):
	def back_to_main_menu(self):
		self.manager.transition = SlideTransition(direction="right")
		self.manager.current = 'menu'


class ListScreen(SubView):
	def load(self, list):
		# Récupérer la liste correspondante à l'adresse host:port/list
		pass

class ShowScreen(SubView):
	def load(self, object):
		# Récupérer les infos de l'objet à visualiser
		pass


class DraggableLabel(Label):
    '''A label you can drag upside-down'''
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            # assure ourselves we will get the updates of this motion
            touch.grab(self)
            return True

        return super(DraggableLabel, self).on_touch_down(touch)

    def on_touch_move(self, touch):
        if touch.grab_current is self:
            # really straightforward...
            self.y = touch.y
            return True

        return super(DraggableLabel, self).on_touch_move(touch)

    def on_touch_up(self, touch):
        if touch.grab_current is self:
            # check if the movement direction was up or down
            if touch.dy < 0:
                a = Animation(y=0) # down? put the bar all the way down
            else:
                a = Animation(top=self.parent.top) # up? put it at the top

            a.start(self) # actually start the animation
            return True

        return super(DraggableLabel, self).on_touch_up(touch)

    def restart(self):
    	Animation(top=self.parent.top).start(self)


class InsightApp(App):
	def build(self):
		manager = ScreenManager()

		# ajout de l'instance de connexion
		manager.add_widget(Connexion(name='connexion'))

		# ajout de la vue 'menu'
		manager.add_widget(MainMenu(name='menu'))

		# ajout de la vue 'lists'
		manager.add_widget(ListScreen(name='lists'))

		manager.transition = SlideTransition(direction="left")
		return manager


if __name__ == '__main__':
    InsightApp().run()