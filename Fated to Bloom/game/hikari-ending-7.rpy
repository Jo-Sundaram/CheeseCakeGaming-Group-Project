label hikariEnding7:
    scene black with fade
    if chooseTakano:
        me"\"Where could he be?\""
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
    play sound "heartbeat.ogg" fadein 1.0
    scene ryu dead
    "I rush to his  side and prop him up against the wall."
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
    "Before I realise, it was already too late, and as I slowly go limp,  my eyes start to flutter shut."
    stop sound
    scene black with fade
    play sound "Evil Laughing Woman Sound.ogg"
    unknown"\"Hehehe, you shouldn't have started meddling [name]... now you will face the consequences.\""
    stop sound
    "..."
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
    scene ryu dead 2
    "My eyes focus on  the bloody body of Ryu."
    me" \"You...RYu…\""
    "I struggled against the urge to vomit."
    "I could barely make out any words."
    hikari"\" HAhaha… You can barely speak! You know, this reminds of something that happened here 12 years ago...\""
    me"\" No...You murderer! YOU -- Arrkhg! \""
    "I felt a sharp pain in my stomach, the cold metal and an intense burning pain."
    scene hikari close
    hikari"\" Time to join them, [name].\""
    show passout2
    "My eyes closed, and I heard the sound of laughter before it all went black."
    play sound "Evil Laughing Woman Sound.ogg"
    scene ryu mc dead
    stop sound fadeout 3.0
    with Pause(3)
    jump credits
    
    return
