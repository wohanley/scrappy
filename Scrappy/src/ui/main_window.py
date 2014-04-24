from PyQt5 import QtWidgets
from .main_window_ui import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    """
    The main editor window.
    """

    def __init__(self):
        super(MainWindow, self).__init__()
        
        # Set up UI using generated code from designer file.
        Ui_MainWindow().setupUi(self)