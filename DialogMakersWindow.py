
# A class for a dialog to save database settings
class DialogMakersWindow(QDialog):
    """Creates a dialog to open software developer and software info"""

    # Constructor
    def __init__(self):
        super().__init__()

        loadUi("DialogMakersWindow.ui", self)

        self.setWindowTitle('Sovelluksen tiedot')

        # Elements
        self.makersL = self.makersLabel
        self.makersD = self.makersDialog
        self.makersPrgrIL = self.makersPrgrInfoLabel
        self.makersTB = self.makersTextBrowser

        # Set values of elements according to the current settings
        # Create an object to use setting methods
        self.databaseOperation = pgModule.DatabaseOperation() # Needed in slots -> self

        # Signals

    # Slots

    # Peru button closes the dialog
    def closeDialog(self):
        self.close()
