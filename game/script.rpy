
#CONSTANTS characters: 

define e = Character("Interviewer", color = "#b12f76")
define narrator_name = Character(None)
define m = Character("[]", color = "#e6dce1")
define iv_throw = ["Kiss","embarrass","Domain","pebble throw"]
define effect = ["SUPER EFFECTIVE","EFFECTIVE","INEFFECTIVE"]
#Variables 
#Player
default player_name = "Player"
default persuasion = 5

default player_hp = 100
default iv_hp = 100

#Functions

#Start
label start:
   

    

    scene bg room
    play music "audio/tiger_flute.mp3" fadein 1.0

    "Welcome to Sell me this pen"
    $ player_name = renpy.input("Enter your name: ").strip()

    show interviewer normal

    e "Nice to meet you, [player_name]!"
    e "are you ready to start the interview?"
    menu:
        
            "Yes":
                jump interview
            "No":
                e "Then leave"
                jump real_fight



label interview:
    show screen persuasion_bar
    e "Great! Let's begin."
    e "Take this pen and sell it to me."
    "You got a PEN!"
    e""
    menu:
        
        "Sell the pen":
            label ergonomics:
            e "Tell me about the ergonomics of the pen." 
            menu:
            
                "This pen can write words alot":
                    e "yeah thats what they all say"
                    $ persuasion += 0
                    show interviewer normal
                "This pen is ugly and cheap":
                    e "so why would anyong but you want it?"
                    $ persuasion += -1
                    call loss_check
                    
                    show interviewer hmm
                    menu:
                        "The ugly design is actually a unique feature that makes it stand out":
                            e "shut up."
                            $ persuasion += -1
                            call loss_check
                            show interviewer hmm

                        "its cheap so who cares ":
                            e "..."
                            e "I do because I'm buying it stupid"
                            $ persuasion += -1
                            call loss_check
                            show interviewer hmm

                        "That was pretty rude, you kinda hurt my feelings":
                            show interviewer hmm
                            e "..."
                            e "..."
                            show interviewer blush
                            e "ok I.. {w=3.0} apolo.. {w=1.0} apologize"
                            $ persuasion += 1
                            show interviewer normal
                        

                "This pen has a ergonomic design and is very comfortable to hold":
                    e "how did a nitwit like you get so tastefull"
                    "..."  
                    $ persuasion += 1
                    show interviewer normal



                "The pen has got a disease":
                    show interviewer raise
                    e "Is it contagious?"
                    $ persuasion += -1
                    call loss_check
                    menu:
                        "potentially...":
                            "Just take a vaccine you'd be fine"
                            e "True but..."
                            e "..."
                            e "I'm an antivaxxer"
                            $ persuasion += -1
                            show interviewer hmm
                            call loss_check 
                            e "Tell me about the ink then."
                            menu:
                                "This pen's ink is diseased ":

                                    e "the ink ? what the hell is wrong with this pen"
                                    $ persuasion += -1
                                    call loss_check
                                "idk why dont you take a look at it?":
                                    "You threw ink at the interviewer"
                                    call fight
                                    
                                    
                                        
                                    

            label inkyness:
            e "Tell me about the inkyness of the pen."
            menu:
            
                "This pen can write words alot":
                    e "yeah thats what they all say"
                    $ persuasion += 0
                    

                "This pen's fluids are so wonderfull and exquisite  ":
                    e "Hmm{w=2}\nHow so?"
                    $ persuasion += 1

                "This pen has a ergonomic design and is very comfortable to hold":
                    e "yeah thats not really inky tho is it?"
                    $ persuasion += -1
                    call loss_check
            
            label price:
                e "How much does this pen cost?"
                menu:
                    "Not a lot":
                        e"so its cheap?"
                        menu:
                            "Yes":
                                "yeah all the materials are cheap and will break in less than a second of use!"
                                e"..."
                                e"Isn't this just a scam?"
                                menu:
                                    "yeah":
                                        e"Im not buying ts if you say its a scam cro 😭"
                                        $ persuasion -= 1
                                        call loss_check
                                    "nah":
                                        e"Yeah i DON'T belive you whatsoever"
                                        $ persuasion -= 1
                                        call loss_check
                                    



                    "Quite a lot":
                        e"Does that mean the build quality is good?"
                           
                    "ion know!":
                        e"..."
                        e"Ahh i get it\nNice joke!"
                        
                    "how much are you willing to pay for it?":
                        stop music fadeout 1
                        play sound "audio/ice teas.mp3"
                        
                        scene bg bar 
                        e"{cps=25}You should order a drink before asking questions  {nw}{/cps}"
                        scene bg order
                        "{cps=15}Then ice teas, 4 of them {w=3.0}{/cps} {nw}"
                        scene bg ice teas
                        "... {w=3.0}{nw}"
                        stop sound
                        play music "audio/tiger_flute.mp3" fadein 0.5
                        scene bg room
                        "..."




            label weight:
                e"how much does it weigh?"
                menu:
                    "6000 grams":
                        e"thats really heavy for a pen and very unpracticle "
                        $ persuasion -= 1
                        call loss_check
                    "7 Arroba":
                        e"thats really heavy for a pen and very unpracticle "
                        $ persuasion -= 1
                        call loss_check
                    "3 drachms":
                        e"weird unit but it still a very normal mass. Its very practicle!"
                        $ persuasion += 1
                    "10 kneel":
                        e"thats really heavy for a pen and very unpracticle "
                        $ persuasion -= 1
                        call loss_check

            label colour:
                e"What's the colour"
                menu:
                    "That's bone":
                        
                        e"wohoah {w=1.0} very nice"
                        e"look at that"
                        e"whats the lettering called?"
                        "Silian Rail"   
                        $ persuasion += 1
                    "pale nimbus white":
                        e"Nice, Very ... Nice"
                        $ persuasion += 1
                    "Subtle off white colouring, tastefull thickness of it, it even has a watermark":
                        e"Oh my god"
                        $ persuasion += 2

                    "Golden yellow":
                        e"looks like piss fr" 
                        $ persuasion -= 1
                        call loss_check
                
            label durability:
                e"How durable is this pen?"
                menu:
                    "Its very durable":
                        e"Do u got a  example of this?  "
                        menu:
                            "It's so strong it can kill a man":
                                e"yeah right"
                                menu:
                                    "I can show you":
                                        jump real_fight
                                    "You got me!":
                                        $ persuasion -= 1
                                        call loss_check
                                    

                    

            label lethality:
                e"How lethal is this pen?"
                menu:
                    "Its very lethal":
                        e"oh my"
                    
                    "not very, but it can keep you company!":
                        e"..."
                    

                    "Why don't you try and find out!":

                        jump real_fight
            
            label conclusion:
                e "Well, I think I've heard enough."
                e "How well do you think you did? "
                menu:
                    "The best! ":
                        "Find someone better than me if you  can\n but until then, i'll still be this cocky"
                        $ persuasion -= 1
                        show interviewer hmm
                        e "..."
                        e "your not getting hired anytime soon "
                        jump end_interview  

                    "i dont knowwww":
                        e "What do you know then"
                        e "your clearly not a good fit for this company"
                        jump end_interview
                    
                    "you have a very pretty face":
                        show interviewer blush  
                        e"...{w=1.0} ba.. baka! {w=1.0} "
                        e"stop staring at me like that! {w=1.0} "
                        e"eugh! leave already! {w=1.0} "
                        $ persuasion += 1
                        call persuasion_check
                        
                    
                

        





        "Dont sell the pen":
            e "I see. Well, thank you for your time."
            jump real_fight

