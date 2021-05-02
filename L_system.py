from processing import *


class LSystem:
  def __init__(self, axiom = 'F', length = 10.0):
    self.rules = [
      ('F', 'FF+F+F+F+F+F-F')  # this transforms F into the sequence on the right
      # FF+[+F--G+F]-[-F+F--F]
    ]
    self.current = axiom             # start with the "axiom"
    self.generation = 0              # we're at generation 0
    self.printSentence()

    # for drawing of the currnet sentence
    self.length = length             # the length of each segment
    self.angle = 90                  # the angle to go left or right

  def generate(self):
    print('Calculating...')
    next = ''
    for char in self.current:
      rule_matched = False
      for rule in self.rules:
        if rule[0] == char:          # if we find the character in one of our rules:
          next += rule[1]            # apply its replacement to next
          rule_matched = True
          break
      if not rule_matched:           # if we don't:
          next += char               # keep the character as is in next
    self.current = next
    self.generation += 1
    self.printSentence()

  def printSentence(self):
    print('Generation ' + str(self.generation) + ': ' + self.current)

  def draw(self, startX, startY):
    pushMatrix()
    translate(startX, startY)
    for char in self.current:          # go through each characters in the current sentence:
      if char == 'F':                  # F ... draw a line and move forward
        stroke(random(0, 255), random(0, 255), random(0, 255))
        line(0, 0, 0, -self.length)
        translate(0, -self.length)
      elif char == 'G':                # G ... move forward (currently unused)
        fill(255, 0, 11)
        ellipse(0, 0, self.length, self.length)
        translate(0, -self.length)
      elif char == '+':                # + ... turn right
        rotate(radians(self.angle))
      elif char == '-':                # - ... turn left
        rotate(radians(-self.angle))
      elif char == '[':                # [ ... store current location
        pushMatrix()
      elif char == ']':                # ] ... restore previous location
        popMatrix()
    popMatrix()
    # Note: this is just one possible set of drawing commands, you can add
    # or modify those rules according to your liking.


lsystem = None
pMousePressed = False


def setup():
  global lsystem
  size(1200, 800)
  lsystem = LSystem('F', height/3.0)

def draw():
  global pMousePressed

  background(0)

  lsystem.draw(300, 400)

  if mousePressed and not pMousePressed:
    lsystem.generate()     # new generation
    lsystem.length *= 0.5  # shorten the length of the segments
  pMousePressed = mousePressed


run()
