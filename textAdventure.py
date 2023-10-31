# To Do
# fix: backwards command totally broken. not moving backward and in some cases moving forwards?

# Setup
import time
import random

# Commands
yes_no = ["yes", "no"]
commands = ["left", "right", "forward", "backward", "look around", "light torch", "quit"]

# Flags for tracking position in level, likelihood of death by Grue, inventory items, solved puzzles, etc.

levelFlag = 0
grueFlag = 0
doorKey = 0
riddleStage = 0
puzzleSolved = 0
evilPlans = 0

# Introduction

name = input("What is your name, adventurer?\n")
print("Hello, " + name + ". You are on a quest.")
print("You are standing on the edge of a dark swamp.")
print("Not far ahead of you is the Tower.")
print("Lately, people have vanished from the area surrounding it.")
print("Elizabeth, from Dead Orleans, wants to you ascend the Tower and find out what is going on.")
print("You can type 'help' to print a list of commands.")
print("If you need a hint, type 'hint' as well.")

#First stage

response = ""
while response not in yes_no:
    response = input("Do you approach the Tower? \nyes/no\n")
    if response == "yes":
        print("You walk towards the Tower. The sun seems to set a little faster.\n")
    elif response == "no":
        print("Oh, well, never mind then. Goodbye, " + name + ".")
        time.sleep(3)
        quit()
    else:
        print("I didn't understand that.\n")

# outside the tower

levelFlag = 0

while levelFlag < 1:
        print("The Tower looms over you. There are five stories, \nfrom the ground floor to the fifth at the peak.")
        print("Right in front of you is a heavy wooden door.")
        response = input("Enter a command.\n")
        if response == "look around":
            print("You look around the area.")
            print("The sun is beginning to set to your left, the west.")
            print("In front of you is the tower. It is all that remains of a forgotten king.")
            print("The tower is in better condition than you expected.")
            print("No windows are broken, only a few bricks have fallen.")
            print("You know beneath your feet, in the foul swamp, is the sunken ruins of a castle.")
            print("The tower is conspicuously absent of any plant growth.")
            print("There are no vines, no trees, not even moss between bricks.")
            print("Behind the tower, you can see more swampland. It seems to stretch on forever.")
            print("To your right, there are hills and little else to interest you.")
            print("Behind you are more hills, and beyond them Dead Orleans, a haven in this frightful land.")
            print("\n")

        elif response == "left":
            print("You walk to the left side of the tower.")
            print("You see more of the same. Old brickwork, without the marks of nature.")
            print("Certainly the marks of poor craftmanship, though.")
            print("The king must have cheaped out on labour.")
            print("You walk back to the front of the tower.")
            print("\n")
            
        elif response == "right":
            print("You walk to the right side of the tower.")
            print("On this wall, you can see a window just too high up to reach.")
            print("It is filthy and obscured with dirt.")
            print("There are four more windows evenly spaced for each floor.")
            print("\n")
            
        elif response == "backward":
            print("Coward. Move onwards.")
            print("\n")
            
        elif response == "forward":
            print("You push against the door. It reluctantly gives a little, \nso you push harder and it opens fully.")
            print("You enter the tower.")
            print("\n")
            levelFlag = 1

        elif response == "help":
            print(commands)
            print("\n")

        elif response == "hint":
            print("Your goal is to ascend the tower. You should enter the tower to do so.")
            print("However, looking around is never a bad idea.")
            print("\n")

        elif response == "quit":
            quitAsk = input("Are you sure you want to quit? yes/no\n")

            if quitAsk == "yes":
                print("Thank you for playing.")
                print("\n")
                time.sleep(3)
                quit()
            
            elif quitAsk == "no":
                print("You decide to stay.")
                print("\n")
            
            else:
                print("I didn't understand that.")
                print("\n")
            
        else:
            print("I didn't understand that.")
            print("\n")

# ground floor, unlit

levelFlag = 1