label fight:
    e "What the hell is wrong wih you"
    e "Thats it {w=2.0} Fight me!"
    "You got into a fight with the interviewer"
    menu:
        "Fight":
            play music "audio/t u s k.mp3"
            menu:
                "i forgot to mention it":
                    "You pounced and pin the interviewer to the wall like a gecko"
                    show interviewer blush
                    e"..."
                    e "Hey.. {w=1.0} s...stop it.. "
                    menu:
                        "Concede and Embrace the loss":
                            jump end_interview
                        "Keep going":
                            "..."
                            "..."
                            "..."
                            

                            

                "punch him":
                    e"owie{nw}"
                    e"your a bully!{nw}"
                    show interviewer sad
                    "Interviewer ran away!{nw}"
                    hide interviewer
                    "You win!"
                    "...{w=1.0}{nw}"
                    "Interviwer joins the battle!"
                    show interviewer hmm
                    e"You thought i was Gone?"
                    menu:
                        "yeah you did cry":
                            e"i DID NOT CRY"
                            show interviewer blush
                            e"..."
                            e"It was all an act i swear!"
                            
                            e"what with the look?"
                            show interviewer hmm
                            e"Thats it im tired of your games"
                        "no":
                            e"So you saw through my plan"
                            e"well [player_name], you seeing this ... {w=2.0}"
                            e"Was ALSO apart of MY PLAN!"
                            e"huh you don't belive me?"
                            e"I guess i gotta show you my real power"


                            
                            




                    jump end_interview

                "Wait for him to attack":
                    "Interviewer used tackle"
                    "tackle was effective"
                    "[player_name] fainted!"
                    jump end_interview

        "Run away":
            e "And STAY OUT!"
            jump end_interview
return






















