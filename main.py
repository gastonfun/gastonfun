from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.utils import platform #modulo para establecer una resolucion simulado de pantalla
from kivy.config import Config # modulo que permite configurar el tamaño de la ventana

#importamos las pantallas y sus respectivas clases
from logica.StartScreen import StartScreen
from logica.MemoryScreen import MemoryScreen
from logica.QuestionScreen import QuestionScreen
from logica.ResultScreen import ResultScreen
#cargamos las pantallas de interfaz
Builder.load_file('GUI/StartScreen.kv')
Builder.load_file('GUI/MemoryScreen.kv')
Builder.load_file('GUI/QuestionScreen.kv')
Builder.load_file('GUI/ResultScreen.kv')

#defino la clase principal que hereda de la clase App, la base principal de kivy   
class Memory_Game(App):
    #result = "" #v<riable global para llevar a cabo la pantalla de resultados PROXIMAMENTE
    def build(self):
        sm = ScreenManager() #creo la instancia para la clase Screenmanager para gestionar las pantallas
        #creo las pantallas 
        sm.add_widget(StartScreen(name='principal'))
        sm.add_widget(MemoryScreen(name='memoriza'))
        sm.add_widget(QuestionScreen(name='responde'))
        sm.add_widget(ResultScreen(name='resultado'))
        return sm   


if __name__ == '__main__':
    if platform == 'linux':
        Config.set('graphics', 'width', '720')
        Config.set('graphics', 'height', '1600')
    #NO ME ESTARIA FUNCIONANDO EL REDIMENSIONADO...
    Memory_Game().run()