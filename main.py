import pytesseract
import pre_process
import post_process
import find_block_text
import argparse
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.OMP_THREAD_LIMIT=2 #thread num

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to image that will be processed by OCR / tesseract")
ap.add_argument("-pre", "--preprocess", type=str, default="True", help="preprocessing method that is applied to the image")
ap.add_argument("-post", "--postprocess", type=str, default="False", help="postprocessing method that is applied to the image")
ap.add_argument("-fbl", "--findblocktext", type=str, default="False", help="find_block_text method that is applied to the image")
ap.add_argument("-m", "--model", type=str, default="vie_best", help="model tesseract")


args = vars(ap.parse_args())
model_lang= args["model"]
file_name= args["image"]
if args["preprocess"] == "True":
    img = pre_process.process_image_for_ocr(file_name)
else :
    img = cv2.imread(file_name)

Text=pytesseract.image_to_string(img, lang=model_lang)
loi_sai=dict()

if args["postprocess"] == "True":
    Text=post_process.post_process(Text)
    loi_sai=post_process.check_cta(Text)

print(Text)
if bool(loi_sai) :
    print(u'Các từ sai là: \n')
    for key,value in loi_sai.items():
        print(u'Từ số' + str(key)+ ':' + value+' \n')
        