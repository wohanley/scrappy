from PyQt5 import QtWidgets
from .main_window_ui import Ui_MainWindow
from parse.nltk_scraps import ScrapExtracter

class MainWindow(QtWidgets.QMainWindow):
    """
    The main editor window.
    """

    def __init__(self):
        super(MainWindow, self).__init__()
        
        self._scrapExtracter = ScrapExtracter()
        
        # set up UI using generated code from designer file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # handle save button click
        self.ui.actionSave.triggered.connect(self._actionSaveTriggered)
        
    def _actionSaveTriggered(self):
        """
        Save the current document.
        """
        self._scrapExtracter.extract_scraps(self.ui.textEdit.toPlainText())