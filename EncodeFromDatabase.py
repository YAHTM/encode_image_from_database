
import numpy as np
import cv2 # opencv
import insightface
from insightface.app import FaceAnalysis

# buffalo_l model
app_l = FaceAnalysis(name='buffalo_l',
                     root='insightface_model',
                     providers=['CPUExecutionProvider']) 
# ['CUDAExecutionProvider', 'CPUExecutionProvider']

app_l.prepare(ctx_id=0, det_size=(640,640))


# load buffalo sc model
app_sc = FaceAnalysis(name='buffalo_sc',
                      root='insightface_model')
# providers=['CPUExecutionProvider']
app_sc.prepare(ctx_id=0, det_size=(640,640))


# lead image from database
import mysql.connector
import cv2
import urllib

# اطلاعات مربوط به اتصال
host = "himalayas.liara.cloud"
port = 30290
username = "root"
password = "XSYrbTJ2bjpDtg5lE8liZTpx"
database = "admiring_varahamihira"

# ایجاد اتصال
connection = mysql.connector.connect(
    host=host,
    port=port,
    user=username,
    password=password,
    database=database,
)

# بررسی صحت اتصال
if connection.is_connected():
    print("اتصال به پایگاه داده با موفقیت انجام شد!")
else:
    print("خطا در اتصال به پایگاه داده")

#### ایجاد cursor
cursor = connection.cursor()

# اجرای کوئری
query = "SELECT face FROM NewPerson WHERE id = 23"
cursor.execute(query)

# دریافت نتیجه
result = cursor.fetchone()

# بستن cursor و اتصال
cursor.close()
connection.close()

# ذخیره آدرس در متغیر
link = result[0]

# چاپ آدرس
print(link)


response = urllib.request.urlopen(f"{link}")
image = cv2.imdecode(np.frombuffer(response.read(), dtype=np.uint8), cv2.IMREAD_COLOR)
# risize image to 500*500
new_image = cv2.resize(image, (1000, 1000))
cv2.imshow("Image", new_image)
cv2.waitKey(0)
cv2.destroyAllWindows

# results_l is encodes from image
results_l = app_l.get(new_image)

print(results_l)


