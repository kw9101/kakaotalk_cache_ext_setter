# -*- coding: cp949 -*-

import os
import shutil 

def _get_filepath_list_pair(_target_dir) :
	target_dir = os.path.normpath(_target_dir) # remove trailing separator.
	for (path, dir, files) in os.walk(target_dir):
		for fname in files:
			fullfname = path + "\\" + fname

			if path == "":
				continue

			if os.path.isdir(fullfname):
				continue
			fSize = os.path.getsize(fullfname)

			if fSize < 50 * 1024:
				continue

			if os.path.splitext(fullfname)[1] == '':
				src = ""
				dest = ""
				if fSize < 1024 * 1024:
					os.rename (fullfname, fullfname + ".jpg")
					src = fullfname +".jpg"
					dest = fname + ".jpg"

					#shutil.move(fullfname + ".jpg", fname + ".jpg")
				else:
					os.rename (fullfname, fullfname + ".3gp")
					src = fullfname +".3gp"
					dest = fname + ".3gp"
					#shutil.move(fullfname + ".3gp", fname + ".3gp")
				shutil.move(src, dest)

_get_filepath_list_pair('.')