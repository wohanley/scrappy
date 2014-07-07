from PyQt5 import QtWidgets
from main_window_ui import Ui_MainWindow
from scrappy.parse.nltk_scraps import ScrapExtracter
from scrappy.ui.highlight import highlight_chunks, YellowBackground

class MainWindow(QtWidgets.QMainWindow):
    """
    The main editor window.
    """

    def __init__(self):
        
        super(MainWindow, self).__init__()
        
        self._scrapExtracter = ScrapExtracter()
        self._highlight = highlight_chunks
        
        # set up UI using generated code from designer file
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)
        
        # called on every change to the text document
        self._ui.textEdit.document().contentsChange.connect(self._update_tree)
        
        # handle save button click
        self._ui.actionSave.triggered.connect(self._save)
        
    def _update_tree(self, position, charsRemoved, charsAdded):
        """
        Sync text in the document with the parse tree.
        """
        self._scraps = self._scrapExtracter.extract_scraps(
            self._ui.textEdit.toPlainText())
        self._update_document()
        
    def _update_document(self):
        """
        Update the document to reflect the parse tree.
        """
        self._highlight(self._ui.textEdit, self._scraps,
                        YellowBackground())
    
    def _save(self):
        pass