import os
from datetime import date

root_dir = os.path.abspath(os.path.dirname(__file__))
# source image. swap this out.
file_name = 'tokyo'
img = loadImage(root_dir + '\\assets\\img\\' + str(file_name) + '.jpg')
width = img.width
height = img.height

x = y = 1

node_colors = {}


def setup():
  size(width, height)  # set size to the size of your source image
  frameRate(240)

  color_counts = {}
  most_popular_color = None
  most_popular_color_count = 0
  for x in range(1, width + 1):
    for y in range(1, height + 1):
      node_color = img.get(x, y)
      node_colors[str(x) + ',' + str(y)] = node_color
      if color_counts.get(node_color) is not None:
        color_counts[node_color] += 1
        if color_counts.get(node_color) > most_popular_color_count:
          most_popular_color = node_color
          most_popular_color_count = color_counts.get(node_color)
      else:
        color_counts[node_color] = 1
  background(most_popular_color)


def draw():
  global x, y

  node_color = node_colors.get(str(x) + ',' + str(y))
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
