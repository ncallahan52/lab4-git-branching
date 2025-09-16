def intro():
    print("You wake up falling from the sky, wind screaming past.")
    print("Parachute to the right. Best friend to the left.")
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Hesitation is its own gravity. You commit too late.")

def left_path():
    print("You speed left, locking arms with your friend.")
    print("Below: the emergency supply drone! A ripcord handle dangles.")
    act = input("Do you (grab) the drone handle or (stabilize) your friend? ").strip().lower()
    if act == "grab":
        print("You snatch the handle; a rescue chute snaps open above both of you!")
        print("Hero move. You steer toward a clearing. You both survive.")
    elif act == "stabilize":
        print("You stabilize your friend first, syncing your tumble.")
        print("Teamwork pays off, the drone auto-detects and deploys a chute for two.")
        print("You land together, laughing in shock.")
    else:
        print("Choice lost to the wind. But fate is kind and the drone deploys anyway.")

def right_path():
    print("You spear toward the parachute backpack, catching it midair.")
    print("Without thinking, you snap it open, then angle back toward your friend.")
    print("You reach them just in time and share the harness. Two heroes, one chute.")

if __name__ == "__main__":
    intro()
