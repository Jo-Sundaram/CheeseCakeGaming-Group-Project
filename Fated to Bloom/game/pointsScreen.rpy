screen points:
    text"[points]"
    
#####################
###HIKARI ENDINGS###
####################

label pointsCalcHikari:
    play sound "choiceEffect3.ogg"
    ####################################
    ## If you saw the jumpsuit in the first night ##
    ####################################
    if seenGrey: 
        if points == 4.5:
            ## MC and Ryu know about everything, leads to good ending
            jump hikariBestEnding
            
        elif points == 4:
            if ryuknows:
                ## Ryu and MC knows about the Jumpsuit , the jumpsuit smell and the chemical smell, leads to second good ending
                jump hikariEnding2
            
            elif not tellRyu:
                if points > 2  and points < 4:
                    ## MC knows about everything but Ryu does not know about the chemicals, leads to 8th ending
                        jump hikariEnding7
            
            
        elif points == 3:
            ## Ryu and MC knows about the Jumpsuit  and the chemical, leads to 3rd ending
            jump hikariEnding3
            
        elif  points == 1.5:
            #Ryu and MC knows the Jumpsuit
            jump hikariEnding8
            
     #######################################   
    ##  If you didn't see the jumpsuit the first night ##
    #######################################
    else:
        if points == 3:
            ## Ryu and MC knows about the interrogation , the jumpsuit smell and the chemical smell, leads to second good ending
            jump hikariEnding2
            
        elif  points == 1.5:
            if tellRyu:
                ## MC and Ryu know about the chemicals only
                jump hikariEnding5
            else:
                if points == 2.5 or points == 1.5:
                    ## MC knows some stuffs, Ryu does not know about the chemical
                    jump hikariEnding8
                    
        elif points == 2:
            ## Ryu and MC knows about the Jumpsuit OR Interrogation, and the chemical 
            jump hikariEnding3
         
            
            
            
           
######################
###TAKANO ENDINGS###
######################

label pointsCalcTakano:
    play sound "choiceEffect3.ogg"
    ####################################
    ## If you saw the jumpsuit in the first night ##
    ####################################    
    if seenGrey:
        if ryuknows:
            if points == 4.5 or points == 4:
            
                ## MC and Ryu know about everything or mostly everything, leads to good ending
                jump takanoBestEnding
                
        else:
            if points > 2 and points < 4.5:
                     ## MC knows about everything but Ryu does not know about the chemicals, leads to 8th ending
                jump takanoEnding8
            
            
        if points == 3:
            ## Ryu and MC knows about the Jumpsuit  and the chemical, leads to 3rd ending
            jump takanoEnding3
            
        elif  points == 1.5:
            #Ryu and MC knows the Jumpsuit
            jump takanoEnding8
            
            
    #######################################   
    ##  If you didn't see the jumpsuit the first night ##
    #######################################
    else:
        if points == 3:
            ## Ryu and MC knows about the interrogation , the jumpsuit smell and the chemical smell, leads to second good ending
            jump takanoBestEnding
            
        elif  points == 1.5:
            if tellRyu:
                ## MC and Ryu know about the chemicals only
                jump takanoEnding5
            else:
                if points == 2.5 or points == 1.5:
                    ## MC knows some stuffs, Ryu does not know about the chemical
                    jump takanoEnding8
                    
        elif points == 2:
            ## Ryu and MC knows about the Jumpsuit OR Interrogation, and the chemical 
            jump takanoEnding3
        
        elif points == 1:
            ## MC knows about the chemical only
            jump takanoEnding8
            
        elif points == 0.5 or points == 0:
            jump takanoEnding6
