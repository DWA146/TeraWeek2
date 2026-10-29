
#CONSTANTS characters: 

define e = Character("Interviewer", color = "#b12f76")
define narrator_name = Character(None)
define m = Character("[]", color = "#e6dce1")

#Variables 
#Player
default player_name = "Player"
default persuasion = 0

#Start
label start:

    

    scene bg room
    play music "audio/tiger_flute.mp3" fadein 1.0

    "Welcome to Sell me this pen"
    $ player_name = renpy.input("Enter your name: ").strip()

    show interviewer normal at center
        zoom 1.5



    "Nice to meet you, [player_name]!"
    return