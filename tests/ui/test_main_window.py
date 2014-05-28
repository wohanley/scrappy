import unittest
import mock
from scrappy.ui.main_window import MainWindow

@mock.patch('scrappy.ui.main_window.Ui_MainWindow')
@mock.patch('PyQt5.QtWidgets.QMainWindow.__init__')
class TestMainWindow(unittest.TestCase):
    
    def test_constructor_sets_up_ui(self, mock_q_main_window_init, mock_ui):
        
        window = MainWindow()
        
        mock_ui.return_value.setupUi.assert_called_once_with(window)
        
    @mock.patch('scrappy.ui.main_window.ScrapExtracter')
    def test_update_document_extracts_scraps(self, mock_extracter,
                                             mock_q_main_window_init,
                                             mock_ui):
        """
        This strikes me as a technically less than ideal solution. Really I
        think it would be better to simulate a Qt signal and avoid calling a
        private function.
        """
        window = MainWindow()
        window._update_document()
        
        mock_extracter.return_value.extract_scraps.assert_called_once_with(
            mock_ui.return_value.textEdit.toPlainText())


if __name__ == "__main__":
    unittest.main()