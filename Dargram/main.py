from kivy.app import App  
from kivy.uix.label import Label  
from kivy.uix.button import Button  
from kivy.uix.textinput import TextInput  
from kivy.uix.screenmanager import ScreenManager,Screen  
from kivy.uix.floatlayout import FloatLayout 
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.image import Image


anim_1 = Animation(pos_hint ={'y':0.55, "x":0.2}, duration = 0.5) + Animation(pos_hint ={'y':0.45, "x":0.2}, duration = 0.5)
anim_1.repeat = True

anim_2 = Animation(pos_hint ={'y':0.55, "x":0.7}, duration = 0.5) + Animation(pos_hint ={'y':0.45, "x":0.7}, duration = 0.5)
anim_2.repeat = True

anim_3 = Animation(pos_hint ={'y':0.25, "x":0.7}, duration = 0.5) + Animation(pos_hint ={'y':0.35, "x":0.7}, duration = 0.5)
anim_3.repeat = True

anim_4 = Animation(pos_hint ={'y':0.25, "x":0.2}, duration = 0.5) + Animation(pos_hint ={'y':0.35, "x":0.2}, duration = 0.5)
anim_4.repeat = True


img_of_chuka = Image(source = 'image.jpeg', size_hint = (0.2, 0.2), pos_hint = {'y': 0.75, "x":0.05})
img_of_bilka = Image(source = 'bilka.jpg', size_hint = (0.15, 0.15), pos_hint = {'y': 0.8, "x":0.005})
img_of_clock = Image(source = 'clock.jpg', size_hint = (0.15, 0.15), pos_hint = {'y': 0.8, "x":0.1})
img_of_apples = Image(source = 'apples.jpg', size_hint = (0.15, 0.15), pos_hint = {'y': 0.7, "x":0.05})
img_of_logic = Image(source = 'logika.jpg', size_hint = (0.7, 0.5), pos_hint = {'y': 0.5, "x":0.15})
img_of_letsgo = Image(source = 'letsgo.jpg', size_hint = (0.3, 0.3), pos_hint = {'y': 0.6, "x":0.05})

