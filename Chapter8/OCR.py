import easyocr

reader = easyocr.Reader(['ja'], gpu=False)
reader = easyocr.Reader(['ja'])
result = reader.readtext('index.png')
