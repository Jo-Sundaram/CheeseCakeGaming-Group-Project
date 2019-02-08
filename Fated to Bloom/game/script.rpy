# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define me = Character("[name]",who_color="#C80764")
define teacher = Character("Teacher", who_color="#cc9588")
define uncle = Character("Uncle", who_color="#4fa5c6")
define aunt = Character("Aunt", who_color="#b7a2ef")
define ryu = Character("Ryu", who_color="dd4b16")
define unknown = Character("???", who_color="#b2abab")
define prez = Character("Class President", who_color="#5cf9c2")
define hikari = Character("Ms. Hikari", who_color="#cd5bea")
define takano = Character("Mr. Takano", who_color="#677570")
define news = Character("News Anchor", who_color="ff5656")
define cops = Character("Police Officer", who_color="#057e93")

# These are audio channels for layering different sounds on top of eachother
init python:
    renpy.music.register_channel("one", mixer=None, loop=None, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)
    renpy.music.register_channel("two", mixer=None, loop=None, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)

     
image hikari sinister quick:
    "hikari sinister.png"
    pause 1.0
    "hikari happy.png"
    
image logo = "cheese.png"
image warning = "warning.png"
image clueless = "clueless.png"
image credits = Movie(channel = "credits anim", play = "Fated_to_Bloom_Credits2.webm",)
image splash = Movie(channel = "splash anim", play = "start-animation.webm")
image storage2 = Movie(channel="storage anim", play="storage_animation.webm")
image nightroad2 = Movie(channel="nightroad anim", play="nightroad-animation.webm")
image passout1 = Movie(channel="passout1 anim", play = "passout-ryualive-fromchem.webm")
image passout2 = Movie(channel="fadeout anim", play = "fadeout.webm")
image fadin1= Movie(channel="fadein1 anim ", play= "fadin1.webm")
image fadin2 = Movie(channel = "fadin2 anim" , play = "fadin2.webm")
image passout3 = Movie(channel = "passout3 anim", play = "classroom-passout.webm")
image passout4 = Movie(channel ="passout4 anim", play = "dead-ryu-passout.webm")

# VARIABLES TO CALCULATE DIFFERENT ENDINGS
default late = False
default seenGrey = False
default interrogate = False 
default suit = False
default chemical = False
default points = 0
default ryuknows= False
default chooseTakano = False

label splashscreen:
    scene black
    with Pause(1)    
    show logo with fade
    with Pause(3)  
    show warning with fade
    with Pause (4)    
    show splash
    with Pause(7)
    return

# The game starts here
label start:
    stop music fadeout 1.0
    show screen points
    scene black
   
   
    # Enter your character's name
    python:
        name = renpy.input(("What's your name?"))

        name = name.strip() or __("MC")
    
    

        

    
    
#Scenes for nightmare flashback
    play music "<from 0.0 to 7.25>heartbeat.ogg" fadein 1.0
    # Heart beat sound effect:   https://www.youtube.com/watch?v=UMUZz-v077M 
   
    
    scene father
    with fade
    " {i}Father...{/i}"
    
    scene mother
    with fade
    "{i}Mother... {/i}"
 
    scene black
    with hpunch
    "\"{i}[name]! Run!{/i}\""
    
    play sound "<from 7.80>Evil Laughing Woman Sound.ogg" fadein 1.0
    with hpunch
    "\"{i}HAHAHAHAHA!!{/i}\""           #Evil laughing woman sound effect: https://www.youtube.com/watch?v=wRqc_yVhN6c
    
    stop sound fadeout 1.0
    with hpunch
    with hpunch
    "\"{i}Mom... Dad... what-!{/i}\""
    
    play music "horror-heartbeat.ogg"
    # This "Horror heartbeat" effect was made by cutting and editing this "Horror Build-Up" sound effect: https://www.youtube.com/watch?v=HLF25YeHfO8
    # And layering the previous heartbeat effect over it ( Heart beat sound effect - https://www.youtube.com/watch?v=UMUZz-v077M )
    
    scene mom death with fade
   
    scene dad death with fade
   
    scene mom death with fade
    
    scene dad death with fade
    "\"{i}No!{/i}\""
    
    scene mom death
    "\"{i}NO!!{/i}\""
    
    scene dad death
    "\"{i}NO NO NO NO NO NO NO!{/i}\""
    
    scene black
    with hpunch
    with hpunch
    with hpunch
    with hpunch
    play music "<from 25.0 to 25.80>horror-heartbeat.ogg"
    "{size=+7}\"NOOOOOOOOOOOO!\"{/size}"
    
    stop music
    scene bedroom morning
    with hpunch
    "*GASP* {w}*huff...* {w}*huff...*"
   
    # Woke up from the nightmare and understand where you are
    me"Another nightmare..."
    me"For the 4th time in a row..."
    
    scene alarm clock
    play music  "Angel Beats! OST_ School Days.ogg" fadein 3.0 #Stolen from-- I mean *borrowed* from the Angel Beats! OST - School Days:
                                                                                                # https://www.youtube.com/watch?v=pQe61SsF4dA&list=PL300ktMVZEzp9NYpErqvPBX-DxO0E4h3n&index=2
    "{i}8:20 am{/i}"
    "10 minutes before school starts..."
    me"Shoot! I better get ready."
    
    with vpunch
    uncle"{size=+10} \"[name]! Go get my newspaper!\"{/size}"
    me"\"{i}Ugh{/i} I'm coming Uncle!\""    
    menu:
        "Get dressed":
            jump getDressed
        
           
