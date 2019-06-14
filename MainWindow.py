from GameLogics import Level
from Game_interface import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

import colors


class MyWin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

        # мои переменные
        self.g = Level(0)
        self.g.create_level()
        self.select_col = self.g.get_select_col()
        self.score = self.g.get_score()
        self.level = 1

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.timer_tick)

        self.buttonStart.clicked.connect(self.start)


    def keyPressEvent(self, event):
        dict = {
            QtCore.Qt.Key_W: self.up,
            QtCore.Qt.Key_S: self.down,
            QtCore.Qt.Key_A: self.left,
            QtCore.Qt.Key_D: self.right
        }
        try:
            dict[event.key()]()
        except:
            pass

    def show_matrix_in_table(self):
        self.select_col = self.g.get_select_col()
        for row in range(self.g.height):
            for col in range(self.g.width):
                item = self.g[row, col]
                cellinfo = QTableWidgetItem(' ')
                if item == -2:
                    cellinfo = QTableWidgetItem('Dinamit')
                # Только для чтения
                cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(row, col, cellinfo)
                color = colors.my_color[item]
                if col == self.select_col and item == 0:
                    color = (200, 200, 200)
                self.tableWidget.item(row, col).setBackground(QtGui.QColor(color[0], color[1], color[2]))

        # 2 таблица
        cell = QTableWidgetItem(' ')
        # Только для чтения
        cell.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        self.tableWidget_2.setItem(0, 0, cell)
        sel_block = self.g.get_select_blocks()
        c = colors.my_color[sel_block['color']]
        self.tableWidget_2.item(0, 0).setBackground(QtGui.QColor(c[0], c[1], c[2]))
        self.label.setText("x" + str(sel_block['count']))
        self.label_score.setText("Score: " + str(self.score))
        self.label_level.setText("Level " + str(self.level))
        self.label.setFont(QtGui.QFont('SansSerif', 20))
        self.label_score.setFont(QtGui.QFont('SansSerif', 20))
        self.label_level.setFont(QtGui.QFont('SansSerif', 20))


    def decor_update_view(func):
        def wrapped(self, *args, **kwargs):
            func(self, *args, **kwargs)
            self.show_matrix_in_table(*args, **kwargs)
        return wrapped

    # Описываем функции
    @decor_update_view
    def left(self):
        self.g.move_select_column('left')


    @decor_update_view
    def right(self):
        self.g.move_select_column('right')


    @decor_update_view
    def down(self):
        self.g.take_blocks()


    @decor_update_view
    def up(self):
        self.g.update()
        self.score = self.g.get_score()
        self.check_new_level()


    @decor_update_view
    def timer_tick(self):
        self.g.add_row()
        if self.g.check_game_over():
            self.timer.stop()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Game Over!")
            msg.setInformativeText("Level " + str(self.level))
            msg.setWindowTitle("Tetris")
            msg.addButton('Окей', QMessageBox.AcceptRole)
            msg.addButton('Отмена', QMessageBox.RejectRole)
            msg.exec()


    def start(self):
        self.g = Level(0)
        self.g.create_level()
        self.select_col = self.g.get_select_col()
        self.score = self.g.get_score()
        self.level = 1

        self.show_matrix_in_table()
        self.timer.start(5000)


    def check_new_level(self):
        if self.score >= 2500:
            self.new_level()


    def new_level(self):
        self.level += 1
        self.g = Level(0)
        self.g.create_level()
        self.score = self.g.get_score()
        self.select_col = self.g.get_select_col()
