label hikariEnding5:
    if chooseTakano:
        me"\"I'll go find Ms. Hikari instead.\""
    else:
        me"\"I have a feeling Ms. Hikari knows something I don't.\""
        "With a new sense of determination, I head towards Ms. Hikari's classroom and hope for the best."
    scene classroom end of day with fade
    "With a new sense of determination, I head towards Ms.hikari's classroom and hope for the best."
    "As I open the door to the classroom, I hear shuffling within the room."
    me"\" Hello? Is anyone--!!\""
    "As I scan around the classroom, I see a figure slumped down against the wall at the back of the class."
    me" Is that…"
    me"\"Ryu!?"
    play sound "heartbeat.ogg"
    scene ryu dead
    "I rush to his side and prop him up against the wall."
    me"\"Ryu? Come on man talk to me!\""
    "It wasn't until I held him, that I smelled something metallic."
    "I place my hand against his side and feel something… wet."
    me"\"What the…\""
    scene blood hand
    me"\"R...yu...?\""
    me"\"No... it can't be...\""
    scene ryu dead
    "I start to shake his body, hoping he'd wake up. His head just moved lifelessly."
    me"\"AAAAAARRRRGGGGHHH!!! RYU!!\""
    "I continue trying, but someone grabbed me and shoved a cloth in my face. As I try to struggle out of the attacker's grip, I inhale a sweet smell."
    me"{i} The chemical! SHI-!"
    scene passout4
    stop sound
    scene black with fade
    play sound "<from 11.50>Evil Laughing Woman Sound.ogg"
    unknown"\"Hehehe, you shouldn't have started meddling [name]... now you will face the consequences.\""
    stop sound fadeout 1.0
    
    scene fadin2
    "As I slowly start to wake up, the scent of metal and slight decay comes through my nose."
    me"\"urgh…\""
    unknown"\"Ah, it seems our guest of honour has decided to join us.\""
    play music "Dark Music - Into The Nightmare.ogg" fadein 1.0 #Dark Music - Into The Nightmare:  https://www.youtube.com/watch?v=BOTTMyPPy9M
    
    scene hikari up close
    me"\"What the hell…?\""
    "She smirks at me."
    hikari"\"You must be wondering, \“What is going on?\” well, you are about to join your friend here.\""
    "She explains, then steps to the side."
    scene ryu dead
    "My eyes focus on  the bloody body of Ryu."
    me" \"You...RYu…\""
    scene hikari desk knife angry
    hikari"\"I’m wasting time, it’s time to join him, [name]!\""
    scene hikari up close
    "She raised her knife and brought it down, but before it could reach me the door busted open."
    
    with hpunch
    scene policeatdoor
    cops"\"HANDS UP WHERE I CAN SEE THEM.\""
    hikari"\"WHAT THE HELL!? IMPOSSIBLE!\""
    hikari"\"URG!! I'm not letting you go so easily!\""
    scene black with hpunch
    "She tried to finish me off before they could reach her but it was too late. They surrounded her and had her handcuffed.\""
    scene detained with fade
    
    "They took us both out; I was taken to the ambulance parked outside to get checked for injuries."
    scene see ryu with fade
    "As I waited by the ambulance, I see Ryu being taken out of the school."
    me"\"RYU!\""
    me"I ran over to him, but an officer grabbed onto me and held me back."
    with vpunch
    me"\"LET ME GO! I HAVE TO SEE HIM!\""
    cops"\"Sir, I have some bad news for you..."
    me"\" NO! LET ME GO! I HAVE TO MAKE SURE HE'S OKAY!\""
    cops"\"Sir, we're going to need you to calm down!\""
    me"\"No! Please, just let me go, just let me go, I... I...\""
    scene mc cry with fade
    "..."
    scene blur with fade
    "I watched them fit Ryu onto a bodybag, and all I could do was drop to my knees and cry, as I knew, my best and only friend, had just died, trying to save me."
    scene detained2 with fade
    "Hikari came out of the building, handcuffed, and stared at me with a smirk."
    scene blur with fade
    stop music fadeout 3.0
    "Everything was a blur. I couldn't take my eyes away from the black bag that held him."
    "As the officers were doing the cleanup, they thanked me for finding the killer and said they'd give me a reward for my troubles. While they talked, everything they said went in one ear and out the other."
    scene mc cry with fade
    cops"\"Kid? You alright?\""
    me"\"...\""
    play one "Sangos - Theme.ogg" #This is taken from the Inuyasha OST - Sango's Theme: https://www.youtube.com/watch?v=gJ7gMdeqEBo
    me"\"What good is a reward, {w}if it was at the cost of your best friend?\""
    scene black with fade
    with Pause(1)
    scene grave2 with fade
    with Pause(3)
    jump credits
    
    return
