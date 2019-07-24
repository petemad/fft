from PyQt5 import QtWidgets , QtCore 
from PyQt5.QtCore import pyqtSignal , pyqtSlot 
from dialog import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog , QMessageBox
from PyQt5.QtGui import QPixmap , QImage
import numpy
import qimage2ndarray  
import sys
from numpy import errstate
import cv2
import time
import threading
import copy


class ApplicationWindow(QtWidgets.QMainWindow):
    
    progressSignal = pyqtSignal()

    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnBrowse.clicked.connect(self.Browse_clicked2)
        self.ui.btnStart.clicked.connect(self.btnStart_clicked)
        self.ui.btnPause.clicked.connect(self.btnPause_clicked)
        self.progressSignal.connect(self.progressBar)
        self.ui.progressBar.setRange(0, 64)
        self.progressBarValue = 0
        self.ui.btnStart.setEnabled(True)

    def Browse_clicked2 (self) :
        fileName, _filter = QFileDialog.getOpenFileName(self, "Title", "Default File", "Filter -- All Files (*);;Image Files (*.jpeg)")
        try :
            numPix = int(self.ui.TextBoxPixel.toPlainText())
        except ValueError :
            QMessageBox.question(self, 'Error', "Please!!  Enter number of pixels frist.", QMessageBox.Ok)

        if 64 % numPix != 0 :
            QMessageBox.question(self, 'Error', "Please!!  Enter number of pixels. or make sure it is factor of 64", QMessageBox.Ok)
            return
        

        try :    
            if fileName:
 
                global myImage
                myImage = cv2.imread(fileName , cv2.IMREAD_GRAYSCALE)
                height, width = myImage.shape
                if height != width or height != 128 :
                    QMessageBox.question(self, 'Error', "please insert 128 x 128 photo", QMessageBox.Ok)
                    return
                try :

                    qImg = QImage(myImage.data, width, height, QImage.Format_Grayscale8).rgbSwapped()
                    pixmap = QPixmap.fromImage(qImg)
                    x=128/pixmap.width()
                    y=128/pixmap.height()
                    pixmap = pixmap.scaled(int(pixmap.height()*y), int(pixmap.width()*x))
                    #self.ui.btnStart.setEnabled(True)

                    self.ui.btnPause.setEnabled(False)
                    self.ui.lblImg.setPixmap(QPixmap.fromImage(qImg))
                    self.ui.lblImg.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) 
                except :
                    QMessageBox.question(self, 'Error', "It is not an Image", QMessageBox.Ok)
                    return
        except :
            self.ui.btnStart.setEnabled(True)
            QMessageBox.question(self, 'Error', "Please insert only images", QMessageBox.Ok)
            return
          

    def theLastModification (self) :
        try :
            img = copy.deepcopy(myImage)
            compareImg = copy.deepcopy(myImage)
            numPix=int(self.ui.TextBoxPixel.toPlainText())
            if 64 % numPix != 0 :
                QMessageBox.question(self, 'Error', "number of pixels must be factor of 64", QMessageBox.Ok)
                return
        except :
            self.ui.btnStart.setEnabled(True)
            self.ui.btnPause.setEnabled(False)
            self.ui.btnBrowse.setEnabled(True)
            return

        for i in range(0,64,numPix) :
            self.progressBarValue = i
            self.progressSignal.emit()
            try :
                self.ui.btnPause.setEnabled(True)
                numPix = int(self.ui.TextBoxPixel.toPlainText())
            except :
                self.ui.btnStart.setEnabled(True)
                self.ui.btnBrowse.setEnabled(True)
                return
            try :

                if i == 0 :
                    imgFft = numpy.fft.fft2(img)
                    imgFftShift = numpy.fft.fftshift(imgFft) 
                    with errstate(divide='ignore'):
                        magspec = 20 * numpy.log(numpy.abs(imgFftShift))
                    #magspec = numpy.asarray(magspec, dtype=numpy.uint8)
                    qImg = qimage2ndarray.array2qimage(magspec)
                    self.ui.lblImgFft.setPixmap(QPixmap.fromImage(qImg))
                    self.ui.lblImgFft.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

                try :
                    for r in range(numPix):
                        for c in range(128):
                            magspec[r+i,c] = 0
                            imgFftShift[r+i,c] = 0
                    for r in range(128-numPix , 128):
                        for c in range(128):
                            magspec[128-i-numPix-r,c] = 0
                            imgFftShift[128-i-numPix-r,c] = 0
                    for r in range(128):
                        for c in range(numPix):
                            magspec[r,c+i] = 0
                            imgFftShift[r, c+i] = 0
                    for r in range(128):
                        for c in range(numPix):
                            magspec[r,128-i-numPix+c] = 0
                            imgFftShift[r, 128-i-numPix+c] = 0
                    q1img = qimage2ndarray.array2qimage(magspec)
                    self.ui.lblImgFft.setPixmap(QPixmap.fromImage(q1img))

                    imgtry = numpy.fft.ifftshift(imgFftShift)            
                    imgtry = numpy.fft.ifft2(imgtry)

                    #imagspec = numpy.asarray(imgtry, dtype=numpy.uint8)
                    q2img = qimage2ndarray.array2qimage(imgtry)
                    time.sleep(0.1)

                    self.ui.lblImg.setPixmap(QPixmap.fromImage(q2img))
                    self.ui.lblImg.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) 
                except :
                    img = copy.deepcopy(myImage)
                    i = 0
                    self.ui.btnStart.setEnabled(True)
                    return
            except :
                self.ui.btnStart.setEnabled(True)
                return
        try :
            if myImage.all() == compareImg.all() :
                self.theLastModification2()
            else :
                self.ui.btnStart.setEnabled(True)
                return
        except :
            self.ui.btnStart.setEnabled(True)
            return

    def theLastModification2 (self ,) :
        try :
            img = copy.deepcopy(myImage)
            compareImg = copy.deepcopy(myImage)
            numPix = int(self.ui.TextBoxPixel.toPlainText())
            if 64 % numPix != 0 :
                QMessageBox.question(self, 'Error', "number of pixels must be factor of 64", QMessageBox.Ok)
        except NameError :
            self.ui.btnStart.setEnabled(True)
            self.ui.btnPause.setEnabled(False)
            self.ui.btnBrowse.setEnabled(True)
            return

        for i in range(0,64,numPix) :
            self.progressBarValue = 64-i
            self.progressSignal.emit()

            try :
                numPix = int(self.ui.TextBoxPixel.toPlainText())
            except :
                self.ui.btnStart.setEnabled(True)
                self.ui.btnBrowse.setEnabled(True)
                return

            try :
                if i == 0 :
                    imgFft = numpy.fft.fft2(img)
                    imgFftShift = numpy.fft.fftshift(imgFft) 
                    with errstate(divide='ignore'):
                        magspec = 20 * numpy.log(numpy.abs(imgFftShift))
                    #magspec = numpy.asarray(magspec, dtype=numpy.uint8)

                    qImg = qimage2ndarray.array2qimage(magspec)
                    self.ui.lblImgFft.setPixmap(QPixmap.fromImage(qImg))
                    self.ui.lblImgFft.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
                    

                try :
                    for r in range(i+numPix):
                        for c in range(i+numPix):
                            magspec[64-r,64-c] = 0
                            imgFftShift[64-r,64-c] = 0

                    for r in range(i+numPix):
                        for c in range(i+numPix):
                            magspec[64+r,64+c] = 0
                            imgFftShift[64+r,64+c] = 0
            
                    for r in range(i+numPix):
                        for c in range(i+numPix):
                            magspec[64-r,64+c] = 0
                            imgFftShift[64-r,64+c] = 0

                    for r in range(i+numPix):
                        for c in range(i+numPix):
                            magspec[64+r,64-c] = 0
                            imgFftShift[64+r,64-c] = 0

                    q1img = qimage2ndarray.array2qimage(magspec)
                    self.ui.lblImgFft.setPixmap(QPixmap.fromImage(q1img))

                    imgtry = numpy.fft.ifftshift(imgFftShift)        
                    imgtry = numpy.fft.ifft2(imgtry)
                    
                    #imagspec = numpy.asarray(imgtry, dtype=numpy.uint8)
                    q2img = qimage2ndarray.array2qimage(imgtry)
                    
                    self.ui.lblImg.setPixmap(QPixmap.fromImage(q2img))
                    self.ui.lblImg.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) 

                    time.sleep(0.1)


                except :
                    img = copy.deepcopy(myImage)
                    i = 0
                    self.ui.btnStart.setEnabled(True)
                    return
            except :
                self.ui.btnStart.setEnabled(True)
                return
        try :
            if myImage.all() == compareImg.all() :
                self.theLastModification()
            else :
                self.ui.btnStart.setEnabled(True)
                return
        except :
            self.ui.btnStart.setEnabled(True)
            return    
            
    def btnStart_clicked(self):
        global numPix
        try :
            numPix = int(self.ui.TextBoxPixel.toPlainText())
        except :
            QMessageBox.question(self,'Error',"Please enter number of pixels")
        if 64 % numPix != 0 :
            QMessageBox.question(self, 'Error', "number of pixels must be factor of 64", QMessageBox.Ok)
            self.ui.btnStart.setEnabled(True)
            return

        try :

            self.ui.btnPause.setEnabled(True)
            self.ui.btnStart.setEnabled(False)
            self.ui.TextBoxPixel.setEnabled(False)
            numPix = int(self.ui.TextBoxPixel.toPlainText())
            global t1
            t1 = threading.Thread(target=self.theLastModification)
            t1.start()   
        except IndexError :
            QMessageBox.question(self, 'Error' , "Index error ! please reduce number of pixels or change the photo", QMessageBox.Ok)    
        except NameError :
            QMessageBox.question(self , 'Error' , "Please insert the photo frist" , QMessageBox.Ok)
        except :
            QMessageBox.question(self , 'Error' , "Please!! enter a proper integer" , QMessageBox.Ok)
            self.ui.btnPause.setEnabled(False)
            self.ui.btnStart.setEnabled(True)
            self.ui.TextBoxPixel.setEnabled(True)
            self.ui.btnBrowse.setEnabled(True)
        

    def btnPause_clicked(self):
        try : 
            timeToWait = float(self.ui.timeText.toPlainText())
            self.ui.btnPause.setEnabled(False)
            self.ui.TextBoxPixel.setEnabled(True)
            self.ui.btnBrowse.setEnabled(True)
        except :
            timeToWait=0
            self.ui.btnPause.setEnabled(False)
            self.ui.TextBoxPixel.setEnabled(True)
            self.ui.btnBrowse.setEnabled(True)
            return
        time.sleep(timeToWait)
        return
     
    progressSignal = pyqtSignal()

    @pyqtSlot()   
    def progressBar (self) :
        self.ui.progressBar.setValue(self.progressBarValue)           

   
            
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    app.exec_()

if __name__ == "__main__":
    main()