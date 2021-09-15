from __init__ import *

CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

class Ui(QWidget):
    
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.setFixedSize(700, 400)

        self.width = 1000
        self.height = 650

        self.mainWindowTitle = 'Meme Generator -ohTitus'
        self.secondWindowTitle = 'Second Page'
        
        self.setFixedSize(self.width, self.height)
        

        self.menu = QStackedLayout()
        
        self.mainWindow = QWidget()
        self.secondWindow = QWidget()
        self.drakepostingWindow = QWidget()
        
        self.mainWindowUi()
        self.secondWindowUi()
        self.drakepostingWindowUi()
    
        self.menu.addWidget(self.mainWindow)
        self.menu.addWidget(self.secondWindow)
        self.menu.addWidget(self.drakepostingWindow)


    def mainWindowUi(self):


        self.mainWindow.setWindowTitle(self.mainWindowTitle)
        self.setWindowIcon(QIcon(CURRENT_DIRECTORY + '\\images\\pepe.jpg'))
        self.mainWindow.setFixedSize(self.width, self.height)

        self.mainWindowBackgroundTemplate = QLabel(self.mainWindow)
        self.mainWindowBackgroundTemplate.setPixmap(QPixmap(CURRENT_DIRECTORY + "\\images\\mainWindowBackground.png"))

        self.mainWindow_to_drakeposting = QPushButton(self.mainWindow)
        self.mainWindow_to_drakeposting.setCursor(QCursor(Qt.PointingHandCursor))
        self.mainWindow_to_drakeposting.setText('Drakeposting Meme Generator')
        self.mainWindow_to_drakeposting.setFont(QFont('KG HAPPY', 20))
        self.mainWindow_to_drakeposting.move(150,240)
        self.mainWindow_to_drakeposting.setStyleSheet('border: 3px solid white;'
         'border-radius : 10;'
          'padding: 15px;'
           'background-color: #18172C;'
            'color: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 rgb(199, 79, 232), stop:1 rgb(60, 147, 240));')



        self.mainWindow_to_secondWindow = QPushButton(self.mainWindow)
        self.mainWindow_to_secondWindow.setCursor(Qt.PointingHandCursor)
        self.mainWindow_to_secondWindow.setStyleSheet('border: transparent;' )



    def drakepostingWindowUi(self):
        DEFAULT_FILENAME = "drakeposting" + str(randint(100, 999))

        self.mainfont = QFont('Didact Gothic', 15)
        self.hkgrotesk = QFont('HK Grotesk Medium', 20)
        self.drakepostingWindowBackground = QLabel(self.drakepostingWindow)
        self.drakepostingWindowBackground.setPixmap(QPixmap(CURRENT_DIRECTORY + "\\images\\drakepostingbackground.jpg"))


        def selectDrakePostingImage1():


            openDrakepostingImage1 = QFileDialog.getOpenFileName(caption='Select a Image/Media File', directory=os.getcwd(), filter='Standard Image File (*.png *.jpg *.jpeg *.tiff *.bmp);;')

            global image1
            image1 = openDrakepostingImage1[0]

            image1ex = QLabel(self.drakepostingWindow)
            image1expixmap1 = QPixmap(image1)
            image1expixmap = image1expixmap1.scaled(171, 166)
            image1ex.setPixmap(image1expixmap)
            image1ex.move(230, 268)

            image1ex.adjustSize()
            image1ex.show()

        def selectDrakePostingImage2():

            openDrakepostingImage2 = QFileDialog.getOpenFileName(caption='Select a Image/Media File', directory=os.getcwd(), filter='Standard Image File (*.png *.jpg *.jpeg *.tiff *.bmp);;')

            global image2
            image2 = openDrakepostingImage2[0]
            image2ex = QLabel(self.drakepostingWindow)
            image2expixmap1 = QPixmap(image2)
            image2expixmap = image2expixmap1.scaled(171, 166)
            image2ex.setPixmap(image2expixmap)
            image2ex.move(230, 437)
            image2ex.adjustSize()
            image2ex.show()





        def setFileName():
            global output_filename
            output_filename = self.filenameField.text().strip()

            windows_invalidcharacters = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
            windows_invalidfilenames =  ['CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9']

            if any(i in output_filename for i in windows_invalidcharacters):
                QMessageBox.warning(self, "Invalid Characters!", 'Windows Filenames cannot include characters listed below:\n<  >  :  "  \\ / | ? *')
            elif output_filename == "":
                QMessageBox.warning(self, "Empty Filename!", "Please enter a valid filename before setting it.")

            else:
                pass

            for item in windows_invalidfilenames:
                if item == output_filename:
                    QMessageBox.warning(self, "Invalid Filename!", "Windows Filenames cannot include characters listed below:\n'CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7', 'COM8', 'COM9', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9'")
                    break
                else:
                    continue

            self.filenameField.clear()
            self.filenameField.setPlaceholderText(output_filename)


            global output_filepath
            output_filepath = CURRENT_DIRECTORY + "\\" + output_filename + ".png"



        def drake(image1, image2):




            drake = Image.open(CURRENT_DIRECTORY +  '\\images\\300px-Drakeposting.jpg')

            image1 = Image.open(image1)
            image2 = Image.open(image2)
            image1 = image1.resize((150, 145))
            image2 = image2.resize((150, 145))

            drake.paste(image1, (150, 0))
            drake.paste(image2,(150, 147))


            if "output_filepath" in globals():
                drake.save(output_filepath)
            else:
                drake.save("drakeposting" + str(randint(100, 199)) + ".png")
            drake.show()



        def runDrakeFunction():
            imageSave_signal = True
            try:
                try:
                    drake(image1=image1, image2=image2)
                except NameError:
                    QMessageBox.warning(self, "Missing Images", "Please select both images!")
                    imageSave_signal = False
                except AttributeError:
                    QMessageBox.warning(self, "(NULL)", 'Please reselect your images!')
                    imageSave_signal = False

            except ValueError:
                display_notification(title="Meme Generator", text="Image could not be created!")
                QMessageBox.about(self, "Please set a filename!", "You have set an invalid, or empty filename. Please fix that by setting it with valid characters and try again!")
                if (self.filenameField.placeholderText()) == "" and (len(self.filenameField.text().strip()) > 0):


                    self.setFileName_reminder = QLabel(self.drakepostingWindow)
                    self.setFileName_reminder.setFont(QFont('HK Grotesk', 13))
                    self.setFileName_reminder.setText('           Tip!\nMake sure to intialize\nthe filename by clicking\n      "Set Filename"!')
                    self.setFileName_reminder.setStyleSheet('border: 5px solid red')
                    self.setFileName_reminder.move(655, 220)
                    self.setFileName_reminder.adjustSize()
                    self.setFileName_reminder.show()

                    self.setFilenameToolTipTimer = QTimer()
                    self.setFilenameToolTipTimer.start(8000)
                    self.setFilenameToolTipTimer.timeout.connect(lambda: self.setFileName_reminder.hide())
                    imageSave_signal = False



            if imageSave_signal == True:
                QApplication.setOverrideCursor(Qt.WaitCursor)
                self.WaitCursorTimer = QTimer()
                self.WaitCursorTimer.start(5)
                self.WaitCursorTimer.timeout.connect(lambda: QApplication.restoreOverrideCursor())
                display_notification(title="Image saved!", text=output_filename + " was saved in " + CURRENT_DIRECTORY)
                #toastNotif.show_toast("Image Successfully Saved!", "Image was saved in " + CURRENT_DIRECTORY, threaded=True)



        self.drakepostingWindow.setFixedSize(self.width, self.height)
        self.drakepostingWindow_to_mainWindow = QPushButton(self.drakepostingWindow)
        self.drakepostingWindow_to_mainWindow.setText('Back')
        self.drakepostingWindow_to_mainWindow.setFont(QFont('KG Happy', 19))
        self.drakepostingWindow_to_mainWindow.setStyleSheet("background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 rgb(199, 79, 232), stop:1 rgb(60, 147, 240));" "border:5px solid black;")
        self.drakepostingWindow_to_mainWindow.setCursor(QCursor(Qt.PointingHandCursor))
        self.drakepostingWindow_to_mainWindow.resize(150, 50)
        self.drakepostingWindow_to_mainWindow.move(25, 100)


        ##
        ## GET FIRST IMAGE
        ##
        self.drakepostingGetImage1 = QPushButton(self.drakepostingWindow)
        self.drakepostingGetImage1.setFont(self.mainfont)
        self.drakepostingGetImage1.setStyleSheet('background-color: rgb(163, 91, 227)')
        self.drakepostingGetImage1.setText('Select Image (1)')
        self.drakepostingGetImage1.resize(150, 50)
        self.drakepostingGetImage1.move(435, 352)
        self.drakepostingGetImage1.setCursor(QCursor(Qt.PointingHandCursor))
        self.drakepostingGetImage1.clicked.connect(selectDrakePostingImage1)


        ##
        ## GET SECOND IMAGE
        ##
        self.drakepostingGetImage2 = QPushButton(self.drakepostingWindow)
        self.drakepostingGetImage2.setFont(self.mainfont)
        self.drakepostingGetImage2.setStyleSheet('background-color: rgb(113, 91, 227)')
        self.drakepostingGetImage2.setText('Select Image (2)')
        self.drakepostingGetImage2.resize(150, 50)
        self.drakepostingGetImage2.move(435, 515)
        self.drakepostingGetImage2.setCursor(QCursor(Qt.PointingHandCursor))
        self.drakepostingGetImage2.clicked.connect(selectDrakePostingImage2)


        ##
        ## (CREATE IMAGE) SAVE IMAGE AND DISPLAY
        ##
        self.create_drakeposting = QPushButton(self.drakepostingWindow)
        self.create_drakeposting.setStyleSheet('background-color: rgb(54, 130, 163);')
        self.create_drakeposting.setCursor(QCursor(Qt.PointingHandCursor))
        self.create_drakeposting.setText('Create Image')
        self.create_drakeposting.setFont(self.hkgrotesk)
        self.create_drakeposting.resize(190, 55)
        self.create_drakeposting.move(649, 515)
        self.create_drakeposting.clicked.connect(runDrakeFunction)
        ##
        ## FILENAME QLINEEDIT
        ##
        self.filenameField = QLineEdit(self.drakepostingWindow)
        self.filenameField.setFont(self.hkgrotesk)
        self.filenameField.setPlaceholderText('Enter Here')
        self.filenameField.setAlignment(Qt.AlignCenter)
        self.filenameField.move(630, 320)
        self.filenameField.resize(220, 45)


        ##
        ## SET FILENAME FROM ENTRYBOX
        ##
        self.setFileNameBtn = QPushButton(self.drakepostingWindow)
        self.setFileNameBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.setFileNameBtn.setFont(self.hkgrotesk)
        self.setFileNameBtn.setText('Set Filename')
        self.setFileNameBtn.resize(180, 55)
        self.setFileNameBtn.move(650, 415)
        self.setFileNameBtn.clicked.connect(setFileName)


    def secondWindowUi(self):

        self.secondWindow.setFixedSize(self.width, self.height)
        self.secondWindow.setWindowTitle(self.secondWindowTitle)
        
        self.secondWindow_to_mainWindow = QPushButton(self.secondWindow)





class Main(QMainWindow, Ui):

    def __init__(self):

        super(Main, self).__init__()
        self.setupUi(self)
        
        self.mainWindow_to_secondWindow.clicked.connect(self.secondWindowIndex)
        self.secondWindow_to_mainWindow.clicked.connect(self.mainWindowIndex)
        self.mainWindow_to_drakeposting.clicked.connect(self.drakepostingWindowIndex)
        self.drakepostingWindow_to_mainWindow.clicked.connect(self.mainWindowIndex)


    def mainWindowIndex(self):
        self.menu.setCurrentIndex(0)

    def secondWindowIndex(self):

        self.menu.setCurrentIndex(1)

    def drakepostingWindowIndex(self):

        self.menu.setCurrentIndex(2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    M = Main()
    sys.exit(app.exec())




