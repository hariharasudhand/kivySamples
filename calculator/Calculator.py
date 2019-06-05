import kivy

from kivy.app import App
from kivy.uix.widget import Widget


class CalWindow(Widget):
    btnclickArray = [0]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def buttonAction(self,value1):

        if value1 == 'C':
            self.displayText.text = ''
        elif value1 == '=':
            ans = str(eval(self.displayText.text))

            self.displayText.text = ans
        elif self.displayText.text == '0':
            self.displayText.text = ''
        elif value1 == 'B':
            print('button clicked : ', value1)
            str1 = self.displayText.text
            str1 = str1[1:]
            self.displayText.text = str1
        else:
            self.displayText.text = self.displayText.text + value1





class CalculatorApp(App):
    def build(self):
        cal_window = CalWindow()
        return cal_window



if __name__ == '__main__':
    calWindow = CalculatorApp()
    calWindow.run()
