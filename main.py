import webbrowser
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from pytube import YouTube

class ConverterApp(MDApp):

    def download(self,args):

        link = (self.input.text)
        video = YouTube(link)
        downloads = video.streams.filter(progressive="True", file_extension="mp4").get_by_itag(22).url
        webbrowser.open(downloads)


    def build(self):
        self.theme_cls.primary_palette="Red"
        screen = MDScreen()

        #UI Widgets go here
        self.toolbar = MDTopAppBar(title="Youtube Video Downloader")
        self.toolbar.pos_hint = {"top": 1 }
        screen.add_widget(self.toolbar)

        #logo
        screen.add_widget(Image(source="youtubedllogo.png", pos_hint = {"center_x": 0.1, "center_y":0.8}, size_hint=(0.1,0.1)))
        

        #user input
        self.input = MDTextField(text="",  halign="center", size_hint=(0.6,1),pos_hint={"center_x": 0.5, "center_y":0.72} , font_size=22)
        screen.add_widget(self.input)


        #Labels
        self.label = MDLabel(text="Paste the Youtube link Below",  halign="center", size_hint=(0.6,1),pos_hint={"center_x": 0.5, "center_y":0.8}, font_size=22)
        screen.add_widget(self.label)

        self.label = MDLabel(text="Please wait for some time after clicking download",  halign="center", size_hint=(0.6,1),pos_hint={"center_x": 0.5, "center_y":0.1}, font_size=22)
        screen.add_widget(self.label)

        #download
        screen.add_widget(MDFillRoundFlatButton(text="Download", halign="center", pos_hint={"center_x": 0.5, "center_y":0.60}, font_size=22, on_press=self.download))
    


        return screen




if __name__ == '__main__':
    ConverterApp().run()