import smtplib
from email.mime.text import MIMEText
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import time
import os
from kivy.clock import Clock
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
from email.mime.multipart import MIMEMultipart
from kivy.core.window import Window
from kivy.app import App
from kivymd.app import MDApp
from email.mime.multipart import MIMEMultipart
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import time
from gtts import gTTS
from playsound import playsound
import os
from kivy.clock import Clock
# import numpy as np
# from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
# from keras.models import Sequential, load_model
# from PIL import Image
# import detector
from kivy.properties import StringProperty, NumericProperty
from gtts import gTTS
from playsound import playsound
from PIL import Image
from plyer import vibrator
from camera import CameraCv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

Window.size = (270 * 1.5, 480 * 1.5)

Builder.load_string('''
<LoadingPage>:
    FloatLayout:
        canvas:
            Color:
                rgb: 0, 0, 0
            Rectangle:
                size: self.size
        Label:
            text: 'EYE PICK'
            font_name : 'ym.ttf'
            color : [1, 1, 0,1]
            pos_hint: {"x": .3, "top": .85}
            size_hint: (.4, .1)
            font_style: "H5"
            font_size : 40
        Label:
            text: '같이 가는 미래를 위해'
            font_name : 'ym.ttf'
            color : [1, 1, 0,1]
            pos_hint: {"x": .3, "top": .75}
            size_hint: (.4, .1)
            font_style: "H5"
            font_size : 30
        Label:
            text: '로딩중...'
            font_name : 'ym.ttf'
            color : [1, 1, 0,1]
            pos_hint: {"x": .3, "top": .5}
            size_hint: (.4, .1)
            font_style: "H5"
            font_size : 25
        Label:
            text: 'made by SKKU-BMW'
            font_name : 'ym.ttf'
            color : [1, 1, 0,1]
            pos_hint: {"right": .7, "top": .1}
            size_hint: (.4, .1)
            font_style: "H5"
            font_size: 20

<MainPage>:
    FloatLayout:
        canvas:
            Color:
                rgb: 0, 0, 0
            Rectangle:
                size: self.size
            Color:
                rgb: 1, 1, 0
            Line:
                width: 2.
                rectangle: (self.width*0.025, (self.height*0.35),\
                 self.width*0.955, (self.height*0.4))

        MDRoundFlatButton:
            id: cs_button
            text: '자료 수집 함께하기'
            font_name : 'ym.ttf'
            pos_hint: {"x": 0, 'top': 1}
            font_size: 30
            size_hint: (1, .1)
            orientation: 'vertical'
        CameraCv:
            id: camera1
            pos_hint: {"x":.05, "top": .8}
            size_hint: (.9,.5)
            resolution: (1920, 1080)
            play: False

<CSPage>:
    FloatLayout:
        canvas:
            Color:
                rgb: 0, 0, 0
            Rectangle:
                size: self.size
            Color:
                rgb: 1, 1, 0
            Line:
                width: 1.
                rectangle: (self.width*0.375, (self.height*0.475),\
                self.width*0.45, (self.height*0.1))
            Color:
                rgb: 1, 1, 0
            Line:
                width: 1.
                rectangle: (self.width*0.375, (self.height*0.375),\
                 self.width*0.45, (self.height*0.1))
            Color:
                rgb: 1, 1, 0
            Line:
                width: 1.
                rectangle: (self.width*0.375, (self.height*0.275),\
                 self.width*0.45, (self.height*0.1))
            Color:
                rgb: 1, 1, 0
            Line:
                width: 1.
                rectangle: (self.width*0.375, self.height*0.175,\
                 self.width*0.45, (self.height*0.1))        
        CameraCv:
            id: camera2
            pos_hint: {"x":.3, "top": .88}
            size_hint: (.4,.4)
            resolution: (1920, 1080)        
        MDLabel:
            text: "제품명"
            pos_hint: {"x": .1, "top": .575}
            size_hint: (.4, .1)
            halign: "left"
            color : [1, 1, 0,1]
            font_style: "H5"
            font_name : 'ym.ttf'
            font_size: 28
        MDLabel:
            text: "제조회사"
            pos_hint: {"x": .1, "top": .475}
            size_hint: (.4, .1)
            halign: "left"
            color : [1, 1, 0,1]
            font_style: "H5"
            font_name : 'ym.ttf'
            font_size: 28
        MDLabel:
            text: "가격"
            pos_hint: {"x": .1, "top": .375}
            size_hint: (.4, .1)
            halign: "left"
            color : [1, 1, 0,1]
            font_style: "H5"
            font_name : 'ym.ttf'
            font_size: 28
        MDLabel:
            text: "기타"
            pos_hint: {"x": .1, "top": .275}
            size_hint: (.4, .1)
            halign: "left"
            color : [1, 1, 0,1]
            font_style: "H5"
            font_name : 'ym.ttf'
            font_size: 28
        MDLabel:
            pos_hint: {"x": 0, "top": .88}
            size_hint: (1, .1)
            halign: "center"
            font_style: "H5"
            text: "새로운 음료수 정보를 알려주세요!"
            font_name : 'ym.ttf'
            font_size: 37
            color : [1, 1, 0,1]
        MDTextField:
            id: name
            font_name : 'ym.ttf'
            pos_hint: {"x": .4, "top": .575}
            size_hint: (.4, .1)
            hint_text: "product name"
            color_mode: 'accent'
            line_color_focus: [1, 1, 0,1]
        MDTextField:
            id: company
            font_name : 'ym.ttf'
            pos_hint: {"x": .4, "top": .475}
            size_hint: (.4, .1)
            hint_text: "Company"
            color_mode: 'accent'
            line_color_focus: [1, 1, 0,1]
        MDTextField:
            id: price
            font_name : 'ym.ttf'
            pos_hint: {"x": .4, "top": .375}
            size_hint: (.4, .1)
            hint_text: "Price"
            color_mode: 'accent'
            line_color_focus: [1, 1, 0,1]
        MDTextField:
            id: etc
            font_name : 'ym.ttf'
            pos_hint: {"x": .4, "top": .275}
            size_hint: (.4, .1)
            hint_text: "ETC"
            color_mode: 'accent'
            line_color_focus: [1, 1, 0,1]
        MDLabel:
            id : guid
            pos_hint: {"x": .1, "top": .2}
            size_hint: (.8, .1)
            halign: "center"
            font_style: "H5"
            text: ""
            font_name : 'ym.ttf'
            font_size: 15
            color : [1, 1, 0,1]
        MDRoundFlatButton:
            pos_hint: {"x": .2, "top": .12}
            size_hint: (.6, .09)
            text: "보내기"
            font_name : 'ym.ttf'
            font_size: 25
            on_press: root.email()
            md_bg_color: [1, 1, 0,1]
            text_color: [0, 0, 0, 1]
        MDRaisedButton:
            pos_hint: {"x": 0, "top": 1}
            size_hint: (.2, .1)
            text: "뒤로"
            font_name : 'ym.ttf'
            font_size: 25
            on_press: root.back()
            md_bg_color: [1, 1, 0,1]
            text_color: [0, 0, 0, 1]

<ResultPage>:
    FloatLayout:
        canvas:
            Color:
                rgb: 0, 0, 0
            Rectangle:
                size: self.size
            Color:
                rgb: 1, 1, 0
            Line:
                width: 2.
                rectangle: (self.width*0.08, (self.height)*0.05, \
                self.width*0.85, (self.height)*0.45)
        Label:
            id : guid
            text: '검색한 음료수 정보'
            font_name : 'ym.ttf'
            color : [1, 1, 0,1]
            pos_hint: {"x": .3, "top": .95}
            size_hint: (.4, .1)
            font_style: "H5"
            font_size: 40
        Label:
            id : Name_
            text: '이름 : '
            font_name : 'ym.ttf'
            pos_hint: {"x": .3, "top": .5}
            color : [1, 1, 0,1]
            size_hint: (.4, .1)
            font_style: "H5"
            font_size: 40
        Label:
            id : Name
            text: ''
            font_name : 'ym.ttf'
            pos_hint: {"x": .3, "top": .45}
            color : [1, 1, 0,1]
            size_hint: (.4, .2)
            font_style: "H5"
            font_size: 50
        Label:
            id : Price_
            text: '가격 : '
            font_name : 'ym.ttf'
            pos_hint: {"x": .3, "top": .30}
            color : [1, 1, 0,1]
            size_hint: (.4, .1)
            font_style: "H5"
            font_size: 40
        Label:
            id : Price
            text: ''
            font_name : 'ym.ttf'
            pos_hint: {"x": .3, "top": .25}
            color : [1, 1, 0,1]
            size_hint: (.4, .2)
            font_style: "H5"
            font_size: 50
        Image:
            id : image
            source : ""
            size_hint : (.6,.6)
            pos_hint: {"x": .2, "top": .98}

<ResultPage_2>:
    FloatLayout:
        canvas:
            Color:
                rgb: 0, 0, 0
            Rectangle:
                size: self.size
            Color:
                rgb: 1, 1, 0
            Line:
                width: 2.
                rectangle: (self.width*0.08, (self.height)*0.05, self.width*0.85, (self.height)*0.75)
        Label:
            id : guid
            text: '검색한 음료수 정보'
            font_name : 'ym.ttf'
            color : [1, 1, 0,1]
            pos_hint: {"x": .3, "top": .95}
            size_hint: (.4, .1)
            font_style: "H5"
            font_size: 40

        Label:
            id : Company_
            text: '제조사 : '
            font_name : 'ym.ttf'
            pos_hint: {"x": .3, "top": .70}
            color : [1, 1, 0,1]
            size_hint: (.4, .1)
            font_style: "H5"
            font_size: 40
        Label:
            id : Company
            text: ''
            font_name : 'ym.ttf'
            pos_hint: {"x": .3, "top": .65}
            color : [1, 1, 0,1]
            size_hint: (.4, .2)
            font_style: "H5"
            font_size: 50
        Label:
            id : ETC_
            text: '기타 : '
            font_name : 'ym.ttf'
            pos_hint: {"x": .3, "top": .40}
            color : [1, 1, 0,1]
            size_hint: (.4, .1)
            font_style: "H5"
            font_size: 40
        Label:
            id : ETC
            text: ''
            font_name : 'ym.ttf'
            pos_hint: {"x": .3, "top": .35}
            color : [1, 1, 0,1]
            size_hint: (.4, .2)
            font_style: "H5"
            font_size: 50

<SelectPage>:
    FloatLayout:
        canvas:
            Color:
                rgb: 0, 0, 0
            Rectangle:
                size: self.size
        MDRoundFlatButton:
            text: '추가 정보'
            font_name : 'ym.ttf'
            font_size: 60
            size_hint: (1, .3)
            pos_hint: {"x": 0, 'top': .98}
            on_press: root.up_pressed()
        MDRoundFlatButton:
            text: '어플 닫기'
            font_name : 'ym.ttf'
            font_size: 60
            size_hint: (1, .3)
            pos_hint: {"x": 0, 'top': .65}
            on_press: root.middle_pressed()
        MDRoundFlatButton:
            text: '다시 검색'
            font_name : 'ym.ttf'
            font_size: 60
            size_hint: (1, .3)
            pos_hint: {"x": 0, 'top': .32}
            on_press: root.down_pressed()
''')

