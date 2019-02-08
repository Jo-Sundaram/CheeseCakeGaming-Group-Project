﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define me = Character("[name]")
define teacher = Character("Teacher")
define uncle = Character("Uncle")
define aunt = Character("Aunt")
define ryu = Character("Ryu")
define unknown = Character("???")
define prez = Character("Class President")
define hikari = Character("Ms. Hikari")
define takano = Character("Mr. Takano")
define news = Character("News Anchor")



# Function to make character slide off screen to the right
transform slideawayright:
     linear 1.0  xalign 2.0 
     
 # Function to make character slide off screen to the left
transform slideawayleft:
    linear 1.0 xalign -1.0 
     
# Function to make character slide to the center
transform slidecenter:
        linear 0.5 xalign 0.5
     
image hikari sinister quick:
    "hikari sinister.png"
    pause 1.0
    "hikari happy.png"
     


#define slowdissolve = Dissolve(5.0)

default late = False
default seenGrey = False
default interrogate = False 
# The game starts here.
label start:
    
    scene black
   
   
    # Enter your character's name
    python:
        name = renpy.input(("What's your name?"))

        name = name.strip() or __("MC")
    
    

        

    
    
#Scenes for nightmare flashback
 
    scene father
    with fade
    " {i}Father...{/i}"
    
    scene mother
    with fade
    "{i}Mother... {/i}"
    
    scene black
    with hpunch
    "\"{i}[name]! Run!{/i}\""
    with hpunch
    "\"{i}HAHAHAHAHA!!{/i}\""
    with hpunch
    with hpunch
    "\"{i}Mom... Dad... what-!{/i}\""
    
    scene bloodyhand1
    with fade
    with hpunch
    "\"{i}No!{/i} \""
    
    scene bloodyhand2
    with fade
    with hpunch
    "\"{i}NO! !{/i}\""
    
    scene black
    with hpunch
    "\"{i}NO NO NO NO NO NO NO!{/i}\""
    with hpunch
    with hpunch
    with hpunch
    with hpunch
    "{size=+7}\"NOOOOOOOOOOOO!\"{/size}"
    
    scene bedroom morning
    with hpunch
    "*GASP* {w}*huff...* {w}*huff...*"
   
    # Woke up from the nightmare and understand where you are
    me" Another nightmare..."
    me"For the 4th time this week..."
    
    scene alarm clock
    "{i}8:20 am{/i}"
    "10 minutes before school starts... {p}Shoot! I better get ready"
    
    with vpunch
    uncle"{size=+10} \"[name]! Go get my newspaper!\"{/size}"
    me"\"I'm coming Uncle!\""    
    menu:
        "Get dressed":
            jump getDressed
        
           
label getDressed:
    scene bathroom
    with fade
    me"*humming* {p}\" not bad...\""
    
    with vpunch
    uncle"\"[name]! Where's my damn newspaper!\""
    me"{i} Dammit uncle...{/i} \"I'm coming!\""
    
    menu:
        "Go get the newspaper for your uncle":
            jump  livingRoom
            
label livingRoom:
    scene living room
    with fade
    
    show uncle1 with dissolve
    uncle"\"About time! Death would have gotten to me first if you took longer\""
    me"{i} Ah, if only...{/i} {w} {p} \"Yes I'm sorry geez-- uh Uncle, please forgive me.\""
    uncle"\"What did you say boy?\""
    me"\"Nothing Uncle.\""
    uncle"\"Better have been nothing child. My wife and I graciously allowed you to stay with us, and it be best if you weren't disrespecting us in our own house\""
    me"\"Alright Uncle, I understand.\""
    uncle"\"Good. Now get away from here, I don't want to see your face any more than I have to.\""
    
    menu:
        "Head to the hallway":
                jump homehallway

label homehallway:
    scene homehallway
    "{i}*stomach growls*{/i}"
    me"I should probably grab something to eat ..."
    
    menu:
        "Head to the kitchen":
            jump kitchen
            
            
# Where your aunt denies you food
label kitchen:
    scene fridge
    with fade
    
    me "Let's see what we got..."
    menu:
        "Open fridge":
                jump auntdeniedfood
    
label auntdeniedfood:
    with hpunch
    "{i} SLAM {/i}"
    
    scene kitchen
    show aunt
    aunt"\"What do you think you're doing?\""
    me"\"Uh...Breakfast?\" {w} {p} {i} Please let me have a proper breakfast today and not just a piece of toast like everyday...{/i}"
    aunt"\"HUMPH! \""
    scene toast
    aunt"\"Your breakfast has already been made\""
    
    me"{i} *Sigh*... great...{/i}"
# Decide whether to eat or not
    menu:
        me"Dammit I'm gonna be late for school, should I really eat?"
        "Eh, I'm already late  anyway so might as well.":
            $ late = True
            jump eat
        
         
        "Ugh  I'm gonna be late for the third time this week, if I sprint for it I might make it on time":
        
            jump noEat
        
            
          
          
