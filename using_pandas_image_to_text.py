import cv2
import pandas as pd

# وارد کردن تصویر
image = cv2.imread('D:\pythonInternship\project1\img\Capture241.jpg')

# تبدیل آرایه NumPy به داده‌چاره pandas
df = pd.DataFrame(image)

# نمایش داده‌چاره در پایچارم
print(df.head())