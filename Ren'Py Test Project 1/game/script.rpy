# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define me = Character("[name]")
define teacher = Character("Teacher")
define uncle = Character("Uncle")
define aunt = Character("Aunt")
define ryu = Character("Ryu")
#define slowdissolve = Dissolve(5.0)

default late = False
# The game starts here.

label start:
    
    scene black
   
   
    # Enter your character's name
    python:
        name = renpy.input(("What's your name?"))

        name = name.strip() or __("MC")
    
    

        

    
    
#Scenes for nightmare flashback
 
    scene nightmare
    " {i}Father...{/i}"
    
    scene nightmare1        
    "{i}Mother...no... {/i}"
    
    scene nightmare2
    "{i}...{/i} "
    
    scene black
    "*GASP*, {w} *huff...huff*"
    
    scene morning house
    with fade
    # When you wake up and have to get the newspaper
    "{i}8:20 am{/i}"
    me" Another nightmare..."
    
    scene alarm clock
    "{i}10 minutes before school starts{/i}"
    me"For the 4th time this week..."
    
    scene alarm clock
    with vpunch
    uncle"\"{size=+10}[name]! Go get my newspaper already!{/size}\""
    me"\"Ugh, I'm coming!! {w} {p}  {i} damn geezer can't do it himself...{/i}\""
    menu:
        "Get dressed":
            jump getDressed
        
           
label getDressed:
    scene washroom
    with fade
    me"*humming* {p} not bad..."
    
    with vpunch
    uncle"[name]! Where's my damn newspaper!"
    me"{i} damn geezer... {/i}"
    
    menu:
        "Go get the geezer's newspaper":
            jump  livingRoom
            
label livingRoom:
    scene living room
    with fade
    
    uncle"About time! Death would have gotten to me first if you took longer, {w} {p} stupid child..."
    me"{i} Ah, if only...{/i} {w} {p} Yes I'm sorry geez-- uh Uncle"
    
    "{i}*stomach growls*{/i}"
    me"I should probably grab something to eat ..."
    
    menu:
        "Head to the kitchen":
            jump kitchen
            
            
# Where your aunt denies you food
label kitchen:
    scene kitchen
    with fade
    
    me "Let's see what we got..."
    
    with hpunch
    
    aunt"What do you think you're doing?"
    me"Uh...Breakfast? {w} {p} {i} Please let me have a proper breakfast today and not just a piece of toast like everyday...{/i}"
    aunt"HUMPH! "
    scene bread
    aunt"Your breakfast has already been made"
    
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
        
    aunt"Ew, how barbaric..."
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
    scene hallway
    with fade
    me"{i} Please be before the bell...{/i}"
    with hpunch
    ryu"Hey [name]! Wait up!"
    
    me"Hmm? Someone's coming..."
    show ryu2
    ryu"Oh man, glad I made it in time, right?"
    
  
    me"Ha! As if."
    me"{i}Ah, Ryunosuke Niijima, or Ryu for short, my best friend since 1st year of junior high. A happy-go-lucky guy that has a knack for lifting the mood without much effort.{/i}"
    
    if late:
        "{i}*bell rings*{/i}"
        ryu"Crap! We're gonna be late!"
        menu:
           "Run to class":
            jump schoolDetention
            
           
    else:
        ryu"Well come on! We're gonna be late."
        menu:
           "Run to class":
            jump schoolNoDet
    

label schoolDetention:
    
    scene classroom
    "{i}8:40 am{/i}"
    teacher " [name]! This is the third time this week you've been late! Oh, and you've brought a friend..."
    
    me "Sorry! I overslept--"
    
    teacher "{size=+10}Detention for both of you, today after school!{/size}"
    me"{i} Dammit...{/i}"
    
    jump fourthPeriod
    
    
            
    
label schoolNoDet:
    scene classroom
        
    "{i}*bell rings*{/i}"
        
    teacher " Oh [name] and Nijiima, you're just in time."
        
    "{i}*stomach growls*{/i}"
    
    jump fourthPeriod
    
    
label fourthPeriod:
    scene classroom2
    with wipeleft
    show ryu2
    
    "{i} 11:10 {p} Right before fourth period{/i}"
    "{i}*bell rings*{/i}"
    ryu"Ah crap! I forgot to do the history notes! [name], let me copy yours."
    me"What? Dude, it was like, only 3 pages. Mr Teacher Name is gonna kill you when he finds out."
    ryu"Yeah, well it was 3 pages too long. Just let me copy it before 4th period starts. Come on!"
    me"Alright, alright! Just make it quick."
    ryu"Thanks! You are a lifesaver!"


    scene classroom2
    with fade
    
     
    "{i} 11:40 {p} Fourth period{/i}"
    me"{i} Zzz {w} man school is so boring...{/i}"
    ryu"{size=-5} Hey [name]...{/size}"
    me"{i}*stomach growls* {w} only 10 minutes until lunch...{/i}"
    ryu"{size=-5} [name]?{/size}"
    me"{i} ... And then only two more periods until I return to my dreaded home... {w} wait was somebody calling me?{/i}"
    ryu"{size=+15} [name]!!{/size}"
    me"AH! WHat??"
    ryu"Teacher's calling you dummy"
    show teacher
    "[name]... "
    "(says some teacher stuff)"
    
    "{i} *bell rings* {/i}"
    me"Ah, lunch at last"
    
    menu:
        "Head to roof":
            jump roof
            
label roof:
    scene roof
    with fade
    me"{i}*stomach growls*{/i}"
    me "Great.. I forgot my lunch...{w} again..."
    me"Siggghhhh"
    
    scene aunt2
    with fade
    me"{i} My aunt and uncle promised my parents that they would take care of us if anything happens to them...{/i}"
    me"{i} But now there's only me....{/i}"
    scene uncle2
    with fade
    me"{i} Being fed plain toast and leftovers, if any, while they eat like kings{/i}"
   
    
    
        
    return
        

