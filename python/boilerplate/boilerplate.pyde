import os
from datetime import date

root_dir = os.path.abspath(os.path.dirname(__file__))
# source image. swap this out.
file_name = 'tokyo'
img = loadImage(root_dir + '\\assets\\img\\' + str(file_name) + '.jpg')
width = img.width
height = img.height

x = y = 1


def setup():
  size(width, height)  # set size to the size of your source image
  frameRate(240)


def draw():
  global x, y

  node_color = img.get(x, y)
  stroke(node_color)
  point(x, y)

  if x == width and y == height:
    # done
    saveFrame('final.jpg')
    noLoop()
  else:
    if x < width:
      x += 1
    else:
      x = 1
      y += 1


def mouseClicked():
  saveFrame('frames/' + str(file_name) + '/' + str(date.today()) + '/frame-' +
            str(frameCount) + '.jpg')
