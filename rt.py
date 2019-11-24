#
#
#
#

import cv2 as cv
import numpy as np
import math

def sqr(x):
  return x * x

def toradial(image):
  h, w, c = image.shape
  ret     = np.zeros((min(w, h), min(w, h), c)) 
  r, th   = 0, 0
  x, y    = 0, 0
  for th in range(min(w, h)):
    xs, ys = math.cos(2*math.pi*th/min(w, h)), math.sin(2*math.pi*th/min(w, h))
    for r in range(min(w, h)):
      x, y = (r/2)*xs + w/2, (r/2)*ys + h/2
      ret[th, r] = image[int(y)-1, int(x) - 1]
  return ret

def fromradial(image):
  h, w, c = image.shape
  ret     = np.zeros((min(w, h), min(w, h), c))
  x, y    = 0, 0
  r, th   = 0, 0
  for x in range(min(w, h)):
    for y in range(min(w, h)):
      r, th = math.sqrt(sqr(x - w/2) + sqr(h/2 - y)), min(w, h)*math.atan2(h/2 - y, x - w/2)/(2*math.pi)
      if(r < min(w, h)/2):
        ret[min(w, h)-y-1, x] = image[int(th), int(r)*2]

  return ret
  

image = cv.imread('rerereretext.jpg')
cv.imwrite('unrerereretext.jpg', toradial(toradial(toradial(image))))
