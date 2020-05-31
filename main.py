import os
import sys
import qdarkstyle
from PyQt5.QtCore import QThread, QPersistentModelIndex, pyqtSignal
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QTableWidgetItem,
    QSlider,
    QMessageBox,
    QPushButton
)
from ui import UiMainWindow
from compress import open_image, save_image

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


class MainPage(QMainWindow, UiMainWindow):
    """Main page of the application."""

    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.setupUi(self)
        # slider
        self.img_quality_slider.setMinimum(1)
        self.img_quality_slider.setMaximum(100)
        self.img_quality_slider.setValue(80)
        self.img_quality_slider.setTickPosition(QSlider.TicksBelow)
        self.img_quality_slider.setTickInterval(10)
        self.img_quality_slider.valueChanged.connect(self.display_img_quality_box)
        # line edit
        self.img_quality_box.setText(str(self.img_quality_slider.value()))
        self.img_quality_box.returnPressed.connect(self.adj_img_quality_slider)
        # source path
        self.source_button.clicked.connect(self.set_source_path)
        self.source_path.setText(self.get_parent_current_dir(BASE_PATH))
        # destination path
        self.destination_button.clicked.connect(self.set_destination_path)
        self.destination_path.setText(self.get_parent_current_dir(BASE_PATH))
        # download button
        self.download_button.clicked.connect(self.download)
        # cancel button
        self.cancel_button.clicked.connect(self.close)
        # download imgs filepaths
        self.total_imgs = []

    def display_img_quality_box(self):
        self.img_quality_box.setText(str(self.img_quality_slider.value()))

    def adj_img_quality_slider(self):
        self.img_quality_slider.setValue(int(self.get_cell_text(self.img_quality_box)))

    def set_source_path(self):
        upload_type = self.source_type_popup()
        if upload_type == 'file':
            source_file_path = QFileDialog.getOpenFileNames(
                self, "Open file", BASE_PATH, "JPEG (*.jpg;*.jpeg;*.jpeg2000;*.JPG;*.JPEG);;GIF (*.gif;*.GIF);;PNG (*.png;*.PNG);;TIF (*.tif;*.tiff);;BMP (*.bmp)"
            )
            file_path = self.get_img_from_file(source_file_path)
        else:
            source_folder_path = QFileDialog.getExistingDirectory(
                self, "Open folder", BASE_PATH
            )
            file_path = self.get_img_from_folder(source_folder_path)
        self.total_imgs.extend(file_path)
        # self.total_unique_imgs is the dtype to download images from...
        self.total_unique_imgs = set(self.total_imgs)
        self.set_img_list_widget()
        

    def source_type_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle('Upload Type')
        msg.setText('Are you uploading a file or folder?')
        msg.addButton(QPushButton('File'), QMessageBox.YesRole)
        msg.addButton(QPushButton('Folder'), QMessageBox.YesRole)
        # TODO: enable closing feature on window close button
        upload_type_bool = msg.exec_()
        if not upload_type_bool:
            return 'file'
        return 'folder'

    def get_img_from_file(self, file_path):
        file_path, _ = file_path
        if not file_path:
            return []
        
        parent_folder_first_file = os.path.split(file_path[0])[0]
        self.source_path.setText(self.get_parent_current_dir(parent_folder_first_file))

        return file_path

    def get_img_from_folder(self, folder_path):
        acceptable_img_ext = ('.jpg', '.jpeg', '.jpeg2000', '.gif', '.png', '.PNG', '.tif', '.tiff', '.bmp')
        if not folder_path:
            return []
        file_path = [os.path.abspath(item) for item in os.listdir(folder_path) if not item.startswith('.')]
        file_path = [os.path.abspath(item) for item in file_path if os.path.splitext(item)[1].lower() in acceptable_img_ext]

        return file_path

    def set_img_list_widget(self):
        file_path_dirs = [self.get_parent_current_dir(file) for file in list(self.total_unique_imgs)]
        self.file_list.clear()
        self.file_list.addItems(file_path_dirs)

    def set_destination_path(self):
        self.destination_img_path = QFileDialog.getExistingDirectory(
            self, "Open folder", BASE_PATH
        )
        if not self.destination_img_path:
            self.destination_img_path = BASE_PATH

        _, img_filename = os.path.split(self.source_img_path)
        self.destination_img_path = os.path.join(
            self.destination_img_path, img_filename
        )

        self.destination_path.setText(
            self.get_parent_current_dir(self.destination_img_path)
        )

    def download(self):
        img = open_image(self.source_img_path)
        if not img:
            print("whoops, bad image.")
        else:
            save_image(img, self.destination_img_path, self.img_quality_slider.value())

    @staticmethod
    def get_cell_text(cell_item):
        """Get text of cell value, if empty return empty str."""
        try:
            cell_item = cell_item.text()
            return cell_item
        except AttributeError:
            cell_item = ""
            return cell_item

    @staticmethod
    def get_parent_current_dir(current_path):
        """Get current and parent directory as str."""
        parent_dir, current_dir = os.path.split(current_path)
        parent_dir = os.path.split(parent_dir)[1]  # get tail of parent_dir
        parent_current_dir = f"../{parent_dir}/{current_dir}"

        return parent_current_dir


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainPage()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    widget.show()
    sys.exit(app.exec_())
