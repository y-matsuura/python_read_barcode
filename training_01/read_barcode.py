from pyzbar.pyzbar import decode
import cv2

# 読み取るバーコードを設定
sample_barcode = cv2.imread('sample_barcode.jpeg')

data = decode(sample_barcode)

print(data[0][0].decode('utf-8', 'ignore'))
