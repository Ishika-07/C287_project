from controller import Robot
from controller import Keyboard
from controller import DistanceSensor
from controller import Camera

robot = Robot()
keyboard = Keyboard()

automode = False
timestep=64
key_pressed = 0
prev_key = 0

wheel1=robot.getDevice("wheel1")
wheel1.setPosition(float('inf'))
wheel1.setVelocity(0.0)

wheel2=robot.getDevice("wheel2")
wheel2.setPosition(float('inf'))
wheel2.setVelocity(0.0)

wheel3=robot.getDevice("wheel3")
wheel3.setPosition(float('inf'))
wheel3.setVelocity(0.0)

wheel4=robot.getDevice("wheel4")
wheel4.setPosition(float('inf'))
wheel4.setVelocity(0.0)

speed=4

ds1 = robot.getDevice("ds1")
ds1.enable(timestep)
ds2 = robot.getDevice("ds2")
ds2.enable(timestep)

cam = robot.getDevice("camera")

no_of_turns = 0
img_num = 1
 
keyboard.enable(timestep)
cam.enable(timestep)

while (robot.step(timestep) !=-1):
    prev_key = key_pressed
    key_pressed= keyboard.getKey()
    print(key_pressed)
    
    if(prev_key == -1 and key_pressed == 83):
        cam.getImage()
        pic_name = "img"+str(img_num)+".png"
        cam.saveImage(pic_name, 50)
        img_num+=1
        
    
    if(key_pressed == 65 and prev_key == -1):
        automode = not automode
    
    if(automode):
        ds1_value = ds1.getValue()
        ds2_value = ds2.getValue()
        
        if(ds1_value < 1000 or ds2_value < 1000):
            no_of_turns = 8
        if(no_of_turns > 0):
            wheel1.setVelocity(-speed)
            wheel2.setVelocity(speed)
            wheel3.setVelocity(-speed)
            wheel4.setVelocity(speed)
        else:
            wheel1.setVelocity(speed)
            wheel2.setVelocity(speed)
            wheel3.setVelocity(speed)
            wheel4.setVelocity(speed)
            
    if(not automode):
  
        # front movement - press up arrow key
        if(key_pressed== 315):
            wheel1.setVelocity(speed)
            wheel2.setVelocity(speed)
            wheel3.setVelocity(speed)
            wheel4.setVelocity(speed)
            
        # back movement - press down arrow key   
        if(key_pressed== 317):
            wheel1.setVelocity(-speed)
            wheel2.setVelocity(-speed)
            wheel3.setVelocity(-speed)
            wheel4.setVelocity(-speed)
        
        # left movement - press left arrow key      
        if(key_pressed== 314):
            wheel1.setVelocity(-speed)
            wheel2.setVelocity(speed)
            wheel3.setVelocity(-speed)
            wheel4.setVelocity(speed)
        
        # right movement - press right arrow key     
        if(key_pressed== 316):
            wheel1.setVelocity(speed)
            wheel2.setVelocity(-speed)
            wheel3.setVelocity(speed)
            wheel4.setVelocity(-speed)
        
        # if no key is pressed   
        if(key_pressed== -1):
            wheel1.setVelocity(0)
            wheel2.setVelocity(0)
            wheel3.setVelocity(0)
            wheel4.setVelocity(0)