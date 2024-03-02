from PyQt5 import QtWidgets
from MainWindow import Ui_MainWindow
from Classes.ClassUtility import *

from Classes.MySpinBox import MySpinBox
from Classes.MyDoubleSpinBox import MyDoubleSpinBox
import subprocess


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    FIRST_NUMBER = None

    DICT = {}

    PERCENTAGE = 0

    BLACK_TEXT_A4_ONE_PRICE = 2800
    BLACK_TEXT_A5_ONE_PRICE = 2000
    BLACK_TEXT_A3_ONE_PRICE = 5500

    BLACK_TEXT_A4_TWO_PRICE = 4000
    BLACK_TEXT_A5_TWO_PRICE = 2500
    BLACK_TEXT_A3_TWO_PRICE = 6500

    # ----------------------------

    BLACK_PIC_A4_ONE_PRICE = 3800
    BLACK_PIC_A5_ONE_PRICE = 3000
    BLACK_PIC_A3_ONE_PRICE = 7500

    BLACK_PIC_A4_TWO_PRICE = 6000
    BLACK_PIC_A5_TWO_PRICE = 3500
    BLACK_PIC_A3_TWO_PRICE = 8500

    # --------------------------------------------

    COLOR_TEXT_A4_PRICE = 7300
    COLOR_TEXT_A5_PRICE = 5000
    COLOR_TEXT_A3_PRICE = 12800

    COLOR_PIC_A4_PRICE = 9300
    COLOR_PIC_A5_PRICE = 6000
    COLOR_PIC_A3_PRICE = 16800

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # subprocess.run(["python", "01-ConvertQtCreatorFileToClass.py"])

        self.shortcut = QShortcut(QKeySequence('F5'), self)
        self.shortcut.activated.connect(lambda: (self.clear_boxes()))

        self.shortcut = QShortcut(QKeySequence('Esc'), self)
        self.shortcut.activated.connect(lambda: (self.clear_boxes()))

        self.doubleSpinBox_other_cost = MyDoubleSpinBox(self.centralwidget, self.doubleSpinBox_other_cost_hidden)

        self.doubleSpinBox_other_cost.textChanged.connect(
            lambda: (self.calculate()))

        self.hide_default_spinboxes()

        self.initialize_spinboxes()

        self.initialize_spinboxes_dict()

        self.first_setup()

        self.spinBox_percentage.textChanged.connect(
            lambda: (self.set_percentage()))

        self.pushButton_clear.clicked.connect(lambda: (self.clear_boxes()))

    def set_percentage(self):
        percent = self.spinBox_percentage.text()

        self.PERCENTAGE = percent

        for i in self.DICT:
            spinBox = self.DICT[i][0]

            spinBox.calc()

        self.calculate()

    def calculate(self):
        all_papers_total = int((float(self.doubleSpinBox_other_cost.text())) * 1000)

        dict = self.DICT

        for i in dict:
            spinBox = dict[i][0]
            all_papers_total += spinBox.LAST_CALCULATED_PRICE

        self.label_reult.setText(str(format_int_with_commas(all_papers_total)))

    def initialize_spinboxes_dict(self):
        self.DICT = {
            "black_text_a4_one": [self.my_spinBox_black_text_A4_one,
                                  self.spinBox_black_text_A4_one_hidden,
                                  self.BLACK_TEXT_A4_ONE_PRICE,
                                  self.label_black_before_text_A4_one,
                                  self.label_black_after_text_A4_one,
                                  self.label_black_text_A4_one_total_before,
                                  self.label_black_text_A4_one_total_after,
                                  0],
            "black_text_a5_one": [self.my_spinBox_black_text_A5_one,
                                  self.spinBox_black_text_A5_one_hidden,
                                  self.BLACK_TEXT_A5_ONE_PRICE,
                                  self.label_black_before_text_A5_one,
                                  self.label_black_after_text_A5_one,
                                  self.label_black_text_A5_one_total_before,
                                  self.label_black_text_A5_one_total_after,
                                  0],
            "black_text_a3_one": [self.my_spinBox_black_text_A3_one,
                                  self.spinBox_black_text_A3_one_hidden,
                                  self.BLACK_TEXT_A3_ONE_PRICE,
                                  self.label_black_before_text_A3_one,
                                  self.label_black_after_text_A3_one,
                                  self.label_black_text_A3_one_total_before,
                                  self.label_black_text_A3_one_total_after,
                                  0],
            "black_text_a4_two": [self.my_spinBox_black_text_A4_two,
                                  self.spinBox_black_text_A4_two_hidden,
                                  self.BLACK_TEXT_A4_TWO_PRICE,
                                  self.label_black_before_text_A4_two,
                                  self.label_black_after_text_A4_two,
                                  self.label_black_text_A4_two_total_before,
                                  self.label_black_text_A4_two_total_after,
                                  0],
            "black_text_a5_two": [self.my_spinBox_black_text_A5_two,
                                  self.spinBox_black_text_A5_two_hidden,
                                  self.BLACK_TEXT_A5_TWO_PRICE,
                                  self.label_black_before_text_A5_two,
                                  self.label_black_after_text_A5_two,
                                  self.label_black_text_A5_two_total_before,
                                  self.label_black_text_A5_two_total_after,
                                  0],
            "black_text_a3_two": [self.my_spinBox_black_text_A3_two,
                                  self.spinBox_black_text_A3_two_hidden,
                                  self.BLACK_TEXT_A3_TWO_PRICE,
                                  self.label_black_before_text_A3_two,
                                  self.label_black_after_text_A3_two,
                                  self.label_black_text_A3_two_total_before,
                                  self.label_black_text_A3_two_total_after,
                                  0],
            "black_pic_a4_one": [self.my_spinBox_black_pic_A4_one,
                                 self.spinBox_black_pic_A4_one_hidden,
                                 self.BLACK_PIC_A4_ONE_PRICE,
                                 self.label_black_before_pic_A4_one,
                                 self.label_black_after_pic_A4_one,
                                 self.label_black_pic_A4_one_total_before,
                                 self.label_black_pic_A4_one_total_after,
                                 0],
            "black_pic_a5_one": [self.my_spinBox_black_pic_A5_one,
                                 self.spinBox_black_pic_A5_one_hidden,
                                 self.BLACK_PIC_A5_ONE_PRICE,
                                 self.label_black_before_pic_A5_one,
                                 self.label_black_after_pic_A5_one,
                                 self.label_black_pic_A5_one_total_before,
                                 self.label_black_pic_A5_one_total_after,
                                 0],
            "black_pic_a3_one": [self.my_spinBox_black_pic_A3_one,
                                 self.spinBox_black_pic_A3_one_hidden,
                                 self.BLACK_PIC_A3_ONE_PRICE,
                                 self.label_black_before_pic_A3_one,
                                 self.label_black_after_pic_A3_one,
                                 self.label_black_pic_A3_one_total_before,
                                 self.label_black_pic_A3_one_total_after,
                                 0],
            "black_pic_a4_two": [self.my_spinBox_black_pic_A4_two,
                                 self.spinBox_black_pic_A4_two_hidden,
                                 self.BLACK_PIC_A4_TWO_PRICE,
                                 self.label_black_before_pic_A4_two,
                                 self.label_black_after_pic_A4_two,
                                 self.label_black_pic_A4_two_total_before,
                                 self.label_black_pic_A4_two_total_after,
                                 0],
            "black_pic_a5_two": [self.my_spinBox_black_pic_A5_two,
                                 self.spinBox_black_pic_A5_two_hidden,
                                 self.BLACK_PIC_A5_TWO_PRICE,
                                 self.label_black_before_pic_A5_two,
                                 self.label_black_after_pic_A5_two,
                                 self.label_black_pic_A5_two_total_before,
                                 self.label_black_pic_A5_two_total_after,
                                 0],
            "black_pic_a3_two": [self.my_spinBox_black_pic_A3_two,
                                 self.spinBox_black_pic_A3_two_hidden,
                                 self.BLACK_PIC_A3_TWO_PRICE,
                                 self.label_black_before_pic_A3_two,
                                 self.label_black_after_pic_A3_two,
                                 self.label_black_pic_A3_two_total_before,
                                 self.label_black_pic_A3_two_total_after,
                                 0],
            "color_text_a4": [self.my_spinBox_color_text_A4,
                              self.spinBox_color_text_A4_hidden,
                              self.COLOR_TEXT_A4_PRICE,
                              self.label_color_before_text_A4,
                              self.label_color_after_text_A4,
                              self.label_color_text_A4_total_before,
                              self.label_color_text_A4_total_after,
                              1],
            "color_text_a5": [self.my_spinBox_color_text_A5,
                              self.spinBox_color_text_A5_hidden,
                              self.COLOR_TEXT_A5_PRICE,
                              self.label_color_before_text_A5,
                              self.label_color_after_text_A5,
                              self.label_color_text_A5_total_before,
                              self.label_color_text_A5_total_after,
                              1],
            "color_text_a3": [self.my_spinBox_color_text_A3,
                              self.spinBox_color_text_A3_hidden,
                              self.COLOR_TEXT_A3_PRICE,
                              self.label_color_before_text_A3,
                              self.label_color_after_text_A3,
                              self.label_color_text_A3_total_before,
                              self.label_color_text_A3_total_after,
                              1],
            "color_pic_a4": [self.my_spinBox_color_pic_A4,
                             self.spinBox_color_pic_A4_hidden,
                             self.COLOR_PIC_A4_PRICE,
                             self.label_color_before_pic_A4,
                             self.label_color_after_pic_A4,
                             self.label_color_pic_A4_total_before,
                             self.label_color_pic_A4_total_after,
                             1],
            "color_pic_a5": [self.my_spinBox_color_pic_A5,
                             self.spinBox_color_pic_A5_hidden,
                             self.COLOR_PIC_A5_PRICE,
                             self.label_color_before_pic_A5,
                             self.label_color_after_pic_A5,
                             self.label_color_pic_A5_total_before,
                             self.label_color_pic_A5_total_after,
                             1],
            "color_pic_a3": [self.my_spinBox_color_pic_A3,
                             self.spinBox_color_pic_A3_hidden,
                             self.COLOR_PIC_A3_PRICE,
                             self.label_color_before_pic_A3,
                             self.label_color_after_pic_A3,
                             self.label_color_pic_A3_total_before,
                             self.label_color_pic_A3_total_after,
                             1],

        }

    def initialize_spinboxes(self):
        self.my_spinBox_black_text_A4_one = None
        self.my_spinBox_black_text_A5_one = None
        self.my_spinBox_black_text_A3_one = None

        self.my_spinBox_black_text_A4_two = None
        self.my_spinBox_black_text_A5_two = None
        self.my_spinBox_black_text_A3_two = None

        self.my_spinBox_black_pic_A4_one = None
        self.my_spinBox_black_pic_A5_one = None
        self.my_spinBox_black_pic_A3_one = None

        self.my_spinBox_black_pic_A4_two = None
        self.my_spinBox_black_pic_A5_two = None
        self.my_spinBox_black_pic_A3_two = None

        self.my_spinBox_color_text_A4 = None
        self.my_spinBox_color_text_A5 = None
        self.my_spinBox_color_text_A3 = None

        self.my_spinBox_color_pic_A4 = None
        self.my_spinBox_color_pic_A5 = None
        self.my_spinBox_color_pic_A3 = None

    def first_setup(self):
        for i in self.DICT:
            self.DICT[i][0] = MySpinBox(
                self.centralwidget,
                self.DICT[i],
                self
            )

            self.DICT[i][0].textChanged.connect(
                lambda: (self.calculate()))

    def hide_default_spinboxes(self):

        self.doubleSpinBox_other_cost_hidden.hide()

        self.spinBox_black_text_A3_one_hidden.hide()
        self.spinBox_black_text_A4_one_hidden.hide()
        self.spinBox_black_text_A5_one_hidden.hide()

        self.spinBox_black_text_A3_two_hidden.hide()
        self.spinBox_black_text_A4_two_hidden.hide()
        self.spinBox_black_text_A5_two_hidden.hide()

        self.spinBox_black_pic_A3_one_hidden.hide()
        self.spinBox_black_pic_A4_one_hidden.hide()
        self.spinBox_black_pic_A5_one_hidden.hide()

        self.spinBox_black_pic_A3_two_hidden.hide()
        self.spinBox_black_pic_A4_two_hidden.hide()
        self.spinBox_black_pic_A5_two_hidden.hide()

        self.spinBox_color_text_A3_hidden.hide()
        self.spinBox_color_text_A4_hidden.hide()
        self.spinBox_color_text_A5_hidden.hide()

        self.spinBox_color_pic_A3_hidden.hide()
        self.spinBox_color_pic_A4_hidden.hide()
        self.spinBox_color_pic_A5_hidden.hide()

    def clear_boxes(self):
        for i in self.DICT:
            spinBox = self.DICT[i][0]
            label = self.DICT[i][4]

            spinBox.setValue(0)
            label.setText("0")

        self.spinBox_percentage.setValue(0)
        self.doubleSpinBox_other_cost.setValue(0)

        self.label_reult.setText("0")


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
