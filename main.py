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

hunger = 100

alive = True

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
    
def tamagotchi_face_sadder():
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
    B, F, F, F, F, F, F, B,
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
    
def tamagotchi_face_dead():
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

while alive == True:
  hunger = hunger - 5
  
  for event in s.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":
      
      # Feeding (UP)
      if event.direction == "up" and hunger > 275:
        foreground= (255,0,255)
        s.set_pixels(tamagotchi_face_sad())
        hunger = hunger + 25
      if event.direction == "up" and hunger < 276:
        foreground= (0,255,0)
        s.set_pixels(tamagotchi_face_happy())
        hunger = hunger + 50
      
      
      
      # Hurting (DOWN)
      elif event.direction == "down" and hunger > -50:
        foreground= (0,0,255)
        s.set_pixels(tamagotchi_face_sad())
        hunger = hunger - 10
      elif event.direction == "down" and hunger < -49:
        foreground= (255,255,255)
        s.set_pixels(tamagotchi_face_sadder())
        hunger = hunger - 10
      
      # Piss off (LEFT)
      elif event.direction == "left": 
        foreground= (255,0,0)
        s.set_pixels(tamagotchi_face_angry())
        
      # Kill (RIGHT)
      elif event.direction == "right":
        foreground= (255,255,255)
        s.set_pixels(tamagotchi_face_dead())
      
      time.sleep(1)
  
  change_random_color()
  if hunger > 0 and hunger < 300:
      foreground= (red,green,blue)
      s.set_pixels(tamagotchi_face())
  elif hunger > 299 and hunger < 400:
      foreground= (0,255,0)
      s.set_pixels(tamagotchi_face_sad())
  elif hunger > 399 and hunger < 500:
      foreground= (255,0,255)
      s.set_pixels(tamagotchi_face_sadder())
  elif hunger < 1 and hunger > -50:
      foreground= (0,0,255)
      s.set_pixels(tamagotchi_face_sad())
  elif hunger < 49 and hunger > -100:
      foreground= (255,255,255)
      s.set_pixels(tamagotchi_face_sadder())
  elif hunger < -99 or hunger > 499:
      foreground= (255,255,255)
      s.set_pixels(tamagotchi_face_dead())
      alive = False
  time.sleep(1)