label getDressed:
    play sound "choiceEffect3.ogg"
    scene bathroom
    with fade
    me"\"Hmm...  not bad...\""
    
    with vpunch
    uncle"\"[name]! Where's my damn newspaper!?\""
    me"{i} Damn geezer...{/i} \"I'm coming!\""
    
    menu:
        "Go get the newspaper for your uncle":
            jump  livingRoom
            
label livingRoom:
    play sound "choiceEffect3.ogg"
    scene black with fade
    scene living room
    with fade
    
    show uncle1 with dissolve
    uncle"\"About time! Death would have gotten to me first if you took longer.\""
    me"{i} Ah, if only...{/i} {w} {p} \"Yes I'm sorry geez-- uh Uncle, please forgive me.\""
    show uncle1 at bounce
    uncle"\"What did you say boy?\""
    me"\"Nothing Uncle.\""
    uncle"\"Better have been nothing child. My wife and I graciously allowed you to stay with us, and it be best if you weren't disrespecting us in our own house.\""
    uncle"\"I know your parents had raised you better than that.\""
    me"\"Alright Uncle, I understand.\""
    uncle"\"Good. Now get out of my sight, I don't want to see your face any more than I have to.\""

   
    hide uncle1 with dissolve
    scene living room
    
    play sound "stomach growl.ogg"      # Stomach growl sound effect: https://www.youtube.com/watch?v=ZBKSMqEzIpE
    "{i}*stomach growls*{/i}"
    me"I should probably grab something to eat ..."
    stop sound 
    
    menu:
        "Head to the kitchen":
            jump kitchen
            
            
                        # Where your aunt denies you food
label kitchen:
    play sound "choiceEffect3.ogg"
    scene fridge
    with fade
    
    me "Let's see what we got..."
    menu:
        "Open fridge":
                jump auntdeniedfood
    
                
       
label auntdeniedfood:
    play sound "slam.ogg"   # Slam sound effect: https://www.youtube.com/watch?v=BgqsbwYLjds
    scene fridge 
    with hpunch
    "{i} *SLAM* {/i}"
    scene kitchen
    show aunt
    aunt"\"What do you think you're doing?\""
    me"\"Uh...Breakfast?\" {w} {p} {i} Please let me have a proper breakfast and not just a piece of toast like everyday...{/i}"
    
    aunt"\"HUMPH!\""
    scene toast
    aunt"\"Your breakfast has already been made.\""
    
    me"{i} *Sigh*... great...{/i}"
                        # Decide whether to eat or not
    menu:
        me"Hmm...I'm gonna be late for school, should I really eat?"
        "Eh, I'm already late anyway so might as well.":
            $ late = True
            jump eat
        
         
        "I'm gonna be late for the third time this week if I stay any longer. If I sprint for it I might make it on time.":
        
            jump noEat
        
            
          
          
label eat:
    play sound "choiceEffect3.ogg" # This sound effect was taken (cut and edited) from: 
    me "{i} *Scarfs down the bland toast*{/i} "
    scene kitchen
    show aunt
    aunt"\"Ew, how barbaric...\""
    me "{i} Says the one raising me on plain toast everyday{/i}"
    me"Alright, time to head to school. Better late than never."
    
    menu:
        "Head To School":
            jump school
    

    
label noEat:
    play sound "choiceEffect3.ogg"
    me "Better to be hungry than to get detention."
     
    menu:
        "Head to school":
            jump school 
        
 

 
# Meets up with friend in the hallway
label school:
    play sound "choiceEffect3.ogg"
    scene black with wipeleft
    scene hallway with wipeleft
    me"{i} Please be before the bell...{/i}"
    with hpunch
    unknown"\"Hey [name]! Wait up!\""
    
    me"Hmm? Someone's coming..."
    show ryu with dissolve
    ryu"\"Oh man, glad I made it in time, right?\""
    
  
    me"\"Ha! As if.\""
    me"{i}Ah, Ryunosuke Niijima, or Ryu for short, my best friend since first year of junior high. A happy-go-lucky guy that has a knack for lifting the mood without much effort.{/i}"
    # Determines whether you get detention or not
    if late:
        play sound "school bell.ogg" fadein 1.0 # School bell sound effect: https://www.youtube.com/watch?v=6Tv6gQgj0VQ
        "{i}*Bell rings*{/i}"
        show ryu normal at bounce
        ryu"\"Crap! We're gonna be late!\""
        stop sound fadeout 1.0
        menu:
           "Run to class":
            jump schoolDetention
            
           
    else:
        show ryu happy at bounce
        ryu"\"Well come on! We're gonna be late.\""
        menu:
           "Run to class":
            jump schoolNoDet
    

label schoolDetention:
    play sound "choiceEffect3.ogg"
    scene black with wiperight
    scene clock 8 40 with wiperight
    "{i}8:40 am{/i}"
    scene classroom 8 40
    teacher "\"[name]! This is the third time this week you've been late! Oh, and you've brought a friend...\""
    
    me "\"Sorry! I overslept--\""
    
    teacher "{size=+10}\"Detention for both of you, today after school!\"{/size}"
    me"{i} Dammit...{/i}"
    
    jump fourthPeriod
    
    
            
    