trial = 0
classi_result = None
MP = 0
pg2 = 0
pg3 = 0
pg3_2 = 0
pg4 = 0
image_source = None
image_source_ = None


class LoadingPage(BoxLayout):
    def __init__(self, **kwargs):
        super(LoadingPage, self).__init__(**kwargs)
        Clock.schedule_once(self.GotoMain, 3)

    def GotoMain(self, _):
        My_app.screen_manager.current = "MainPage"


class MainPage(BoxLayout):
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        Clock.schedule_interval(self.check_page, 2)

    def check_page(self, _):
        global MP
        if My_app.screen_manager.current == "MainPage":
            self.check_cam()
            if MP == 0:  # 입장시 한번만 하는 행동
                self.Guid_voice("음료수를 판단하려면 화면을 터치 해주세요")
                MP = 1

    def on_touch_up(self, touch):
        global MP
        if (touch.pos[1] > self.ids.cs_button.pos[1]) \
                and touch.pos[1] < self.ids.cs_button.pos[1] + \
                self.ids.cs_button.size[1] \
                and (touch.pos[0] > self.ids.cs_button.pos[0]) \
                and touch.pos[0] < \
                self.ids.cs_button.pos[0] + self.ids.cs_button.size[0]:
            My_app.screen_manager.current = "CSPage"
            MP = 0
        else:
            self.ids.camera1.play = not self.ids.camera1.play

    def check_cam(self):
        if self.ids.camera1.play:
            self.func1()

    def func1(self):
        global trial
        global classi_result
        global image_source
        global MP
        image_source = self.capture()
        classi_result = None
        print("Start classification...")
        classi_result = self.detection(image_source)
        # vibrator.vibrate(1)
        print("result:", classi_result)
        print(trial)
        if classi_result == None:
            trial += 1
            print("Can not find info")
            if trial > 10:
                self.Guid_voice("음료수를 잘 찾을 수 있게 좌우로 천천히 돌려주세요")
                time.sleep(1)
                trial = 0
        else:
            My_app.screen_manager.current = "ResultPage"
            self.ids.camera1.play = False
            MP = 0

    def capture(self):
        camera = self.ids['camera1']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        image_source = "IMG_" + timestr + ".png"
        print("Captured")
        return image_source

    def detection(self, Image):
        self.img2 = Image
        Drink_info = None
        # Define Path
        model_path = './models/model.h5'
        model_weights_path = './models/weights.h5'
        model = load_model(model_path)
        model.load_weights(model_weights_path)
        img_width, img_height = 150, 150
        x = load_img(Image, target_size=(img_width, img_height))
        x = img_to_array(x)
        x = np.expand_dims(x, axis=0)
        array = model.predict(x)
        result = array[0]
        # print(result)
        answer = np.argmax(result)
        if answer == 1:
            print("Predicted: 콜라")
            Drink_info = ['코카콜라', '코카콜라주식회사', '천오백', '없음']
        elif answer == 0:
            print("Predicted: 사이다")
            Drink_info = ['칠성사이다', '롯데', '천오백', '없음']
        elif answer == 2:
            print("Predicted: 포카리스웨트"),
            Drink_info = ['포카리스웨트', '동아오츠카', '천오백', '없음']
        else:
            print("인식안됨")
            Drink_info = ['ㄴㄴ', 'ㄴㄴ', 'ㄴㄴ']
        return Drink_info

    def Guid_voice(self, sent):
        print("guided sent :", sent)
        txtin = True
        if txtin:
            tts = gTTS(text=sent, lang='ko')
            tts.save("sample.mp3")
            playsound("sample.mp3")
            if os.path.isfile("sample.mp3"):
                os.remove("sample.mp3")
                txtin = False
        return 0


