import os
import cv2 as cv
import numpy as np
from kivy.app import App
from kivy.uix.label import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

class BaseGridLayout(BoxLayout):
    old_path = None
    def __init__(self, **kwargs):
        super(BaseGridLayout, self).__init__(**kwargs)
        Window.bind(on_dropfile = self._on_file_drop)

    def _on_file_drop(self, window, file_path):
        self.ids.image_file.source = file_path.decode("utf-8")     # convert byte to string
        # print(self.ids.image_file.source)
        global old_path
        old_path = self.ids.image_file.source

    def on_button_click(self,color):
        new_grayscaled_image_path = self.filter_colour(color)
        self.ids.image_file.source = new_grayscaled_image_path
        self.ids.image_file.reload()


    def filter_colour(self, color):
        hsv_dict = {'red': ([140,100,50],[180,255,255]), 'blue': ([80, 168, 166],[120,255,255]),
                'green':([30,10,50], [60,255,255])}

        lower = np.array(hsv_dict[color][0])
        upper = np.array(hsv_dict[color][1])

        path = old_path
        print(old_path)
        pathsplitlist = path.split('\\')
        path = '//'.join(pathsplitlist)
        img = cv.imread(path)
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        mask = cv.inRange(hsv, lower, upper)
        mask_inv = cv.bitwise_not(mask)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        res = cv.bitwise_and(img, img, mask=mask)
        background = cv.bitwise_and(gray, gray, mask = mask_inv)
        background = np.stack((background,)*3, axis=-1)
        added_img = cv.add(res, background)
        save_path = os.path.abspath(os.getcwd())+"\images\grayimg.jpg"
        cv.imwrite(save_path, added_img)
        return save_path

class MyApp(App):
    def build(self):
        return BaseGridLayout()

MyApp().run()