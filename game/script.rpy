
define protagonist = Character("XYZ", color="#c8ffc8")

image bg back= "Boardwalk 1.png"
image bg_storm = "Boardwalk 2.png"
image bg bgno = "Swamp 15.png"

image e normal = "lord_normal.png"
image e closed_angry = "lord_closed_angry.png"
image e confused = "lord_confused.png"
image e closed = "lord_closed.png"
image e sad = "lord_sad.png"
image e smile = "lord_smile.png"

image e_girl angry = "Girl_Angry.png"
image e_girl blush = "Girl_Blush.png"
image e_girl confused = "Girl_Confused.png"
image e_girl cry = "Girl_Cry.png"
image e_girl disgust = "Girl_Disgust.png"
image e_girl evil = "Girl_Evil.png"
image e_girl happy = "Girl_Happy.png"
image e_girl neutral = "Girl_Neutral.png"
image e_girl sad = "Girl_Sad.png"
image e_girl smile = "Girl_Smile.png"

image e_boy angry = "Boy_Angry.png"
image e_boy blush = "Boy_Blush.png"
image e_boy confused = "Boy_Confused.png"
image e_boy cry = "Boy_Cry.png"
image e_boy disgust = "Boy_Disgust.png"
image e_boy evil = "Boy_Evil.png"
image e_boy happy = "Boy_Happy.png"
image e_boy neutral = "Boy_Neutral.png"
image e_boy sad = "Boy_Sad.png"
image e_boy smile = "Boy_Smile.png"



image pro angry = "Male_Angry.png"
image pro blush = "Male_Blush.png"
image pro confused = "Male_Confused.png"
image pro cry = "Male_Cry.png"
image pro disgust = "Male_Disgust.png"
image pro evil = "Male_Evil.png"
image pro happy = "Male_Happy.png"
image pro neutral = "Male_Neutral.png"
image pro sad = "Male_Sad.png"
image pro smile = "Male_Smile.png"

image medusa ="medi.png"

label start:
    scene bg back

    $ name_prompt = renpy.input("Enter your name: ")

  
    $ player_name = name_prompt.strip()


    show pro neutral with moveinleft
  
    show pro smile
   
    protagonist "I've arrived to lead you through the stories that have reached your ears, yet tread cautiously, for there's a twist awaiting your awareness... but... remember..."
  

    show pro evil
    show pro blush
    show pro smile
       

    
    protagonist "I am a liar myself, a conjurer of tales, an inheritor of the tradition set forth by the likes of Odysseus and his kin. But fear not, for in my deception, there lies a peculiar honesty."
    show pro evil
  

    protagonist "In this realm of make-believe, you  %(player_name)s hold the reins. Will you succumb to the allure of the fantastical, or dare to question the authenticity of the narrative? The choice is yours."
    show pro smile
 
  
    menu:
        "Yes":
            jump yes_scene
        "No":
            
            jump no_scene
   

label yes_scene:
    scene bg_storm

  
    show e_girl  neutral at left
    show e_boy  neutral  at right
   
  
    protagonist  "Χαίρετε, travelers from afar! Welcome to our sanctuary."
        
    show e_girl smile 
    show e_boy smile
    



    python:
        renpy.say("Grapevine Spirit 2", "Zdravo  wanderers. Your presence brings a curious joy to these lands.")

    show e_girl happy 
    show e_boy neutral


    
    protagonist  "Allow the essence of our tales to dance through your veins."
   
    protagonist "Now,lend me your ears, kindred spirit"
    protagonist "In a realm where gravity seemed to prefer puns over predictability, Medusa found herself at the heart of a cosmic comedy, a stage for satire."

    show e_girl blush

    protagonist "Perseus, the bravado-bearing buffoon, stumbled onto the scene, armed with a sword that looked like it had seen one too many costume parties."

    show e_girl evil
    show e_boy neutral

    python:
        renpy.say("Grapevine Spirit 2", "Oh, but our stone-cold maiden was no stranger to a laugh at the expense of convention.")

    show e_girl smile
    show e_boy sad

    protagonist "With a gaze as sharp as the edge of Perseus' questionable sword, Medusa raised an eyebrow, turning our hero into the world's first statue of bewilderment."

    show e_girl evil
    show e_boy neutral

    protagonist "The epic quest, now more comedic tragedy, left Perseus frozen in a pose that would make even the greatest sculptors scratch their heads."

    show e_girl smile
    show e_boy sad

    python:
        renpy.say("Grapevine Spirit 2", "And so, in the blink of a serpent's eye, Medusa found herself pondering the cosmic irony of fate, sipping a cup of tea with a dash of serpent spice.")

    protagonist "A whimsical yarn where Medusa, with a smirk that could rival the moon, shattered the expectations of myth, leaving Perseus petrified in more ways than one."

    show e_girl evil
    show e_boy sad

    protagonist "The cosmic laughter echoed through the realm, a harmonious blend of satire and the realization that sometimes, the hero doesn't get the last punchline."

   

    protagonist "So, as the curtain falls on this comedic tragedy, let the laughter linger in the air, a reminder that in the cosmic comedy of mythology, even stone-cold maidens can have the last laugh."
    show e_boy confused
    show e_girl cry 
  
    protagonist "Wait, it seems you harbor a desire to alter the story yourself. A twist, you say? Very well, let's add a touch of your narrative."
menu:
        
        "Attempt to Alter the Story":
          
            jump attempt_alter_story

label attempt_alter_story:
    $ max_attempts = 3
    $ attempt_counter = 0

    protagonist "Well, well, you are with aspirations! Feast your feeble mind on this conundrum: What's the sound of your intellect hitting rock bottom? A symphony of cluelessness, no doubt!"
    protagonist "What is the sound of one hand clapping when the universe itself is the audience?"
    while attempt_counter < max_attempts:
        

        $ answer_prompt = renpy.input("Enter your answer: ")

        $ attempt_counter += 1
        show pro confused
        show pro blush
        show pro angry
        protagonist "No, %(answer_prompt)s is not the answer! Try again!"

    # If the player exceeds the attempt limit
    show pro evil
    show pro blush
    protagonist "Fool, are you not? Persisting in your futile attempts to alter the story. The grand stage scoffs at mortal endeavors to influence its timeless script."

    return






label no_scene:
    scene bg bgno
    show pro angry
    protagonist  "Oh, turning back already? The grand tales of adventure and mystery too much for you?"
    show pro evil
    show pro blush
    protagonist " Well then, enjoy your abyss of mundane thoughts"
    return

    

   

   