label schoolNoDet:
    play sound "choiceEffect3.ogg"
    scene black with wiperight
    scene classroom 8 25 with wiperight
    play sound "school bell.ogg" fadein 1.0
    "{i}*Bell rings*{/i}"
    stop sound fadeout 1.0
    teacher " \"Oh [name] and Ryu, you're just in time.\""

    play sound "stomach growl.ogg"
    "{i}*stomach growls*{/i}"
    
    jump fourthPeriod
    
    
label fourthPeriod:
    scene clock 11 20 with wipeleft
    stop music fadeout 1.0
    "{i} 11:20 am {p} Fourth Period{/i}"
    scene classroom 11 20
    with fade
    
    play sound "school bell.ogg" fadein 1.0 
    "{i}*Bell rings*{/i}"
    show ryu normal with dissolve
    stop sound 
    play music "Angel Beats! OST_ Girls Hop.ogg" fadein 3.0 # This was taken from the Angel Beats! OST_ Girls Hop: https://www.youtube.com/watch?v=8bTuNaVfNTE&list=PL300ktMVZEzp9NYpErqvPBX-DxO0E4h3n&index=3
    ryu"\"Ah crap! I forgot to do the history notes! [name], let me copy yours.\""
    me"\"What? Dude, it was like, only 3 pages. Ms. Hikari is gonna kill you when she finds out.\""
    show ryu concerned at down
    ryu"\"Yeah, well it was 3 pages too long. Just let me copy it before class starts. Come on!\""
    
    me"\"Alright, alright! Just make it quick.\""
    show ryu at bounce
    ryu"\"Thanks! You are a lifesaver!\""

    #Introduces the sweet KILLER teacher Hikari
    scene black with wipeleft
    scene clock 11 30 with wipeleft
    
    
    "{i} 11:30 am{/i}"
    "{i} Fourth period {/i}"
    scene classroom 11 30 with fade
    me"{i} Zzz... {w} Man school is so boring...{/i}"
    
    ryu"\"{size=-5}Hey [name]...{/size}\""
    
    if late:
        me"{i}Glad I ate breakfast this morning, I'm getting hungry... {w} good thing there's only 10 minutes until lunch...{/i}"
    else:
        play sound "stomach growl.ogg"
        me"*stomach growls*"
        me"{i}God I'm starving... good thing there's only 20 minutes until lunch.{/i}"

    ryu"{size=-5}\"[name]?\"{/size}"
    me"{i} ... And then only two more periods until I return to my dreaded home... {w} wait was somebody calling me?{/i}"
    
    with hpunch
    ryu"{size=+15}\"[name]!!\"{/size}"
    me"\"AH! What??\""
    ryu"\"Teacher's calling you dummy.\""
    
   
    show hikari with dissolve
     
    hikari"\"[name]... \""
    hikari"\"Dozing off again?\""
    
    "The teacher looks me dead in the eyes and her faced stretched into a wide  grin while leaning in so close that I could smell her mild perfume."
    
    #Change this line
    show hikari sinister quick
    hikari"{size=-7}\"You should have went to sleep earlier{/size}\""
    
    me"\"Uh... what?\""
    show hikari 
    hikari"\"Oh, I said you should be going to bed earlier\""
    show hikari happy at bounce
    hikari"\"Heheh~\""
    
    me"\"Uh-- Heh- Sorry about that Ms. Hikari--\""
    
    play sound "school bell.ogg" fadein 1.0
    "{i} *Bell rings* {/i}"
    stop music fadeout 2.0
    me"Ah, lunch at last"
    
    menu:
        "Head to roof":
            jump roof
                                        #Lunch time, space out over the MC's past
