from PyQt5 import QtGui
from scrappy.parse.nltk_scraps import tree_to_string

def highlight_chunks(editor, tree, hl_format):
    """
    Highlight text in editor according to the supplied parse tree.
    """
    
    original_cursor = editor.textCursor()
    original_format = editor.currentCharFormat()
    
    try:
        editor.moveCursor(QtGui.QTextCursor.Start)
        
        for chunk in tree:
            # select the scrap
            editor.find(tree_to_string(chunk))
            # highlight the scrap
            editor.textCursor().mergeCharFormat(hl_format)
    finally:
        editor.setCurrentCharFormat(original_format)
        editor.setTextCursor(original_cursor)

    
class YellowBackground(QtGui.QTextCharFormat):
    
    def __init__(self):
        super(YellowBackground, self).__init__()
        self.setBackground(QtGui.QBrush(QtGui.QColor("yellow")))