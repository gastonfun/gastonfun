from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty

class QuestionScreen(Screen):
    user_text = StringProperty("")
    random_string = StringProperty("")

    def __init__(self, **kwargs):
        super(QuestionScreen, self).__init__(**kwargs)
        # Puedes inicializar user_text en el constructor de la clase si es necesario
        self.user_text = ""
        self.random_string = ""
    # Creo la funcion que obtiene el texto ingresado por el usuario y lo almacena en la variable user_Text    
    def guardar_texto(self):
        # Obtenemos el texto ingresado por el usuario desde el TextInput
        self.user_text = self.ids.user_input.text
        self.random_string = ""
        print(self.user_text)
        print(self.random_string)
        self.manager.get_screen('resultado').comparar_strings(self.user_text) # llamo a la pantalla para que se realice la operacion
        self.manager.current = 'resultado'
    
    def on_pre_enter(self):
        # Restablece el contenido del TextInput a una cadena vacía
        self.ids.user_input.text = ''
        