label eat:
        
    me "{i} *Scarfs down the bland toast*{/i} "
        
    aunt"\"Ew, how barbaric...\""
    me "{i} Says the one raising me on plain toast everyday{/i} {w} Alright, time to head to school. Better late than never"
    
    menu:
        "Head To School":
            jump school
    

    
label noEat:
    me "Better to be hungry than get detention"
     
    menu:
        "Head to school":
            jump school 
        
 

 
# Meets up with friend in the hallway
label school:
    scene black with wipeleft
    scene hallway with wipeleft
    me"{i} Please be before the bell...{/i}"
    with hpunch
    unknown"\"Hey [name]! Wait up!\""
    
    me"Hmm? Someone's coming..."
    show ryu with dissolve
    ryu"\"Oh man, glad I made it in time, right?\""
    
  
    me"\"Ha! As if.\""
    me"{i}Ah, Ryunosuke Niijima, or Ryu for short, my best friend since 1st year of junior high. A happy-go-lucky guy that has a knack for lifting the mood without much effort.{/i}"
    # Determines whether you get detention or not
    if late:
        show ryu normal
        "{i}*bell rings*{/i}"
        ryu"\"Crap! We're gonna be late!\""
        menu:
           "Run to class":
            jump schoolDetention
            
           
    else:
        show ryu happy
        ryu"\"Well come on! We're gonna be late.\""
        menu:
           "Run to class":
            jump schoolNoDet
    

label schoolDetention:
    
    scene classroom
    "{i}8:40 am{/i}"
    teacher "\" [name]! This is the third time this week you've been late! Oh, and you've brought a friend...\""
    
    me "\"Sorry! I overslept--\""
    
    teacher "\"{size=+10}Detention for both of you, today after school!{/size}\""
    me"{i} Dammit...{/i}"
    
    jump fourthPeriod
    
    
            
    
label schoolNoDet:
    scene classroom with wiperight
        
    "{i}*bell rings*{/i}"
        
    teacher " \"Oh [name] and Ryu, you're just in time.\""
        
    "{i}*stomach growls*{/i}"
    
    jump fourthPeriod
    
    
label fourthPeriod:
    scene classroom2
    with wipeleft
    
    "{i} 11:10 {p} Right before fourth period{/i}"
    "{i}*bell rings*{/i}"
    show ryu normal with dissolve
    ryu"\"Ah crap! I forgot to do the history notes! [name], let me copy yours.\""
    me"\"What? Dude, it was like, only 3 pages. Ms. Hikari is gonna kill you when she finds out.\""
    ryu"\"Yeah, well it was 3 pages too long. Just let me copy it before 4th period starts. Come on!\""
    
    me"\"Alright, alright! Just make it quick.\""
    show ryu
    ryu"\"Thanks! You are a lifesaver!\""

    #Introduces the sweet KILLER teacher Hikari
    scene black with wipeleft
    scene classroom2 with wipeleft
    
    "{i} 11:40 {p} Fourth period{/i}"
    me"{i} Zzz {w} man school is so boring...{/i}"
    
    ryu"\"{size=-5} Hey [name]...{/size}\""
    me"{i}*stomach growls* {w} only 10 minutes until lunch...{/i}"
    
    ryu"{size=-5}\" [name]?\"{/size}"
    me"{i} ... And then only two more periods until I return to my dreaded home... {w} wait was somebody calling me?{/i}"
    
    ryu"{size=+15}\" [name]!!\"{/size}"
    me"\"AH! WHat??\""
    ryu"\"Teacher's calling you dummy\""
    
   
    show hikari with dissolve
     
    hikari"\"[name]... \""
    hikari"\"Dozing off again?\""
    
    "The teacher looks me dead in the eyes and gives me a sweet yet sinister smile while leaning in so close that I could smell her mild parfume"
    
    show hikari sinister quick
    hikari"{size=-7}\"You don't wann a be leaving yourself vulnerable like that{/size}\""
    
    me"\"Uh... what?\""
    
    hikari"\"Oh, I said you should be going to bed earlier\""
    hikari"\"Heheh~\""
    
    me"\"Uh-- Heh- Sorry about that Ms. Hikari--\""
    
    "{i} *bell rings* {/i}"
    me"Ah, lunch at last"
    
    menu:
        "Head to roof":
            jump roof
                                        #Lunch time, space out over the MC's past