while levelFlag < 2:
    print("You are in a dim, spacious room.")
    response = input("Enter a command. \n")
    if response == "look around":
        print("You can see very little. Only a small amount of light follows you into the dark.")
        print("To your right, there is the dirty window you saw from outside.")
        print("Only a trickle of daylight passes the dust.")
        print("To your left, you can see what looks like an unlit torch on the wall.")
        print("Directly in front of you, you can make out a shape that might be a table and chairs.")
        print("\n")

    elif response == "left":
        print("You take a tentative step to your left, but the darkness intimidates you and you go no further.")
        print("\n")

    elif response == "right":
        print("You take a tentative step to your right, but the darkness intimidates you and you go no further.")
        print("\n")

    elif response == "forward":
        print("Walking into this darkness seems like a bad idea. You are likely to be eaten by a Grue.")
        print("\n")
        grueFlag = 1

    elif response == "backward":
        print("There is no need to leave.")
        print("\n")

    elif response == "light torch":
        print("You retrieve a lighter from your pocket and light the torch.")
        print("It catches quicker than you expect, considering the tower is supposed to be abandoned.")
        print("Let there be light!")
        print("\n")
        levelFlag = 2

    elif response == "help":
        print(commands)
        print("\n")

    elif response == "hint":
        print("It is too dark to see. Perhaps a light would be helpful.")
        print("\n")

    elif response == "quit":
            quitAsk = input("Are you sure you want to quit? yes/no\n")

            if quitAsk == "yes":
                print("Thank you for playing.")
                print("\n")
                time.sleep(3)
                quit()
            
            elif quitAsk == "no":
                print("You decide to stay.")
                print("\n")
            
            else:
                print("I didn't understand that.")
                print("\n")

    else:
        print("I didn't understand that.")
        print("\n")

# ground floor, lit

while levelFlag < 3:
    print("You are in a well lit room. Torchlight flickers and although the light is warm, \nthere is still a foreboding presence to the tower.")
    response = input("Enter a command. \n")
    if response == "look around":
        print("The room is now well lit.")
        print("You can see the room is around 15 paces long, perhaps 20 wide.")
        print("You suppose all the rooms will be this size, roughly speaking.")
        print("In the center is a dining table with six chairs. Only one place has been set.")
        print("On the left, there is a fireplace. It is, apart from dust, clean and mostly unused.")
        print("On the right, there is a small kitchen.")
        print("At the far end, there is a set of stairs that ascend, hugging the wall.")
        print("Almost everything is covered in dust, even the floor.")
        print("You cannot miss the footsteps in them.")
        print("They move directly from the entrance to the stairs, clear and confident.")
        print("You cannot tell how long it has been since they were made, but the footsteps unnerve you anyways.")
        print("\n")

    elif response == "left":
        print("You step closer to the fireplace.")
        print("Although it looks untouched, you can see the shredded and burnt remains of paper in the hearth.")
        print("You peer into the fireplace and read a few partial words from the charred papers.")
        print("'Last Wi... ment of... King...'")
        print("'By ord... resurrec... ll be perfor...'")
        print("You can't make out anything more.")
        print("You return to where you stood.")
        print("\n")

    elif response == "right":
        print("You examine the kitchen space.")
        print("The cupboards contain a few ugly, bloated cans. One shelf has a single pan on it, but nothing more.")
        print("It does not look like the kitchen has been used in centuries.")
        print("You return to where you stood.")
        print("\n")

    elif response == "backward":
        print("There is no need to leave. You should move onwards.")
        print("\n")

    elif response == "forward":
        print("You approach the stairs at the end of the room.")
        print("As you pass, you notice that one of the seats at the dining table \nis clean and set for service.")
        print("You are careful to avoid matching the footsteps in the dust.")
        print("The foreboding in you grows stronger.")
        print("\n")

        response = ""
        while response not in yes_no:
            response = input("Do you climb the stairs? yes/no ")
            if response == "yes":
                print("You ascend the stairs to the second floor.")
                print("You reach the top of the stairs. You have the vague sense that you took more steps than you expected.")
                print("\n")
                levelFlag = 3

            elif response == "no":
                print("You retreat back the way you came.")
                print("\n")
                
            else:
                print("I didn't understand that.\n")

    elif response == "help":
        print(commands)
        print("\n")

    elif response == "hint":
        print("You should take a look around before moving onwards.")
        print("\n")

    elif response == "quit":
            quitAsk = input("Are you sure you want to quit? yes/no\n")

            if quitAsk == "yes":
                print("Thank you for playing.")
                print("\n")
                time.sleep(3)
                quit()
            
            elif quitAsk == "no":
                print("You decide to stay.")
                print("\n")
            
            else:
                print("I didn't understand that.")
                print("\n")

    else:
        print("I didn't understand that.")
        print("\n")
    
