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
    imgoptimize.run()

|

The application below will appear.

.. image:: https://i.imgur.com/60QRJUB.png


Operating the application
-------------------------
There are several features - view figure below for visual aid:

1) Sourcing your images.
    - If you click "Source", you're given the option to either upload one or more image files (JPEG or PNG) or select a folder with your images.
        - If you select a folder, only JPEG and PNG images will be uploaded.

2) Working with images.
    - Valid images will populate the viewport. You can remove images from this viewport by selecting one or more items and selecting "Remove".

3) Setting image quality percentage.
    - You can set the image quality percentage by either moving the slider under the "Image quality:" label, or manually entering an image quality percentage value between 1 and 100.

4) Setting destination path.
    - Click "Destination" and select a folder to store your images.

5) Downloading your images.
    - Click "Download" when you are ready to download your images.

6) Exiting the application.
    - Simply click "Cancel" to exit the application.

View video demo `here <https://i.imgur.com/y2zJ4Bc.mp4>`__.

|

.. image:: https://i.imgur.com/MVDkxXF.png

Support
-------
If you find any bug or would like to propose a new feature, please use the `issues tracker <https://github.com/irahorecka/img-optimize/issues>`__. I'll be happy to help!
