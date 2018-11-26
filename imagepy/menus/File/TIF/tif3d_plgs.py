from skimage.io import imread, imsave
import skimage.external.tifffile as tiffile
from imagepy.core.util import fileio
from imagepy import IPy
import os

class Save(fileio.Writer):
	title = 'TIF 3D Save'
	filt = ['TIF']
	note = ['8-bit', 'rgb', 'stack']

	#process
	def run(self, ips, imgs, para = None):
		imsave(para['path'], imgs)

class Open(fileio.Reader):
	title = 'TIF 3D Open'
	filt = ['TIF']

	#process
	def run(self, para = None):
		imgs = imread(para['path']).transpose(2,0,1)
		fp, fn = os.path.split(para['path'])
		fn, fe = os.path.splitext(fn) 
		IPy.show_img(imgs, fn)

class tifffile_Open(fileio.Reader):
	title = "Open with Tifffile"
	filt = ['TIF', 'tif']

	#process
	def run(self, para = None):
		imgs = tiffile.imread(para['path'])
		fp, fn = os.path.split(para['path'])
		fn, fe = os.path.splitext(fn)
		IPy.show_img(imgs, fn)

plgs = [Open, Save, tifffile_Open]