class CSPage(BoxLayout):
    def __init__(self, **kwargs):
        super(CSPage, self).__init__(**kwargs)
        Clock.schedule_interval(self.check_page, 2)

    def check_page(self, _):
        global pg2
        if My_app.screen_manager.current == "CSPage":
            if pg2 == 0:  # 입장시 한번만 하는 행동
                self.ids.camera2.play = True
                pg2 = 1

    def email(self):
        global image_source_
        name = self.ids["name"].text
        company = self.ids["company"].text
        price = self.ids["price"].text
        etc = self.ids["etc"].text
        image_source_ = self.capture()
        print("name =", name, "company =", company, "price =", price, "etc =", etc)

        # 지메일 아이디,앱 비밀번호 입력하기
        email_user = 'kanghyu09@gmail.com'  # <ID> 본인 계정 아이디 입력
        email_password = 'xstyxygvubahjzvk'  # <PASSWORD> 본인 계정 앱 비밀번호 입력
        email_send = '5ekdmsdldl@naver.com'  # <받는곳주소> 수신자 이메일 abc@abc.com 형태로 입력

        # 제목 입력
        subject = '클라우드 소싱 '

        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject

        # 본문 내용 입력
        # body = name + company + price + etc
        # msg.attach(MIMEText(body, 'plain'))

        body = '추가되어야 할 제품입니다. \n이름:%s, 제조사:%s, 가격:%s원, 기타:%s ' % (name, company, price, etc)
        msg.attach(MIMEText(body, 'plain'))

        # filename = '파워에이드.jpg'  # 파일 경로
        attachment = open(image_source_, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment", filename=image_source_)
        msg.attach(part)

        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_user, email_password)

        server.sendmail(email_user, email_send, text)
        server.quit()

        self.ids["guid"].text = "잘 받았습니다! 감사합니다"
        self.ids["name"].text = ""
        self.ids["company"].text = ""
        self.ids["price"].text = ""
        self.ids["etc"].text = ""

    def back(self):
        global pg2
        global image_source_
        My_app.screen_manager.current = "MainPage"
        self.ids.camera2.play = False
        if os.path.isfile(image_source_):
            os.remove(image_source_)
        pg2 = 0

    def capture(self):
        camera = self.ids['camera2']
        timestr = time.strftime("%Y%m%d_%H%M%S_")
        camera.export_to_png("IMG_{}.png".format(timestr))
        image_source = "IMG_" + timestr + ".png"
        print("Captured")
        return image_source


