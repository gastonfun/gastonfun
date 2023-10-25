from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty


class ResultScreen(Screen):
    result = StringProperty("")
    random_string = StringProperty("")

    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        # Puedes inicializar rsult en el constructor de la clase si es necesario
        self.result = ""

    def on_enter(self):
        # Obtienee el valor de random_string de la pantalla anterior
        self.random_string = self.manager.get_screen('memoriza').random_string
        self.user_text = self.manager.get_screen('responde').user_text
        self.actualizar_resultado()

    def comparar_strings(self, user_text):
        memoriza = self.manager.get_screen('memoriza')
        #responde = self.manager.get_screen('responde')
        print(f"memoriza.random_string: {memoriza.random_string}") # ESTE ME Lo iMPriME VACIO POR ENDE NO HACE LA COMPARACION
        print(f"user_text: {user_text}")

        self.result = "Los strings coinciden!!!" if memoriza.random_string == user_text else "Los Strings NO coinciden!"
        self.actualizar_resultado()

    # Actualiza el texto de la etiqueta result_label en la interfaz
    def actualizar_resultado(self):
        self.ids.result_label.text = self.result
