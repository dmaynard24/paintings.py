import os
from datetime import date

root_dir = os.path.abspath(os.path.dirname(__file__))
# source image. swap this out.
file_name = 'beach'
img = loadImage(root_dir + '\\assets\\img\\' + str(file_name) + '.jpg')
width = img.width
height = img.height
area = width * height

x1 = y1 = x2 = y2 = x3 = y3 = x4 = y4 = 0

col = None
max_stroke_length = 12
bristle_thickness = 2
stroke_width = 6
bristle_count = 6

counter = 0

unvisited_nodes = []


def setup():
  size(width, height)  # set size to the size of your source image
  frameRate(240)

  color_counts = {}
  most_popular_color = None
  most_popular_color_count = 0
  for x in range(1, width + 1):
    for y in range(1, height + 1):
      unvisited_nodes.append([x, y])
      node_color = img.get(x, y)
      if color_counts.get(node_color) is not None:
        color_counts[node_color] += 1
        if color_counts.get(node_color) > most_popular_color_count:
          most_popular_color = node_color
          most_popular_color_count = color_counts.get(node_color)
      else:
        color_counts[node_color] = 1
  background(most_popular_color)

  init_new_stroke()


def init_new_stroke():
  global x1, y1, x2, y2, x3, y3, x4, y4, unvisited_nodes, col

  # select random start point for new brushstroke
  random_node_index = int(random(len(unvisited_nodes)))
  x1, y1 = unvisited_nodes[random_node_index]

  # get color of brushstroke for that location
  col = img.get(x1, y1)

  # offset bezier points by some small amount
  s_length = abs(randomGaussian() * max_stroke_length)
  x2 = x1 + random(-s_length, s_length)
  y2 = y1 + random(-s_length, s_length)
  x3 = x1 + random(-s_length, s_length)
  y3 = y1 + random(-s_length, s_length)
  x4 = x1 + random(-s_length, s_length)
  y4 = y1 + random(-s_length, s_length)

  # mark node (and surrounding nodes) as 'visited'
  if random_node_index - width > -1:
    unvisited_nodes.pop(random_node_index - width)
  else:
    print('attempted to pop: ' + str(random_node_index - width) +
          ' out of range')
  if random_node_index - 1 > -1:
    unvisited_nodes.pop(random_node_index - 1)
  else:
    print('attempted to pop: ' + str(random_node_index - 1) + ' out of range')
  if random_node_index > -1 and random_node_index < len(unvisited_nodes):
    unvisited_nodes.pop(random_node_index)
  else:
    print('attempted to pop: ' + str(random_node_index) + ' out of range')
  if random_node_index + 1 < len(unvisited_nodes):
    unvisited_nodes.pop(random_node_index + 1)
  else:
    print('attempted to pop: ' + str(random_node_index + 1) + ' out of range')
  if random_node_index + width < len(unvisited_nodes):
    unvisited_nodes.pop(random_node_index + width)
  else:
    print('attempted to pop: ' + str(random_node_index + width) +
          ' out of range')


def draw():
  global col, bristle_thickness, x1, y1, x2, y2, x3, y3, x4, y4, counter

  if col is not None and len(unvisited_nodes) > 0:
    if len(unvisited_nodes) < area / 2:
      saveFrame('middle.jpg')
    noFill()
    stroke(col, 66)  # add alpha for painterly look
    col = mutate_color(col)  #slightly mutate the color of each bristle
    bristle_thickness = random(1, 4)
    strokeWeight(bristle_thickness)
    bezier(x1, y1, x2, y2, x3, y3, x4, y4)

    # random walk bezier points
    x1 += random(-stroke_width, stroke_width)
    y1 += random(-stroke_width, stroke_width)
    x2 += random(-stroke_width, stroke_width)
    y2 += random(-stroke_width, stroke_width)
    x3 += random(-stroke_width, stroke_width)
    y3 += random(-stroke_width, stroke_width)
    x4 += random(-stroke_width, stroke_width)
    y4 += random(-stroke_width, stroke_width)

    # after so many bristles, reset brushstroke
    counter += 1
    if counter % bristle_count == 0:
      init_new_stroke()
  else:
    # done
    saveFrame('final.jpg')
    noLoop()


def mutate_color(c):
  mr = 10  # mutation rate
  r = red(c)
  g = green(c)
  b = blue(c)

  r += random(-mr, mr)
  r = constrain(r, 0, 255)
  g += random(-mr, mr)
  g = constrain(g, 0, 255)
  b += random(-mr, mr)
  b = constrain(b, 0, 255)

  return color(r, g, b)


def mouseClicked():
  saveFrame('frames/' + str(file_name) + '/' + str(date.today()) + '/frame-' +
            str(frameCount) + '.jpg')
