import os
import sys
import qdarkstyle
from PyQt5.QtCore import QThread, QPersistentModelIndex, pyqtSignal
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QFileDialog,
    QMainWindow,
    QSlider,
    QMessageBox,
    QPushButton,
)
from ui import UiMainWindow
from compress import open_image, save_image
from utils import map_processes

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
        self.destination_img_path = BASE_PATH
        self.destination_button.clicked.connect(self.set_destination_path)
        self.destination_path.setText(self.get_parent_current_dir(BASE_PATH))
        # remove button
        self.file_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.remove_button.clicked.connect(self.remove_selected_img)
        # download button
        self.download_button.clicked.connect(self.download)
        # cancel button
        self.cancel_button.clicked.connect(self.close)
        # download imgs filepaths
        self.total_imgs = {}

    def display_img_quality_box(self):
        self.img_quality_box.setText(str(self.img_quality_slider.value()))

    def adj_img_quality_slider(self):
        self.img_quality_slider.setValue(int(self.get_text(self.img_quality_box)))

    def set_source_path(self):
        upload_type = self.source_type_popup()
        if upload_type == "file":
            source_file_path = QFileDialog.getOpenFileNames(
                self,
                "Open file",
                BASE_PATH,
                ("JPEG (*.jpg;*.jpeg;*.jpeg2000;*.JPG;*.JPEG);;GIF (*.gif;*.GIF);;PNG (*.png;*.PNG);;TIF (*.tif;*.tiff);;BMP (*.bmp)"),
            )
            file_path = self.get_img_from_file(source_file_path)
        else:
            source_folder_path = QFileDialog.getExistingDirectory(
                self, "Open folder", BASE_PATH
            )
            file_path = self.get_img_from_folder(source_folder_path)

        for img in file_path:
            # NOTE: using truncated img path as key can affect scalability in future
            # self.total_imgs is the download dtype ref
            self.total_imgs[self.get_parent_current_dir(img)] = img
        self.set_img_list_widget()

    def source_type_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Upload Type")
        msg.setText("Are you uploading a file or folder?")
        msg.addButton(QPushButton("File"), QMessageBox.YesRole)
        msg.addButton(QPushButton("Folder"), QMessageBox.YesRole)
        # TODO: enable closing feature on window close button
        upload_type_bool = msg.exec_()
        if not upload_type_bool:
            return "file"
        return "folder"

    def get_img_from_file(self, file_path):
        file_path, _ = file_path
        if not file_path:
            return []

        parent_folder_first_file = os.path.split(file_path[0])[0]
        self.source_path.setText(self.get_parent_current_dir(parent_folder_first_file))

        return file_path

    def get_img_from_folder(self, folder_path):
        acceptable_img_ext = (
            ".jpg",
            ".jpeg",
            ".jpeg2000",
            ".gif",
            ".png",
            ".PNG",
            ".tif",
            ".tiff",
            ".bmp",
        )
        if not folder_path:
            return []
        file_path = [
            os.path.join(folder_path, item)
            for item in os.listdir(folder_path)
            if not item.startswith(".")
        ]
        file_path = [
            os.path.join(folder_path, item)
            for item in file_path
            if os.path.splitext(item)[1].lower() in acceptable_img_ext
        ]

        return file_path

    def set_img_list_widget(self):
        file_path_dirs = [
            key for key, value in self.total_imgs.items()
        ]
        self.file_list.clear()
        self.file_list.addItems(file_path_dirs)

    def set_destination_path(self):
        self.destination_img_path = QFileDialog.getExistingDirectory(
            self, "Open folder", BASE_PATH
        )
        if not self.destination_img_path:
            self.destination_img_path = BASE_PATH

        self.destination_path.setText(
            self.get_parent_current_dir(self.destination_img_path)
        )

    def download(self):
        self.parallel_compress(tuple(value for key, value in self.total_imgs.items()))

    def parallel_compress(self, img_path_iter):
        destination_path_iter = [self.destination_img_path for i in img_path_iter]
        img_quality_vals = [self.img_quality_slider.value() for i in img_path_iter]
        args = zip(img_path_iter, destination_path_iter, img_quality_vals)
        compressed_img = map_processes(compress_img, args)

    def remove_selected_img(self):
        selected_img = self.file_list.selectedItems()
        if not selected_img:
            return
        for img in selected_img:
            self.file_list.takeItem(self.file_list.row(img))
            self.total_imgs.pop(self.get_text(img), None)

    @staticmethod
    def get_text(item):
        """Get text of cell value, if empty return empty str."""
        try:
            item = item.text()
            return item
        except AttributeError:
            item = ""
            return item

    @staticmethod
    def get_parent_current_dir(current_path):
        """Get current and parent directory as str."""
        parent_dir, current_dir = os.path.split(current_path)
        parent_dir = os.path.split(parent_dir)[1]  # get tail of parent_dir
        parent_current_dir = f"../{parent_dir}/{current_dir}"

        return parent_current_dir


def compress_img(args):
    source_img_path, destination_image_path, img_quality_val = args
    source_img_name = os.path.split(source_img_path)[1]
    img = open_image(source_img_path)
    if not img:
        print("whoops, bad image.")
    else:
        full_destination_image_path = os.path.join(
            destination_image_path, source_img_name
        )
        save_image(img, full_destination_image_path, img_quality_val)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainPage()
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    widget.show()
    sys.exit(app.exec_())
