import os
import sys

from PIL import Image
from PyQt5 import QtWidgets
from UI import resize

class Resize_init(resize.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(Resize_init, self).__init__()
        self.setupUi(self)
        self.out_dir.clicked.connect(lambda: self.out_dir_field.setText(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")))
        self.save_dir.clicked.connect(lambda: self.save_dir_field.setText(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")))
        self.pushButton.clicked.connect(lambda: resize(self, self.out_dir_field.text(), self.save_dir_field.text(), self.resize.text(), self.comboBox.currentText()))
        self.comboBox.addItems(["NEAREST", "BILINEAR", "BICUBIC", "LANCZOS"])
def resize(self, mydir, savedir, percent_resize, method):
    if mydir != "" and savedir != "" and percent_resize != "":
        for path, subdirs, files in os.walk(mydir):
            for name in files:
                if name.endswith(".tga") or name.endswith(".png"):
                    img = Image.open(os.path.join(path, name))
                    width = img.size[0] * int(percent_resize) / 100
                    height = img.size[1] * int(percent_resize) / 100
                    width = int(width / 4) * 4
                    height = int(height / 4) * 4
                    if width >= 4 and height >= 4:
                        if method == 'NEAREST':
                            img = img.resize((width, height), Image.NEAREST)
                        elif method == 'BILINEAR':
                            img = img.resize((width, height), Image.BILINEAR)
                        elif method == 'BICUBIC':
                            img = img.resize((width, height), Image.BICUBIC)
                        elif method == 'LANCZOS':
                            img = img.resize((width, height), Image.LANCZOS)

                        newpath = path.replace(mydir, savedir)

                        if not os.path.isdir(newpath):
                            os.makedirs(newpath)
                            img.save(os.path.join(newpath, name))
                        else:
                            img.save(os.path.join(newpath, name))
                    elif width < 4 or height < 4:
                        with open(os.path.abspath(os.path.curdir) + '/problemFiles.txt', 'a') as errorFileNames:
                            errorFileNames.write(name + "\n")

        self.statusBar.showMessage("Complete!")
    else:
        self.statusBar.showMessage("Fields must not be empty!")

if __name__=='__main__':
    qapp = QtWidgets.QApplication(sys.argv)
    res = Resize_init()
    res.show()
    qapp.exec_()