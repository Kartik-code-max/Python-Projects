def intro():
    print("You find yourself in a strange land, surrounded by unfamiliar sights.")
    print("You have no memory of how you got here, but you know one thing: you must survive.")
    print("You look ahead and see two paths leading into the unknown.")

    choice = input("Do you take the [left] path or the [right] path? ")

    if choice.lower() == "left":
        forest_path()
    elif choice.lower() == "right":
        mountain_path()
    else:
        print("You stand still, unsure of what to do. Time passes. You must decide!")
        intro()


def forest_path():
    print(
        "\nYou walk into a dense, dark forest. The trees are towering above you, their branches twisting like fingers.")
    print("As you venture deeper, you hear rustling in the bushes. Something is watching you.")

    choice = input("Do you [run] or [hide]? ")

    if choice.lower() == "run":
        print("\nYou sprint forward, heart pounding. The sound grows closer, but you manage to escape into a clearing.")
        treasure_hunt()
    elif choice.lower() == "hide":
        print(
            "\nYou crouch behind a tree, holding your breath. The rustling stops, and after a few minutes, you feel safe again.")
        encounter_mystic()
    else:
        print("Indecision costs you precious time. The danger grows closer.")
        forest_path()


def mountain_path():
    print("\nThe path is steep, rocky, and treacherous. But you're determined to climb it.")
    print("As you reach a narrow ledge, a strong wind almost knocks you off your feet.")

    choice = input("Do you [continue] climbing or [turn back]? ")

    if choice.lower() == "continue":
        print("\nYou dig your fingers into the rock and push through the wind. Eventually, you reach the summit.")
        discover_treasure()
    elif choice.lower() == "turn back":
        print(
            "\nYou decide it's too dangerous and turn back. Unfortunately, as you descend, the rocks beneath you crumble.")
        print("You fall... Game Over.")
    else:
        print("The wind howls as you hesitate. The path ahead waits for your choice.")
        mountain_path()


def treasure_hunt():
    print("\nIn the clearing, you notice something gleaming on the ground. It's a treasure chest!")

    choice = input("Do you [open] the chest or [leave] it? ")

    if choice.lower() == "open":
        print("\nInside, you find gold coins and a mysterious map leading to more riches.")
        print("Congratulations! You've found the treasure and won the game!")
    elif choice.lower() == "leave":
        print("\nYou decide not to take any chances and leave the chest behind.")
        print(
            "As you walk away, you hear a click. The ground opens up beneath you, and you fall into a pit. Game Over.")
    else:
        print("The treasure tempts you, but you must make a decision.")
        treasure_hunt()


def encounter_mystic():
    print("\nAs you catch your breath, an old mystic appears from the shadows.")
    print("She offers you a choice: Wisdom or Power.")

    choice = input("Do you choose [wisdom] or [power]? ")

    if choice.lower() == "wisdom":
        print(
            "\nThe mystic reveals secrets of the universe to you. Your mind expands, and you leave the forest enlightened.")
        print("You win through knowledge and insight!")
    elif choice.lower() == "power":
        print("\nThe mystic grants you immense strength, but you are corrupted by your own desire for control.")
        print("Eventually, you lose yourself. Game Over.")
    else:
        print("The mystic waits patiently for your decision.")
        encounter_mystic()


def discover_treasure():
    print("\nAt the summit, you see a cave. Inside, there's an ancient artifact glowing with power.")

    choice = input("Do you [take] the artifact or [leave] it alone? ")

    if choice.lower() == "take":
        print("\nAs you grab the artifact, the cave begins to collapse!")
        print("You barely escape with your life, but the artifact is yours. You win!")
    elif choice.lower() == "leave":
        print("\nYou respect the ancient powers and leave the artifact untouched.")
        print("As you descend the mountain, you feel at peace. You win through wisdom!")
    else:
        print("The artifact hums with energy. You must decide what to do.")
        discover_treasure()


# Start the game
intro()
