from setuptools import setup, find_packages
import os

VERSION = '0.0.1'
DESCRIPTION = 'A live updating environment for visualisations via Matplotlib.'
LONG_DESCRIPTION = 'A package that allows a Matplotlib plot to be run directly from a file and then adjusts changes made in the code directly without having to restart the animation.'

# Setting up
setup(
    name="mpl_updater",
    version=VERSION,
    author="Ogo Bogo",
    author_email="<ogobogo5@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['matplotlib'],
    keywords=['python', 'graphing', 'matplotlib', 'environment'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
