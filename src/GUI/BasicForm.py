import pyforms
from   pyforms.basewidget import BaseWidget
from   pyforms.controls import ControlText
from   pyforms.controls import ControlButton

class Example(BaseWidget):
    def __init__(self):
        super(Example,self).__init__("Test");
        self._firstname = ControlText("Enter Firstname");
        self._button = ControlButton("PressMe");
        self._button.icon = 'GUI/number-25.jpg'
        self._button.value = self.__ButtonAction;
    def __ButtonAction(self):
        print(self._firstname.value);
pyforms.start_app(Example);