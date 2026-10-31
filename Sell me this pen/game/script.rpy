
#CONSTANTS characters: 

define e = Character("Interviewer", color = "#b12f76")
define narrator_name = Character(None)
define m = Character("[]", color = "#e6dce1")

#Variables 
#Player
default player_name = "Player"
default persuasion = 5

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
                jump end_interview



label interview:
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
                            e "..."
                            e "..."
                            e "ok I.. {w=3.0} apolo.. {w=1.0} apologize"
                            $ persuasion += 1
                            show interviewer normal
                        

                "This pen has a ergonomic design and is very comfortable to hold":
                    e "I see. not bad buckaroo."
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
                                    "nah":
                                        e"Yeah i DON'T belive you whatsoever"
                                        $ persuasion -= 1
                                    



                    "Quite a lot":
                        e"Does that mean the build quality is good?"
                           
                    "ion know!":
                        e"..."
                        e"Ahh i get it\nNice joke!"
                        
                    "how much are you willing to pay for it?":
                        stop music fadeout 1
                        play sound "audio/ice teas.mp3"
                        
                        
                        e"You should order a drink before asking questions"
                        "Then ice teas, 4 of them {w=3.0}"

                        play music "audio/tiger_flute.mp3" fadein 0.5
                        "..."
            label weight:
                e"how much does it weigh?"
                menu:
                    "6000 grams":
                        e"thats really heavy for a pen and very unpracticle "
                        $ persuasion -= 1
                    "7 Arroba":
                        e"thats really heavy for a pen and very unpracticle "
                        $ persuasion -= 1
                    "3 drachms":
                        e"weird unit but it still a very normal mass. Its very practicle!"
                        $ persuasion += 1
                    "10 kneel":
                        e"thats really heavy for a pen and very unpracticle "
                        $ persuasion -= 1
            
            label lethality:
                e"How lethal is this pen?"
                menu:
                    "Its very lethal":
                        e"oh my"
                    "Why don't you try and find out!":

                        call fight 
        





        "Dont sell the pen":
            e "I see. Well, thank you for your time."
            jump end_interview

label fight:
    e "What the hell is wrong wih you"
    e "Thats it {w=2.0} Fight me!"
    "You got into a fight with the interviewer"
    menu:
        "Fight":
            play music "audio/t u s k.mp3"
            menu:
                "Pin him to a wall like a gecko":
                    "You pounced and grappled the interviewer"
                    e"GET OFF ME YOU FOUL BEAST"
                    "you wrestle for a while and you tickle the interviewer on accident"
                    e "Hey.. {w=1.0} s...stop it.. "
                    menu:
                        "Concede and Embrace the loss":
                            jump end_interview
                        "Keep going":
                            "..."
                            "..."
                            "..."
                            

                            

                "punch him":
                    e"owie"
                    e"your a bully!"
                    "Interviewer ran away!"
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



label loss_check:
    if persuasion < 0:
        e"keep the pen im out"
        jump end_interview
    return


label persuasion_check:
    
    if persuasion >= 10:
        e "You drive a hard bargain, "
        "..."
        "i'll take it"
        "..."
        "how much though i only got like 2 rupees "
    else:
        "I-I I didnt want the pen anyway! "
        jump end_interview

    return


label end_interview:
    "..."
    "Game over."









    return