label safePath1:
    play sound "choiceEffect3.ogg"
    $points += 1     
    me"\"Yeah I was just about to leave actually...\""
    takano"\"I just wanted to tell you to be safe on your way home...\""
    "He walked by me very slowly."
    takano"\"It is getting dark after all....{w} ... You can't tell what might happen now...\""
    
    me"\"Oh Uh yeah- thanks!\""
    
    hide takano with dissolve
    scene black with wipeleft
    scene neighbourhood with wipeleft
    
    me"Man our school is filled with weird teachers..."
    play sound "car driving full.ogg" #Car Driving sound effect (cut and edited): https://www.youtube.com/watch?v=N_5MMzx5rOs
    
    "{i}*Car approaching in the distance behind*{/i}"
    
    me"What does he mean by \"be safe\"? As if I wouldn't be safe..."
    me"Whatever, I'm almost home anyway..."
   
    "{i}*Car speeds up*{/i}"
        
    me" \"You can't tell what might happen now\"....{w} Well right now I can tell that... "
    me" The van behind me is moving awfully fast!"
    
    "I quickly jump off to the side of the road."
    with hpunch
    stop sound  fadeout 1.0
    me"That was close..."
    me"*Sigh*, well I'm almost home..."
    
    
    scene black with wipeleft
    scene nightroad
    with wipeleft
    me"Huh? That's a strange looking van..."
    me"Did someone move in?"
    "I walked by it a bit closer to get a peak inside...{w} but all I can see is..."
    scene van close up
    me"A long object  in the passengers seat covered by a white drape... {w} {p} huh... interesting?"
    
    play sound "car start and go.ogg" # Car Start Drive Away Sound Effect: https://www.youtube.com/watch?v=ta8u3CrJiuw
    
    " I found myself staring at the driver talking on his phone, wearing a grey jump suit and... goggles?"
    me"Uh oh, I think the he saw me!"
    "The driver quickly hangs up his call and speeds off."
    scene nightroad car gone
    me"??????"
    stop sound 
    stop one fadeout 1.0
    me"Oddly suspicious..."
    $ seenGrey = True
    menu:
       
       "Head Home":
           jump home
                                #Jumps back to main script untill next deviation 
            
    ################################
    ########## SPLIT 1 -- #############
    ###############################
