import cv2

DEFAULT_IMG_FORMAT = '.jpeg'
DEFAULT_ENCODING = 'utf-8'

class Barcode:
	def __init__ (self, code, id):
		self.code = str(code)
		self.id = str(id)


def readBarcodeImage(filename) -> str:
	image = cv2.imread(filename)
	bd = cv2.barcode.BarcodeDetector()
	retval, decoded_info, dec_type = bd.detectAndDecode(image)

	retval = str(retval)

	if len(retval) < 12:
		return None
	return retval
