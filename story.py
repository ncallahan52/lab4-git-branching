def intro():
    print("You wake up falling from the sky, hundreds of miles per hour.")
    print("You notice a parachute backpack falling to your right.")
    print("You notice your best friend on your left.")
    
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("You flail in indecision. The wind howls…and the moment passes.")

def left_path():
    print("You veer left toward your best friend, hoping you can help.")

def right_path():
    print("You dive right toward the parachute backpack.")

if __name__ == "__main__":
    intro()
