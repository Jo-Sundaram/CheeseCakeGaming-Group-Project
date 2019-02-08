
# Function to make character slide off screen to the right
transform slideawayright:
     linear 1.0  xalign 2.0 
     
 # Function to make character slide off screen to the left
transform slideawayleft:
    linear 1.0 xalign -1.0 
     
# Function to make character slide to the center
transform slidecenter:
        linear 0.5 xalign 0.5
        
 # Function to make character bounce       
transform bounce:
    #xalign 0.5 yalign 1.0
    linear 0.1 yalign -0.5
    linear 0.1 yalign 1.0
  
 # Function to make character slide down a bit
transform down:
    linear 0.3 yalign 2.5
    
transform up:
    yalign 2.5
    linear 0.3 yalign 0.5
