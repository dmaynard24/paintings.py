float x1, y1, x2, y2, x3, y3, x4, y4;
color col;
int counter = 0;
float strokeWidth = 8;
float maxStrokeLength = 32;
int bristleCount = 6;
float bristleThickness = 3;

PImage img;

void setup() {  
  background(255);

  //source image. Add your own here.
  img = loadImage("C:\\Users\\dmaynard\\Google Drive\\Pictures\\smiley-dog-cropped.jpg");
  size(130, 130); // set size to the size of your source image

  initNewStroke();
}

void initNewStroke() {
  // select random start point for new brushstroke
  x1 = random(width);
  y1 = random(height);

  // get color of brushstroke for that location
  col = img.get(int(x1), int(y1));

  float sLength = abs(randomGaussian() * maxStrokeLength);

  //offset bezier points by some small amount
  x2 = x1 + random(-sLength, sLength);
  y2 = y1 + random(-sLength, sLength);
  x3 = x1 + random(-sLength, sLength);
  y3 = y1 + random(-sLength, sLength);
  x4 = x1 + random(-sLength, sLength);
  y4 = y1 + random(-sLength, sLength);
}

void draw() {

  noFill();
  stroke(col, 64); // add alpha for painterly look
  col = mutateColor(col); // slightly mutate the color of each bristle
  bristleThickness = random(1, 4);
  strokeWeight(bristleThickness);
  bezier(x1, y1, x2, y2, x3, y3, x4, y4);

  // random walk bezier points
  x1 += random(-strokeWidth, strokeWidth);
  y1 += random(-strokeWidth, strokeWidth);
  x2 += random(-strokeWidth, strokeWidth);
  y2 += random(-strokeWidth, strokeWidth);
  x3 += random(-strokeWidth, strokeWidth);
  y3 += random(-strokeWidth, strokeWidth);
  x4 += random(-strokeWidth, strokeWidth);
  y4 += random(-strokeWidth, strokeWidth);

  // after so many bristles, reset brushstroke
  counter++;
  if (counter % bristleCount == 0) {
    initNewStroke();
  }
}

color mutateColor(color c) {
  float mr = 10; // mutation rate
  float r = red(c);
  float g = green(c);
  float b = blue(c);

  r += random(-mr, mr);
  r = constrain(r, 0, 255);
  g += random(-mr, mr);
  g = constrain(g, 0, 255);
  b += random(-mr, mr);
  b = constrain(b, 0, 255);
  return color(r, g, b);
}