label real_fight:

    play music "audio/Pledge of Demon.mp3"
     
    #iv_throw = ["Kiss","embarrass","Domain","pebble throw"]
    #effect = ["SUPER EFFECTIVE","EFFECTIVE","INEFFECTIVE"]
    # Super effective = -30
    # effective = -20
    # ineffective = 0
    scene bg battle

    show interviewer angry:
        xalign  0.8
        yalign  0.1
    e"your DONE for kiddo"
    show screen player_health_bar
    show screen iv_health_bar
    while True:  
        if iv_hp <= 20:
            show interviewer livid:
                xalign  0.8
                yalign  0.1
            scene bg battle blood
            play music "audio/oath of enma.mp3"
            
        else:
            show interviewer angry:
                xalign  0.8
                yalign  0.1

        menu:
            "Tackle": 
                show interviewer angry:
                    xalign  0.8
                    yalign  0.1
                $ a = "Tackle"
                call player_attack
                call iv_attack

s
            "Tickle":
                $ a = "Tickle"
                if iv_hp > 20:
                    show interviewer blush:
                        xalign  0.8
                        yalign  0.1 
                    e"what on earth are you doing you perv!{nw}"
                    call player_attack
                    call health_check
                else:
                    "The interviewer can only see red {w=1.0}{nw}"
                    "Tickle is ineffective {w=1.0}{nw}"
                    show interviewer livid:
                        xalign  0.8
                        yalign  0.1

                
                call iv_attack
                call health_check
                

            "Pen stab":
                $ a = "Pen stab"
                call player_attack
                call iv_attack
                call health_check


            "Pen cut":
                $ a = "Pen cut"
                call player_attack
                call iv_attack
                call health_check
                


            "heal": # heal for 10hp
                if player_hp > 75:
                    "you need to be wounded to heal {w=1.0}{nw}"
                    "You also lost ur turn{nw}"
                else:
                    $ player_hp += 15
                
                call iv_attack               
                call health_check
        


label health_check:
    if player_hp <= 0:
        "You Died{w=1.0}{nw}"
        jump end_interview
    if iv_hp <= 0:
        $ renpy.movie_cutscene("images/interviewer death.webm")

        transform slow_zoom:
            align (0.5, 0.5)
            zoom 1.6
            linear 5.0 zoom 2 yalign 0.3
        hide screen player_health_bar
        hide screen iv_health_bar
        scene bg regret at slow_zoom
        "You won{w=1.0}{nw}"
        "...{w=1.0}{nw}"


        "...{w=3.0}{nw}"
        "But you didn't sell the pen{w=1.0}{nw} "
        jump end_interview  
    return

label player_attack:
    $ b = renpy.random.choice(effect)
    "You used [a]{w=1.0}{nw}"
    "[a] was ... {w=1.0} [b]{w=1.0}{nw}"   
    if b == "SUPER EFFECTIVE":
        $ iv_hp -= 30
        "30 DMG{w=1.0}{nw}"
    elif b == "EFFECTIVE":
        $ iv_hp -= 20
        "20 DMG"
    else:
        "Interviewer DOGED{w=1.0}{nw}"
        "No DMG{w=1.0}{nw}"
    return

label iv_attack:
    $ a = renpy.random.choice(iv_throw)
    $ b = renpy.random.choice(effect)
    "Interviewer used [a]{w=1.0}{nw}"
    "[a] was ... {w=1.0} [b]{w=1.0}{nw}"
    if b == "SUPER EFFECTIVE":
        $ player_hp -= 30
        "30 DMG{w=1.0}{nw}"
    elif b == "EFFECTIVE":
        $ player_hp -= 20
        "20 DMG{w=1.0}{nw}"
    else:
        $ player_hp -= 0
        "No DMG"
    return





label loss_check:
    if persuasion < 0:
        e"keep the pen im out"
        jump end_interview
    return


label persuasion_check:
    
    if persuasion >= 10:
        show interviewer raise
        e "You drive a hard bargain, "
        "..."
        e"i'll take it {w=1.0}"
        show interviewer normal
        "..."
        e"how much though i only got like 2 rupees "
        "..."
        menu:
            "3 rupees":
                e"Thats a bit too much for me..."
                show interviewer blush
                e"is there ANY other way i can payyy you?"
                "..."
                "..."
                menu:
                    "Stay with him longer":
                        "..."
                    "No":
                        "You sold all of his assests"

                        "..."

                        "You Lost Your pen"

                        e"Your giving me the pen for free? {w=1.0} "
                        
                        "..."

                        e"Well thanks a "





                jump end_interview
            "2 rupee":
                e"deal"
                jump end_interview
            "Its your pen btw":
                e"Ah well i stole it from the police at the start of the interview "
                "You hear sirens in the distance"
                e"Thats my queue to leave!"
                hide interviewer
                "..."
                "..."
                jump end_interview
    else:
        "You know what keep the pen, i dont want it anymore"
        jump end_interview

    return



label end_interview:
    "..."
    "Game over."
    $ renpy.quit()

    