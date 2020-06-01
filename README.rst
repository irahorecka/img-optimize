img-optimize
================

A python library and GUI application to optimize image files.

License: `MIT <https://en.wikipedia.org/wiki/MIT_License>`__.

Installation
------------

::

    pip install img-optimize

Running the program
-------------------

::

    import imgoptimize

|

The application below will appear.

.. image:: https://i.imgur.com/60QRJUB.png


Operating the application
-------------------------
There are several notable features - view figure below for visual aid:

1) Sourcing your images.
    - If you click "Source", you are given the option to either upload one or more image files (JPEG or PNG) or selecting a folder containing your images.
        - If you select an image folder, only JPEG and PNG images will be uploaded.

2) Working with images.
    - Valid images will populate the viewport. You are able to remove images from this viewport by selecting an image (or more) and clicking "Remove"

3) Setting image quality percentage.
    - You can set the image quality percentage by either moving the slider under the "Image quality:" label, or manually entering the image quality value between 1 and 100.

4) Setting destination path.
    - Click "Destination" and select a folder to store your images.

5) Downloading your images.
    - Click "Download" when you are ready to download your images.

6) Exiting the application.
    - Simply click "Cancel" to exit the application.

|

.. image:: https://i.imgur.com/MVDkxXF.png

Support
-------
If you find any bug or would like to propose a new feature, please use the `issues tracker <https://github.com/irahorecka/img-optimize/issues>`__. I'll be happy to help!