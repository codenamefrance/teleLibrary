# Libraries to convert image to barcode
#from pyzbar.pyzbar import decode
import cv2
#from io import BytesIO

# Library to convert EAN13 code to barcode image
from barcode import EAN13
from barcode.writer import ImageWriter

DEFAULT_IMG_FORMAT = '.jpeg'
DEFAULT_ENCODING = 'utf-8'

class Barcode:
	def __init__ (self, code, id):
		self.code = str(code)
		self.id = str(id)


def readBarcodeImage(filename) -> str:
	im = cv2.imread(filename)

	#pyzbar decoding
	#res = decode(clean_im)

	bd = cv2.barcode.BarcodeDetector()
	retval, decoded_info, dec_type = bd.detectAndDecode(im)

	retval = str(retval)

	if len(retval) < 12:
		return None

	return retval
