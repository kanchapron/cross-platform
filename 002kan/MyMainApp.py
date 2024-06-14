from kivy.app import App

from kivy.uix.screenmanager import ScreenManager, Screen



class Scr_1(Screen):    # UI1
    pass
class Scr_2(Screen):    # UI1
    def add_item(self):
        txt_card1 = self.ids.txt_card1.text
        txt_phone = self.ids.txt_phone.text
        if len(txt_card1) !=13 or len(txt_phone) !=10:
            self.ids.btn_re.text='ไม่พร้อมบันทึกข้อมูล'
        else:
            self.ids.btn_re.text='พร้อมบันทึกข้อมูล'

class UI(ScreenManager): # จัดการหน้าจอต่างๆ
    pass
    
class MyMainApp(App):
    def build(self):
        return UI()

if __name__ == "__main__":
    MyMainApp().run()
