from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen


class StartScreen(Screen):
     #funcion para almacenar el nivel de dificultad del selector
    def on_difficulty_selected(self, difficulty):
        self.memory_screen = self.manager.get_screen('memoriza')
        self.memory_screen.selected_difficulty = difficulty
        print(f"Dificultad seleccionada: {difficulty}")
        #self.manager.current = 'memoriza'