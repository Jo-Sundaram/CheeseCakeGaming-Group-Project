label hikariEnding3:
    scene black with fade
    if chooseTakano:
        me"\"I'll go find Ms.  Hikari instead.\""
    else:
        me"\"I have a feeling Ms. Hikari knows something I don't.\""
        "With a new sense of determination, I head towards Ms. Hikari's classroom and hope for the best."
    scene classroom end of day with fade
    "As I open the door to the classroom, I hear shuffling within the room."
    me"\"Hello? Is anyone here?\""
    show hikari angry with dissolve
    me"\"Ms. Hikari? Uh, do you have a minute?\""
    show hikari at bounce
    play sound "heartbeat.ogg"
    hikari"\"Why, of course! What do you need?\""
    me"\"Well, I need to ask some questions…\""
    "As I turn to the window, I contemplate how I was going to phrase my words."
    me"\"I need to know if-\""
    scene black with hpunch
    scene classroom end of day with hpunch
    "Just as I am about to turn around, Hikari puts me into a headlock with a cloth put to my face."
    "As I try to struggle out of the her grip, I inhale a sweet smell."
    with hpunch
    me"{i} The chemical! SHI-!{/i}"
    scene passout3
    "Before I realize, it was already too late, as I slowly go limp, and my eyes start to flutter shut."
    scene black with fade
    play sound "<from 11.50>Evil Laughing Woman Sound.ogg" 
    hikari"\"Hehehe, you shouldn't have started meddling [name]... now you will face the consequences.\""
    stop sound fadeout 1.0
    
    "..."
    "As I slowly come to, a headache begins to form."
    me" Wha…? I've been tied up?"
    
    play music "Dark Music - Into The Nightmare.ogg" fadein 1.0 #Dark Music - Into The Nightmare:  https://www.youtube.com/watch?v=BOTTMyPPy9M
    
    unknown"\"Well, well, well. Look who decided to wake up and join us.\""
    scene fadin2
    "I focus, only to see...Ms. Hikari smiling in glee, as if she just heard the best piece of news in the world."
    scene hikari up close
    me"\"Ms. Hikari?! What the hell?!\""
    hikari"\"Hello there, [name]. You must be wondering,\"what is going on?\"\""
    scene hikari desk
    "She moved back and sat down on a desk."
    hikari"\"Well, I have some unfortunate news.\""
    hikari"\"It seems your curiosity has taken the better of you, and then you started to interfere with my work.\""
    scene hikari desk knife evil 
    hikari"\"You were getting too close to the truth, so I had to stop you.\""
    scene hikari up close
    hikari"\"And now you will pay!\""
    "She whipped out her knife and began to bring it down on me."
    me"\"OH F--\""
    
    with vpunch
    scene ryu atdoor
    "Just as I am about to think that my life is over, I see the door to the classroom fly open, and in come Ryu!"
    scene ryu atdoor angry
    "He sees what is about to happen and quickly jumps into action, tackling her to the ground."
    scene ryu onground with vpunch
    me"\"RYU!!\""
    ryu"\"Go [name]!! RUN!!\""
    
    "I struggled to get up, but with my hands tied it felt impossible."
    hikari"\"UGH! I should have gotten rid of you when I had the chance!\""

    "With the knife tight in her grip, Hikari raised her arm up and swung the knife down into Ryu’s side."
    ryu" \"JUST RUN-- \""
    scene ryu stabbed with vpunch
    ryu"\"AAUUGhH\""
    me"\"RYU!!\""
    ryu"\"JUST... GO!"
    "I managed to get up and ran out of the class."
    scene hallway
    " I ran as fast as I could to find Takano to call the cops, with Hikari’s laughter echoing through the halls."
    scene black with fade
    "Within a few minutes, the police and the ambulance arrived at the school and managed to stop Hikari before anyone else could get hurt."
    "As I waited by the ambulance, I see Ryu being taken out of the school."
    scene see ryu with fade
    me"\"RYU!\""
    me"I ran over to him, but an officer grabbed onto me and held me back."
    with hpunch
    me"\"LET ME GO! I HAVE TO SEE HIM!\""
    cops"\"Sir, please calm down. I have some bad news for you..."
    with hpunch
    me"\"NO! LET ME GO! I HAVE TO MAKE SURE HE'S OKAY!\""
    cops"\"Sir, we're going to need you to calm down!\""
    me"\"No! Please, just let me go, just let me go, I... I...\""
    scene mc cry with fade
    "..."
    scene blur with fade
    "I watched them fit Ryu onto a bodybag, and all I could do was drop to my knees and cry, as I knew, my best and only friend, had just died, trying to save me."
    scene detained 2 with fade
    "Hikari came out of the building, handcuffed, and stared at me with a smirk."
    scene blur with fade
    stop music fadeout 1.0
    "Everything was a blur. I couldn't take my eyes away from the black bag that held him."
    "As the officers were doing the cleanup, they thanked me for finding the killer and said they'd give me a reward for my troubles. While they talked, everything they said went in one ear and out the other."
    cops"\"Kid? You alright?\""
    me"\"...\""
    play one "Sad Epic Emotional Music - Farewell Life.ogg" # Sad Epic Emotional Music - Farewell Life: https://www.youtube.com/watch?v=eD0XEH3qVCk
    me"\"What good is a reward, {w}if it was at the cost of your best friend?\""
    scene black with fade
    scene grave with fade
    with Pause(3)
    jump credits
    
    return