label roof:
    play sound "choiceEffect3.ogg"
    
    scene black with wiperight
    scene roof with wiperight
    me"Man, what was up with that teacher..."
    
    play sound "stomach growl.ogg"
    
    "{i}*stomach growls*{/i}"
    me"Urgh, never mind that."
   
    "I open my bag."
    me "Great.. I forgot my lunch...{w} again..."
    play music "sad theme.ogg" fadein 3.0   # This was taken (cut and edited) from the Made in Abyss OST - Pathway: https://www.youtube.com/watch?v=nk8COybCLuU
    me"Urghhhh"
    scene aunt2
    with fade
    me"{i} My aunt and uncle promised my parents that they would take care of me if anything happens to them...{/i}"
    me"{i} And here I am....{/i}"
    ryu"{size=-5}\"Hey [name]...\"{/size}"
    scene uncle2
    with fade
    me"{i} Being fed plain toast and leftovers, if any, while they eat like kings.{/i}"
    me"{i} So much for family...{/i}"
    ryu"{size=-5}\"Tsk, hey [name]!\"{/size}"
    scene parents flashback with fade
    me"{i}Sure my parents might have been wealthy, but that's all my uncle and aunt seem to care about.{/i}"
    scene black with fade
    me"{i} I would've been better off if --{/i}"
    
    stop music
    play sound "slam.ogg"
    with vpunch
    "{size=+10} {i}SLAP{/i} {/size}"
    
    scene roof
    show ryu flat                               #Ryu is a good boi and gives MC food
    me"\"OW! What the hell man?!\""
    
    play music "Angel Beats! OST_ School Days.ogg" fadein 3.0
    
    show ryu happy at down
    ryu" \"Heheh, sorry about that.\""
    ryu"\"You were spacing out again, {w}and from what it looked like I thought you were gonna...\""
    
    show ryu at bounce
    ryu"\"Er... nevermind heh.\""
    
    me"\"Hah, yeah...{w} I guess I have been spacing out a lot lately.\""
    
    show ryu 
    ryu"\"Um here, I could hear your stomach from the other side of class.\""
    
    "He hands me a lunch box, filled with delicious homemade food."
    "I can barely make out the word \"Thanks\" without drooling over it."
    
    me"\"Aw Ryu, you shouldn't ha--\""
    stop music fadeout 3.0
    show ryu happy
    ryu"\"Hey, I know how it is...{w} {p} ...and besides, my mom loves you anyways {w}( ...more than me sometimes.)\""
    me"{i} Well, I guess some good things came out of it after all.{/i}"
   
    play music "Deserted-Streets.ogg" fadein 1.0 # "Deserted Streets" by Eric Matyas: http://soundimage.org/dark-ominous/
    show ryu normal at bounce
    ryu"\"Anyways, Have you heard the recent stuff on the news?\""
    me"\"No? What's going on?\""
    
    ryu"\"Remember that serial killer case last year in the next city over? The one who dissapeared after a while?\""
    me"\"Oh yeah, I remember that.\""
    ryu"\"Apprently there have been a couple murders north of our city.{w}  It's pretty scary.\""
    me"\"Damn. You think it might be the same person?\""
    show ryu flat
    ryu"\"That's what the media is conspiring... {w}{p} I hope the police actually catch them this time.\""
    me"\"Yeah....\""
    me"{i} I've already had my fair share of murders...{/i}"
    stop music fadeout 1.0
    
    scene black with wipeleft
    scene classroom sixth with wipeleft
    play sound "school bell.ogg" fadein 1.0 
    "{i} *Bell rings* {/i}"
    "6th period"
    stop sound 
    
    play music "Angel Beats! OST_ Girls Hop.ogg" fadein 3.0
    me"Alright, time for sixth period. Hope I don't die of boredom..."
    teacher"\"Blah blah blah….\""
    me"Argh, nevermind that. I'm taking a nap."
   
    scene black with fade
    scene black with fade
    scene classroom end of day
    play sound "school bell.ogg" fadein 1.0
    "{i} *Final bell rings* {/i}"
    stop sound fadeout 1.0
 
    show ryu with dissolve
    ryu"\"Finally awake are you?\""
    me"\"Heh, did I miss anything important?\""
    ryu"*shrugs* \"Not much really, I'm pretty sure a few other kids fell asleep too haha.\""
                                                  #DETENTION
    if late:
        me"\"Alright, time to get detention over with.\""
        show ryu flat
        ryu"\"Aww man, I forgot about that, guess we're not leaving for a while.\""
        jump lockers
    else:
        me"\"Alright well, time to head out then.\""
       
        jump lockers
    

    
   
label lockers:
    scene black with wipeleft
    scene lockers with wipeleft
    show ryu flat with dissolve
    
    if late:
        ryu"\"Man that detention was a waste of time, they could have made us do chores or something!\""
        me"\"Hey don't give them any ideas!\""
        me"\"I personally liked napping for an hour...\""
        
        show ryu 
        ryu"\"Anyways, it's getting dark.\""
        
        show ryu happy
        ryu"\"See ya tomorrow!\""
        
        hide ryu with dissolve
        with fade
    
    else:
        ryu"\"Sorry I can't hang out after school, I got some stuff to do at home.\""
        me"\"No worries, see you tomorrow!\""
        show ryu happy at bounce
        ryu"\"See ya!\""
        hide ryu happy with easeoutleft

        #Introduces creepy GOOD teacher Takano

    stop music fadeout 1.0
    
    "We waved goodbye"
    "As I was heading out I ran into my creepy old homeroom teacher, Mr. Takano."
    
    play one "Suspense Music - Project Phoenix.ogg" fadein 1.0 # Suspense music by Project Phoenix: https://www.youtube.com/watch?v=UtRF2m5oAzI
    show takano with dissolve
    takano"\"Why, hello there [name]...\""
    
    me"\"Uh h-hello sir\""
    takano"\"Are you heading out now?\""
        
    ################################
    ########## BLOCK 1 #############
    ###############################
    menu:
        "Was he waiting for me?"
        
        "Stay and talk to him":
            jump safePath1
           
                               # IF YOU CHOOSE TO TALK TO HIM, YOU JUMP TO THE SAFE PATH (safePath1)
        "Make an excuse to leave":
            jump badPath2
                                          # IF YOU CHOOSE TO NOT TALK TO HIM, YOU JUMP TO THE BAD PATH (badPath2)
            
                        
                                          #Back home, finish the day 