# second floor, unlit

levelFlag = 3

while levelFlag < 4:
    print("This room is dark as well.")
    response = input("Enter a command. \n")
    if response == "look around":
        print("The sun outside seems to have set, and the little light it cast in here has faded.")
        print("For a brief moment, as you squint into the dark, you have the sense \nthat you and something in the gloom have locked eyes.")
        print("You quickly look away.")
        print("On your left is another torch.")
        print("On your right is a dusty darkness. You can see nothing.")
        print("\n")

    elif response == "left":
        print("You cautiously take a step to the left.")
        print("The gloom envelops you so deeply you cannot see your hands.")
        print("You immediately return to the stairway.")
        print("\n")

    elif response == "right":
        print("You take a frightened step to the right.")
        print("Before you take another, an image enters your mind.")
        print("A pair of cracked lips, licked by a foul tongue.")
        print("A mouth with too many teeth, leering in the black.")
        print("You decide against going any further.")
        print("\n")

    elif response == "backward":
        print("You should move onwards.")
        print("\n")

    elif response == "forward":

        if grueFlag == 2:
            print("You take a brief, terrified step out of the light and sense \nthat something in the dark has mimicked your movements.")
            print("A hot gust of air - some might call it a breath - ruffles your hair.")
            print("You attempt to retreat into the light, but a horrible, scaled thing wraps itself around your ankle.")
            print("Before you can react, you are dragged into the dark. You have been eaten by a Grue.")
            quit()
        
        if grueFlag == 1:
            print("There is a strong, horrifying presence looming at you from the darkness. \nYou are extremely likely to be eaten by a Grue.")
            print("\n")
            grueFlag = grueFlag + 1

        if grueFlag == 0:
            print("The room is deeply dark, more so than the previous. \nYou are likely to be eaten by a Grue.")
            print("\n")
            grueFlag = grueFlag + 1

    elif response == "light torch":
        print("You light the torch on your left, as you did the previous one.")
        print("As you fumble at your lighter, you hear a noise beneath the crack of flint.")
        print("A scuttling? A pattering? A tipping and toeing of monstrous feet?")
        print("You keep your terrified gaze set upon the blackness, but...")
        print("But there is nothing unusual to be seen as light fills the room.")
        print("\n")
        levelFlag = 4

    elif response == "help":
        print(commands)
        print("\n")

    elif response == "hint":
        print("You shouldn't take a step forward until the darkness is cleared.")
        print("\n")

    elif response == "quit":
            quitAsk = input("Are you sure you want to quit? yes/no\n")

            if quitAsk == "yes":
                print("Thank you for playing.")
                print("\n")
                time.sleep(3)
                quit()
            
            elif quitAsk == "no":
                print("You decide to stay.")
                print("\n")
            
            else:
                print("I didn't understand that.")
                print("\n")

    else:
        print("I didn't understand that.")
        print("\n")

# second floor, lit

levelFlag = 4

