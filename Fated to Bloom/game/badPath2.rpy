label badPath2:
    me" \"Uh sorry, my aunt wants me home right away.\""
    me"\"Gotta go!\""
 
    
    scene neighbourhood
    with fade
    me"*Huff, huff*.... Man I could've sworn he was following me."
    play two "<loop 7.00>car driving.ogg" #Car Driving sound effect (cut and edited): https://www.youtube.com/watch?v=N_5MMzx5rOs
    
    "{i}*Car approaching in the distance behind*{/i}"
    "My speed walk turned into a paranoid jog."
    me"What a creepy teacher, he's probably not married."
    "{i}*Car speeds up*{/i}"
    
    me"I better get home quickly."
    "I noticed the sound of a car getting louder and louder."
    me"That car sounds pretty close behind me."
    "I turn around to look behind me and-"
    scene black with fade
    play two "<from 16.80>car driving full.ogg" #Car Driving sound effect (cut and edited): https://www.youtube.com/watch?v=N_5MMzx5rOs
    scene car
    me"\"SHI--\""
    with hpunch
    with vpunch
    
    show nightroad2 
    "I quickly jumped over on the side of the road, {w} {p} just barely avoiding the van from behind."
    "I hit my head hard on the sidewalk, and everything was a bit unfocused."
    stop two 
    scene nightroad car gone
    play two "car driving.ogg" #Car Driving sound effect (cut and edited): https://www.youtube.com/watch?v=N_5MMzx5rOs
    "When I got up, the van had already driven away."
    me"That was waaaay too close."
    stop two
    stop one fadeout 3.0
        
    menu:                       #Jump back to main script
       "Head Home":
           jump home 

label headHome:
    play sound "choiceEffect3.ogg"
    scene bedroom night with fade
    play music "Gothic Music - Forbidden Lullaby.ogg" fadein 1.0 # Gothic Music - Forbidden Lullaby: https://www.youtube.com/watch?v=RQmVl-A55vc
    me"\"Huh, looks like no one's home. {w} Thankfully.\""
    "At last, a little time to myself."
    
    scene comp news
    "I turn on my computer to see a video of the local news talking about the recent murders going on north of the city."
    "I click on the video, but I'm sure the police will catch them soon. I have nothing to worry about."
    
    news"{i} \"This just in: There has been a report of a missing person south of the city.\" {/i}"
    
    me"...I guess I'm wrong."
    news"{i} \" ...used a special chemical that put's his victims to sleep. Forensics found it to have a slightly sweet smell....\" {/i}"
    
    me"Whatever, it's probably not that big of a deal."
    
    news"{i} \" ...found a piece of grey cloth that seemed to have ripped off his clothing when he escaped. Last known image of the killer was from a security footage outside of a gas station.\" {/i}"
    
    "They showed a low quiality image of the man oustide a gas station at night."
    
    news"{i} \" ... he is visible wearing a grey jumpsuit.\" {/i}"
    
    me"\"A grey jumpsuit? Huh...\""
    
    if seenGrey:
        me"\"Wasn't that guy also wearing a grey jumpsuit...?\""
        me"\"I'll talk to Ryu about this tomorrow...\""
    elif interrogate:
        me"\"Takano was acting weird about a grey jumpsuit in the storage room earlier..."
        me"\"I'll talk to Ryu about this tomorrow...\""
    else:
        me"\"Where have I seen that before...\""
        "I couldn't quite put my finger on it. Nonetheless, people will definitely be talking about this at school tomorrow."
    scene bedroom night with fade
    me"*Yawn* \"Might as well go to bed before they get home\""
    stop music fadeout 1.0
    scene black with fade
    jump missingPrez    ## JUMP TO MAIN SCRIPT

