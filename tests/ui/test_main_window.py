import unittest
import mock
from scrappy.ui.main_window import MainWindow

@mock.patch('scrappy.ui.main_window.Ui_MainWindow')
@mock.patch('PyQt5.QtWidgets.QMainWindow.__init__')
@mock.patch('PyQt5.QtWidgets.QPlainTextEdit.__init__')
class TestMainWindow(unittest.TestCase):
    
    def test_constructor_sets_up_ui(self, mock_q_plain_text_edit_init,
                                    mock_q_main_window_init,
                                    mock_ui):
        
        window = MainWindow()
        
        mock_ui.return_value.setupUi.assert_called_once_with(window)
        
    @mock.patch('scrappy.ui.main_window.ScrapExtracter')
    @mock.patch('scrappy.ui.highlight.highlight_chunks')
    def test_update_tree_extracts_scraps(self, mock_highlighter,
                                         mock_extracter,
                                         mock_q_plain_text_edit_init,
                                         mock_q_main_window_init,
                                         mock_ui):
        """
        This strikes me as a technically less than ideal solution.
        Really I think it would be better to simulate a Qt signal and
        avoid calling a private function.
        """
        window = MainWindow()
        window._update_tree(None, None, None)
        
        mock_extracter.return_value.extract_scraps.assert_called_once_with(
            mock_ui.return_value.textEdit.toPlainText())
        mock_highlighter.assert_called_once()


if __name__ == "__main__":
    unittest.main()