class Zero(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()
        lab_logika = Label(text = "Задачі на Logik'у", size_hint = (0.2, 0.15), pos_hint ={'y':0.75, "x":0.4})
        but_for_sec_win = Button(text = "Початок", size_hint = (0.2, 0.15), pos_hint ={'y':0.17, "x":0.4}, background_color = (0.7, 0.3, 1.1))

        line.add_widget(lab_logika)
        line.add_widget(but_for_sec_win)
        self.add_widget(line)
        line.add_widget(img_of_letsgo)

        but_for_sec_win.on_press = self.next
    def next(self):
        self.manager.transition.direction = "up"
        self.manager.current = "one"

class One(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()

        lab_q1 = Label(text = "Годинник показує чверть на 9.\n Який час буде показувати годинник через п'яту частину години?", size_hint = (0.2, 0.15), pos_hint ={'y':0.75, "x":0.4})
        q1_correct = Button(text = '8:27', size_hint = (0.2, 0.05), pos_hint = {'y': 0.45, "x": 0.2 }, background_color = (0.7, 0.3, 1.1))
        q1_uncorrect_1 = Button(text = '8.30', size_hint = (0.2, 0.05), pos_hint = {'y': 0.45, "x": 0.7 }, background_color = (0.7, 0.3, 1.1)) 
        q1_uncorrect_2 = Button(text = '8:37', size_hint = (0.2, 0.05), pos_hint = {'y': 0.35, "x": 0.2 }, background_color = (0.7, 0.3, 1.1))
        q1_uncorrect_3 = Button(text = '8.40', size_hint = (0.2, 0.05), pos_hint = {'y': 0.35, "x": 0.7 }, background_color = (0.7, 0.3, 1.1))


        anim_1.start(q1_correct)
        anim_2.start(q1_uncorrect_1)
        anim_3.start(q1_uncorrect_2)
        anim_4.start(q1_uncorrect_3)

        line.add_widget(lab_q1)
        line.add_widget(q1_correct)
        line.add_widget(q1_uncorrect_1)
        line.add_widget(q1_uncorrect_2)
        line.add_widget(q1_uncorrect_3)
        self.add_widget(line)
        line.add_widget(img_of_clock)

        q1_correct.on_press = self.next
    def next(self):
        self.manager.transition.direction = "down"
        self.manager.current = "two"

class Two(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()

        lab_q2 = Label(text = 'Щука важить 1кг та ще половину своєї маси.\nЯка загальна маса щуки?', size_hint = (0.2, 0.15), pos_hint ={'y':0.75, "x":0.4})
        q2_uncorrect_2 = Button(text = '1', size_hint = (0.2, 0.05), pos_hint = {'y': 0.45, "x": 0.2}, background_color = (0.5, 0.3, 1.1))
        q2_uncorrect_1 = Button(text = '1.75', size_hint = (0.2, 0.05), pos_hint = {'y': 0.45, "x": 0.7}, background_color = (0.5, 0.3, 1.1)) 
        q2_correct = Button(text = '2', size_hint = (0.2, 0.05), pos_hint = {'y': 0.35, "x": 0.2 }, background_color = (0.5, 0.3, 1.1))
        q2_uncorrect_3 = Button(text = '1.5', size_hint = (0.2, 0.05), pos_hint = {'y': 0.35, "x": 0.7}, background_color = (0.5, 0.3, 1.1))

        anim_1.start(q2_uncorrect_2)
        anim_2.start(q2_uncorrect_1)
        anim_3.start(q2_correct)
        anim_4.start(q2_uncorrect_3)

        line.add_widget(lab_q2)
        line.add_widget(q2_correct)
        line.add_widget(q2_uncorrect_1)
        line.add_widget(q2_uncorrect_2)
        line.add_widget(q2_uncorrect_3)
        self.add_widget(line)
        line.add_widget(img_of_chuka)

        q2_correct.on_press = self.next
    def next(self):
        self.manager.transition.direction = "right"
        self.manager.current = "three"

class Three(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()

        lab_q3 = Label(text = 'На дереві сиділи 2 білки, одна з них вирішила стрибнути по горішок.\n Скільки білок залишилось на дереві?', size_hint = (0.2, 0.15), pos_hint ={'y':0.75, "x":0.4})
        q3_uncorrect_2 = Button(text = '0', size_hint = (0.2, 0.05), pos_hint = {'y': 0.45, "x": 0.2}, background_color = (0.3, 0.7, 1.1))
        q3_uncorrect_1 = Button(text = '1', size_hint = (0.2, 0.05), pos_hint = {'y': 0.45, "x": 0.7}, background_color = (0.3, 0.7, 1.1)) 
        q3_correct = Button(text = '2', size_hint = (0.2, 0.05), pos_hint = {'y': 0.35, "x": 0.2 }, background_color = (0.3, 0.7, 1.1))
        q3_uncorrect_3 = Button(text = '3', size_hint = (0.2, 0.05), pos_hint = {'y': 0.35, "x": 0.7}, background_color = (0.3, 0.7, 1.1))

        anim_1.start(q3_uncorrect_2)
        anim_2.start(q3_uncorrect_1)
        anim_3.start(q3_correct)
        anim_4.start(q3_uncorrect_3)

        line.add_widget(lab_q3)
        line.add_widget(q3_uncorrect_2)
        line.add_widget(q3_uncorrect_1)
        line.add_widget(q3_correct)
        line.add_widget(q3_uncorrect_3)
        self.add_widget(line)
        line.add_widget(img_of_bilka)

        q3_correct.on_press = self.next
    def next(self):
        self.manager.transition.direction = "left"
        self.manager.current = "four"

class Four(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        line = FloatLayout()

        lab_q4 = Label(text = 'Петро вирішив купити яблуко, але йому не вистачає 3 грн, Оленка теж хоче купити яблуко, але їй не вистачає 1 грн.\n Тоді Петро та Оленка вирішили купити одне яблуко на двох, але їм все одно не вистачає 1 грн. \n Скільки коштує яблуко?', size_hint = (0.2, 0.15), pos_hint ={'y':0.75, "x":0.4})
        q4_uncorrect_2 = Button(text = '1', size_hint = (0.2, 0.05), pos_hint = {'y': 0.45, "x": 0.2}, background_color = (0.3, 0.7, 1.6))
        q4_uncorrect_1 = Button(text = '4', size_hint = (0.2, 0.05), pos_hint = {'y': 0.45, "x": 0.7}, background_color = (0.3, 0.7, 1.6)) 
        q4_correct = Button(text = '3', size_hint = (0.2, 0.05), pos_hint = {'y': 0.35, "x": 0.2 }, background_color = (0.3, 0.7, 1.6))
        q4_uncorrect_3 = Button(text = '5', size_hint = (0.2, 0.05), pos_hint = {'y': 0.35, "x": 0.7}, background_color = (0.3, 0.7, 1.6))

        anim_1.start(q4_uncorrect_2)
        anim_2.start(q4_uncorrect_1)
        anim_3.start(q4_correct)
        anim_4.start(q4_uncorrect_3)

        line.add_widget(lab_q4)
        line.add_widget(q4_uncorrect_2)
        line.add_widget(q4_uncorrect_1)
        line.add_widget(q4_correct)
        line.add_widget(q4_uncorrect_3)
        self.add_widget(line)
        line.add_widget(img_of_apples)

        q4_correct.on_press = self.next
    def next(self):
        self.manager.transition.direction = "right"
        self.manager.current = "last"

class Last(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        lab_q5 = Label(text = 'Дякую за проходження тесту.Якщо ви дійшли до цього вікна, то у вас хороша логіка :)\n Бажаєте пройти ще раз?', size_hint = (0.2, 0.15), pos_hint ={'y':0.40, "x":0.4})
        line = FloatLayout()
        but_for_start = Button(text = "Початок", size_hint = (0.2, 0.15), pos_hint ={'y':0.10, "x":0.4}, background_color = (0.3, 0.7, 0.5))
        self.add_widget(but_for_start)
        self.add_widget(lab_q5)
        self.add_widget(line)
        line.add_widget(img_of_logic)

        but_for_start.on_press = self.next
    def next(self):
        self.manager.transition.direction = "left"
        self.manager.current = "one"


class MyApp(App):
    def build(self):
        screen_width, screen_height = Window.size
        Window.size = (screen_width, screen_height)
        main_screen = ScreenManager()
        main_screen.add_widget(Zero(name = 'zero'))
        main_screen.add_widget(One(name = 'one'))
        main_screen.add_widget(Two(name = 'two'))
        main_screen.add_widget(Three(name = 'three'))
        main_screen.add_widget(Four(name = 'four'))
        main_screen.add_widget(Last(name = 'last'))
        return main_screen

app = MyApp()
app.run()