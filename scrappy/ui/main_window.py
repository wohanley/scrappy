from PyQt5 import QtWidgets
from main_window_ui import Ui_MainWindow
from scrappy.document import Document
from scrappy.parse.nltk_scraps import ScrapExtracter
from scrappy.ui.highlight import highlight_chunks, YellowBackground

class MainWindow(QtWidgets.QMainWindow):
    """
    The main editor window.
    """

    def __init__(self):
        
        super(MainWindow, self).__init__()
        
        self._document = Document()
        self._scrapExtracter = ScrapExtracter()
        self._highlight = highlight_chunks
        
        # set up UI using generated code from designer file
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        
        # handle save button click
        self._ui.actionSave.triggered.connect(self._update_document)
        
    def _update_document(self):
        """
        Add text in the editor to the document object.
        """
        self._document.parse_tree = (self._scrapExtracter
            .extract_scraps(self._ui.textEdit.toPlainText()))
        self._highlight(self._ui.textEdit, self._document.parse_tree,
                        YellowBackground())