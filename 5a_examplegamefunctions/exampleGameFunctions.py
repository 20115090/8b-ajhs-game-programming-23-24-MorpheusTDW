#example game functions project phillip henry v1.0
import random
def functionOne():
    pass


def playerselect(row, playernumber, charcterpick, column ):
    if row > 5 and playernumber >= 1 and charcterpick == 'kimberly':
        charcterpick = True
    elif row > 6 and playernumber >= 3 and charcterpick == 'jackthedog':
        charcterpick = False 
    else:
        print('choose a fighter in the ring')
        incorrectfighter = True
        return incorrectfighter
    return playerselect
def choosefighter(row):
    print('player 1 please choose a fighter')
    if row > 5:
        playerselect = 'anyone from row 5'
        fightersfromrow5 = ('kimberly, jack, reaper, chaos, scorpion, zero, kasmo')
        fighterlist = ['kimberly']

print("Welcome to the Fighting Game!")   
maps = ["City", "Forest", "Arena"]
print("Select a Map:")
for i, map_option in (maps, 1):
    print(f"{i}. {map_option}")
    map_choice = (input("Enter the number of your chosen map: "))
    selected_map = maps[map_choice - 1]
    
   