import time
index = ["help", "Y", "y", "N", "n", "left", "right", "forward"]
people = [("clementine's respect for you" == 1), ("Lee Everett" == 1)]
inventory = ["Baseball bat".lower(), "switchblade".lower(), "Fists".lower()]
null_key = "Invalid selection!"

while True:
    def ask_play_game():
        while True:
            yes_no = input("Would you like to play the Zombie game? Y/N: ")
            if yes_no.lower() == "y":
                print("""Game Started!
                This game is filled to the brim with death! You'll need to pick the right path to survive.""")
            elif yes_no.lower() == "n":
                print("Maybe next time!")
            else:
                print("Invalid input, please enter yes (Y) or no (N).")


    while True:
        Yes_No = input("Would you like to play the Zombie game? Y/N: ")
        if Yes_No.upper() == "Y" or Yes_No.lower():
            print("""Game Started!
            This game is filled to the brim with death! You'll need to pick the right path to survive.""")
            break
        elif Yes_No.lower() == "n":
            print("Maybe next time!")
            exit()
        else:
            print("Invalid input, please enter yes (Y) or no (N).")

    answer_ally = input('''You wake up in an ally, there's fire EVERYWHERE!
You turn down an ally theres a convicted murderer to your left and a tax evader to your right 
and a unknown street ahead. Where do you go?
    left - convicted murderer
    right - Tax Evader
    Forward - Unknown street ahead: ''')

    if answer_ally == "left":
        print("""You go left even knowing theres a blood thirsty murderer to you left.
            Not surprisingly you are immediately murdered!  He eats your face!""")
        import os
        import sys


        def restart_program():
            python = sys.executable
            os.execl(python, python, *sys.argv)


        while True:
            answer = input("Would you like to play again? Y/N: ")
            if answer.lower() == "y":
                restart_program()
            elif answer.lower() == "n":
                break

    if answer_ally == "right":

        answer_pay_YN = input("""You run right, directly into the path of the tax evader.
                 you get lucky as its not tax season and he's not mad.
                    He promises to let you walk if you pay him $100.00  . Do You pay him Y/N: """)
        while answer_pay_YN != "Y".lower() and answer_pay_YN != "N".lower():
            print("INVALID RESPONSE")
            answer_pay_YN = input("""You run right, directly into the path of the tax evader.
                             you get lucky as its not tax season and he's not mad.
                                He promises to let you walk if you pay him $100.00  . Do You pay him Y/N: """)

        if answer_pay_YN == "y":
            pass
        if answer_pay_YN.lower() == "n":
            answer_pay_N = input("""The tax invader curses and pulls a knife on you!
                        DO YOU...
                        A) - Try and swat it away?
                        B) - change your mind and give him the money.
                        C) - summon Cthulhu to eat him
                        Player Response: """)

            # Tax answer number 1
            if answer_pay_N == "A".lower():
                answer_pay_N1 = input("""You attempt to swat the knife away and get stabbed in the gut
                        You DIE!
                        Retry? Y/N : """)

                while answer_pay_N1 != "Y".lower() and answer_pay_N1 != "N".lower():
                    print("INVALID RESPONSE")

                    answer_pay_N1 = input("""You attempt to swat the knife away and get stabbed in the gut
                        You DIE!
                        Retry? Y/N : """)
                if answer_pay_N1 == "Y".lower():
                    continue
                if answer_pay_N1 == "N".lower():
                    print("Game END!")
                break
            if answer_pay_N == "B".lower():
                print("The tax evader decides you should have died anyway and stabs you through the neck.")
                break

            if answer_pay_N == "C".lower():
                lee_summons_cthulu = input("""Lee Summons Cthulhu
                        Lee is killed and eaten by Cthulhu!
                        Restart Game Y/N?: """)

                if lee_summons_cthulu == "y".lower():
                    continue

                elif lee_summons_cthulu == "N".lower():
                    print("Game END!")
                    break
                else:
                    print("INVALID RESPONSE")
            else:
                print("INVALID RESPONSE")

        if answer_pay_YN == "y".lower():
            answer_pay_YN = input("""you pay him and he lets you go. you see a farm house in the distance. a residential 
            neighbourhood to your " "left and a church to your right.
                  
                  forward - Go to farm house,
                  left - Go to residential neighbourhood,
                  right - Go to the church :  """)
        if answer_pay_YN == "forward":
            answer_farm_house = input("""You walk to the farm house... you see one zombie in the window.
                 There could be more but you won't know until you go in.
                      Does Lee kick in the Front door! He could also go though the basement door or jump through the window?
                      
               front - Lee KICKS down the front door
               basement - Lee goes through the basement door.
                window - Lee goes through the window
                : """)
            if answer_farm_house == "front":
                print("""Lee kills the zombie!
                        He lives happily in that farm house and clementine goes to live with her parents.)
                        Thanks for playing!
                        Credits:
                        Ideas/programmer David Tuckey""")

            if answer_farm_house == "basement":
                print("""Lee kills the zombie!
                                        He lives happily in that farm house and clementine goes to live with her parents.
                        Thanks for playing!
                        Credits:
                        Ideas/programmer David Tuckey""")

            if answer_farm_house == "window":
                print("""Lee climes through the window and kills the zombie!
                                        He lives peacefully in that farm house and clementine goes to live with her parents.
                                        
                            Thanks for playing!
                            Credits:
                            Ideas/programmer David Tuckey""")