label takeSuit:
    if not interrogate:
        play sound "choiceEffect3.ogg"
    $suit = True
    $points += 1
    play music "sneaky theme.ogg" fadein 3.0 # Cartoon Sneaking Music: https://www.youtube.com/watch?v=V5cpUa8zXIc
    me"\"That's okay, I was planning on sneaking into the storage room anyways.\""
    show ryu normal
    ryu"\"What for?\""
    
    if interrogate and seenGrey:
        me"\"To get a better look at what Mr. Takano was hiding.\""
        me"\"Well, {i} if {/i} he was hiding something...\""
    else :
       me"\"To get a better look at what I saw eariler before Takano kicked me out.\""
       
    show ryu 
    ryu"\"I got your back [name], {w}{p} Ms. Hikari told me to serve my detention by helping her clean out her office.\""
    ryu"\"I'll keep her distracted so she doesn't go to the storage room while you're there.\""
    
    me"\"Sweet! I knew I could count on you Ryu.\""
    show ryu happy at bounce
    ryu"\"Just make sure you don't run into Takano again....{w} {p} Then we'd both be dead.\""
    
    show ryu 
    ryu"\"Anyway, I gotta run. Cya!\""
    
    hide ryu with easeoutright
    
    me"Alrighty time for some snooping."
    
    scene black with wiperight
    scene storage room with wiperight
    me"Hmm ok, I wasn't followed this time."
    scene trash with dissolve
    me"Good, the jumpsuit is still there..."
    me"There's something really weird about it... I should take it home to inspect it more."
    "I kneel down to pick it up when..."
    play sound"Newborn - Kitten.ogg" # Meowing Sound Effect: https://www.youtube.com/watch?v=vAwyncCIijQ
    "{i} \"Meow\"{/i}"
    
    me"\"What the heck?\""
    "I pull the jumpsuit out only to find...."
    
    scene trashcan close cat
    "{i}\"Meow\"{/i}"
    stop sound fadeout 1.0
    
    me"\"A kitten? Is that what Takano was hiding?\""
    me"\"Aw but she's so cute... And I thought Takano was the type who would club kittens.\""
    
    "I stuff the jumpsuit in my bag and reached down to pick up the kitten."
    with vpunch
    takano"\"YOU!\""
    "The hair on my back shot straight up."
    me"Uh ohh....."
    
    scene storage room cat
    show takano upset with dissolve
    
    takano"\"Haven't I told you already...\""
    takano"\"Your invasive tendencies will result in an unfortunate ending for you.\""
    takano"\"I'm sure you don't want to join your friend in detention again.\""
    
    me"\"Uh-- I'm sorry sir I was just... Uh...\""
    "I quickly realized that I couldn't make a valid excuse while holding a kitten."
    
    takano"\"*Sigh* {w} {p} I see you've discovered my secret.\""
    
    me"\"But... why a kitten?\""
    show takano happy
    "His normally creepy expression turned somber, yet compassionate as I handed the kitten to him."
    "I never thought that was possible."
    
    takano"\"I found her on the street the other night, and unfortunately her mother.... well...\""
    takano"\"I couldn't just leave the poor thing there, but my apartement building does not allow pets.\""
    takano"\"I'm going to find a new home for her soon. {w} {p}Please, I beg you not to tell anyone about her, or else she'll be taken away.\""
    me"\"I won't.\""
    me"{i} Or else he might club me instead!{/i}"
    takano"\"Good.\""
    
    show takano
    "He returned back to his creepy self, and slightly more scary than before."
    takano"\"Now if you know what's good for you, you will leave immediately.\""
    takano"\"In fact, I may have to have a little chat with your class president.\""
    
    show takano upset
    takano"\".... {w}Well what are you waiting for? {w} {p} {size=+10} {b} GET OUT!!!{b} {/size}\""
    stop music fadeout 1.0
    "Yikes!"
    
    scene black with wiperight
    scene bedroom night  with wiperight
    play music "<from 0.0 to 85.0>Death Note Soundtrack - Ls Theme.ogg" fadein 3.0 # This is taken from the Death Note OST - L's Theme (A): https://www.youtube.com/watch?v=MTGlrcReWrk
    me"Huh, looks like no one's home.{w} Thankfully."
    "I let out a sigh of relief, at least I get some time to myself now."
    
    scene comp news
    "I decide to turn on my computer. The news was the first thing that popped up on the screen." 
    "The article is talking about the recent murders north of the city."
    
    me"So about that jumpsuit..." 
    "I click on the video for some background noise while I fumble around with the grey clothing. I'm sure the police will catch the murderer soon. I have nothing to worry about."
    
    news"{i} \"This just in: There has been a report of a missing person south of the city.\" {/i}"
    
    "...I guess I'm wrong."
    
    me"Huh. this jumsuit has a really weird smell to it..."
    me"It's... almost sweet. But not sweet enough to be a parfume or anything.... Maybe Takano used it to make the kitten more comfortable with sleeping in it."
    
    "The news anchors were going over all of the information the police collected with the mystery killer, which I wasn't paying much attention to."
    
    news"{i} \" ...used a special chemical that put's his victims to sleep. Forensics found it to have a slightly sweet smell....\" {/i}"
    
    me"\"Wait huh?\""
    
    news"{i} \" ...found a piece of grey cloth that seemed to have ripped off his clothing when he escaped. Last known image of the killer was from a security footage outside of a gas station.\" {/i}"
    
    "They showed a low quiality image of the man oustide a gas station at night."
    
    news"{i} \" ... he is visible wearing a grey jumpsuit.\" {/i}"
    
    me"No way..."
    
    scene comp
    
    me"I gotta tell Ryu about this tommorow."
    stop music fadeout 1.0
    
                                 #Jump back to main script
    jump missingPrez
    
label tellRyu:
    
    me"\"Actually... There's something I need to tell you. It's about what I found in the storage room yesterday after school.\""
    ryu"\"You didn't run into Takano did you??\""
    me"\"Heh yeah he caught me snooping again...\""
    me"\"But that's not what I wanted to talk to you about - \""
    
    play sound "school bell.ogg" fadein 1.0
    "{i}*bell rings*{/i}"
    stop sound
    show ryu flat
    ryu"\" *sigh* I guess it's gonna have to wait until lunch...\""
    
    jump fourthPeriod2  ## FOURTHPERIOD2 in MAIN SCRIPT
    