label home:
    play sound "choiceEffect3.ogg"
    scene black with wiperight
    scene livingroom night with wiperight
    play music "<loop 0.900>sleep theme.ogg"   # This was taken (cut and looped) from the Made in Abyss OST - Tomorrow: https://www.youtube.com/watch?v=BeSbmS06k1k 
    
   
    me"*Sigh* Finally home..."
    me"What a weird day..."
    menu:
        "Time for bed":
            jump bedtime
            
label bedtime:
    play sound "choiceEffect3.ogg"
    scene bedroom night
    with fade
    
    me"I plop onto my bed and curl up in my blanket"
    me"Here's to hoping for no nightmares tonight..."
    me"Like I say every night...."
    
    scene black with fade
    stop music fadeout 2.0
    "ZZz {w} Zzz..."
                                                          #START OF DAY 2
    with fade
    with hpunch
    play music "Alarm Clock Sound Effect.ogg" # Alarm clock sound effect: https://www.youtube.com/watch?v=QZSMSxODaLo
    "{size=-5}*beep*{/size}"
    with vpunch
    "*beep*"
    with hpunch
    "{size=+5}*beep*{/size}"
    me"Arrgghhh...Shut uppp...."
    
    scene alarm clock 2
    "{i}7:30 am{/i}"
    with vpunch
    "{size=+10}*bee-{/size}"
    with vpunch
    play sound "slam.ogg"
    stop music
    "{size=+10}{i} *SLAM*{/i}{/size}"
    
    
    scene bedroom morning with fade
    me"*Siighhh*"
    me"Wait a minute...{w}{p} No nightmares?"
    play music "Angel Beats! OST_ Girls Hop.ogg" fadein 1.0
    me"I can't believe it...I actually slept!"
    
    menu:
        "Get ready for school":
            jump getReady
                
label getReady:
    play sound "choiceEffect3.ogg"
    scene black with fade
    scene bathroom with fade
    
    me"Heh, I actually got ready on time for once!"
    
    menu:
        "Head downstairs":
            jump livingroom
label livingroom:
    play sound "choiceEffect3.ogg"
    scene black with wiperight
    scene living room with wiperight
    show uncle1 at right 
    show aunt at left

    uncle"\"{size=+3}Hey boy!{/size} Since you're up so early go get my -!\""
    me"\"Yes uncle!\""
    with fade
    me"\"Here you go\""
    uncle"\"Wow that was fast....{w} Ehh whatever just get out of my face!\""
    
    scene black with dissolve
    scene kitchen with dissolve
    me"Better grab my toast."
    
    show aunt with easeinleft
    aunt"\"Huh, I'm glad you're finally being grateful for the breakfast I prepar--\""
    me"\"Gotta go!\""
    menu:
        aunt"\"Wha-! Don't walk away while I'm talking to you!\""
        "Run to School":
            jump schoolDay2
                                        
label schoolDay2:                       #Class President asks you to get stuff from storage
    play sound "choiceEffect3.ogg"
    scene black with fade
    scene classroom 8 with fade
    show student prez with dissolve
    show student prez at bounce
    
    prez"\"Hey [name]! You're here early today.\""
    prez"\"Since you're here, would you mind grabbing some supplies from the storage room for me?\""
    me"\"Sure, what do ya need?\""
    prez"\"Just some more chalk, pencils and paper since we're starting to run out. {w} {p} In fact, there should be a box with our class number on it.\""
    
    menu:
        me"\"Oh alright\""
        "Head to storage room":
            jump storageroom
            
label storageroom:
    play sound "choiceEffect3.ogg"
    play music "Angel Beats! OST_ Today is Ok.ogg" fadein 1.0# This was taken from the Angel Beats! OST_ Today is Ok:  https://www.youtube.com/watch?v=K-fCDDdtsiA&index=5&list=PL300ktMVZEzp9NYpErqvPBX-DxO0E4h3n
    scene black with wiperight 
    scene storage room trash with wiperight
                                        #You go to storage and find something unnerving
    me"{i}Jeez there's a bunch of boxes in here{/i}"
    me"{i}It's as if no one's cleaned this place out in years{/i}"
    me"{i}Hmmm... paper... pencils...{/i}"
    me"{i}...? Even the trash is overflowing! {/i}"
    
    scene trash
    
    if seenGrey:                        #IF you saw the grey jumpsuit or not
        jump heKnows
        
    else:
       jump doesntKnow
        
label heKnows:
        
    me"Huh? what is that?"
    me"Is that... a jumpsuit?"
    "I kneel down to inspect it"
    me"No...I've seen this before..."
    "I was about to pick it up from the bin when-"
    
    play sound "slam.ogg"
    stop music
    with hpunch
    "{size=+10}{i}*SLAM*{i}{/size}"             #Takano catches you snooping around
    
    jump Takano
    
label doesntKnow:
    me"What in the world? Where did this come from?"
    me"It doesn't look like any school uniform..."
    me"It's a jumpsuit"
    "I was about to pick it up from the bin to inspect it when - "
    play sound "slam.ogg"
    stop music
    with hpunch
    "{size=+10}{i}*SLAM*{i}{/size}"  
    jump Takano
  
