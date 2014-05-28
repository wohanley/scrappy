import unittest
import mock
from scrappy.ui.main_window import MainWindow

class TestMainWindow(unittest.TestCase):

    @mock.patch('scrappy.ui.main_window.Ui_MainWindow')
    @mock.patch('PyQt5.QtWidgets.QMainWindow.__init__')
    def test_constructor_sets_up_ui(self, mock_q_main_window_init, mock_ui):
        
        window = MainWindow()
        
        mock_ui.return_value.setupUi.assert_called_once_with(window)


if __name__ == "__main__":
    unittest.main()