label onRoof:
    # TALK TO RYU ABOUT THE JUMPSUIT
    scene black with wiperight
    scene roof with wiperight
    show ryu
    ryu"\"Ugh finally, I'm {b}starving{/b}.\""
    
    "He takes out two paper lunch bags and hands one to me, then proceeds to take a big bite out of his sandwich."
    
    ryu" *Chewing* \"So you wanted to tell me something earlier?\""
    
    me"\"Yeah it was about what I found last night in the storage room.\""
    
    show ryu normal
    ryu"\"Oh yeah, Takano caught you didn't he?\""
    me"\"Yeah, and guess what? He{i} was{/i} hiding something!\""
    ryu"\"What was it?\""
    me"\"It was a stray kitten, but that wasn't the weird part.\""
    
    show ryu flat
    ryu"\"Seems pretty weird to me, {w} (doesn't he club kittens as a hobby?)\""
    me"\"It was what he was using to hide the kitten: A grey jumpsuit.\""
    show ryu normal at bounce
    ryu"\"Where the hell did he get a jumpsuit from?\""
    show ryu flat

    ## IF / ELSE BLOCK: 
    if seenGrey:
       me"\"I'm not sure, but I've seen the jumpsuit before.\""
       me"\"When walked home the other night, I almost got hit by a white va-\""
       show ryu angry at bounce
        
       ryu"\"YOU WHAT?!\""
            
       me"\"Anyways, when I got to my neightbourhood there was a white van parked on the side of the road, and I think the driver was wearing it.\""
       
       show ryu flat
       ryu"\"...So someone in a grey jumpsuit is out to run you over?\""
       
       me"\"Maybe, but that's not all.\""
     
    else:
        me"\"I'm not sure, but I had a really weird feeling about it.\""
        me"\"And guess what?\""
    
    #######################################################################################################
    me"\"Last night, they were talking about that serial killer on the news and they showed an image of him wearing a grey jumpsuit.\""
    show ryu flat
    ryu"\"Hmm........... Ok so? I'm sure a lot of people wear jumpsuits. {w} {p} Like garbage collectors.\""
    me"\"Yeah, but they also talked about one of the killer's strategies of using a sleeping chemical on his victims. Apparently the chemical has a slightly sweet smell.\""
    ryu"\"Ok... so --\""
    
    stop one fadeout 1.0
    " I quickly rip out the jumpsuit from my bag, and stick it in his face."
    me"\"Smell this.\""
    
    "He takes a whiff."

    ryu"\"It's... almost sweet, and somehow familiar...\""
    ryu"\"So you think Takano was using the killer's jumpsuit?\""
    show ryu normal
    me"\"Well if Takano had it, it can only mean...\""
    
    show ryu concerned
    
    "We exchanged a look of fear."

    scene black with fade
    scene lockers with fade
    play music "Angel Beats! OST_ Today is Ok.ogg" fadein 1.0
    
    "{i}End of the day{/i}"
    "I could barely pay attention in class. All I could think about was that the killer could potentially be in our very school."
    ryu"\"{size=-5}Something doesn't add up...\" {/size}"
    
    me"\"What'd you say?\""
    
    show ryu normal with dissolve
    ryu"\"I said something doesn't add up. I know that smell on the jumpsuit.\""
    ryu"\"It's like Ms. Hikari's parfume.\""
    me"\"Woah, and how would {i}you{/i} know what that smells like?\""
    show ryu flat at bounce
    ryu"\"Cuz I spent all of my detention with her, duh.\""
    me"\"Hikari's perfume on Takano's -or rather- the {i}killer's{/i}  jumpsuit...\""
    ryu"\"Yeah.\""
    show ryu normal at bounce
    ryu"\"And also, I don't think we have enough evidence to accuse him of being the killer.\""
    me"\"So I guess we can't really tell anyone about it just yet.\""
    show ryu flat
    ryu" *Sigh* \"Well I gotta run, my mom's pretty mad about me getting detention, {w} {i}again{/i}.\""
    hide ryu flat with easeoutleft
    
    play sound "foot - steps.ogg" fadein 1.0 # Foot steps sound effect: https://www.youtube.com/watch?v=ByTCbyCJh9c
    "I went back to my locker to grab a notebook when I heard someone shuffle away."
    
    stop sound fadeout 1.0
    "But when I looked around, no one was there."

      
    me"Whatever, I should get going as well."
    
    scene hallway with fade
    "I made my way down the hall, took a right and passed the storage room towards the exit."
    "As I passed it I heard some objects being pushed around {w} {p} and then a voice muttering something."
    stop music fadeout 1.0
    me"{i}\"Takano...\" {i}"
    
    menu:
        "Investigate":
          jump investigateStorage # INVESTIGATE THE STORAGE ROOM
         
          