label roof:
    scene black with wiperight
    scene roof with wiperight
    me"Man, what was up with that teacher..."
    "{i}*stomach growls*{/i}"
    me"Urrrgg, never mind that"
    "I open my bag"
    me "Great.. I forgot my lunch...{w} again..."
    me"Siggghhhh"
    
    scene aunt2
    with fade
    me"{i} My aunt and uncle promised my parents that they would take care of me if anything happens to them...{/i}"
    me"{i} And here I am....{/i}"
    ryu"{size=-5}\" Hey [name]...\"{/size}"
    scene uncle2
    with fade
    me"{i} Being fed plain toast and leftovers, if any, while they eat like kings{/i}"
    me"{i} So much for family...{/i}"
    ryu"{size=-5}\" tsk,hey  [name]!\"{/size}"
    scene black
    me"{i} I would've been better off if --{/i}"
    
    with vpunch
    "{size=+10} {i}SLAP{/i} {/size}"
    
    scene roof
    show ryu flat                               #Ryu is a good boi and gives MC food
    
    me"\"OW! What the hell man?!\""
    
    show ryu happy
    ryu" \"Heheh, sorry about that.\""
    ryu"\"You were spacing out again, {w} and from what it looked like I thought you were gonna...\""
    
    show ryu
    ryu"\"Er... nevermind heh\""
    
    me"\"Hah, yeah...{w} I guess I have been spacing out a lot lately\""
    ryu"\"Um here, I could hear your stomach from the otherside of class\""
    
    "He hands me a lunch box, filled with delicious homemade food"
    "I can barely make out the word \"Thanks\" without drooling over it"
    
    me"\" Aw Ryu, you shouldn't ha--\""
    
    show ryu happy
    ryu"\"Hey, I know how it is...{w} {p} ...and besides, my mom loves you anyway {w} (more than me sometimes)\""
    me"{i} Well, I guess some good things came out of it after all{/i}"
    
    show ryu normal
    ryu"\"Anyways, Have you heard the recent stuff on the news?\""
    me"\"No? What's going on?\""
    
    ryu"\" Remember that serial killer case last year in the next city over? The one who dissapeared after a while?\""
    me"\"Oh yeah I remember that.\""
    ryu"\" Apprently there have been a couple murders north of our city.{w}  It's pretty scary\""
    me"\" Damn, you think it might be the same person?\""
    show ryu flat
    ryu"\"That's what the media is conspiring... {w}{p} I hope the police actually catch them this time\""
    me"\" Yeah....\""
    me"{i} I've already had my fair share of that...{/i}"
    
    scene black with wipeleft
    scene classroom3  with wipeleft

    "{w} {i} *bell rings* {/i}"
    "6th period"
    
    me"Alright, time for 6th period, and hoping to not die of boredom."
    teacher"\"blah blah blah….\""
    me"Argh, nevermind that.  I'm taking a nap."
   
    scene black with fade
    ""
    scene classroom3
    "{i} *final bell rings* {/i}"
 
    show ryu with dissolve
    ryu"\"Finally awake are you?\""
    me"\"Heh, did I miss anything important?\""
    ryu"*shrugs* \"not much really, I'm pretty sure a few other kids fell asleep too haha\""
                                                  #DETENTION
    if late:
        me"\"Alright, time to get detention over with\""
        ryu"\"Aww man, I forgot about that, guess we're not leaving for a while\""
        jump lockers
    else:
        me"\"Alright well, time to head out then\""
       
        jump lockers
    

    
   
label lockers:
    scene black with wipeleft
    scene lockers with wipeleft
    show ryu
    
    if late:
        ryu"\"Man that detention was a waste of time, they could have made us do chores or something\""
        me"\"Hey don't give them any ideas!\""
        me"\"I personally liked napping for an hour...\""
        ryu"\"Anyways, it's getting dark\""
        ryu"\"See ya tomorrow!\""
        
        hide ryu
        with fade
    
    else:
        ryu"\"Sorry I can't hang out after school, I got some stuff to do at home\""
        me"\"No worries, see you tomorrow!\""
        hide ryu with easeoutleft

        #Introduces creepy GOOD teacher Takano

    "We waved goodbye"
    "As I was heading out I ran into my creepy old homeroom teacher from last year"
    
    show takano with dissolve
    takano"\"Why, hello there [name]...\""
    
    me"\"Uh h-hello sir\""
    takano"\"Are you heading out now?\""
    menu:
        "Did he know I was here?"
        "Stay and talk to him":
            jump safe
        "Make an excuse to get away":
            jump closeCall


            #SCENE 3: You avoid the car easy and manage to get a glimpse of the driver
