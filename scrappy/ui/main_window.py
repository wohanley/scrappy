from PyQt5 import QtWidgets
from .main_window_ui import Ui_MainWindow
from scrappy.parse.nltk_scraps import ScrapExtracter
from scrappy.document import Document

class MainWindow(QtWidgets.QMainWindow):
    """
    The main editor window.
    """

    def __init__(self):
        
        super(MainWindow, self).__init__()
        
        self._document = Document()
        self._scrapExtracter = ScrapExtracter()
        
        # set up UI using generated code from designer file
        ui = Ui_MainWindow()
        ui.setupUi(self)
        
        # handle save button click
        ui.actionSave.triggered.connect(self._update_document)
        
    def _update_document(self):
        """
        Add text in the editor to the document object.
        """
        self._document.parse_tree = self._scrapExtracter.extract_scraps(self.ui.textEdit.toPlainText())