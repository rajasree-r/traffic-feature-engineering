# -*- coding: utf-8 -*-
"""unzipper.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zs8AqFoEihKoUZ-9dfI55oCm-bPhEJOT
"""

import zipfile


def unzip_file(zip_path, extract_path):

    zip_ref = zipfile.ZipFile(zip_path, 'r')
    zip_ref.extractall(extract_path)
    zip_ref.close()