label safe:
    me"\"Yeah I was just about to leave actually...\""
    takano"\"I just wanted to tell you to be safe on your way home...\""
    " He walked by me very slowly"
    takano"\"It is getting dark after all....{w} ... You can't tell what might happen now...\""
    
    me"\"Oh Uh yeah- thanks!\""
    
    hide takano with dissolve
    scene black with wipeleft
    scene night road with wipeleft
    
    me"Man our school is filled with weird teachers..."
    
    "{i}*Car approaching in the distance behind*{/i}"
    
    me"What does he mean by \"be safe\", as if I wouldn't be safe..."
    me"Whatever, I'm almost home anyway..."
    
    "{i}*Car speeds up*{/i}"
        
    me" \"You can't tell what might happen now\"....{w} Well right now I can tell that "
    me" The van behing me is moving awfully fast!"
    
    "I quickly jump off to the side of the road"
    with hpunch
    
    me"That was close..."
    me"*Sigh*, well I'm almost home."
    
    scene neighbourhood
    with wipeleft
    
    me"Huh? That's a strange looking van..."
    me"Did someone move in?"
    "I walked by it a bit closer to get a peak inside...{w} but all I can see is..."
    me"A long object  in the passengers seat covered by a white drape... {w} {p} huh... interesting?"
    " I found myself staring at the driver talking on his phone, wearing a grey jump suit and... goggles?"
    me"Uh oh, I think the he saw me!"
    "The driver quickly hangs up his call and speeds off"
    me"??????"
    me"Oddly suspicious..."
    $ seenGrey = True
    menu:
       "Head Home":
           jump home
    
    
                # SCENE 4: You just barely avoid the van but don't get a glimpse of the driver
label closeCall:
    me" \"Uh sorry, my aunt wants me home right away\""
    me"\"Gotta go!\""
 
    
    scene night road
    with fade
    
    me"*huff, huff*.... Man I could've sworn he was following me"
    
    "{i}*Car approaching in the distance behind*{/i}"
    "My speed walk turned into a paranoid jog"
    me"What a creepy teacher, he's probably not married"
    "{i}*Car speeds up*{/i}"
    
    me"I better get home quickly"
    "As I was about to turn into my neighbourhood, I noticed a van from the corner of my eye..."
    "Headed sTRAIGHT FOR ME!!"
    me"\"SHI--\""
    with hpunch
    with vpunch
    
    scene neighbourhood 
    with fade
    "I quickly jumped over on the side of the road, {w} {p} just barely avoiding the van from behind"
    me"\"What the hell!?\""
    "I whip around to get a look at the driver, but all I could see was..."
    me"A long object, drapped by a white sheet, resting in the passenger seat. Weird"

    me"That was waaaay too close"
    
    menu:
       "Head Home":
           jump home
                                #Back home, finish the day 
label home:
    scene black with wiperight
    scene livingroom night with wiperight
    me"*Siigh* Finally home..."
    me"What a weird day..."
    menu:
        "Time for bed":
            jump bedtime
            
label bedtime:
    scene bedroom night
    with fade
    
    me"I plop onto my bed and curl up in my blanket"
    me"Here's to hoping for no nightmares tonight..."
    me"Like I say every night...."
    
    scene black with fade
    "ZZz {w} Zzz..."

                        #Start of Day 2
    with fade
    with hpunch
    "{size=-5}*beep*{/size}"
    with vpunch
    "*beep*"
    with hpunch
    "{size=+5}*beep*{/size}"
    me"Arrgghhh...Shut uppp...."
    
    scene alarm clock
    "{i}7:30 am{/i}"
    with vpunch
    "{size=+10}*bee-{/size}"
    with vpunch
    "{size=+10}{i} *SLAM*{/i}{/size}"
    
    scene bedroom morning with fade
    me"*siighhh*"
    me"wait a minute...{w}{p} No nightmares?"
    me"I can't believe it! I actually slept!"
    
    menu:
        "Get ready for school":
            jump getReady
                
label getReady:
    
    scene bathroom with fade
    
    me"Wow, I actually got ready on time for once!"
    
    menu:
        "Head downstairs":
            jump livingroom
label livingroom:
        
    scene living room with wiperight
    show uncle1 at right
    show aunt at left
    
    uncle"\"{size=+3}Hey boy!{/size} Since you're up so early go get my -!\""
    me"\"Yes uncle!\""
    with fade
    me"\"Here you go \""
    uncle"\"Wow that was fast....{w} Ehh whatever just get out of my face!\""
    
    scene kitchen with dissolve
    me"Better grab my toast"
    
    show aunt with fade
    aunt"\"Huh, I'm glad you're finally being gratefull for the breakfast I prepar--\""
    me"\"Gotta go!\""
    menu:
        aunt"\"Wha-! Don't walk away when I'm lecturing you!\""
        "Run to School":
            jump schoolDay2
                                        
label schoolDay2:                       #Class President asks you to get stuff from storage
    scene classroom3 with fade
    show student prez
    
    prez"\"Hey [name!] You're here early today!\""
    prez"\"Since you're here, would you mind grabbing some supplies from the storage room?\""
    me"\"Sure, what do ya need?\""
    prez"\"Just some more chalk, pencils and paper. {w} {p} In fact, there should be a box with our class number on it\""
    
    menu:
        me"\"Oh alright\""
        "Head to storage room":
            jump storageroom
            