#GO LEFT
        elif answer_pay_YN == "left".lower():
            answer_residential_neighbourhood = input("""You walk to the residential neighbourhood.
                      you hear a sound coming from the trunk of an abandoned car. open the trunk? Y/N : """)
            if answer_residential_neighbourhood == "Y".lower():
                answer_open_trunk_Y = input("""You open the trunk and find a girl.
                          she's 11, she tells you her name is clementine and You introduce your self as Lee
                           she tells you that a crazy guy locked her in the trunk.
                          Try to find the guy who did this?.....  Y/N:  """)
                if answer_open_trunk_Y.lower() == "n":
                    print("Your a horable person!")
                    break
                if answer_open_trunk_Y.lower() == "y":
                    answer_house_search = input("""You start searching the nearby houses and find him.
                    He's dead, the needle still sticking out of his forearm with a switchblade in his pocket.
                    Found item : switchblade
                        return - return to clementine :)
                        leave - continue the story by your self... : """)
                    if answer_house_search == "return".lower():
                        answer_lee_zombie_horde = input("""You return to clementine. she tells you...
                              clementines cut off by the sound of gun fire in the house next door.
                              two people a man and woman run out with a HOARD of zombies right behind them.
                              
                              weapons at your disposal include: baseball bat, switchblade, and your fists.
                              Options:
                              Help  - Lee will attempt to help the two people.
                              Dont - Lee and clementine will flee.
                              : """)
                        if answer_lee_zombie_horde == "Help".lower():
                            weapon_check = input("what weapon?: ")
                            if weapon_check == "switchblade":
                                Lee = input("""Lee starts stabbing the zombies one by one in the eye and the two people
                                    manage to get to safety""")

                            while weapon_check not in inventory:
                                print("not in inventory")
                                weapon_check = input("what weapon?: ")

                        elif answer_lee_zombie_horde == "Dont".lower() or answer_lee_zombie_horde == "Don't".lower():
                            answer_dont = input("""Lee and clementine flee to a nearby building.
                                            They watch in horror as the man and woman get ripped to pieces by zombies""")

    elif answer_ally == "forward".lower():
        answer_zombie_kid_car_YN = input(
            """You make your way out of the ally and notice a zombie trying to eat a little kid in a car. help them?
            Y/N: """)
        if answer_zombie_kid_car_YN == "Y".lower():
            if answer_zombie_kid_car_YN != "Y".lower() or answer_zombie_kid_car_YN == "N".lower():
                print("Your response does not contain letters Y or N")
            answer_help_kid = input("""You decide to help the kid. you have an option of a 
            Type (A): brick - Use brick on zombie
            Type (B): baseball bat - Use baseball bat """)
            if answer_help_kid == "A".lower():
                print('''You smash the zombie in the head with the brick!.
             The zombie collapses and dies.''')

            if answer_help_kid == "B".lower():
                answer_strike_zombie_with_bat = input("""
                You STRIKE the zombie with the bat! The zombie is killed!
                
                you notice that the sound of the zombie being killed has attracted other zombies in the area.
                          You tell clementine that they need to move and begin to sneak your way out of the area.
                          You move slowly, being careful not to attract attention to yourself.
                          However, as you round a corner, you see a group of zombies blocking your path.
                          
                         A) Fight your way through the zombies with your weapon of choice.
                         B) Look for an alternative escape route.
                
                        Your response: """)
                if answer_strike_zombie_with_bat == "A".lower():
                    print("""You fight off the zombies and make a run for it,
                            successfully escaping the area with clementine. """)

                    time.sleep(7)

                    input("""If you successfully fight off the zombies and escape the area with the kid,
                     Lee and Clementine find themselves in a deserted street with no one in sight.
                      Lee breathes a sigh of relief.
                       They realizes that they need to find a safe place to hide and plan your next move.""")

                if answer_strike_zombie_with_bat == "B".lower():
                    print("""You find a back alley and make your way out of the area undetected.
                    You become lost in the maze of streets and alleys, eventually becoming trapped by a group of zombies.
                    Lee and clementine try to fight them off but there luck runs out.
                    They become the next lunch for those zombies.""")
                    answer = input("Would you like to play again? Y/N: ")
                    if answer.lower() == "y":
                        continue
                    elif answer.lower() == "n":
                        print("Good By")
                        break
