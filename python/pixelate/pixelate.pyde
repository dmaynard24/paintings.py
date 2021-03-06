import os
from datetime import date

root_dir = os.path.abspath(os.path.dirname(__file__))
# source image. swap this out.
file_name = 'tokyo'
saved_frames_path = 'frames/' + str(file_name) + '/' + str(date.today())
img = loadImage(root_dir + '\\assets\\img\\' + str(file_name) + '.jpg')
extent = 1
width = int(img.width / extent) * extent
height = int(img.height / extent) * extent

x = y = 0


def setup():
  size(width, height)  # set size to the size of your source image
  noStroke()
  frameRate(240)

  # instant
  for x in range(0, width, extent):
    for y in range(0, height, extent):
      get_local_popular_color(x, y)


def get_local_popular_color(start_x, start_y):
  color_counts = {}
  most_popular_color = None
  most_popular_color_count = 0
  for x in range(start_x, start_x + extent):
    # if x >= width:
    #   break
    for y in range(start_y, start_y + extent):
      # if y >= height:
      #   break
      node_color = img.get(x, y)
      if color_counts.get(node_color) is not None:
        color_counts[node_color] += 1
        if color_counts.get(node_color) > most_popular_color_count:
          most_popular_color = node_color
          most_popular_color_count = color_counts.get(node_color)
      else:
        color_counts[node_color] = 1

  # no two colors were the same
  if most_popular_color == None:
    most_popular_color = img.get(int(start_x + extent / 2),
                                 int(start_y + extent / 2))

  fill(most_popular_color)
  square(start_x, start_y, extent)


def draw():
  global x, y

  # get_local_popular_color(x, y)

  # if x >= width and y >= height:
  #   # done
  #   saveFrame(saved_frames_path + '/final.jpg')
  #   noLoop()
  # else:
  #   if x < width:
  #     x += extent
  #   else:
  #     x = 0
  #     y += extent


def mouseClicked():
  saveFrame(saved_frames_path + '/frame-' + str(frameCount) + '.jpg')