label Takano:
    
   scene storage room trash
   show takano
   me"\"AH!\""
   takano"\"Hmmmm? what do we have here?\""
   "I quickly drop the jumpsuit back in the bin"
   me"\"Oh uh... I was sent by our class president to get some supplies\""
   me"\"Wh...Why are you here?\""
   
   "He walks in slowly with a creepy smile."
   
   takano"\"I wonder... why am I here?\""
   
   me"{i} Oh no... Did he catch me snooping around?{/i}"

   show takano upset at bounce
   takano"\"OH yes, that's right... {w} {p} I came here because I saw you walk in... without a teacher.\""
   me"\"Oh. Uh, well the class prez gave me a list of things to get from here so..."
   
   takano"\"Yes well, you shouldn't be in here without a teacher.\""
   me"{i} Is that even a rule?{/i}"
   
   play music "Deserted-Streets.ogg" fadein 3.0
   takano"\"Now hurry along now. {w}Shoo!\""
   
   me"{i} He's acting strangely suspicious...{/i}"
   me"\"Why in a hurry? Is there something you need? {w} {i}Plus I still haven't got my supplies.{/i}\""
   "He glares at me."
   show takano happy at bounce
   takano"\" ... No. I have nothing to hide, now shouldn't you grab your supplies and get going?\""
   show takano
   "He put on his creepy smile again and gestures towards the door."
   ################################
   ########## BLOCK 2 #############
   ###############################
   menu:                        # INTERROGATION 
           me"{i} Something's not right here...{/i}"
       
           "Interrogate him":
               
               $interrogate = True
               
               jump interrogate
              
           "Leave him be":
              play sound "choiceEffect3.ogg"
              me"{i} He seems pretty mad.{/i}"
              jump leaveStorage
                    
              
label interrogate:  #Interrogate him
    play sound "choiceEffect3.ogg"
    if seenGrey:
       $points +=1              # Points based on previous choices
    else:
       $points += 0.5
       
    me"Doing this will probably get me killed but…"
    me"\"Excuse me for being frank, but why are you getting so defensive, Mr.Takano? Are you hiding something? Is it in this room perhaps?\""
    takano"\"I've said it before, I have no reason to hide anything.\""
    me"\"Then why are you trying to rush me out of this room?\""
    me"{i}Could this have something to do with the jumpsuit?{/i}"
    show takano upset
    takano"\"N-No reason...Just getting you back to class! Yes, now grab your supplies and hurry along!\""
    "He gives a large, creepy grin and slides the door open just a crack."
    show takano at bounce
    takano"\"Now get back to class, unless you want to get in trouble...hehehehe\""
    "I quickly grabbed our class box and gave him a look of bewilderment as I slowly take a step towards the door."
    me"\"...Ok then.\""
    
    "He slams the door behind me."
    scene hallway
    me"What the hell...?"
    me"Ugh whatever, I  better head back anyways."
    
    menu:
        "Head back to class":
            jump returnclass
            
            
label leaveStorage:     #Leave him be
    if seenGrey:
        $points += 0.5
    else:
        $points += 0
        
    "I blink to myself and assume for the best. {w} {p} (He’s probably just doing his job, considering I'm not usually allowed to be here and he’s always been kinda weird.)"
    me"\"Right.. I was just about to leave, don't worry about me.\""
    takano"\"Yes, yes, child. Now run along.\""
    "I quickly grabbed our class box and shuffled towards the door."
    "He slams the door behind me as I stepped out of the room."
    scene hallway
    me"What the hell...?"
    me"Ugh whatever, I  better head back anyways."
    stop music fadeout 1.0
    menu:
        "Head back to class":
            jump returnclass
            
