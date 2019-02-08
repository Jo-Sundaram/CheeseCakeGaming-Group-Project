label takanoBestEnding:
    $chooseTakano = True
    scene black with fade
    me"I have a feeling Mr. Takano knows something I don't……"
    "With a new sense of determination, I head towards Mr. Takano's classroom and hope for the best."
    scene classroom 11 with fade
    show takano
    play music "Suspense Music - Project Phoenix.ogg" fadein 1.0
    me"\"MR. TAKANO!\""
    takano"\"Yes, [name]? What do ya want?\""
    me"\"I knew you were hiding something!\""
    takano" \"Wha..? Yes you already know about my kitten.\""
    me"\"No, I’m talking about this!\""
    "I whip out the bottle of chemical from my bag and lay it infront of him."
    me"Why were you hiding this in the storage room?\""
    show takano upset
    takano" \"What the hell?! I wasn’t hiding that! Wait… you went in the storage room last night?\""
    me"\"Yeah I did, it was me. I saw Ms. Hikari in there looking for something and saw this.\""
    takano"\" Well I have no idea how that ended up in there, I went back to use get old jumpsuit my kitten was sleeping in and it was GONE!\""
    me"\"Where did you get the jumpsuit? Maybe to help you dispose of the bodies??\""
    takano"\"WHAT are you talking about?!It was in the trash when I found it!\""
    takano"\"Also, Ryu was supposed to be here 10 minutes ago...\""
    me"Oh my god… This man really doesn’t know anything! I’ve been interrogating the wrong person this whole time!!"
    stop music fadeout 1.0
    
    menu:
        "Go to Ms. Hikari":
            jump hikariEnding2
         
label takanoEnding3:
    $chooseTakano = True
    scene black with fade  
    me"I have a feeling Mr. Takano knows something I don't……"
    "With a new sense of determination, I head towards Mr. Takano's classroom and hope for the best."
    scene classroom 11 with fade
    show takano
    me"\"MR. TAKANO!\""
    play music "Suspense Music - Project Phoenix.ogg" fadein 1.0
    takano"\"Yes, [name]? What do ya want?\""
    me"\"I knew you were hiding something!\""
    takano"\"Wha..? You know about my kitten?\""
    me"\"What? Your kitten?  No, I’m talking about this!\""
    "I whip out the bottle of chemical from my bag and lay it infront of him."
    me"\"Why were you hiding this in the storage room?\""
    takano"\"What the hell?! I wasn’t hiding that! Wait… you went in the storage room last night?\""
    me"\"Yeah I did, it was me. I saw Ms. Hikari in there looking for something and saw this.\""
    takano"\"Well I have no idea how that ended up in there, i went back to use get old jumpsuit my kitten was sleeping in and it was GONE!\""
    me"\"Where did you get the jumpsuit?\""
    takano"\"It was in the trash when I found it\""
    takano"\"Also, Ryu was supposed to be here 10 minutes ago...\""
    me"Oh my god… This man really doesn’t know anything! I’ve been interrogating the wrong person this whole time!!"
    stop music fadeout 1.0
    menu:
        "Go to Ms. Hikari":
            jump hikariEnding3
            
label takanoEnding5:
    $chooseTakano = True
    scene black with fade
    me" I have a feeling Mr. Takano knows something I don't……"
    "With a new sense of determination, I head towards Mr. Takano's classroom and hope for the best."
    scene classroom 11 with fade
    show takano
    play music "Suspense Music - Project Phoenix.ogg" fadein 1.0
    me"\"MR. TAKANO!\""
    takano"\"Yes, [name]? What do ya want?\""
    me"\"I knew you were hiding something!\""
    takano"\"Wha..? You know about my kitten?\""
    me"\"What? Your kitten? No, I’m talking about this!\""
    "I whip out the bottle of chemical from my bag and lay it infront of him."
    me"\"Why were you hiding this in the storage room?\""
    takano"\"What the hell?! I wasn’t hiding that! Wait… you went in the storage room last night?\""
    me"\"Yeah I did, it was me. I saw Ms. Hikari in there looking for something and saw this.\""
    takano"\"Well I have no idea how that ended up in there, i went back to use get old jumpsuit my kitten was sleeping in and it was GONE!\""
    me"\"What jumpsuit?\""
    takano"\"It was in the trash when I found it\""
    takano"\"Also, Ryu was supposed to be here 10 minutes ago...\""
    me"Oh my god… This man really doesn’t know anything! I’ve been interrogating the wrong person this whole time!!"
    stop music fadeout 1.0
    menu:
        "Go to Ms. Hikari":
            jump hikariEnding5
    
label takanoEnding6:
    $chooseTakano = True
    scene black with fade
    scene classroom end of day with fade
    show takano upset
    play music "Suspense Music - Project Phoenix.ogg" fadein 1.0
    me"\"Hey Mr. Takano, Ryu left his notes behind.\""
    takano"\"Yeah, and he also left detention behind.\""
    me"\"Wait he’s not here?\""
    takano"\"Nope, if that kid doesn’t show up in 10 minutes he’s gonna get double detention tomorrow.\""
    me"\"That dummy, he’s probably looking for his notebook or something. I’ll go look for him.\""
    scene black with fade
    scene hallway with fade
    "I went out to search for him, but he wasn’t in the halls..."
    scene black with fade
    scene lockers with fade
    "...or at the lockers."
    stop music fadeout 1.0
    menu:
        "Continue looking for him":
            jump hikariEnding8
         
        "Give up and go home":
            jump dead
        
label dead:
    play one"<from 10.0>Silent Shadows.ogg" fadein 1.0 # Ominous Music: https://www.youtube.com/watch?v=QTFLYCMkyiM&t=79s
    me"\"Sigh, It’s like he disappeared. Whatever, I’ll give it to him tomorrow.\""
    scene black with fade
    scene neighbourhood with fade
    "As I made my way home, I had this nagging feeling like I was being followed."
    "I felt a tap on my shoulder and turned around."
    with hpunch
    me"\"ARGH!\""
 
    me"Cherry blossoms... ?"
    scene black with fade
    play sound "Evil Laughing Woman Sound.ogg"
    unknown"\"Don’t think I was going to let you get away...\""
    scene clueless with fade
    stop sound fadeout 3.0
    with Pause(7)
    jump credits
  
    return
  
    
label takanoEnding8:
    $chooseTakano = True
    scene classroom end of day with fade
    show takano upset
    play music "Death Note Soundtrack - Ls Theme.ogg" fadein 1.0
    me"\"Hey Mr. Takano, Ryu left his notes behind.\""
    takano"\"Yeah, and he also left detention behind.\""
    me"\"Wait he’s not here?\""
    takano"\"Nope, if that kid doesn’t show up in 10 minutes he’s gonna get double detention tomorrow.\""
    me"\"Wait... if he's not here then...\""
    stop music fadeout 1.0
    
    menu:
        "Go to Ms. Hikari":
            jump hikariEnding8
            
    return
