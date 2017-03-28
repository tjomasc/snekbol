Installation
============

snekBOL supports Python 3 (tested on python 3.4+). It is almost pure python so should work on any
OS that supports the libxml2 and libxlst libraries (required for lxml). It has been tested on
MacOS and Linux; Windows may or may not be supported, I havn't tested it.

Using pip
---------

snekBOL can easily be installed from PyPi using pip. You must ensure that libxml2 and libxslt are
install first otherwise it won't install.

``pip install snekbol``

Using setup.py
--------------

If you require the latest development version you can download from Github and install manually.
Again, like with pip you will need to have libxml2 and libxslt installed first.

1. Get the code from github `git clone https://github.com/tjomas/snekbol`
2. Change to the directory and install using `python setup.py install`
