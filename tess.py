from PIL import Image
import pytesseract
from googletrans import Translator
# 指定Tesseract可执行文件的路径（如果它不在系统路径中）
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 打开图像文件
image = Image.open('file-page1.jpg')

# 使用Tesseract进行光学字符识别
text = pytesseract.image_to_string(image)

# 打印识别出的文本
print(text)
translator = Translator()

#
# # 将英文文本翻译成中文
translated_text = translator.translate(text, src='en', dest='zh-CN')
print(type(translated_text))
