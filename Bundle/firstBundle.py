from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager

Window.fullscreen = False
Window.size = (460, 660)

KV = """
MDScreen :
    id: mine
    md_bg_color: [224/255,224/255,224/255,1]
    name: 'Bundle'
    on_enter:
        app.anim(back)
        app.anim1(back1)
        app.i(lab)        
        app.swipe(iconn)
        app.text(label)
        
        
    MDFloatLayout:
        id: back
        size_hint_y: 0.6
        pos_hint: {"center_y": 1.8}
        radius: [0, 0, 0, 90]
        canvas:
            Color:
                rgb:  (255, 99, 71)
            Rectangle:
                size: self.size
                pos: self.pos
    MDFloatLayout:
        id: back1
        size_hint_y: 0.6
        pos_hint: {"center_y": 1.8}
        radius: [0, 0, 0, 40]
        canvas:
            Color:
                rgb:  (255, 99, 71)
            Ellipse:
                size: self.size
                pos: self.pos
    MDIconButton:
        id: iconn
        icon: 'bold.png'
        pos_hint: {"center_x": 0.3, "center_y": 0.8529}
        user_font_size: '60sp'
        theme_text_color: 'Custom'
        text_color: 1, 0, 1, 0
        opacity:0
    
    MDLabel:
        id: label
        text:f"[font=Arial]U N D L E[/font]"
        markup: True
        pos_hint: {"center_y": 0.85, "center_x": 0.77}
        halign: "center"
        theme_text_color:"Custom"
        text_color :0, 0, 0
        font_style: "H4"
        opacity: 0
  
    MDTextField:
        id: email
        icon_right: "email"
        hint_text: 'username'
        helper_text: "e.g: adam@domain or username"
        helper_text_mode: "on_focus"
        pos_hint: {"center_x": 0.5, "center_y": 0.46}
        current_hint_text_color: 0, 0, 0, 1
        color_module:  'Custom'
        size_hint_x: 0.8
    MDTextField:
        id: password
        icon_right: 'lock'
        hint_text: 'password'
        pos_hint: {"center_x": 0.5, "center_y": 0.34}
        current_hint_text_color: 0, 0, 0, 1
        size_hint_x: 0.8
        password: True
    MDLabel:
        id: lab
        text:"Double  Click"
        pos_hint: {"center_x": 0.5, "center_y": 0.07}
        halign: "center"
        theme_text_color:"Custom"
        text_color :0, 0, 0, 1
        font_style: "H5"
        opacity: 0
    MDIconButton:
        id : go
        icon: 'q.png'
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        user_font_size: '60sp'
        
     

        on_press: app.vi(go)
    MDIconButton:
        id : hea
        icon: 'h.png'
        pos_hint: {"center_x": 0.7, "center_y": 0.005}
        user_font_size: '30sp'
        opacity : 0
    MDIconButton:
        id : hear
        icon: 'h.png'
        pos_hint: {"center_x": 0.5, "center_y": 0.005}
        user_font_size: '30sp'
        opacity : 0
    MDIconButton:
        id : heart
        icon: 'h.png'
        pos_hint: {"center_x": 0.3, "center_y": 0.005}
        user_font_size: '30sp'
        opacity : 0
    
    MDIconButton:
        id: vin        
        icon: 'q.png'
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        user_font_size: '60sp'
        on_press: app.icons(heart)
        on_press: app.icons(hear)
        on_press: app.icons(hea)
        
        on_press: app.save(root.ids.email.text)  
        on_press: app.sav(root.ids.password.text)
        on_press : app.vi(vin)
        
    
            
              
        

"""







from kivy.lang import Builder

from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.config import Config
l=[]
j=[]
class Bundle(MDApp):
    def changescreen(self, name):
        screen_manager =  name

    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_string(KV))
        return screen_manager

    def anim(self, widget):
        anim = Animation(pos_hint={"center_y": 1.16})
        anim.start(widget)

    def close(self):
        Window.close()

    def anim1(self, widget):
        anim = Animation(pos_hint={"center_y": 0.85})
        anim.start(widget)



    def icons(self, widget):
        anim = Animation(pos_hint={"center_y": 0.005}, duration= 0.2, opacity= 0)
        anim += Animation(pos_hint={"center_y": 2}, duration=4, opacity = 1)
        anim.start(widget)
    def i(self, widget):
        k = Animation(opacity=1, duration=1.5)
        k += Animation(opacity=0, duration=1.5)
        k.start(widget)

    def text(self, widget):
        k = Animation(opacity=0, duration=1.5)
        k += Animation(opacity=1, duration=1.5)
        k.start(widget)
    def swipe(self, widget):
        k = Animation(opacity=0,pos_hint={"center_x": 0.3}, duration=1)
        k += Animation(opacity=1, duration=1.5, pos_hint={"center_x": 0.5})
        k.start(widget)
    def texl(self, widget):
        anim = Animation(pos_hint={"center_y": 2},opacity=1 )
        anim += Animation(pos_hint={"center_y": 0.7},opacity=1, duration=.5)
        anim.start(widget)
    def texo(self, widget):
        anim = Animation(pos_hint={"center_y": 2})
        anim += Animation(pos_hint={"center_y": 0.7}, duration=1, opacity = 1)
        anim.start(widget)
    def texg(self, widget):
        anim = Animation(pos_hint={"center_y": 2})
        anim += Animation(pos_hint={"center_y": 0.7}, duration=1.5, opacity = 1)
        anim.start(widget)
    def texi(self, widget):
        anim = Animation(pos_hint={"center_y": 2})
        anim += Animation(pos_hint={"center_y": 0.7}, duration=2, opacity = 1)
        anim.start(widget)
    def texn(self, widget):
        anim = Animation(pos_hint={"center_y": 2})
        anim += Animation(pos_hint={"center_y": 0.7}, duration=2.5, opacity = 1)
        anim.start(widget)
    def vi(self, widget):
        anim = Animation(opacity=1, disabled = True)
        anim += Animation(opacity=0)
        anim.start(widget)



    def sav(self, password):
        j.append(password)
    def save(self, mail):
        l.append(mail)
    def next(self):
        self.root.ids.next.load_next(mode='next')


                
if __name__ == '__main__':
    app = Bundle()
    app.run()
