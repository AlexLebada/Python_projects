from RPG_battle.classes.game import bcolors

def gui_status():
    print("\n\n")
    print("NAME                  HP                                   MP")
    print("                       _________________________           __________")
    print(bcolors.BOLD + "Valos:         " +
          "460/460|" + bcolors.OKGREEN + "█████████████████████████" + bcolors.ENDC + bcolors.BOLD
          + "|    " +
          "65/65|" + bcolors.OKBLUE + "██████████" + bcolors.ENDC + "|")

    print("                       _________________________           __________")
    print("Valos:         460/460|█████████████████████████|    65/65|██████████|")

    print("                       _________________________           __________")
    print("Valos:         460/460|█████████████████████████|    65/65|██████████|")

    print("\n\n")