class ResultPage(BoxLayout):
    def __init__(self, **kwargs):
        super(ResultPage, self).__init__(**kwargs)
        Clock.schedule_interval(self.check_page, 2)

    def check_page(self, _):
        global pg3
        if My_app.screen_manager.current == "ResultPage":
            if pg3 == 0:
                pg3 = 1
                self.func3()

    def func3(self):
        global classi_result
        print("classification Done")
        self.ids.image.source = image_source
        self.ids.Name.text = classi_result[0]
        self.ids.Price.text = str(classi_result[2])
        Clock.schedule_once(self.Guid, 10)

    def Guid(self, _):
        global classi_result
        global image_source
        self.Guid_voice("이 음료수는  %s이고 가격은 %s원입니다    \
        다음 안내를 위해 화면을 터치해주세요" % (str(classi_result[0]), \
                                 str(classi_result[2])))
        if os.path.isfile(image_source):
            os.remove(image_source)

    def on_touch_up(self, touch):
        global pg3
        My_app.screen_manager.current = "SelectPage"
        pg3 = 0

    def Guid_voice(self, sent):
        print("guided sent :", sent)
        txtin = True
        if txtin:
            tts = gTTS(text=sent, lang='ko')
            tts.save("sample.mp3")
            playsound("sample.mp3")
            time.sleep(5)
            if os.path.isfile("sample.mp3"):
                os.remove("sample.mp3")
                txtin = False
        return 0