label storageroom:
    scene black with wiperight 
    scene storage room with wiperight
                                        #You go to storage and find something unnerving
    me"*cough cough* {w} {p} Ew, it's pretty dusty in here"
    me"It seems like this placed hasn't been cleaned in years"
    me"Hmmm gym equipment....chairs... oh I see our class box"
    with vpunch
    "{i}*Trips over garbage can*{i}"
    
    me"Oopsie-{w} wait a minute..."
    
    show trash with dissolve
    
    if seenGrey:
        jump heKnows
        
    else:
        jump doesntKnow
        
label heKnows:
        
    me"What is that?"
    me"Is that a ... grey  jumpsuit?"
    "I kneel down to inspect it"
    me"No...I've seen this before..."
    "I was about to pick it up from the bin to inspect it when -"
    with hpunch
    "{size=+10}{i}*SLAM*{i}{/size}"             #Takano catches you snooping around
    jump Takano
   
label doesntKnow:
    me"What in the world? Where did this come from?"
    me"It doesn't look like any school uniform..."
    me"It's a grey jumpsuit"
    "I was about to pick it up from the bin to inspect it when - "
    with hpunch
    "{size=+10}{i}*SLAM*{i}{/size}"  
    jump Takano
       
label Takano:
   hide trash
   show takano
   me"\"AH!\""
   takano"\"Hmmmm What do we have here?\""
   "I quickly drop the jumpsuit in the bin"
   me"\"Oh uh... I was sent by our class president to get some supplies\""
   me"\"Wh...Why are you here?\""
   
   "He walks in slowly with a creepy smile"
   
   takano"\"I wonder... why am I here?\""
   
   me"{i} Oh no... Did he catch me snooping around?{/i}"
   
   takano"\"OH yes, that's right... {w} {p} I came here because I saw you walk in... without a teacher \""
   me"\"Oh. Uh, well the class prez gave me a list of things to get from here so..."
   
   takano"\" Yes well, you shouldn't be in here without a teacher,\""
   me"{i} Is that even a rule?{/i}"
   takano"\" Now hurry along now {w} Shoo!\""
   
   me"{i} He's acting strangely suspicious...{/i}"
   me"\" Why in a hurry? Is there something you need? {w} (plus I still haven't got my supplies)\""
   "He glares a me"
   takano"\" ... No. I have nothing to hide, now shouldn't you get going?\""
   
   "He put on his creepy smile again and gestures towards the door"
   
   menu:                        # He's acting weird, choose to interrogate him or leave him be
       me"{i} Something's not right here...{/i}"
       
       "Interrogate him":
           $interrogate = True
           jump interrogate
       "Leave it be and return to class":
           jump leaveStorage
           
   
label interrogate:                      #Interrogate him
    me"Doing this will probably get me killed but…"
    me"\" Why are you getting so defensive Mr.Takano? Are you hiding something? In this room Perhaps?\""
    takano"\"I've said it before, I have no reason to hide anything.\""
    me"\"Then Why are you trying to rush me out of this room?\""
    me"Could this have something to do with the jumpsuit?"
    takano"\"N-No reason...Just getting you back to class! Yes, that is what I was doing!\""
    "He gives a large, creepy grin and slides the door open just a crack"
    takano"\"Now get back to class, unless you want to get in trouble...hehehehe\""
    "I quickly grabbed our class box and gave him a look of bewilderment as I slowly take a step towards the door"
    me"\"...ok then.\""
    
    "He slams the door behind me"
    
    me"What the hell...?"
    me"Ugh whatever, I  better head back anyways"
    
    menu:
        "Head back to class":
            jump returnclass
            
            
label leaveStorage:     #Leave him be
    "I blink to myself and assume for the best {w} {p} (He’s probably just doing his job, considering i'm not usually allowed to be here and he’s always been kinda weird)"
    me"\" Right.. I was just about to leave, don't worry about me\""
    takano"\"Yes, yes, child. Now run along.\""
    "I quickly grabbed our class box and shuffled towards the door"
    "He slams the door behind me as I stepped out of the room"
    me"What the hell...?"
    me"Ugh whatever, I  better head back anyways"
    
    menu:
        "Head back to class":
            jump returnclass
            
