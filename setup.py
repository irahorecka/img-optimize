"""Setup for img-optimize package."""

import setuptools


with open("README.rst") as f:
    README = f.read()

setuptools.setup(
    author="Ira Horecka",
    author_email="ira89@icloud.com",
    name="img-optimize",
    license="MIT",
    description="A python library and GUI application to optimize image files.",
    version="v0.1.4",
    long_description=README,
    long_description_content_type="text/x-rst",
    url="https://github.com/irahorecka/img-optimize",
    packages=["imgoptimize"],
    python_requires=">=3.6",
    install_requires=["PyQt5", "QDarkStyle", "Pillow"],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ],
)