class ResultPage_2(BoxLayout):
    def __init__(self, **kwargs):
        super(ResultPage_2, self).__init__(**kwargs)
        Clock.schedule_interval(self.check_page, 1)

    def check_page(self, _):
        global pg3_2
        if My_app.screen_manager.current == "ResultPage_2":
            if pg3_2 == 0:
                pg3_2 = 1
                self.func3()

    def func3(self):
        global classi_result
        print("classification Done")
        self.ids.Company.text = classi_result[1]
        self.ids.ETC.text = str(classi_result[3])
        Clock.schedule_once(self.Guid, 1)

    def Guid(self, _):
        global classi_result
        self.Guid_voice("음료수를 만든 제조사는   %s이고 %s와 같은 특징이 있어요    \
        다음 안내를 위해 화면을 터치해주세요" % (str(classi_result[1]), \

                                str(classi_result[3])))

    def on_touch_up(self, touch):
        global pg3_2
        My_app.screen_manager.current = "SelectPage"
        pg3_2 = 0

    def Guid_voice(self, sent):
        print("guided sent :", sent)
        txtin = True
        if txtin:
            tts = gTTS(text=sent, lang='ko')
            tts.save("sample.mp3")
            playsound("sample.mp3")
            time.sleep(5)
            if os.path.isfile("sample.mp3"):
                os.remove("sample.mp3")
                txtin = False
        return 0


class SelectPage(BoxLayout):
    def __init__(self, **kwargs):
        super(SelectPage, self).__init__(**kwargs)
        Clock.schedule_interval(self.check_page, 2)

    def check_page(self, _):
        global pg4
        if My_app.screen_manager.current == "SelectPage":
            if pg4 == 0:
                pg4 = 1
                self.Guid_voice("더많은 정보는 상단, 다시 검색은 하단, \
                어플 닫기는 화면 중간을 눌러주세요")

    def up_pressed(self):
        My_app.screen_manager.current = "ResultPage_2"

    def middle_pressed(self):
        My_app.stop()

    def down_pressed(self):
        global pg4
        pg4 = 0
        My_app.screen_manager.current = "MainPage"

    def Guid_voice(self, sent):
        print("guided sent :", sent)
        txtin = True
        if txtin:
            tts = gTTS(text=sent, lang='ko')
            tts.save("sample.mp3")
            playsound("sample.mp3")
            time.sleep(5)
            if os.path.isfile("sample.mp3"):
                os.remove("sample.mp3")
                txtin = False
        return 0


class EpicApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.screen_manager = ScreenManager()

        self.loading_page = LoadingPage()
        screen = Screen(name="LoadingPage")
        screen.add_widget(self.loading_page)
        self.screen_manager.add_widget(screen)

        self.cam_page = MainPage()
        screen = Screen(name="MainPage")
        screen.add_widget(self.cam_page)
        self.screen_manager.add_widget(screen)

        self.sub_page2 = CSPage()
        screen = Screen(name="CSPage")
        screen.add_widget(self.sub_page2)
        self.screen_manager.add_widget(screen)

        self.sub_page3 = ResultPage()
        screen = Screen(name="ResultPage")
        screen.add_widget(self.sub_page3)
        self.screen_manager.add_widget(screen)

        self.sub_page3_2 = ResultPage_2()
        screen = Screen(name="ResultPage_2")
        screen.add_widget(self.sub_page3_2)
        self.screen_manager.add_widget(screen)

        self.sub_page4 = SelectPage()
        screen = Screen(name="SelectPage")
        screen.add_widget(self.sub_page4)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == '__main__':
    My_app = EpicApp()
    My_app.run()