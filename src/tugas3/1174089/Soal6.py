# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 22:42:58 2019

@author: ADVENT
"""

import shapefile # Meng-import library shapefile
sf = shapefile.Reader("No10") # untuk membaca file dari nama filenya tanpa ekstensi
anu=sf.shapes() # untuk Menyimpan hasil yang dibaca kedalam variable anu
anu[0].shapeType # untuk Melihat shapetype didalam array object anu yang pertama 