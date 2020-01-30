import os
from datetime import date

root_dir = os.path.abspath(os.path.dirname(__file__))
# source image. swap this out.
file_name = 'tokyo'
saved_frames_path = 'frames/' + str(file_name) + '/' + str(date.today())
img = loadImage(root_dir + '\\assets\\img\\' + str(file_name) + '.jpg')
width = img.width
height = img.height

x = y = 0


def setup():
  size(width, height)  # set size to the size of your source image
  frameRate(240)

  # instant
  # for x in range(0, width):
  #   for y in range(0, height):
  #     node_color = img.get(x, y)
  #     stroke(node_color)
  #     point(x, y)


def draw():
  global x, y

  node_color = img.get(x, y)
  stroke(node_color)
  point(x, y)

  if x == width and y == height:
    # done
    saveFrame(saved_frames_path + '/final.jpg')
    noLoop()
  else:
    if x < width:
      x += 1
    else:
      x = 0
      y += 1


def mouseClicked():
  saveFrame(saved_frames_path + '/frame-' + str(frameCount) + '.jpg')