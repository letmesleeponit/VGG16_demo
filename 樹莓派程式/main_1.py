import os
import tensorflow
import time
from tensorflow.keras.models import load_model
from keras.preprocessing import image

### 樹梅派1 : 拍照片，接著判斷是否有貓咪出現，同時將訊號傳給另一個樹莓派

model = load_model('test.h5', compile = False)

while True:
    print('start to take a photo')
    os.system('fswebcam /dev/video0 --no-banner --no-info 150x150 -q ./img1.jpg')
    print('start to predict this feature')
    img = image.load_img('./img1.jpg',target_size=(150,150))
    img = image.img_to_array(img)
    img = img.reshape((1,) + img.shape)
    ans = round(float(model.predict(img)[0][0]))
    print(ans)
    
    if ans == 1:
        print('There have a cat')
        print('Power on')
        os.system('mosquitto_pub -h 192.168.0.13 -t test -m "There have a cat"')
        time.sleep(5)
    else:
        os.system('mosquitto_pub -h 192.168.0.13 -t test -m "No cat"')   
        time.sleep(2) 
#fswebcam /dev/video0 --no-banner -r 150x150 -q ./img1.jpg
