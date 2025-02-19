from controller import Robot
from controller import Keyboard
from controller import DistanceSensor
import random

robot = Robot()
keyboard = Keyboard()

timestep = 64


wheel1 = robot.getDevice("wheel1")
wheel1.setPosition(float('inf'))
wheel1.setVelocity(0.0)

wheel2 = robot.getDevice("wheel2")
wheel2.setPosition(float('inf'))
wheel2.setVelocity(0.0)

wheel3 = robot.getDevice("wheel3")
wheel3.setPosition(float('inf'))
wheel3.setVelocity(0.0)

wheel4 = robot.getDevice("wheel4")
wheel4.setPosition(float('inf'))
wheel4.setVelocity(0.0)

ds_left = robot.getDevice("ds_left")
ds_right= robot.getDevice("ds_right")

ds_left.enable(timestep)
ds_right.enable(timestep)

speed = 4
number_of_turns = 0

keyboard.enable(timestep)
random_direction = 0

prev_key = 0
key_pressed = -1

autoMode = True

while (robot.step(timestep) != -1):
    prev_key = key_pressed
    key_pressed = keyboard.getKey()
    print(key_pressed)

    #  automode is key 'q'
    if(prev_key == -1  and  key_pressed == 81):
        autoMode = not autoMode

    
    if(autoMode):      
        ds_left_value = ds_left.getValue()
        ds_right_value = ds_right.getValue()
        
        if(ds_left_value<1000 or ds_right_value<1000):
            number_of_turns = 8
          
        if(number_of_turns == 0):
            random_direction = random.choice([0,1])
         
        if(number_of_turns > 0):
            number_of_turns = number_of_turns - 1
            if(random_direction == 0):
                wheel1.setVelocity(-speed)
                wheel2.setVelocity(speed)
                wheel3.setVelocity(-speed)
                wheel4.setVelocity(speed)
            elif(random_direction == 1):
                wheel1.setVelocity(speed)
                wheel2.setVelocity(-speed)
                wheel3.setVelocity(speed)
                wheel4.setVelocity(-speed)
        else:
            wheel1.setVelocity(speed)
            wheel2.setVelocity(speed)
            wheel3.setVelocity(speed)
            wheel4.setVelocity(speed)
         
    
    if(not autoMode):
        # 'w' for forward
        if(key_pressed == 87):
            wheel1.setVelocity(speed)
            wheel2.setVelocity(speed)
            wheel3.setVelocity(speed)
            wheel4.setVelocity(speed)
        # 'a' for left    
        if(key_pressed == 65):
            wheel1.setVelocity(-speed)
            wheel2.setVelocity(speed)
            wheel3.setVelocity(-speed)
            wheel4.setVelocity(speed)
        # 's' for backward
        if(key_pressed == 83):
            wheel1.setVelocity(-speed)
            wheel2.setVelocity(-speed)
            wheel3.setVelocity(-speed)
            wheel4.setVelocity(-speed)
        # 'd' for right
        if(key_pressed == 68):
            wheel1.setVelocity(speed)
            wheel2.setVelocity(-speed)
            wheel3.setVelocity(speed)
            wheel4.setVelocity(-speed)
        
        # if no key is pressed   
        if(key_pressed == -1):
            wheel1.setVelocity(0)
            wheel2.setVelocity(0)
            wheel3.setVelocity(0)
            wheel4.setVelocity(0)
        
            
        