while levelFlag < 5:
    print("The room is now lit.")

    response = input("Enter a command. \n")
    
    if response == "look around":
        print("Whatever creature was in the dark (was there anything there at all?) has fled.")
        print("You are in an old, dusty library. The books around you are in many different languages.")
        print("The labels you can read are all old or outdated. They cite theories now proven false.")
        print("Titles like 'Trickle Down Economics' and 'Austerity Measures.'")
        print("You notice that there is no window on this floor. Where there was one on the lower floor,")
        print(" is covered up by another bookshelf.")
        print("Bookshelves line the walls from floor to ceiling.")
        print("You cannot see the far end of the room, for the bookshelves in the way.")
        print("There is an archway ahead of you, where it is darker though still safe to walk.")
        print("Though you are alone, you don't feel like it.")
        print("\n")

    elif response == "left":
        print("You approach a bookcase to your left and pull out a book.")
        print("It is leatherbound and heavy. You recognize the letters on the front, \nbut it is plainly a different language.")
        print("'księga umarłych,' it reads.")
        response = input("Open the book? \nyes/no ")
        if response == "yes":
            print("You open the book to a random page.")
            print("Well, random if someone didn't use it to hide keys.")
            print("A large brass key is pressed into a cutout in the book.")
            print("Someone plainly only opens the book to this section to retrieve their key.")
            print("You take and pocket the key.")
            print("\n")
            doorKey = 1
        elif response == "no":
            print("Well, I'm sure it's nothing.")
            print("\n")

        else:
            print("I didn't understand that.")

        print("You replace the book.")
        print("\n")

    elif response == "right":
        print("You approach a bookcase to your right and pull out a random book.")
        print("'A Practical Guide to Necromancy: The Art and Soul of Resurrection.'")
        print("Some light bedtime reading?")
        response = input("Open the book? \nyes/no ")
        if response == "yes":
            print("You open the book to a random page.")
            print("You do not recognize the words inside.")
            print("They are not even the same letters as the title, and they seem to shift around slightly.")
            print("Many of the pages are dogeared and well worn.")
            print("Even as you try to read the book, you realise that perhaps this book is reading you.")
            print("You replace the book, unsettled.")

        elif response == "no":
            print("That is probably the wise decision.")
        print("You put the book back.")
        print("\n")

    elif response == "backward":
        print("You should move onwards.")
        print("\n")

    elif response == "forward":
        print("You move deeper into the library.")
        print("The archway seems the only way forward, so you cross it.")
        print("The area ahead is darkened, but you can see the stairs ahead.")
        response = input("Approach the stairs? yes/no\n")
        if doorKey == 1 and response == "yes":
            print("You ascend the stairs. At the top step \n(how many steps was that? " + str(random.randint(6,19)) + "? It felt like more) \nyou find a door.")
            print("It is locked, but you take the key from your pocket and open the door.")
            print("It creaks open with a sense of warped age.")
            print("You enter the next room.")
            print("\n")
            levelFlag = 5

        elif doorKey == 0 and response == "yes":
            print("You ascend the stairs. At the top, you find a door.")
            print("You try the handle, but it is locked.")
            print("There is a large, brass keyhole. There are a great many scratches around it.")
            print("You return down the stairs.")
            print("\n")

        elif response == "no":
            print("You return to the entrance.")
            print("\n")

        else:
            print("I didn't understand that.")
            print("\n")

    elif response == "help":
        print(commands)
        print("\n")

    elif response == "hint":
        print("You're in a library! Take a look around, read some books.")
        print("All sorts of strange things in books these days.")
        print("\n")

    elif response == "quit":
            quitAsk = input("Are you sure you want to quit? yes/no\n")

            if quitAsk == "yes":
                print("Thank you for playing.")
                print("\n")
                time.sleep(3)
                quit()
            
            elif quitAsk == "no":
                print("You decide to stay.")
                print("\n")
            
            else:
                print("I didn't understand that.")
                print("\n")

    else:
        print("I didn't understand that.")
        print("\n")

#third floor, riddles
#(brody from Jaws voice) "you're gonna need some jankier code."

levelFlag = 5