label investigateStorage:
    play sound "choiceEffect3.ogg"
    $points +=1
    $chemical =True
    scene storage room with fade
    play music "sneaky theme.ogg" fadein 3.0
    "I turned back and opened the door {i}just{/i} a crack. But when I peaked inside, Mr. Takano wasn't there."
    show hikari nervous with dissolve
    "Instead, it was Ms. Hikari mumbling to herself."
    me"What the hell is she doing there?" 
    
    hikari" {size=-5} \"...where...? Uggh where!?\" {/size} "
    me"She seems pretty agitated, that's never a good sign."
    scene hallway
    "I decided to hide around the corner and wait for her to leave."
    "After a few minutes, she let out a huff and walked calmly out of the room."
    me"I wonder what she could've been searching for..."
    scene black with wipeleft
    scene storage2 with wipeleft
    
    "I snuck back inside the room."
    "Everything looked okay, but something felt a bit off."
   
    me"Whatever she was looking for must have been pretty important..."
    "I think I heard some bottles clinking behind the shelves."
    scene close up storage
    "I got a bit closer to the shelves to see what was there."
    me "{i} Don't tell me she was hiding alcohol.{/i}"
    "In a rush, I knocked some of the boxes on the floor. Oops."
    "But it wasn't alcohol..."
    scene close up chemical with fade
    "They were bottles of some sort of chemical."
    me"This definitely wasn't here before....Or maybe it was..."
    me"Hmm... Contains chloroform and... cherry blossoms?!?"
    scene storage bottle2 with fade
    "I put the bottle in my bag and made my way out."
    "My foot stepped on something, I picked it up to inspect it."
    scene storage bottle with fade
    me"One of Hikari's hairclips, I'm sure she'll be missing this."
    scene hallway with fade
    
    "As I made my way down the hall I saw Takano walking towards me."
    me"{i}Oh no, just act natural...{/i}"
    show takano upset with dissolve
    hide takano with easeoutright
    
    "But he didn't even notice I was there and kept walking..."
    "...Right into the storage room."
    me"God dammit, I better get out of here fast."
    menu:
        "Head Home":
            jump home2
            
label home2:
    play sound "choiceEffect3.ogg"
    scene black with fade
    scene livingroom night with fade
    
    me"Ryu would love to hear about this tomorrow."
    stop music fadeout 1.0
    
    jump day4   ## JUMP TO MAIN DAY 4 IN MAIN SCRIPT
    
label optionToTell:     ###OPTION TO TELL RYU --> STAY ON PATH OR JUMP TO BAD PATH
    me"\"Yeah that doesn't make any sense! I even --\""
    me"{i} Wait...{/i}"
    menu:
        me"{i}Should I really tell him about what I found last night?{/i}"
        "Tell him, he deserves to know":
            jump ryuKnows                        ## STAY ON PATH
            
        "Don't tell him, it could put him in danger":
            jump ryuDoesntKnow  ## JUMP TO RYUDOESNTKNOW in file BADPATH2

label ryuKnows:
    $ryuknows = True
    play sound "choiceEffect3.ogg"
    $points += 0.5
    
    me"\"I even saw who trashed the storage room.\""
    show ryu normal
    ryu"\"You did?\""
    me"\"Yeah.\""
    me"\"It was me.\""
    show ryu angry at bounce
    ryu"\"What the hell man?!\""
    me"\"I only did it because I saw that Ms. Hikari was looking for something!\""
    me"\"And whatever it was seemed to have been pretty important!\""
    show ryu flat
    ryu"\"Really? What?\""
    
    "I pulled out the bottle of chemical and Ms. Hikari's hairclip."
    
    me"\"I found the bottle behind the shelf, and her hairclip on the floor.\""
    show ryu flat
    ryu"\"What's the bottle?\""
    me"\"From the look of it, I'd say some sort of sedative chemical.\""
    
    "He took the bottle and slighty opened the lid to take a whiff. Not enough to take effect, however."
    
    show ryu normal at bounce
    ryu"\"Holy crap...\""
    ryu"\"I think we may have enough evidence to call the police on {i}someone{/i}. But who?\""
    me"\"I have a plan, but I don't think going to detention is the best idea for you.\""
    show ryu at bounce
    ryu"\"I'm way ahead of you.\""
    ryu"\"I'll meet you by the lockers afterschool.\""
    stop one fadeout 1.0
    scene black with fade 
    scene lockers with fade
    "{i}End of the Day{/i}"
    me"Where is he.... He said he'd meet me here."
    me"I should ask someone."
    me"\"Hey, have you seen Ryu anywhere?\''"
    unknown"\"Yeah, he told me he was on his way to detention.\""
    me"\"WHAT!? I told him not to go!\""
    me"Whatever, he did say he had a plan of his own..."
    me"Time to follow through on mine."
    
    menu:
        me"Who should I interrogate?"
        "Ms. Hikari":
            jump pointsCalcHikari
            
        "Mr. Takano":
            jump pointsCalcTakano
    

