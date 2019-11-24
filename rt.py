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
  '''Brings an image to r theta domain in the biggest possible circe it can'''
  h, w, c = image.shape
  ret     = np.zeros((min(w, h), min(w, h), c)) 
  r, th   = 0, 0
  x, y    = 0, 0
  for th in range(min(w, h)):
    # find radius scalers for x and y
    xs, ys = math.cos(2*math.pi*th/min(w, h)), math.sin(2*math.pi*th/min(w, h))
    for r in range(min(w, h)):
      # find corresponding x & y coords to r & th coords
      # x = r*cos(th); y = r*sin(th)
      x, y = (r/2)*xs + w/2, (r/2)*ys + h/2
      ret[th, r] = image[int(y)-1, int(x) - 1]
  return ret

def fromradial(image):
  '''Brings an image back from r theta domain keeping the biggest possible circle'''
  h, w, c = image.shape
  ret     = np.zeros((min(w, h), min(w, h), c))
  x, y    = 0, 0
  r, th   = 0, 0
  for x in range(min(w, h)):
    for y in range(min(w, h)):
      # find corresponding r, theta for x, y
      # r = sqrt(x^2 + y^2); th = atan(y/x)
      r, th = math.sqrt(sqr(x - w/2) + sqr(h/2 - y)), min(w, h)*math.atan2(h/2 - y, x - w/2)/(2*math.pi)
      if(r < min(w, h)/2):
        # we can only resample if we are in the largest circle
        ret[min(w, h)-y-1, x] = image[int(th), int(r)*2]

  return ret
