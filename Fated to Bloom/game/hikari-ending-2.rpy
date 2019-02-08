label hikariEnding2:
    scene black with fade
    if chooseTakano:
        me"\"I'll go find Ms.  Hikari instead.\""
    else:
        me"\"I have a feeling Ms. Hikari knows something I don't.\""
        "With a new sense of determination, I head towards Ms. Hikari's classroom and hope for the best."
    scene classroom end of day
    "When I went inside the classroom, Ms. Hikari wasn't there. I wonder if I should-"
    play sound "heartbeat.ogg" fadein 1.0
    unknown"*groan*"
    me"\"Hello?? Who's there?\""
    "I looked around the classroom and found the source of the sound."
    scene ryu tied up
    me"\"Ryu?! What the hell?!\""
    "I grabbed his shoulders and started to shake him."
    with hpunch
    me"\"Ryu!\""
    with hpunch
    me"\"Dude, come on!\""
    scene ryu eyes opened slight
    ryu"\"Hnghhhh\""
    me"\"Ryu?! Can you hear me? What's going on?\""
    ryu"\"Wha...\""
    scene ryu eyes wide
    ryu"\"LOOK OUT!\""
    
    me"\"What are you-!\""
    "Before I could finish my sentence, someone had grabbed me and shoved a cloth in my face. As I try to struggle out of the attacker's grip, I inhale a sweet smell."
    me"{i} The chemical! SHI-!"
    scene passout1
    ryu"\"[name]! NO!\""
    scene black with fade
    play sound "Evil Laughing Woman Sound.ogg"
    unknown"\"Hehehe, you shouldn't have started meddling [name]... now you will face the consequences.\""
    stop sound fadeout 1.0
    "..."
    "..."
    with hpunch
    ryu"\"C'mon man, you gotta wake up!\""
    me"\"Who...?\""
    ryu"\"It's me, Ryu! C'mon, you gotta get up before she comes back!\""
    scene fadin1
    play music "Dark Music - Into The Nightmare.ogg" fadein 1.0 #Dark Music - Into The Nightmare:  https://www.youtube.com/watch?v=BOTTMyPPy9M
    me"*groan* \"What the hell happened...?\""
    scene ryu tied up concern with fade
    ryu"\"You were knocked out, that's what. But hey, I know who the murderer is-\""
    unknown"\"Well, well, well... look who decided to wake up and join us."
    me"\"That voice!\""
    scene hikari desk
    me"\"Ms. Hikari?! What the hell?!\""
    hikari"\"Hello there [name]... you must be wondering \"What's going on?\"\""
    hikari"\"Well... I have some unfortunate news...\""
    hikari"\"It seems that curiosity has taken the better of you, and then you started to interfere with my work...\""
    scene hikari desk evil
    hikari"\"You were getting too close to the truth, so I had to stop you, no matter what...\""
    hikari" \"The fear in your eyes, it reminds of this poor, sappy couple I killed what, {w}must have been 12 years ago now?\""
    me"{i}12 years ago?{/i}"
    me"\"Wha...What? Who were they!?\""
    play sound "<from 5.0>Evil Laughing Woman Sound.ogg"
    hikari"\"Haha...HAHAHAAHA! You boys thought you were so clever!  Now look at you, helpless, just like they were! HAHAhahHA\""
    stop sound fadeout 1.0
    show hikari desk knife 
    "She whipped out a knife and held it up menacingly."
    hikari"\"Unfortunately for you two, you won't be so lucky as your little class president, whatever his name is.\""
    ryu"\"That was you too!? Where is he?\""
    show hikari desk knife confused
    hikari"\"I found that he wasn't quite worth my time, so I dropped him off somehwere while he wa still knocked out.\""
    me"She still hadn't answered my question."
    me"\"Tell me! Who was that couple you murdered!?\""
    stop music fadeout 1.0
    play sound "heartbeat.ogg"
    show hikari desk knife angry
    hikari"\"Alright that's enough with you, time to end things one and for all.\""
    "She lifted up her knife, but before she could bring it down the door busted open."
    play music "Death Note Soundtrack - Ls Theme.ogg" fadein 1.0
    with hpunch
    
    
    scene policeatdoor
    cops"\"Put your hands in the air where I can see them!\""
    hikari"\"What!? IMPOSSIBLE!\""
    ryu"\"Yes! Right in the nick of time!\""
    scene hikari desk knife angry
    "She turns towards Ryu and sneers."
    hikari"\"You will pay!\""
    scene black with hpunch
    "Just as Hikari is about to lunge for Ryu, an officer grabs her and holds her back. She drops the knife and trys to get out of his grip, with no prevail."
    cops"\"Not a chance lady!\""
 
    scene detained with fade
    "As the officers release us from our binds, Hikari was being detained."
    scene classroom end of day
    show ryu with dissolve
    show ryu at bounce
    ryu"\"Ha! Take that!\""
    me"\"Ryu, you shouldn't provoke her.\""
    show ryu happy
    ryu"\"Aw relax [name]! {w}She's got handcuffs on her! We're fiiiine.\""
    show ryu
    me"\"I'm curious...how did you know the cops would come?\""
    "He grins at me and explains while being smug."
    show ryu happy at down
    ryu"\"Well I got worried about the chemicals being used against us, so I called the cops in advance.\""
    "I smile at him and nod my head."
    
    me"\"Good thinking, Ryu. Now how about we get outta here?\""
    show ryu at bounce
    ryu"\"You betcha!\""
    stop music fadeout 5.0
    me"With all this craziness, I'm kind of glad it happened."
    scene parents flashback with fade
    me"Although... I never got to know the truth behind my parents murder..."
    
    play one "Angel Beats! OST_ Light Drop.ogg" fadein 2.0 # This is taken from the Angel Beats! OST - Light Drop:  https://www.youtube.com/watch?v=6dmM4FDuHnY&index=19&list=PL300ktMVZEzp9NYpErqvPBX-DxO0E4h3n
    ryu"\"Man, all this crime solving is making me hungry! You up for some ramen?\" {p} he asks as he pats his stomach."
    "I smile and respond with a laugh."
    scene classroom end of day
    show ryu with dissolve
    me"\"You bet! Lets get outta here.\""
    "And just like that, Ryu slung his arm over my shoulder as we proceed to walk towards our favourite ramen place."
    me"\"Oh by the way, you're paying.\""
    show ryu normal at bounce
    ryu"\"What?!\""
    scene black with fade
    scene ending happy 2 with fade
    with Pause(3)
    jump credits


    
return
