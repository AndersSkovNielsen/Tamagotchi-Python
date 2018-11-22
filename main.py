from sense_hat import SenseHat
import time
import random

s = SenseHat()
#s.low_light = True

red = 0
blue = 0
green = 255;
foreground = (red, green, blue)
background = (0, 0, 0)
minimum = -20
maximum = 20

def change_random_color():
    global red
    global green
    global blue
    color_number = random.randint(1,3) # random number between 1 and 3
    if color_number == 1: red = clamp(red + random.randint(minimum, maximum), 0, 255)
    elif color_number == 2: green = clamp(green + random.randint(minimum, maximum), 0, 255)
    else: blue = clamp(blue + random.randint(minimum, maximum), 0, 255)

def clamp(n, smallest, largest): return max(smallest, min(n, largest))

def tamagotchi_face():
    B = background
    F = foreground
    image = [ 
    B, B, B, B, B, B, B, B,
    B, B, F, B, B, F, B, B,
    B, B, F, B, B, F, B, B,
    B, B, B, B, B, B, B, B,
    B, F, B, B, B, B, F, B,
    B, F, B, B, B, B, F, B,
    B, B, F, F, F, F, B, B,
    B, B, B, B, B, B, B, B,
    ]
    return image
    
def tamagotchi_face_sad():
    B = background
    F = foreground
    image = [ 
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, F, F, B, B, F, F, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, F, F, F, F, B, B,
    B, F, B, B, B, B, F, B,
    B, B, B, B, B, B, B, B,
    ]
    return image
    
def tamagotchi_face_happy():
    B = background
    F = foreground
    image = [ 
    B, B, B, B, B, B, B, B,
    B, B, F, B, B, F, B, B,
    B, F, B, F, F, B, F, B,
    B, B, B, B, B, B, B, B,
    B, F, F, F, F, F, F, B,
    B, F, B, B, B, B, F, B,
    B, B, F, F, F, F, B, B,
    B, B, B, B, B, B, B, B,
    ]
    return image
    
def tamagotchi_face_angry():
    B = background
    F = foreground
    image = [ 
    B, B, B, B, B, B, B, B,
    B, F, B, B, B, B, F, B,
    B, B, F, B, B, F, B, B,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    B, B, F, F, F, F, B, B,
    B, F, F, F, F, F, F, B,
    B, B, B, B, B, B, B, B,
    ]
    return image
    
def tamagotchi_face_poor():
    B = background
    F = foreground
    image = [ 
    B, B, F, F, F, F, B, B,
    B, F, B, F, F, B, F, B,
    B, F, B, F, F, B, F, B,
    B, F, F, F, F, F, F, B,
    B, B, F, F, F, F, B, B,
    B, B, F, B, B, F, B, B,
    B, B, F, B, B, F, B, B,
    B, B, F, F, F, F, B, B,
    ]
    return image

s.set_pixels(tamagotchi_face())

while True:
  for event in s.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":
      
      # Check which direction
      if event.direction == "up":
        foreground= (0,255,0)
        s.set_pixels(tamagotchi_face_happy())      # Up arrow
      elif event.direction == "down":
        foreground= (0,0,255)
        s.set_pixels(tamagotchi_face_sad())      # Down arrow
      elif event.direction == "left": 
        foreground= (255,0,0)
        s.set_pixels(tamagotchi_face_angry())      # Left arrow
      elif event.direction == "right":
        foreground= (255,255,255)
        s.set_pixels(tamagotchi_face_poor())      # Right arrow
      elif event.direction == "middle":
        s.show_letter("M")      # Enter key
      
      time.sleep(1)
  
  change_random_color()
  foreground= (red,green,blue)
  s.set_pixels(tamagotchi_face())
  time.sleep(0.05)