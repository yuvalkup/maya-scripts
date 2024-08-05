import maya.OpenMaya as om
import maya.OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtWidgets, QtCore

def maya_main_window():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

class LabelPromptDialog(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(LabelPromptDialog, self).__init__(parent)
        self.setWindowTitle("Replay Button Label")
        self.setFixedSize(300, 100)

        self.text_field = QtWidgets.QLineEdit(self)
        self.text_field.setPlaceholderText("Enter your label here...")
        self.text_field.textChanged.connect(self.update_buttons)

        self.save_button = QtWidgets.QPushButton("Save", self)
        self.save_button.clicked.connect(self.accept)
        self.save_button.setEnabled(False)

        self.discard_button = QtWidgets.QPushButton("Discard", self)
        self.discard_button.clicked.connect(self.reject)

        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.discard_button)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.text_field)
        main_layout.addLayout(button_layout)

    def update_buttons(self):
        self.save_button.setEnabled(bool(self.text_field.text().strip()))

    def get_text(self):
        return self.text_field.text() if self.exec_() == QtWidgets.QDialog.Accepted else None

def show_simple_prompt():
    dialog = LabelPromptDialog()
    result = dialog.get_text()
    return result
