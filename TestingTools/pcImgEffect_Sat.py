from picamera.array import PiRGBArray
from picamera import PiCamera

import time
import cv2

ImgWidth = 640
ImgHeight = 480

camera = PiCamera(resolution=(ImgWidth, ImgHeight), framerate=30)

#camera.sharpness = 100
#camera.saturation = 100
camera.ISO = 100
camera.video_stabilization = False

camera.exposure_mode ='auto'

#camera.awb_mode = 'off'
camera.awb_mode = 'auto'
#camera.awb_mode = 'sunlight'
#camera.awb_mode = 'cloudy'
#camera.awb_mode = 'shade'
#camera.awb_mode = 'tungsten'
#camera.awb_mode = 'fluorescent'
#camera.awb_mode = 'incandescent'
#camera.awb_mode = 'flash'
#camera.awb_mode = 'horizon'

camera.image_effect = 'saturation'
#camera.image_effect = 'deinterlace1'
#camera.image_effect = 'deinterlace2'

#-------------------------------------

#camera.meter_mode = 'average'
#camera.meter_mode = 'spot'
#camera.meter_mode = 'backlit'
#camera.meter_mode = 'matrix'

rawCapture = PiRGBArray(camera, size=(ImgWidth, ImgHeight))

time.sleep(0.5)

i=1

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    #camera.capture(['image%000005d.jpg' % i])
    image = frame.array
    e1 = cv2.getTickCount()    
    
    cv2.imshow("img",image)
    cv2.imwrite("ImageEffect_Sat_%000005d.jpg" % i, image)

    e2 = cv2.getTickCount()
    t = (e1-e2/cv2.getTickFrequency())

    print t
    
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)
    
    if key == ord("q"):
        break

    i+=1
    
#camera.capture_sequence(['image%0004d.jpg' % i for i in range(10)])
