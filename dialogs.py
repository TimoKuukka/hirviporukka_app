import sys
from PyQt5.QtWidgets import *

class DialogMakersWindow(QDialog):
    """Main Window for testing dialogs."""

    def __init__(self):
        QMainWindow().__init__()

        self.makersDialog('Pääikkuna dialogien testaukseen')

        # Add dialogs to be tested here and run them as follows:
        makersDialog = DialogMakersWindow()
        makersDialog.exec()


# Some tests
if __name__ == "__main__":

    # Create a testing application
    testApp = DialogMakersWindow(sys.argv)

    # Create a main window for testing a dialog
    testMainWindow = DialogMakersWindow()
    testMainWindow.show()

    # Run the testing application
    testApp.exec()