from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen


class UI(ScreenManager): # หน้าจอต่างๆ เชื่อมโยงไปที่ .kv
    pass
class Scr_knowledge(Screen):    # UI1
    pass
class Scr_bmi(Screen): 
    def cal_bmi(self):
    #ค่า bmi = น้ำหนัก กก/(ส่วนสูง เมตร X ส่วนสูง เมตร)
        weight = float(self.ids.txt_weight.text)
        height = float(self.ids.txt_height.text)
        height = height/100

        bmi = weight/(height*height)    #สูตรคำนวน bmiS
        self.ids.lbl_bmi.text=str(bmi)
        if bmi > 35:
            self.ids.lbl_bmi.color="#FF0000"    #แดง
            self.ids.img_bmi.source="pic/5.PNG"
        elif bmi >30:
            self.ids.lbl_bmi.color="#FF6633"    #ส้ม
            self.ids.img_bmi.source="pic/4.PNG"
        elif bmi >25:
            self.ids.lbl_bmi.color="#FFFF33"    #เหลือง
            self.ids.img_bmi.source="pic/3.PNG"
        elif bmi >18:
            self.ids.lbl_bmi.color="#99FF00"    #เขียว
            self.ids.img_bmi.source="pic/2.PNG"
        else:
            self.ids.lbl_bmi.color="#99FFFF"    #ฟ้า
            self.ids.img_bmi.source="pic/1.PNG"
class bmiApp(App):
    def build(self):
        return UI()

if __name__=='__main__':
    bmiApp().run()