label onRoof2:
    # TALK TO RYU ABOUT THE JUMPSUIT
    scene black with wiperight
    scene roof with wiperight
    show ryu with dissolve
    ryu"\"Ugh finally, I'm {b}starving{/b}\"" 
    "He takes out two paper lunch bags and hands one to me, then takes a big bite out of his sandwich."
    show ryu happy at bounce
    ryu" *Chewing* \"So you wanted to tell me something earlier?\""
    me"\"Last night, they were talking about that serial killer on the news and they showed an image of him wearing a grey jumpsuit.\""
    show ryu flat
    ryu"\"Hmm........... Ok so? I'm sure a lot of people wear jumpsuits. {w} {p} Like garbage collectors.\""
    
    if seenGrey:
       me"\"I'm not sure, but I've seen the jumpsuit before.\""
       me"\"When walked home the other night, I almost got hit by a white va-\""
       show ryu angry at bounce
        
       ryu"\"YOU WHAT?!\""
            
       me"\"Anyways, when I got to my neightbourhood there was a white van parked on the side of the road, and I think the driver was wearing it.\""
       
       show ryu flat 
       ryu"\"It might not be the same one. Don't think too much about it. Just be more careful next time you idiot!\""
       me"Yeah yeah, whatever."
       
    elif interrogate:
        me"\"Remember how I told you I saw something odd in the storage room yesterday? The thing Takano was acting weird about?\""
        ryu"\"Yeah? What of it?\""
        me"\"It was a grey jumpsuit.\""
        show ryu normal at bounce
        ryu"\"So what? It might not be the same one. Don't think too much about it, it probably meant nothing.\""
        show ryu flat
        me"\"Yeah, alright...\""

    show ryu happy
    ryu"\"C'mon, let's just get the rest of the day over with.\""
    me"\"Yeah, let's go.\""
    
label endOfDay2:
    scene black with fade
    scene lockers with fade
    "{i}End of the day{/i}"
    show ryu flat with dissolve
    ryu" *Sigh* \"Well I gotta run, my mom's pretty mad about me getting detention, {w} {i}again{/i}.\""
    me"\"Yeah, see you tomorrow.\""
    hide ryu with easeoutleft
    scene hallway with fade
    "{i} End of the day{/i}"
    "I made my way down the hall, took a right and passed the storage room towards the exit."
    "As I passed it I heard some objects being pushed around {w} {p} and then a voice muttering something."
    me"\"I wonder what's going on in there?\""
    
    ##OPTION TO INVESTIGATE STORAGE 
    
    menu:
        "Go check it out":
            jump investigateStorage     # JUMPS TO INVESTIGATE STORAGE in file SAFE PATH1
            $chemical = True
            
            
        "It's probably just the janitors":
          jump stay    # STAY ON PATH
          
label stay:
    play sound "choiceEffect3.ogg"
    me"\"It's probably nothing, besides, I'm not allowed in there.\""
    
    scene black with wipeleft
    scene livingroom night with wipeleft
    
    stop one fadeout 1.0
    me"\"*YAWN* What a long day.\""
    me"\"I hope they find our classmate soon.\""
    
    jump day4 ## JUMP TO DAY 3 IN MAIN SCRIPT
   
    
label ryuDoesntKnow:    ## RYU DOES NOT KNOW ABOUT HIKARI AND THE CHEMICALS
    if chemical:
        play sound "choiceEffect3.ogg"
    me"\"Well that doesn't make sense...\""
    me"\"Although, I did hear someone in there last night... Maybe he thought that was you?\""
    
    show ryu normal
    ryu"*SIGH*\"I don't see how he could have mistaken me for it, but I don't really have proof to say I didn't...\""
    show ryu cry at down
    me"\"Yeah, I guess you'll just have to accept it.\""
    
    scene black with wiperight
    scene lockers with wiperight
    "{i} End of the day{/i}"
    show ryu flat with dissolve
    ryu"\"Well I better get going then, UGH.\""
    me"\"Yeah, I don't think your mom will be too happy about this.\""
    
    show ryu happy at bounce
    ryu"\"Definitely not! She's gonna kill me when I get home!\""
    me"\"Haha don't worry, I'll come to your funeral.\""
    
    show ryu
    ryu"\"Gee, thanks man.\""
    ryu"\"Cya later!\""
    me"\"Yeah, see ya.\""
    
    hide ryu with easeoutleft
    
    "I walked by our lockers as I made my way out."
    stop one fadeout 1.0
    me"Wait a minute, he left his locker open."
    "I went to close it for him."
    me"AND he left his notebook in here, that idiot."
    me"I better give this to him."
    menu:
        "Go find Ryu":
            jump pointsCalcTakano
    
    
    