label returnclass:              #Talk to class president and Ryu
    
    scene black with wipeleft
    scene classroom3 with wipeleft
    show student prez with dissolve
    prez"\" oh [name],  you're back!\""
    me"\"Yeah,  here are the supplies you asked for\""
    prez"\"Thank you, I appreciate your cooperation, but uh... \""
    prez"\"If I may ask, why are you sweating profusely? Surely the box wasn’t {i}that{/i} heavy.\""
    "I wipe my brow and realize he was right, as if I just ran 5 miles or something"
    me"{i} How embarrassing {/i}"
    me"\" Uh yeah no.... {w} {p} I just had a run in with Mr. Takano\""
    prez"\" YIKES! That's never good\""
    prez"\"He's always been a  bit...err... how should I say this...\""
    prez"\"Downright creepy. {w} {p} Anyways, thanks for grabbing the supplies!\""
    
    me"\" Haha, anytime\""
    
    hide student prez
    show ryu with dissolve
   
    
    ryu"\"Hey man, you got here early\""
    me"\"Yeah, I was grabbing some supplies and ran into Takano\""
    ryu"\"Ooooh yikes.... what happened?\""
    
    if interrogate :
        me"\" I saw something oddly familiar in there and he caught me snooping around...{w}{p} 
        then he started rushing me to get out cuz apparently I'm not allowed in storage without a teacher.\'"
        
        ryu"Huh? I don't think that's even a rule...\""
        
        me"\" Yeah, and when I asked him why the hurry he started acting weird and suspicious,\""
        me"\" I think he was hiding something there...\""
        
        ryu"\"Hmmm... You know...\""
        ryu"\" I think you might be on to something\""
        
        me"\" You really think so?\""
        ryu"\" I never trusted that teacher, there was always something up with him.\""
        
        ryu"\"I wonder what he would  hide in there anyway.....\""
        me"\"Who knows?\""
        
    else:
        me"\" I saw something odd in there and he caught me snooping around...{w}{p} 
        then he started rushing me to get out cuz apparently I'm not allowed in storage without a teacher.\'"
        
        prez"Huh? That's not even a rule...\""
        
        me"Yeah, well I didn't think much of it. He was being really creepy and I wanted out.\""
        ryu"\" Well, you're not wrong there. {w} {p} He is a pretty odd teacher... but I wouldn't worry too much of him. Just watch out next time.\""
        me"\" Yeah...Thanks\""
        
    "*bell rings*"
    teacher"\" Alright class take your seats...\""
    
    
    scene classroom2 with wipeleft      #Ryu forgets his notes again
    "{i} Fourth Period{/i}"
    show ryu normal
    ryu"\" No...\""
    show ryu concerned
    ryu"\" Oh nooo.....\""
    me"\" What's with the {i}\"Oh noes\"{/i}?\""
    ryu"\"I left my notebook  at home\""
    me"\"Oh no...{w} {p} Hikari is {i}reeeaally{/i} gonna get you now...\""
    "{i} *bell rings* {/i}"
    ryu"\" Ohh what am I gonna do--\""
    with vpunch
    show hikari at right with easeinright
    show ryu at left 
    
    hikari"\"Hmm... What {i} are {/i} you going to do, Niijima...\""
    
    show ryu normal
    ryu"\"OH... uhhh...\""
    
    hikari"\"We're going to have to talk about this later Niijima, {w} {p} now both of you take your seats.\""
    
    hide hikari with easeoutright
    
    show ryu cry
    ryu"\"Man....\""
    
    
    
    scene hallway with wiperight                #Ryu gets detention, MC goes back to the storage room
    "{i} End of the day{/i}"
    show ryu flat with dissolve
    me"\"Hey, what happened with Hikari earlier?\""
    show ryu normal
    ryu"\"{i}*Siiiigghhh*{/i}\""
    ryu"\"Detention... {w} Again...\""
    me"\"Man that sucks \""
    ryu"\" Yep... guess I can't hang out today either \""
    me"\"That's okay, I was planning on sneaking into the storage room anyways\""
    ryu"\"What for?\""
    
    if interrogate:
        me"\"To get a better look at what Mr. Takano was hiding\""
        me"\"Well, {i} if {/i} he was hiding something...\""
    else:
        me"\"Because I need to get a better look at what I saw back there this morning\""
        me"\"I don't know... I just have this really weird feeling about it\""
        
    show ryu 
    ryu"\"I got your back [name], {w}{p} Ms. Hikari told me to serve my detention by helping her clean out her office\""
    ryu"\"I'll keep her distracted so she doesn't go to the storage room while you're there.\""
    
    me"\" Sweet! I knew I could count on you Ryu\""
    show ryu happy
    ryu"\"Just make sure you don't run into Takano again....{w} {p} Then we'd both be dead\""
    
    show ryu 
    ryu"\"Anyway, I gotta run. Cya!\""
    
    hide ryu with easeoutright
    
    me"Alrighty time for some snooping"
    
    scene black with wiperight
    scene storage room with wiperight
    me"Hmm ok, I wasn't followed this time"
    show trash with dissolve
    me"Good, the jumpsuit is still there..."
    me"There's something really weird about it... I should take it home to inspect it more"
    "I kneel down to pick it up when..."
    "{i} \"Meow, meow\"{/i}"
    
    me"\"What the heck? \""
    "I pull the jumpsuit out only to find...."
    
    hide trash 
    show kitten with dissolve
    "\"Meow\""
    
    me"\"A kitten? Is that what Takano was hiding?\""
    me"\"Aw but she's so cute... And I thought Takano was the type who would club kittens\""
    
    "I stuff the jumpsuit in my bag and reached down to pick up the kitten"
    with vpunch
    takano"\"YOU!\""
    "The hair on my back shot straight up"
    me"Uh ohh....."
    
    hide kitten
    show takano with dissolve
    
    takano"\"Haven't I told you already...\""
    takano"\" Your invasive tendencies will result in an unfortunate ending for you\""
    takano"\" I'm sure you don't want to join your friend in detention again\""
    
    me"\"Uh-- I'm sorry sir I was just.. Uh ..\""
    "I quickly realized that I couldn't make a valid excuse while holding a kitten"
    
    takano"\" *Sigh* {w} {p} I see you've discovered my secret\""
    
    me"\" But... why a kitten?\""
    
    "His normally creepy expression turned somber, yet compassionate as I handed the kitten to him."
    "I never thought that was possible"
    
    takano"\" I found her on the street the other night, and unfortunately her mother.... well...\""
    takano"\"I couldn't just leave the poor thing there, but my apartement building does not allow pets\""
    takano"\"I'm going to find a new home for her soon. {w} {p}Please, I beg you not to tell anyone about her, or else she'll be taken away\""
    me"\" I won't\""
    me"{i} Or else he might club me instead{/i}"
    takano"\"Good.\""
    
    "He returned back to his creepy self, and slightly more scary than before"
    takano"\"Now if you know what's good for you, you will leave immediately.\""
    takano"\"In fact, I may have to have a little chat with your class president\""
    
    takano"\".... {w} Well what are you waiting for? {w} {p} {size=+10} {b} GET OUT!!!{b} {/size}\""
    
    "Yikes!"
    
    scene black with wiperight
    scene livingroom night with wiperight
    
    me"Huh, looks like no one's home.{w} Thankfully"
    "I let out a sigh of relief, at least I get some time to myself now"
    
    me"So about that jumpsuit..."
    
    "I decide to switch on the T.V. for some background noise while I fumble around with the grey clothing"
    "The local news channel is going on about the recent murders north of the city, but I'm sure the police will catch them soon. We have nothing to worry about"
    
    news"{i} \" This just in: There has been a report of a missing person south of the city.\" {/i}"
    
    "...I guess I'm wrong."
    
    me"Huh. this jumsuit has a really weird smell to it..."
    me"It's... almost sweet. But not sweet enough to be a parfume or anything.... Maybe Takano used it to make the kitten more comfortable with sleeping in it."
    
    "The news anchors were going over all of the information the police collected with the mystery killer, which I wasn't paying much attention to"
    
    news"{i} \" ...used a special chemical that put's his victims to sleep. Forensics found it to have a slightly sweet smell....\" {/i}"
    
    me"\"Wait huh?\""
    
    news"{i} \" ...found a piece of grey cloth that seemed to have ripped off his clothing when he escaped. Last known image of the killer was from a security footage outside of a gas station.\" {/i}"
    
    "They showed a low quiality image of the man oustide a gas station at night"
    
    news"{i} \" ... he is visible wearing a grey jumpsuit.\" {/i}"
    
    me"No way..."
    
    me"I gotta tell Ryu about this tommorow"
    
    
    
    scene black with fade
    scene classroom with fade
    
    "{i} 8:25 am{/i}"
    
    me"Weird... Everyone seems a bit depressed, even Ryu"
    
    "Some people were teary-eyed"
    
    menu:
        "Talk to Ryu":
            jump talkToRyu
        
    
        
