import os
from datetime import date

root_dir = os.path.abspath(os.path.dirname(__file__))
# source image. swap this out.
file_name = 'singapore'
saved_frames_path = 'frames/' + str(file_name) + '/' + str(date.today())
img = loadImage(root_dir + '\\assets\\img\\' + str(file_name) + '.jpg')
width = img.width
height = img.height

diameter = int(random(12, 24))
radius = diameter / 2

unvisited_nodes = []


def setup():
  size(width, height)  # set size to the size of your source image
  frameRate(240)

  color_counts = {}
  most_popular_color = None
  most_popular_color_count = 0
  for x in range(1, width + 1):
    for y in range(1, height + 1):
      node_color = img.get(x, y)
      unvisited_nodes.append({'coords': [x, y], 'color': node_color})
      if color_counts.get(node_color) is not None:
        color_counts[node_color] += 1
        if color_counts.get(node_color) > most_popular_color_count:
          most_popular_color = node_color
          most_popular_color_count = color_counts.get(node_color)
      else:
        color_counts[node_color] = 1
  background(most_popular_color)


def draw():
  global img, diameter, radius

  smooth()

  # select random start point for new brushstroke
  random_node_index = int(random(len(unvisited_nodes)))
  random_node = unvisited_nodes[random_node_index]
  x, y = random_node['coords']

  # get color of brushstroke for that location
  col = random_node['color']
  noStroke()

  # draw an ellipse at that location with that color
  fill(col, 100)
  diameter = int(random(12, 24))
  radius = diameter / 2
  ellipse(x, y, diameter, diameter)

  # mark node (and surrounding nodes) as 'visited'
  pop_node_at_index(random_node_index)
  # for _ in range(radius):
  #   pop_node_at_index(random_node_index)


def pop_node_at_index(i):
  if i > -1 and i < len(unvisited_nodes):
    # fill(255, 255, 0)
    # x, y = unvisited_nodes[str(i)]
    # ellipse(x, y, 1, 1)
    unvisited_nodes.pop(i)
  else:
    print('attempted to pop: ' + str(i) + ' out of range')


def mouseClicked():
  saveFrame(saved_frames_path + '/frame-' + str(frameCount) + '.jpg')