while levelFlag < 6:
    print("This room is already lit.")

    response = input("Enter a command. \n")

    if response == "backward":
        print("You return down the stairs.")
        print("You count " + str(random.randint(6,19)) + " this time.")
        print("...but you somehow end up exactly where you started.")
        print("It would seem you are unable to retreat the way you came.")

    # i can't get this to work even though it is identical to all the previous backward levelFlags
    # programming is dumb
    # fuck it 
    # not a bug if it's a feature

    elif response == "look around" and puzzleSolved == 1:
        print("You examine the pedestal again.")
        print("Having solved the puzzle, it is empty of papers. There is no ash.")
        print("The room is empty apart from the pedestal and the doors at either end.")
        print("\n")

    elif response == "look around" and puzzleSolved == 0:
        print("Unlike the previous floors, this room is already lit.")
        print("It is bare, apart from a pedestal in the center of the room, \nand the stairs at the opposite end.")
        print("On the pedestal sits a few sheets of paper and a pencil.")
        response = input("Read the papers? yes/no \n")

        if response == "yes":
            print("You read the papers.")
            print("\n")
            print("'If you don't keep me, I will break. What am I?")
            response = input("What is your answer? \n")

            if response == "promise":
                print("You write your answer down on the paper.")
                print("As you finish, the paper suddenly bursts into sickly green flame and vanishes.")
                print("The next paper is unharmed.")
                print("\n")
                riddleStage = 1

            else:
                print("You write down your answer on the paper.")
                print("As you finish, the paper bursts into bright red flames.")
                print("It rapidly burns away, revealing... the same sheet of paper.")
                print("Wrong answer, you suppose. Try again.")
                print("\n")    

            while riddleStage == 1:
                print("You read the next sheet.")
                print("'What runs out when you push it?'")
                print("\n")

                response = input("What is your answer? \n")

                if response == "luck":
                    print("You write down your answer on the paper.")
                    print("Once again, the paper catches fire and burns away.")
                    print("There is another riddle here.")
                    print("\n")
                    riddleStage = 2

                else:
                    print("You write down your answer on the paper.")
                    print("As you finish, the paper bursts into bright red flames.")
                    print("It rapidly burns away, revealing... the same sheet of paper.")
                    print("Wrong answer, you suppose. Try again.")
                    print("\n")    

                    # this was buggy as all hell
                    # and now, though, it works
                    # it may be a problem soon

                    # spring bug reporting
                    # only write comments in haiku
                    # enraged wildfires

            while riddleStage == 2:
                print("You read the last sheet.")
                print("'I am fair, fair am I. Rich or poor, young or old, all are equal in my eye.'")
                print("\n")

                response = input("What is your answer? \n")

                if response == "death":
                    print("You write down your answer on the paper.")
                    print("The paper once again burns away.")
                    print("You hear a loud 'THUNK' come from the stairs as the door unlocks.")
                    riddleStage = 3
                    puzzleSolved = 1
                    print("\n")

                else:
                    print("You write down your answer on the paper.")
                    print("As you finish, the paper bursts into bright red flames.")
                    print("It rapidly burns away, revealing... the same sheet of paper.")
                    print("Wrong answer, you suppose. Try again.")
                    print("\n")


        elif response == "no":
            print("You leave the papers alone.")
            print("\n")

        else:
            print("I didn't understand that.")
            print("\n")

    

    elif puzzleSolved == 0 and response == "forward":
        print("You walk past the pedestal to the stairs.")
        print("You take the stairs up. How strange, you expected a puzzle.")
        print("You emerge... in the same room. Somehow, you have gone up " + str(random.randint(6,20)) + " stairs \nand ended up where you started.")
        print("Perhaps you should take a look at the pedestal.")
        print("\n")

    elif puzzleSolved == 1 and response == "forward":
        print("Having solved the puzzle, you approach the stairs.")
        print("You take the stairs with no unusual events.")
        print("It even seems like there are a normal amount of steps.")
        levelFlag = 6
        print("\n")

    elif response == "left":
        print("There's nothing else to look at.")
        print("\n")

    elif response == "right":
        print("There's nothing else to look at.")
        print("\n")

    elif response == "hint":
        print("The only hint you're getting here is to check out the pedestal.")
        print("These riddles are meant for kids, you know.")
        print("\n")

    elif response == "help":
        print(commands)
        print("\n")

    elif response == "quit":
            quitAsk = input("Are you sure you want to quit? yes/no\n")

            if quitAsk == "yes":
                print("Thank you for playing.")
                print("\n")
                time.sleep(3)
                quit()
            
            elif quitAsk == "no":
                print("You decide to stay.")
                print("\n")
            
            else:
                print("I didn't understand that.")
                print("\n")

    else:
        print("I didn't understand that.")
        print("\n")

# fourth floor, the bedroom

levelFlag = 6