label talkToRyu:
    me"\"Hey Ryu,  what's with everyone?\""
    show ryu concerned with dissolve
    
    ryu"\"You haven't heard yet huh\""
    
    me"\"No... I just got here\""
    
    ryu"\" I only found out a few minutes ago.. {w}  apparently the class president went missing last night\""
    
    me"\"WHAT!?\""
    
    show ryu normal 
    
    ryu"\" That was my reaction as well. At first I though he ran away, but he would never do that. He's an honour roll student\""
    ryu"\"Then somone mentioned that news report last night\""
    me"\"Of someone going missing in our side of the city? I heard that too, but I'm sure it's not... it can't be...\""
    ryu"\"Man I sure hope not... To think the killer may actually be in our area...\""
    
    "He shuddered at the thought"
    
    me"\"Actually... There's something I need to tell you. It's about what I found in the storage room yesterday after school\""
    ryu"\"You didn't run into Takano did you??\""
    me"\"Heh yeah he caught me snooping again...\""
    me"\"But that's not what I wanted to talk to you about - \""
    
    "{i}*bell rings*{/i}"
    
    show ryu flat
    ryu"\" *sigh* I guess it's gonna have to wait until lunch...\""
    
    scene black with wipeleft
    scene classroom2 with wipeleft
    
    "{i} Fourth period{/i}"
    
    show hikari at right with easeinright
    hikari"\" I'm sure you've learned your lesson this time, Nijiima.\""
    
    show ryu at left with dissolve
    
    ryu"\"Oh heh...yes ma'am\""
    
    hide ryu with easeoutleft
    "She turned to face me"
    
    show hikari at slidecenter
    
    hikari"\"How are you, [name]? I'm sure the recent incident with your class president has affected all of us\""
    me"\" Yeah, it's pretty scary... He was a good friend to everyone, even with the teachers\""
    hikari"\"Yes, so I've heard. Unfortunately, I never had to chance to formally meet him.\""
    hikari"\"What a shame. Anyway, take your seats everyone. Class is starting.\""
    
    hide hikari with dissolve
    
    me"Huh, she didn't sound very sincere"
    me"Whatever, I hope this class goes by fast. I reeaally need to talk to Ryu"
    
