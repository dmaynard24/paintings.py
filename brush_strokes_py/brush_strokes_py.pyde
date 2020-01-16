# source image. swap this out.
img = loadImage("C:\\repos\\processing\\brush_strokes_py\\assets\\img\\tokyo.jpg")
width = img.width
height = img.height

x1 = y1 = x2 = y2 = x3 = y3 = x4 = y4 = 0

col = None
max_stroke_length = 32
bristle_thickness = 3
stroke_width = 8
bristle_count = 6

counter = 0

visited_coords = {}
for x in range(1, width + 1):
  for y in range(1, height + 1):
    visited_coords[str(x) + ',' + str(y)] = False

def setup():  
  size(width, height) # set size to the size of your source image
  background(255)
  init_new_stroke()

def init_new_stroke():
  global x1, y1, x2, y2, x3, y3, x4, y4, visited_coords, col

  # select random start point for new brushstroke
  x1 = int(random(width))
  y1 = int(random(height))

  while visited_coords.get(str(x1) + ',' + str(y1)) == True:
    x1 = int(random(width))
    y1 = int(random(height))

  # get color of brushstroke for that location
  global col
  col = img.get(x1, y1)
  
  # offset bezier points by some small amount
  s_length = abs(randomGaussian() * max_stroke_length)
  x2 = x1 + random(-s_length, s_length)
  y2 = y1 + random(-s_length, s_length)
  x3 = x1 + random(-s_length, s_length)
  y3 = y1 + random(-s_length, s_length)
  x4 = x1 + random(-s_length, s_length)
  y4 = y1 + random(-s_length, s_length)

  # mark coord as visited
  visited_coords[str(x1) + ',' + str(y1)] = True

def draw():
  global col, bristle_thickness, x1, y1, x2, y2, x3, y3, x4, y4, counter

  if col is not None and False in visited_coords.values():
    noFill()
    stroke(col, 64) # add alpha for painterly look
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