while levelFlag < 7:
    print("You are on the fourth floor.")
    print("\n")

    response = input("Enter a command. \n")

    if response == "look around":
        print("You examine the room.")
        print("It is plainly a bedroom.")
        print("At the far end are the stairs to the final floor.")
        print("On your right is a bed, tall and ornate. Fit for a king.")
        print("Closer to your left, there is a desk overflowing with books and papers.")
        print("A fireplace is next to it, full of ash.")
        print("The room is not dusty, and strangely, already lit.")
        print("You cannot quite tell from where the light is coming from.")
        print("Scattered all around are more books, papers, tools whose uses you can't figure out.")
        print("The bedroom has a scent to it that you cannot place.")
        print("\n")

    elif response == "backward":
        print("You return down the stairs.")
        print("You count " + str(random.randint(6,19)) + " this time.")
        print("...but you somehow end up exactly where you started.")
        print("It would seem you are unable to retreat the way you came.")
    
    elif response == "left":
        print("You examine the desk and fireplace.")
        print("The papers and books are a mess. No rhyme or reason in their organisation.")
        print("Many of the books bear unusual runes or patterns you don't understand.")
        print("A few hold recognizable symbols of magick. One says 'animate' or 'lively,' depending on the context.")
        print("The fireplace is packed full of ash. Has it ever been cleaned?")
        print("You poke through the ash, but there is nothing of interest.")
        print("\n")

    elif response == "right":
        print("You look at the bed.")
        print("It is a well made, oak bed. There are carvings of knights and wizards on the headboard.")
        print("It is unmade, but oddly, the sheets seem clean.")
        print("In the gap between pillows, you spot a sheet of paper and pull it out.")
        print("The paper is a drawing, perhaps an early sketch for an official portrait.")
        print("The drawing is of two men, side by side.")
        print("One is older, with a beard and a crown. He stands next to the younger man, who is sitting on a quickly sketched chair.")
        print("The younger man is smiling. The older man is not.")
        print("For some reason, the picture makes you feel a little sad. You carefully replace it.")
        print("\n")

    elif response == "forward":
        print("You cross the room to the stairs.")
        print("The room unnerves you, in its solemn way.")
        print("\n")

        response = input("Ascend the stairs to the final floor? yes/no\n")

        if response == "yes":
            print("You climb the final set of stairs.")
            print("\n")
            levelFlag = 7

        elif response == "no":
            print("You decide against moving onward, for now.")
            print("\n")

        else:
            print("I didn't understand that.")
            print("\n")

    elif response == "hint":
        print("There is nothing to solve here. Look around, then move onwards.")
        print("\n")

    elif response == "help":
        print(commands)
        print("\n")

    elif response == "quit":
            quitAsk = input("Are you sure you want to quit? yes/no\n")

            if quitAsk == "yes":
                print("Thank you for playing.")
                print("\n")
                time.sleep(3)
                quit()
            
            elif quitAsk == "no":
                print("You decide to stay.")
                print("\n")
            
            else:
                print("I didn't understand that.")
                print("\n")

    else:
        print("I didn't understand that.")


# final floor, the laboratory

