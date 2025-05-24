import rolling_dice_functions as rdf

"""
App to simulate the rolling of 1-2 dice. 
"""


while True:
    user_choice = input("Choose your roll. [1-2] ")
    num_dice = rdf.parse_input(user_choice)

    roll_results = rdf.roll_dice(num_dice)
    dice_face_diagram = rdf.generate_dice_faces_diagram(roll_results)
    print(f"\n{dice_face_diagram}")
    again = input("\n Run again? (yes/no) ")
    if again == "yes":
        continue
    else:
        break
