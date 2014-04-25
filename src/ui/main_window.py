from PyQt5 import QtWidgets
from .main_window_ui import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    """
    The main editor window.
    """

    def __init__(self):
        super(MainWindow, self).__init__()
        
        # set up UI using generated code from designer file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # handle save button click
        self.ui.actionSave.triggered.connect(self._actionSaveTriggered)
        
    def _actionSaveTriggered(self):
        """
        Save the current document.
        """
        pass