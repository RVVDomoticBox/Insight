from kivy.app import App
from kivy.uix.widget import Widget


class mainWindow(Widget):
    pass


class InsightApp(App):
    def build(self):
        return mainWindow()


if __name__ == '__main__':
    InsightApp().run()