label returnclass:              #Talk to class president and Ryu
    play sound "choiceEffect3.ogg"
    play music "Angel Beats! OST_ Today is Ok.ogg" fadein 1.0
    scene black with wipeleft
    scene classroom 8 25 with wipeleft
    show student prez with dissolve
    prez"\"Oh [name],  you're back!\""
    me"\"Yeah,  here are the supplies you asked for.\""
    prez"\"Thank you, I appreciate your cooperation, but uh... \""
    show student prez smirk at bounce
    prez"\"If I may ask, why are you sweating profusely? Surely the box wasn’t {i}that{/i} heavy.\""
    "I wipe my brow and realize he was right, it was like I just ran 5 miles or something."
    me"{i} How embarrassing...{/i}"
    me"\"Uh yeah no.... {w} {p} I just had a run in with Mr. Takano.\""
    show student prez concern at bounce
    prez"\"Oh man, That's never a good sign.\""
    prez"\"He's always been a  bit...err... how should I say this...\""
    show student prez
    prez"\"Downright creepy. {w} {p} Anyways, thanks for grabbing the supplies!\""
    
    me"\"Haha, anytime\""
    hide student prez with dissolve
    show ryu with dissolve 
    ryu"\"Hey man, you got here early!\""
    me"\"Yeah, I was grabbing some supplies from the storage room and ran into Takano.\""
    show ryu concerned at down
    ryu"\"Ooooh yikes.... what happened?\""
    ####################################################
    #### IF / ELSE BLOCK: SeenGrey and Interrogation #########
    ###################################################
    if interrogate and seenGrey:
        me"\"I saw something odd, but familiar in there and he caught me snooping around...\""
        me"\"Then he started rushing me to get out cuz apparently I'm not allowed in storage without a teacher.\""
        
        show ryu normal at bounce
        ryu"\"Huh? I don't think that's even a rule...\""
        
        me"\"Yeah, and when I asked him why the hurry he started acting weird and suspicious.\""
        me"\"I think he was hiding something there...\""
        
        show ryu flat
        ryu"\"Hmmm... You know...\""
        ryu"\"I think you might be on to something.\""
        
        me"\"You really think so?\""
        ryu"\"I never trusted that teacher, there was always something up with him.\""
        
        show ryu normal
        ryu"\"I wonder what he would hide in there anyway.....\""
        show ryu flat
        me"\"Who knows?\""
        
        
    elif interrogate:
        me"\"I saw something odd, but familiar in there and he caught me snooping around...\""
        me"\"Then he started rushing me to get out cuz apparently I'm not allowed in storage without a teacher.\""
        
        show ryu normal at bounce
        ryu"\"Huh? I don't think that's even a rule...\""
        
        me"\"Yeah, and when I asked him why the hurry he started acting weird and suspicious.\""

        ryu"\"Hmm, I wonder why he would be so defensive of the storage room?....\""
        show ryu flat
        me"\"Who knows?\""

    elif seenGrey:
        me"\"I saw something  odd, but familiar in there and he caught me snooping around...{w}{p} then he started rushing me to get out cuz apparently I'm not allowed in storage without a teacher.\""
        show ryu normal at bounce
        ryu"\"Huh? I don't think that's even a rule...\""
        me"Yeah, well I didn't think much of it. He was being really creepy and I wanted out.\""
        show ryu flat
        ryu"\"Well, you're not wrong there. {w} {p} He is a pretty odd teacher... but I wouldn't worry too much of him. Just watch out next time.\""
        me"\"Yeah...Thanks\""
        
    else:
        me"\"I saw something odd in there and he caught me snooping around...{w}{p}   then he started rushing me to get out cuz apparently I'm not allowed in storage without a teacher.\""
        
        show ryu normal at bounce
        ryu"\"Huh? That's not even a rule...\""
        show ryu flat
        me"\"Yeah, well I didn't think much of it. He was being really creepy and I wanted out.\""
        ryu"\"Well, you're not wrong there. {w} {p} He is a pretty odd teacher... but I wouldn't worry too much of him. Just watch out next time.\""
        me"\"Yeah...Thanks.\""
   
    stop music fadeout 1.0

    play sound "school bell.ogg" fadein 1.0
    "*Bell rings*"
    
    teacher"\"Alright class, take your seats...\""
    scene black with wipeleft
    scene classroom 11 30 with wipeleft      #Ryu forgets his notes again
    "{i} Fourth Period{/i}"
    play music "Angel Beats! OST_ Girls Hop.ogg" fadein 1.0
    show ryu normal with dissolve
    ryu"\"No...\""
    show ryu concerned at bounce
    ryu"\"Oh nooo.....\""
    me"\"What's with the {i}\"Oh no's\"{/i}?\""
    ryu"\"I left my notebook  at home\""
    me"\"Oh no...{w} Hikari is {i}reeeaally{/i} gonna get you now...\""
    ryu"\"Ohh what am I gonna do--\""
    with vpunch
    show hikari at right with easeinright
    show ryu flat at left
    hikari"\"Hmm... What {i} are {/i} you going to do?\""
    
    show ryu normal
    ryu"\"OH... uhhh...\""
    
    hikari"\"We're going to have to talk about this later Niijima.\""
    show hikari happy at bounce
    hikari"\"For now, both of you take your seats.\""
    
    hide hikari with easeoutright
    
    show ryu cry at down
    ryu"\"Man....\""
    
    
    scene black with wiperight
    scene hallway with wiperight                #Ryu gets detention, MC goes back to the storage room
    "{i} End of the day{/i}"
    show ryu flat with dissolve
    me"\"Hey, what happened with Hikari earlier?\""
    show ryu normal
    ryu"\"{i}Urghhhhhh{/i}\""
    ryu"\"Detention... {w} Again...\""
    me"\"Man that sucks.\""
    show ryu flat
    stop music fadeout 1.0
    ryu"\"Yep... Guess I can't hang out today either.\""
    me"\"Yeah...Guess so.\""
    ############################
    ####### SPLIT 1 #############
    ###########################
    if interrogate and seenGrey:        # TAKE THE SUIT --> TAKESUIT in file SAFEPATH1
        jump takeSuit       
        
    elif interrogate or seenGrey:
        
        menu: 
            me"{i}Whatever happened in the storage room was definitely weird. {w} {p} Maybe I should go back?{/i}"       # TAKE THE SUIT --> TAKESUIT in file SAFEPATH1
            "Go back to investigate":
                jump takeSuit
                
            "Forget about it and go home":       # DON'T TAKE THE SUIT --> HEADHOME in file BADPATH2
                me"\"That's okay, I'll see you tomorrow then!\""
                show ryu at bounce
                ryu"\"Yeah, I gotta run. See you!\""
                hide ryu flat with easeoutright
                jump headHome
                
                
    else:                       # DON'T TAKE THE SUIT --> HEADHOME in file BADPATH2
        me"\"That's okay, I'll see you tomorrow then!\""
        show ryu flat 
        ryu"\"Yeah, I gotta run. See you!\""
        hide ryu flat with easeoutright
        
        menu:
            "Head Home":
                jump headHome
                
                
                
