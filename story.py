def intro():
    print("You wake up falling. The world is a roar of wind and fear.")
    print("Parachute to the right. Best friend to the left.")
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("You hesitate—the sky does not.")

def left_path():
    print("You cut left toward your friend, but a black-gloved drone paces you.")
    print("Its speaker crackles: 'One life for power. Nod, and I save you alone.'")
    bargain = input("Do you (nod) to accept or (refuse) the bargain? ").strip().lower()
    if bargain == "nod":
        print("A chute blossoms above you alone. Your friend spins away, eyes wide.")
        print("You land with a strange coin in your palm. It hums with promises.")
        print("Power always exacts interest. The villain’s path begins.")
    elif bargain == "refuse":
        print("You refuse. The drone snarls and peels away.")
        print("No deal, no help. But your friend grabs your arm'Together!'")
        print("You tumble, improvise a harness from straps, and both barely survive.")
    else:
        print("Silence answers the drone. It loses interest. Gravity does not.")

def right_path():
    print("You seize the parachute, but a second pack flickers into existence.")
    print("'Choose,' whispers a voice. 'Use it for you (self) or share it (share)?'")
    use = input("Your choice? (self/share): ").strip().lower()
    if use == "self":
        print("You pull alone. The ground races up for your friend. The coin appears in your pocket.")
        print("You land safely.")
    elif use == "share":
        print("You split the harness and angle back. The voice fades, disappointed.")
        print("Not a villain today. You both live.")
    else:
        print("No answer, no mercy. The sky judges quickly.")

if __name__ == "__main__":
    intro()
