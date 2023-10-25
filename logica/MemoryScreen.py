from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.properties import StringProperty, NumericProperty
import string
import random


# creo la clase para la principal que al entrar en la pantalla genera un string aleatorio
class MemoryScreen(Screen):
    # sin esta propiedad jamas se vera en la interfaz grafica
    random_string_label = StringProperty()
    timer_label = StringProperty()  # idem
    time_left = NumericProperty()  # idem
    timer_event = None
    random_string = StringProperty("")
 #para hacer comparaciones y mostrar en pantalla
    def __init__(self, **kwargs):
        super(MemoryScreen, self).__init__(**kwargs)
        # Puedes inicializar random_string en el constructor de la clase si es necesario
        self.random_string = ""
    
    def on_enter(self):
        self.time_left = 6  # estableciendo el temporizador
        self.timer_event = Clock.schedule_interval(
            self.update_timer, 1)  # actualizar el tiempo restante
        self.random_string = ""  # refresca el ransom string
        self.manager.get_screen('memoriza')
        random_string_label = self.ids.random_string_label #declado el ids para poder imprimir

        print(random_string_label.text)
# creando la funcion para generar caracteres  aleatorios en base a la dificultad establecida por el desplegable

    def generar_cadena_alfanumerica(self):
        # length = # Falta corregir la variable para que el programa no se detenga si el usuario no selecciono una dificultad
        if self.selected_difficulty == "Facil":
            length = 4
            random_string = ''.join(random.choices(
                string.ascii_letters + string.digits, k=length))
            self.ids.random_string_label.text = random_string
            # print(f"Random String: {random_string}")
        elif self.selected_difficulty == "Medio":
            length = 6
            random_string = ''.join(random.choices(
                string.ascii_letters + string.digits, k=length))
            self.ids.random_string_label.text = random_string
            # print(f"Random String: {random_string}")
        elif self.selected_difficulty == "Dificil":
            length = 8
            random_string = ''.join(random.choices(
                string.ascii_letters + string.digits, k=length))
            self.ids.random_string_label.text = random_string
            print(f"Random String: {random_string}")
##################################################################################

    def update_timer(self, dt):
        self.time_left -= 1
        self.timer_label = str(self.time_left)
        if self.time_left <= 0:
            self.timer_label = "Terminó el tiempo"
            self.timer_event.cancel() #permanecer en la siguiente pantalla
            self.manager.current = 'responde'
        else:
            self.timer_label = f"Tiempo restante: {self.time_left} segundos"
        # Avanza a la pantalla de pregunta cuando se agote el tiempo de xx segundos