label missingPrez :              
    scene black with fade
    scene clock 8 25 with fade
    "{i} 8:25 am{/i}"                   # START OF DAY 3
    scene classroom 8 25 with fade
    play music "Suspense Music - Project Phoenix.ogg" 
    me"Weird... Everyone seems a bit depressed, even Ryu."
    
    "Some people were a bit teary-eyed."
    
    menu:
        "Talk to Ryu":
            jump talkToRyu
        
    
        
label talkToRyu:
    play sound "choiceEffect3.ogg"
    show ryu concerned with dissolve
    me"\"Hey Ryu,  what's with everyone?\""
    
    
    ryu"\"You haven't heard yet huh?\""
    
    me"\"No... I just got here\""
    
    ryu"\"I only found out a few minutes ago... {w}apparently the class president went missing last night.\""
    
    me"\"WHAT!?\""
    
    show ryu normal at bounce
    
    ryu"\"At first I though he ran away, but he would never do that! He's an honour student!\""
    ryu"\"Then somone mentioned that news report last night --\""
    show ryu flat
    me"\"Of someone going missing in our side of the city? I heard that too, but I'm sure it's not... it can't be...\""
    show ryu concerned
    ryu"\"Man I sure hope not... To think the killer may actually be in our area...\""
    
    "He shuddered at the thought."
    if suit:
        jump tellRyu            #IF YOU TOOK THE SUIT --> TAKESUIT in file SAFEPATH1
                                
    else: 
        jump fourthPeriod2      #ELSE STAY ON PATH
        
label fourthPeriod2:   
    stop music fadeout 1.0
    scene black with wipeleft
    scene classroom 11 30 with wipeleft
    play one "Angel Beats! OST_ School Days.ogg"
    "{i} Fourth period{/i}"
    show hikari at right with easeinright
    hikari"\"I'm sure you've learned your lesson this time, Nijiima.\""
    
    show ryu at left with dissolve
    
    ryu"\"Oh heh...yes ma'am.\""
    
    hide ryu with easeoutleft
    "She turned to face me."
    
    show hikari at slidecenter
    
    hikari"\"How are you, [name]? I'm sure the recent incident with your class president has affected all of us.\""
    me"\"Yeah, it's pretty scary... He was a good friend to everyone, even with the teachers.\""
    hikari"\"Yes, so I've heard. Unfortunately, I never had to chance to formally meet him.\""
    hikari"\"What a shame. Anyway, take your seats everyone. Class is starting.\""
    
    hide hikari with dissolve
    
    me"Huh, she didn't sound very sincere."
    ## IF / ELSE BLOCK:
    if suit: 
        me"Whatever, I hope this class goes by fast. I reeaally need to talk to Ryu."
        jump onRoof     ## TALK TO RYU --> ONROOF in file SAFEPATH1
     
    else:
        if seenGrey or interrogate:
            jump onRoof2  ## ENDOFDAY2 in file BADPATH2
        else:
            jump endOfDay2
            
label day4:
    scene black with fade
    scene classroom 8 25  with fade
    "{i}8:25 am{/i}"
    play music "Angel Beats! OST_ Girls Hop.ogg" fadein 1.0
    "People were still talking about the class president..."
    "Who knows when the police will find him."
    
    "But where's Ryu? He's usually here before me."
    
    play sound "school bell.ogg" fadein 1.0
    "{i} *Bell rings* {i} "
    stop sound fadeout 1.0
    "The door swung open and in ran Ryu."
    
    show ryu flat at center with easeinright
    
    me"\"Hey, you made it!\""
    
    show ryu flat
    ryu"\"You won't believe what just happened.\""
    if chemical:
        
        me"\"You won't believe what I found -- wait what happened?\""
    else:
        me"\"What?\""
    show ryu angry at bounce
    ryu"\"I just got detention AGAIN from Takano!\""
    show ryu flat
    me"\"What the hell? Why--\""
    with vpunch
    stop music fadeout 1.0
    teacher"{size=+5} \"BOYS! Class has started, take your seats NOW!\" {/size}"
    
    ryu"*Sigghh*"
    hide ryu with dissolve

 
    scene black with fade
    scene roof with fade
    play one "Angel Beats! OST_ Today is Ok.ogg" fadein 1.0
    show ryu flat with dissolve
    me"\"So what happened with Takano?\""
    show ryu normal at bounce
    ryu"\"Apparently I trashed the storage room yesterday after school, {w} {p} but I wasn't even at school.\""
    ryu"\"You even saw me leave!\""
    show ryu flat
    if chemical:                                ## IF YOU SAW THE CHEMICALS
        jump optionToTell               # JUMP TO OPTIONTOTELL in file SAFEPATH1

    else:
        jump ryuDoesntKnow      #ELSE JUMP TO BADPATH2
   
     
    return
    
    
    
    


    
    # scene black
    #with fade
    #with hpunch
    #show dev
    #"{i} Hello friend...{/i}"
    #"{i} You have reached the end of the demo... {/i}"
    # "{i} Come back again later.... when more of the story has progressed....{/i}"
    # "{i} Until then.... {/i}" 
    
         

        
        
    
        

