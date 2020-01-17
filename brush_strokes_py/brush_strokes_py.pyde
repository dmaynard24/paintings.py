# source image. swap this out.
img = loadImage("C:\\repos\\processing\\brush_strokes_py\\assets\\img\\tokyo-paint.jpg")
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

color_counts = {}
most_popular_color = None
most_popular_color_count = 0;
unvisited_nodes = []
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

def setup():  
  size(width, height) # set size to the size of your source image
  background(most_popular_color)
  init_new_stroke()

def init_new_stroke():
  global x1, y1, x2, y2, x3, y3, x4, y4, unvisited_nodes, col

  # select random start point for new brushstroke
  random_node_index = int(random(1, len(unvisited_nodes)))
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
  try:
    del unvisited_nodes[random_node_index - width]
  except:
    print('error: ' + str(random_node_index - width) + ' out of range')
  try:
    del unvisited_nodes[random_node_index - 1]
  except:
    print('error: ' + str(random_node_index - 1) + ' out of range')
  del unvisited_nodes[random_node_index]
  try:
    del unvisited_nodes[random_node_index + 1]
  except:
    print('error: ' + str(random_node_index + 1) + ' out of range ' + str(len(unvisited_nodes)))
  try:
    del unvisited_nodes[random_node_index + width]
  except:
    print('error: ' + str(random_node_index + width) + ' out of range ' + str(len(unvisited_nodes)))


def draw():
  global col, bristle_thickness, x1, y1, x2, y2, x3, y3, x4, y4, counter

  if col is not None and len(unvisited_nodes) > 0:
    print(len(unvisited_nodes))
    noFill()
    stroke(col, 66) # add alpha for painterly look
    col = mutate_color(col) #slightly mutate the color of each bristle
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
    print('done!')
    noLoop()

def mutate_color(c):
  mr = 10 # mutation rate
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
