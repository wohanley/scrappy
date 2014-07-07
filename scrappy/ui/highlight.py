from PyQt5 import QtGui

def highlight_chunks(editor, scraps, hl_format):
    """
    Highlight text in editor according to the supplied parse tree.
    """
    
    original_cursor = editor.textCursor()
    original_format = editor.currentCharFormat()
    
    try:
        editor.moveCursor(QtGui.QTextCursor.Start)
        
        for scrap in scraps:
            # select the scrap
            editor.find(scrap)
            # highlight the scrap
            editor.textCursor().mergeCharFormat(hl_format)
    finally:
        editor.setCurrentCharFormat(original_format)
        editor.setTextCursor(original_cursor)

    
class YellowBackground(QtGui.QTextCharFormat):
    
    def __init__(self):
        super(YellowBackground, self).__init__()
        self.setBackground(QtGui.QBrush(QtGui.QColor("yellow")))