levelFlag = 7
while levelFlag < 8:
    print("You are on the final floor.")

    response = input("Enter a command. \n")

    if response == "look around":
        print("You examine the room.")
        print("This would appear to be a laboratory of some kind.")
        print("In the center of the room is a great big workbench.")
        print("All over it are various bottled liquids.")
        print("Beakers of bubbling, purple liquids, some steaming, some hissing, others still as death.")
        print("Many are linked up by rubber tubes, or electrickal wiring.")
        print("There is no natural light - the sun has long set - and the room is lit by a variety of electricks.")
        print("Off to the left is another bench, this one clear. It is roughly as long as you are tall.")
        print("A great many sheets of paper plaster the walls, mostly anatomical drawings.")
        print("They seem to be of humans... mostly. There are some cross sections of pointed ears.")
        print("Others of skulls with tusks and horns.")
        print("Most unnervingly, some of them are clearly stuck together, with lines denoting... incisions? Stitches?")
        print("You cannot read the scribbled, messy notes attached to them.")
        print("There is a sickly sweet scent in the air.")
        print("You swallow with a dry throat.")
        print("\n")

    elif response == "forward" and evilPlans == 0:
        print("You take cautious steps towards the central workbench.")
        print("Careful not to breathe in the steam and smoke of chemicals, you look around.")
        print("There are a great collection of not just chemicals and more books, but tools of all manner.")
        print("Bonesaws, hacksaws, scalpels, others with sinister, otherworldly looks to them.")
        print("You decide not to touch the tools and instead look through the books.")
        print("Many are again unintelligible, but you find a notebook with words you can read.") 
        print("'EXP'RIMENT NOTES'")
        response = input("Read the notebook? yes/no\n")

        if response == "yes":
            print("You open the notebook.")
            print("Much of this is legible, thankfully. You are no scientist, but \nthese are plainly hundreds of experiments.")
            print("More drawings of dead animals, labelled with many notes.")
            print("All manner of creatures have been tested. Dogs and wolves at first...")
            print("Then hawks, falcons, crows, even pigeons...")
            print("Then some freakish things that must be from the swamps nearby...")
            print("Many have 'FAILURE' scribbled underneath the drawings.")
            print("As you flick deeper into the notes, 'SUCCESS' becomes more common.")
            print("The successes have several pages devoted to them. 'Dog reviv'd f'r three days.  Did refuse to consume bef're second-death.'")
            print("'Crows gentle aft'r ressurrection.' '60~ days bef're chemical breakdown occurs'")
            print("Most horrifyingly, you eventually find not just animals, but corpses of humans and sentient beings.")
            print("Elves, dwarves, an orc, tusks chipped and cheeks sunken.")
            print("The last few pages are taken up by a single experiment, with a great collection of notes made to it.")
            print("The central drawing is of a corpse - a skeleton, really - with a crudely drawn crown added to it.")
            print("Above it, in large bold letters, is the experiments name...")
            print("'MINE OWN SON'")
            print("'SUCCESS'")
            print("Your stomach tightens. You take the notebook and decide to leave.")
            evilPlans = 1
            print("\n")

        elif response == "no":
            print("You leave the things alone.")
            print("\n")

        else:
            print("I didn't understand that.")
            print("\n")

    elif response == "forward" and evilPlans == 1:
        print("You examine the workbench again.")
        print("Nothing has changed, apart from the notebook you have stolen.")
        print("You do not know what these chemicals and sciences are for, but you can guess.")
        print("You should go.")
        print("\n")

    elif response == "backward" and evilPlans == 0:
        print("You cannot leave just yet. You should investigate further.")
        print("\n")

    elif response == "backward" and evilPlans == 1:
        print("You practically bolt out the door, leaving the horror show behind.")
        print("The stairs creak beneath your rapid footsteps as you flee.")
        print("Out past the unmade bed, through the strange riddle room")
        print("Back down through the library, the kitchen behind you.")
        print("You flee out into the night. The darkness out here is safer than any in the tower.")
        print("You don't pause to collect yourself and instead immediately head south for Dead Orleans.")
        print("You must be spread the word. A necromancer is at large...")
        print("\n")
        print("Thank you for playing! This was The Tower, a text adventure.")
        print("This was my first game. I hope you liked it.")
        print("Written and programmed by Billy Walker.")
        time.sleep(30)
        print("\n")

    elif response == "left":
        print("You approach the workbench on the left.")
        print("There are an unnerving collection of stains, only some of them blood.")
        print("You can take a closer look at some of the drawings.")
        print("They indicate areas on the body. Only some of the writing is legible.")
        print("'Resurrectionism... Surgical assessments...' symbols that resemble black magicks...")
        print("You had better finish looking around and leave, quickly.")
        print("\n")

    elif response == "right":
        print("You examine some of the equipment more closely.")
        print("The largest container is a colorless liquid.")
        print("You (really quite foolishly) take a sniff of it. It smells like pickles.")
        print("You feel a little lightheaded. Don't do that again.")
        print("There are other jars you decide against touching.")
        print("You track the wiring with your eyes, weaving its way from ")
        print("the bench on the left to a large container full of some mysterious fluid and what looks like")
        print("copper or bronze plates. Probably wise to leave it alone.")
        print("More cabling runs from the containers up and out through the window. You cannot see where it leads.")
        print("\n")

    elif response == "hint":
        print("There is no need for a hint here. I advise you look around thoroughly before leaving.")
        print("\n")
    
    elif response == "help":
        print(commands)
        print("\n")

    elif response == "quit":
            quitAsk = input("Are you sure you want to quit? yes/no\n")

            if quitAsk == "yes":
                print("Thank you for playing.")
                print("\n")
                time.sleep(3)
                quit()
            
            elif quitAsk == "no":
                print("You decide to stay.")
                print("\n")
            
            else:
                print("I didn't understand that.")
                print("\n")

    else:
        print("I didn't understand that.")
        print("\n")