#Talk to Ryu about the jumpsuit
    scene black with wiperight
    scene roof with wiperight
    show ryu
    ryu"\"Ugh finally, I'm {b}starving{/b}\""
    
    "He takes out two paper lunch bags and hands one to me, then takes a big bite out of his sandwich"
    
    ryu" *Chewing* \"So you wanted to tell me something earlier?\""
    
    me"\"Yeah it was about what I found last night in the storage room\""
    
    ryu"\"Oh yeah, Takano caught you didn't he?\""
    me"\"Yeah, and guess what? He {i} was{/i} hiding something!\""
    ryu"\" What was it?\""
    me"\"It was a stray kitten, but that wasn't the weird part\""
    
    show ryu flat
    ryu"\"Seems pretty weird to me, {w} (doesn't he club kittens as a hobby?)\""
    me"\" It was what he was using to hide the kitten: A grey jumpsuit\""
    ryu"\"Where the hell did he get a jumpsuit from?\""

    #If you saw the driver of the van or not
    if seenGrey:
        me"\"I'm not sure, but I've seen the jumpsuit before.\""
        me"\"When walked home the other night, I almost got hit by a white va-\""
        show ryu normal
        ryu"\"YOU WHAT?!\""
        me"\"Anyways, when I got to my neightbourhood there was a white van parked on the side of the road, and I think the driver was wearing it\""
        ryu"\"...So someone in a grey jumpsuit is out to run you over?\""
        me"\"Maybe, but that's not all,\""
        
    else: 
        me"\"I'm not sure, but there's definitely something suspicious about the jumpsuit\""
        ryu"\"How so?\""
        
    me"\"Last night, they were talking about that serial killer on the news and they showed an image of him wearing a grey jumpsuit\""
    show ryu flat
    ryu"\"Hmm........... Ok so? I'm sure a lot of people wear jumpsuits. {w} {p} Like garbage collectors\""
    me"\"Yeah, but they also talked about one of the killer's strategies of using a sleeping chemical on his victims. Apparently the chemical has a slightly sweet smell\""
    ryu"\"Ok... so --\""
    
    " So I quickly rip out the jumpsuit from my bag and stick it in his face"
    me"\"Smell this\""
    
    "He takes a whiff"

    ryu"\"It's... almost sweet, and somehow familiar...\""
    ryu"\"So you think Takano was using the killer's jumpsuit?\""
    me"\"Well if Takano had it, it can only mean...\""
    
    show ryu concerned
    
    "We exchanged a look of fear"
    
   
    scene black with fade
    scene lockers with fade
    "{i}End of the day{/i}"
    "I could barely pay attention in class. All I could think about was that the killer could potentially be in our very school"
    ryu"\"{size=-5}Something doesn't add up...\" {/size}"
    
    me"\"What'd you say?\""
    
    show ryu normal with dissolve
    ryu"\"I said something doesn't add up. I know that smell on the jumpsuit\""
    ryu"\"It's like Ms. Hikari's parfume\""
    me"\"Woah, and how would {i}you{/i} know what that smells like?\""
    ryu"\"Cuz I spent all of my detention with her, duh. \""
    me"\"Hikari's perfume on Takano's -or rather- the {i} killer's{/i}  jumpsuit...\""
    ryu"\"Yeah\""
    show ryu flat
    ryu"\"And also, I don't think we have enough evidence to accuse him of being the killer\""
    me"\"So I guess we can't really tell anyone about it just yet\""
    ryu" *Sigh* \" Well I gotta run, my mom's pretty mad about me getting detention, {w} {i}again{/i}\""
    hide ryu with easeoutleft
    
    "I went back to my locker to grab a notebook when I heard someone shuffle away."
    "But when I looked around, no one was there"

    
   
     
    return
    
    
    
    


    
    # scene black
    #with fade
    #with hpunch
    #show dev
    #"{i} Hello friend...{/i}"
    #"{i} You have reached the end of the demo... {/i}"
    # "{i} Come back again later.... when more of the story has progressed....{/i}"
    # "{i} Until then.... {/i}" 
    
         

        
        
    
        

