
# Text Adventure Game: Condition 3
# Olive Stokoszynski, DaeQuan Peele, Faye Glynn
# April 9, 2020

#Refactor into python3 by Daequan Peele
#April 9, 2025
import random
from colorama import Fore, Style
# The items the player has taken.
restart_inventory = ["twan notebook", "apartment key"]
inventory = ["twan notebook", "apartment key"]
# Descriptions for each item the player can take.
itemDescriptions = {"twan notebook" : "An event planner for writing TWANs. There are recent notes, even though you’ve been on vacation for weeks.", "apartment key" : "Your apartment key. Home sweet home.", "ajax can" :"A can of Ajax. It may come in handy later.", "sab key" : "A key to the SAB closet in Woolworth room.", "pool cue" : "A pool cue. It might be useful for prying something open or self defense.", "classroom note" : "A note you found in the classroom. It reads: 'Beware the beast that awaits you at Ground Hunt. Bring a bucket if you want to leave with your life'.", "library note" : "A note you found in the library. It reads: 'haha funne dmq plus another thing defeat beast.'", "key fob" : "A key fob. It will let you enter other buildings.", "pizza dough" : "Pizza dough you found in the PFM. Try throwing it at the grease monster.", "bucket" : "A bucket. Might be good for mixing things.", "dmq" : "A jug of DMQ you found in the clinic. Wonder what it's good for?"}
currentRoom = "nowhere"

y = Fore.YELLOW
reset = Style.RESET_ALL

def gameoval():
  print("\nGAME OVER")
  print("Would you like to play again? (y or n)")

  if input() == "y":
    print("Very well, you begin anew.")
    print("")
    print("")
    inventory.clear()
    startGame(restart_inventory)
  else:
    print("ok bye")
def common(userInput, inventory, description):
  match(userInput):
    case "help": 
      print("\nHere are some commands that might come in handy:\nlook - tells you the description for the room you're in\ninventory - tells you all the items you currently have\nexamine (item) - gives you the description for an item in your inventory\ne - quits the game\n\nAll correct inputs will be 'use [noun]', 'go [place]', or just '[place]'.\nPossible inputs can be written in yellow")
    case "look":
      print(description)
    case "inventory":
      for item in inventory:
        print(item)
    case "e":
      print("\nExiting...")
      exit()
    case _:
      parts = userInput.split()
      #print(f"DEBUG: parts = {parts}")
      match parts:
        case ["examine", *rest] if " ".join(rest) in inventory:
          print(f"{itemDescriptions[" ".join(rest)]}")
        case ["use", *rest] if " ".join(rest) in inventory:
          use_command(" ".join(rest))
        #print(itemDescriptions[item])
        case ["examine", _] | ["use", _]:
          print("Item not in inventory")
        #case _:
        #  print("Unknown Command")    
        #print(repr(input.split()))
  return False
def use_command(item):
  global currentRoom
  match currentRoom:
    case "wattsLawn":
      print("Nothing to use that on.")
    case _:
      print("Not implemented yet! (teehee)") 
# The intro to the game
def startGame(inventory):
  print("Welcome to Condition 3!\n\nIn this adventure, you are Taylor Parsons,investigating NCSSM while on vacation after hearing about the sudden disappearance of all the student body and faculty.\nMany rumors have manifested about what the cause of the disappearance was including:\nA viral outbreak in Royall,\nA monster that materialized from cafeteria grease,\nand A shadowy beast that emerged from Ground Hunt.\n\nYou are NCSSM's last hope: \nYour is goal to find and rescue the students and faculty, return the campus to its glory, and provide a safe, fun, and engaging experience for its people. \nAre you ready to begin? (y or n)")

  #input = input()

  if input() == "y":
    print("\nYou approach the derelict institution with your mind clear, trying to stay focused." \
    "\nYou check your watch, it's a tad bit past check. " \
    "\nYou look up to see WATTS HOSPITAL in decrepit gold lettering. It’s time to get to the bottom of this.")
    #print("swag centipede")
    wattsLawn(inventory)
  else:
    print("ok bye")
    return
  # Watts Lawn, the first area. The player can travel to Hill Street or Royall, and attempt to travel to Bryan.

def wattsLawn(inventory):
  global currentRoom
  currentRoom = "wattsLawn"
  actions = 0
  locale = "\n++++++++++++" +"\nWatts Lawn\n"+"++++++++++++\n" 
  description = "You step foot onto Watts Lawn. It's usually sparsely populated, though this is...different.\nYou can’t get into most of the buildings without your key fob, but you need to get inside to investigate."
  print(locale)
  print(description)
  
  while True:
    if actions < 5:
      print("\nWhere will you go?")
    else:
      print("\nTry saying "+Fore.YELLOW+"Bryan, Royall, Hunt or Hill."+Style.RESET_ALL)
    #Test of ball knowledge, do you know NCSSM campus?
    userInput = input("> ").strip().lower()
    
    match userInput:
      case "bryan":
        print("You walk to the main entrance, but the door won't open. Try somewhere else.")
        actions += 1
      case "royall":
        royall(inventory)
      case "hunt":
        print("You can't go in there without a fob.")
        actions += 1
      case "hill":
        print("You walk over to Hill Street. There's not much here.")
        hillStreet(inventory)
        #actions += 1
      case "etc" | "pec" |"pfm" | "reynolds" | "watts" | "beall" | "hunt":
        print("You can't get there without a fob.")
        actions += 1 
      case "north" | "south" |"east" | "west":
        print("Try saying a building instead of a direction.")
        actions += 1
      case _:
        print("Unknown Command")
        actions += 1
    if common(userInput, inventory, description):
      continue
    
  # Royall, a sub-area the player can travel to without a fob. If the player enters, they lose.
def royall(inventory):
  print("\nRoyall\nThe infected surroundings of Royall have taken over your body, and you succumb to a mysterious infection. \nYou pass out and fall into a coma. Pathologists will study this event for ages.")
  gameoval()
  # The next area after Watts Lawn. From here, the player progresses into Ground Hill through the back door.
def hillStreet(inventory):
  global currentRoom 
  currentRoom = "hillStreet"
  locale = "\n+++++++++++++" + "\nHill Street\n"+"+++++++++++++\n"
  description = "The road in front of Hill House, once used for Happy Half and casual conversation. \nThere are still faint lines of chalk from a recent block party. \nThe" +Fore.YELLOW+"main door"+Style.RESET_ALL+"to Hill is"+Fore.GREEN+" locked"+Style.RESET_ALL+", but perhaps you can go around to the"+Fore.YELLOW+"back door"+Style.RESET_ALL+"."
  print(locale)
  print(description)

  while True:
    userInput = input("> ").strip().lower()
    
    match userInput:
      case "back door" | "go around" | "behind":
        print("As always, the back door is unlocked. You open the door and walk into Ground Hill.")
        groundHill(inventory)
      case "front door" | "main door":
        print("You can't get inside without a key fob.")
      case "watts":
        print("There's no reason to go back to Watts.")
      case "window":
        print("You can't open the window.")
      case _:
        print("Unknown Command")
    if common(userInput, inventory, description):
      continue

# Ground Hill, the player's entrance to the rest of the building. The player can travel to First Hill or Hill Tunnel.
def groundHill(inventory):
  global currentRoom 
  currentRoom = "groundHill"
  locale = locale = "\n+++++++++++++" + "\nGround Hill\n"+"+++++++++++++\n" 
  description = "The lower floor of Hill, used primarily for Language and Residential Education classes. \nThe classrooms are locked, but it looks like the "+Fore.YELLOW+"elevator"+Style.RESET_ALL+"is operational. \nThe "+Fore.YELLOW+"tunnel"+Style.RESET_ALL+" is also open."
  print(locale)
  print(description)
  while True:
    userInput = input("> ").strip().lower()
    
    match userInput:
      case "elevator":
        print("You take the elevator up to First Hill.")
        firstHill(inventory)
      case "tunnel":
        print("You walk into Hill Tunnel.")
        hillTunnel(inventory)
      case _:
        print()
    if common(userInput, inventory, description):
      continue

# First Hill, one of two areas the player can access from Ground Hill. The player can access their apartment and the bathroom, or travel to Hill Lounge or Ground Hill.
def firstHill(inventory):
  locale = "\n+++++++++++++" + "\nFirst Hill\n"+"+++++++++++++\n"
  description = "Your domain. You can travel to the"+Fore.YELLOW+"bathroom"+Style.RESET_ALL+", your "+Fore.YELLOW+"apartment"+Style.RESET_ALL+", "+Fore.YELLOW+"Hill Lounge"+Style.RESET_ALL+", or "+Fore.YELLOW+"Ground Hill"+Style.RESET_ALL+"."
  print(locale)
  print(description)
  while True:
    userInput = input("> ").strip().lower()
    
    match userInput:
      case "bathroom":
        if "ajax can" in inventory:
          print("You inspect the bathroom. Nothing else of use inside.")
        else:
          print("You inspect the bathroom. There is a can of Ajax. Will you take it? "+y+"(y or n)"+reset)
          response = input()
          if response == "y":
              print("You take the Ajax and return to the hallway.")
              inventory.append("ajax can")
          else:
              print("You leave the Ajax behind and return to the hallway.")
      case "apartment":

        if "SAB key" in inventory:
          print("You go inside your apartment. There doesn't seem to be anything else you need.")
        else:
          print("You go inside your apartment. Looks like all of your stuff is still here. There's a familiar key on the table. Will you take it?" +y+"(y or n)"+reset)
          response = input()
          if response == "y":
              print("You pocket the key and return to the hallway. It appears to be the key to the SAB closet in Woolworth.")
              inventory.append("SAB key")
          else:
              print("You leave the key behind and return to the hallway.")

      case "lounge":
        print("You walk over to Hill Lounge.")
        hillLounge(inventory)
      case "ground hill":
        print("You go back down the elevator to Ground Hill.")
        groundHill(inventory)
      case _:
        print("Unknown Command")
    if common(userInput, inventory, description):
      continue

# Hill Lounge. The player needs to go here to get the pool cue in order to open the door to Ground Watts.
def hillLounge(inventory):
  description = "\nFirst Hill\nThe main lounge of Hill House. Ugh, the pool table is uncovered. You can return to First Hill or go to Ground Hill. There is a pool cue lying on the table."
  print(description)

  while True:
    userInput = input("> ").strip().lower()
    match userInput:
      case "pool cue":
        if "pool cue" in inventory:
          print("You've already taken the pool cue.")
        else:
          print("You take the pool cue.")
          inventory.append("pool cue")
          description = "\nFirst Hill\nThe main lounge of Hill House. Ugh, the pool table is uncovered. You can return to First Hill or go to Ground Hill."
      case "first hill":
        print("You return to First Hill.")
        firstHill(inventory)
      case "ground hill":
        print("You go down to Ground Hill.")
        groundHill(inventory)
      case _:
        print("Unknown Command")
    if common(userInput, inventory, description):
      continue

# Checks if the door to Ground Watts is open. It is set to true when the boards have been pryed off.
wattsDoorOpen = False

# Hill Tunnel. The player needs the pool cue to progress in order to pry the boards off the door to Ground Watts.
def hillTunnel(inventory):
  actions = 0
  description = "\nHill Tunnel\nThe underground tunnel connecting Ground Hill and Ground Watts. Very convenient to have when it’s raining. To your north is the door to Ground Watts, and to your south is Ground Hill."
  if wattsDoorOpen == False:
    description += " The door to Ground Watts has been boarded shut."

  print(description)
  while True:
    userInput = input("> ").strip().lower()
    match userInput:
      case "pry boards":
        if wattsDoorOpen:
          print("You've already taken the boards off.")
        elif "pool cue" in inventory:
          print("You pry the boards off the with the pool cue.")
          actions += 1
          wattsDoorOpen = True
          description = "\nHill Tunnel\nThe underground tunnel connecting Ground Hill and Ground Watts. Very convenient to have when it’s raining. To your north is the door to Ground Watts, and to your south is Ground Hill."
        else:
          print("You don't have anything to take the boards off with.")

      case "door":
        if wattsDoorOpen:
          print("You enter the door into Ground Watts.")
          groundWatts(inventory)
        else:
          print("The door is boarded shut.")
          actions += 1
      case "ground hill":
        print("You return to Ground Hill.")
        groundHill(inventory)
      case _:
        print("Uknown Command")
    if common(userInput, inventory, description):
      continue

    print("Try prying the boards off with something. Use the help command to get a list of basic commands.") if actions > 4 and wattsDoorOpen == False else None

# Ground Watts. From here, the player can access the classroom, First Watts, and Hill Tunnel.
def groundWatts(inventory):
  description = "\nGround Watts\nThis was once used for humanities classrooms, now, it's empty. There is an open classroom to your left. You can return to Hill Tunnel, go up to First Watts, or enter the classroom."
  print(description)
  while True:
    userInput = input("> ").strip().lower()
    match userInput:
      case "classroom":
        if "classroom note" in inventory:
          print("A classroom. There isn't anything else in here.")
        else:
          print("A classroom, usually filled with the social sciences. The lack of windows does make it a tad stuffy though...but maybe that’s the point. There's a note attached on one of the desks. Will you read it? (y or n)")
        response = input()
        if response == "y":
          print("It reads: 'Beware the beast that awaits you at Ground Hunt. Bring a bucket if you want to leave with your life'.\nYou shrug and put the note in your TWAN notebook.")
          inventory.append("classroom note")
        else:
          print("You ignore it and leave the room.")
      case "tunnel":
        print("You return to Hill Tunnel.")
        hillTunnel(inventory)
      case "first watts":
        print("You go up the stairs to First Watts.")
        firstWatts(inventory)
      case _:
        print("Unknown Command")
    if common(userInput, inventory, description):
      continue

# First Watts. Has the entrance to Reynolds Hallway, and a notice not to go to Royall
def firstWatts(inventory):
  description = "\nFirst Watts\nAdministrative offices were located here, but honestly it really clashed with the hospital aesthetic. There's a notice on the door:\n'Notice- Royall has been closed down for renovations. Please do not go near it, it may prove dangerous. ~The Chancellor.'\nYou can go back to Ground Hill or to Reynolds Hallway."
  print(description)
  while True:
    userInput = input("> ").strip().lower()
    match userInput:
      case "ground hill":
        print("You walk down to Ground Hill.")
        groundHill(inventory)
      case "reynolds":
        print("You walk through Watts to Reynolds Hallway.")
        reynoldsHallway(inventory)
      case _:
        print("Unknown Command")
    if common(userInput, inventory, description):
      continue
# Reynolds Hallway. Transition area to get to Bryan Hallway.
def reynoldsHallway(inventory):
  description = "\nReynolds Hallway\nThe Art Studio is here, as well as some female halls. It leads to Bryan Hallway and First Watts."
  print(description)
  while True:
    userInput = input("> ").strip().lower()
    match userInput:
      case "watts":
        print("You walk through the hallway to First Watts.")
        firstWatts(inventory)
      case "bryan":
        print("You follow the hallway into Bryan Hallway.")
        bryanHallway(inventory)
      case _:
        print("Unknown Command")
    if common(userInput, inventory, description):
      continue

# Bryan Hallway. From here, the library, Bryan Lobby, the PFM, and Reynolds Hallway can be accessed.
def bryanHallway():
  description = "\nBryan Hallway\nOne of the main highways of NCSSM. You can get to the Library, Bryan Lobby, and the PFM using this, or to Reynolds Hallway."
  print(description)
  while True:
    userInput = input("> ").strip().lower()
    match userInput:
      case "library":
        if "library note" in inventory:
          print("The library is locked.")
        else:
          print("The library is locked, but there's a note stuck to the door. Will you read it? (y or n)")
        response = input()
        if response == "y":
          print("It reads: 'haha funne dmq plus another thing defeat beast.'\nYou shrug and put the note in your TWAN notebook.")
          inventory.append("library note")
        else:
          print("You ignore the note.")
      case "lobby":
        print("You walk into Bryan Lobby.")
        bryanLobby(inventory)
      case "pfm":
        print("You walk downstairs to enter the PFM.")
        pfm(inventory)
      case "reynolds":
        print("You return to Reynolds Hallway.")
        reynoldsHallway(inventory)
      case _:
        print("Unknown Command")
    if common(userInput, inventory, description):
      continue

# Bryan Lobby. The player gets the key fob here, which is needed to progress further.
def bryanLobby(inventory):
  description = "\nBryan Lobby\nAn information station, filled with staff working tirelessly to address any and all issues. At least, it used to be."
  description += " There is a key fob on the desk." if "key fob" not in inventory else None
  print(description)
  while True:
    userInput = input("> ").strip().lower()
    match userInput:
      case "bryan":
        print("You return to Bryan Hallway.")
        bryanHallway(inventory)
      case "take key fob":
        if "key fob" in inventory:
          print("You've already taken the key fob.")
        else:
          print("You took the key fob.")
          inventory.append("key fob")
          description = "\nBryan Lobby\nAn information station, filled with staff working tirelessly to address any and all issues. At least, it used to be."
      case _:
        print("Unknown Command")
    if common(userInput, inventory, description):
      continue

# Checks whether the grease monster has been defeated. The PFM can be accessed normally if is true, and it will initiate the fight if false.
greaseDefeat = False

# The PFM, where the player encounters the grease monster. After the monster is defeated, it's just another room.
def pfm(inventory):
  description = "\nThe PFM\nThis is where students went to feed/fuel themselves. Despite not having the most glowing reviews, the staff worked tirelessly to put a smile on kids faces. Now it has an odd stench of grease..."
  description += " You can go to Bryan Lobby or the Pit from here." if greaseDefeat == True else None
  print(description)
  if greaseDefeat == True:
    while True:
      userInput = input("> ").strip().lower()
      match userInput:
        case "bryan":
          print("You open up the gate and walk to Bryan Hallway.")
          bryanHallway(inventory)
        case "pit":
          print("You exit the PFM and enter the Pit.")
          thePit(inventory)
        case _:
          print("Unknown Command")
      if common(userInput, inventory, description):
        continue
  else:
    print("Hurrying into the PFM, you hear the deep, guttural noises of a beast. Do you proceed onward? (y or n)")
    if input() == "y":
      greaseFight(description)
    else:
      print("You back slowly away and return to Bryan Hallway.")
      bryanHallway(inventory)

# The fight with the grease monster. The player defeats it by getting dough from the kitchen and throwing it at the monster. If the number of turns exceeds 10, the player loses.
def greaseFight(inventory):
  turns = 0
  description = "\nYou cannot believe your eyes. It is, as the rumors foretold, a giant monster made from grease. It hurls a glob of grease at you that you quickly evade, but it hits the door behind you and seals it shut. The monster blocks the exit to the Pit. What will you do?"
  print(description)
  while True:
    userInput = input("> ").strip().lower()
    match userInput:
      case "fight":
        print("There's no use trying to punch a grease monster.")
      case "cue":
        print("You try to stab the grease monster with the pool cue, but it doesn't harm the monster.")
      case "kitchen":
        print("You sprint past the monster and dive into the kitchen, looking around for anything that may be of use. Your eyes light up as they land upon the solution: PFM pizza dough.")
        inventory.append("pizza dough")
      case "throw pizza dough":
        print("You begin hurling globs of pizza dough at the monster while defiantly yelling 'Let's not do that.' The beast shrieks as it melts, its essence absorbed into the dough, leaving behind only a greasy pile.\nElated by your success, you search the PFM for the students and faculty, but you cannot find them. Disappointed, you exit the building and continue onwards.")
        inventory.pop()
        thePit(inventory)
      case _:
        print("Uknown Command")
        turns += 1
    if common(userInput, inventory, description):
      continue
    
    print("")
    print("The grease monster approaches you. You'll have to find something to defeat it.") if turns == 5 else None
    print("The grease monster will defeat you if you don't act quickly. Check the kitchen.") if turns == 8 else None
    if turns > 10:
      print("You've taken too long to react. The grease monster absorbs you.")  # Game Over
      gameoval()

# A transition area between the PFM and the rest of the outside. Woolworth can also be accessed from here.
def thePit(inventory):
  description = "\nThe Pit\nIt’s the pit. You can go to Woolworth Room with your newly acquired fob, back to the PFM, or around the rest of campus, like Hunt."
  print(description)
  while True:
    userInput = input("> ").strip().lower()
    match userInput:
      case "pfm":
        print("You enter the PFM.")
        pfm(inventory)
      case "woolworth":
        print("You enter the Woolworth Room.")
        woolworth(inventory)
      case "hunt":
        print("You walk over to Hunt and fob into the Lobby.")
        huntLobby(inventory)
      case "royal":
        print("You might not want to do that, given the Chancellor's warning. Do you still wish to proceed? (y or n)")
        if input() == "y":
          royall(inventory)
        else:
          print("You remain at the Pit.")
      case "pec":
        print("I'll probably put an easter egg or something here, but for now there's nothing.")
      case _:
        print("Unknown Command")
    if common(userInput, inventory, description):
      continue

# The Woolworth Room, where the SAB closet can be found.
def woolworth(inventory):
  description = "\nWoolworth Room\nA place of recreation for students, often occupied by table tennis players. You can access the SAB closet from here."
  print(description)
  while True:
    userInput = input("> ").strip().lower()
    match userInput:
      case "pit":
        print("You return outside to the Pit.")
        thePit(inventory)
      case "closet":
        if "sab key" and "bucket" in inventory:
          print("You open the closet. Nothing else of use.")
        elif "sab key" in inventory: #sab key and no bucket
          print("You unlock the closet using the SAB key. There is a bucket inside. Will you take it? (y or n)")
          if input() == "y":
            print("You take the bucket")
            inventory.append("bucket")
          else:
            print("You reject the bucket and lock the closet.")
        else:#no sab key
          print("The closet is locked.")
      case _:
        print("Unkown Command")
    if common(userInput, inventory, description):
      continue

# Hunt Lobby. From here, the player can head to the clinic.
def huntLobby(inventory):
  description = "\nHunt Lobby\nNo running. There's a sign pointing to the clinic."
  print(description)
  while True:
    userInput = input("> ").strip().lower()
    match userInput:
      case "clinic":
        print("You walk over to the clinic.")
        clinic(inventory)
      case "outside":
        print("You return outside.")
        thePit(inventory)
      case _:
        print("Unknown Command")
    if common(userInput, inventory, description):
      continue

# The Clinic, where the player finds the DMQ and enters Ground Hunt for the final fight.
def clinic(inventory):
  description = "\nClinic\nA place for students to go when they are feeling unwell, to recieve medicine, or to get out of class for a day. There is a giant hole in the corner of the room that appears to lead into a tunnel."
  description += " There is a jug of DMQ on the table as well as a note." if inventory.include("dmq") else None
  print(description)
  while True:
    userInput = input("> ").strip().lower()
    match userInput:
      case "note":
        if inventory.include("clinic note") == False:
          print("You read the note. It reads: 'Do not jump down this hole without a can of Ajax.'\nYou put the note in your twan notebook.")
          inventory.append("clinic note")
      case "dmq":
        if inventory.include("dmq") == False:
          print("You take the DMQ.")
          inventory.append("dmq")
          #look at below,, description doesn't change?
          #description = "\nClinic\nA place for students to go when they are feeling unwell, to recieve medicine, or to get out of class for a day. There is a giant hole in the corner of the room that appears to lead into a tunnel."
      case "lobby":
        print("You return to Hunt Lobby.")
        huntLobby(inventory)
      case "hole":
          print("It doesn't seem like you'll be able to get back up easily. Are you sure your want to jump down? (y or n)")
          if input() == "y":
            print("You brace yourself and jump down the hole.")
            groundHunt(inventory)
          else:
            print("You decide to make prepartions first.")
      case _:
        print("Unknown Command")
    if common(userInput, inventory, description):
      continue


def groundHunt():
  health = 10
  description = "\nGround Hunt\nThe underbelly of Hunt, where mysterious things lurk. Only lit by candles, the cries of trapped students echo down the moist halls."
  print("\nYou land on the ground with a hard fall. Standing up, you stagger through the tunnel in darkness towards a light at the end. Stepping into the light, you find yourself in a dungeon: the legendary Ground Hunt. You see your colleagues and students trapped in cages, but they appear unharmed. You run towards them, but they motion for you to stop and be quiet. Turning to your right, you see a shadowy mass quickly approaching you. It steps into the light, and you finally see the perpetrator: the pipecats.\nYou don't have a chance to react before they surround you. They stare steely-eyed into your soul, and you begin to dread the fate that awaits you.")
  cat1(inventory, health)
  print("swag centipede")
  cat2(inventory, health)
  print("swag elephant")
  cat3(inventory, health)
  print("swag albatross")


  # Battle with the first pipecat. There are five different actions that can be used (attack, dodge, observe, item, reason) in combat with the cat. Cat 1 will be defeated by using the pool cue. If the player tries to attack the cat, it will do 1-3 damage.
def cat1(inventory, health):
  if dmqUsed == True: return
  description = f"\nOne of them approaches you. You have {health} health. What will you do? (attack, dodge, item, observe, reason)"
  print(description)
  while True:
    userInput = input("> ").strip().lower()
    match userInput:
      case "attack":
        num = random.randint[1,3]
        print(f"You run up and try to kick the cat, but it jumps out of the way and hisses at you. It runs up and scratches you. {num} damage taken.")
        health -= num

      case "dodge":
        print("You ready yourself to dodge the cat's attack, but it doesn't move.")

      case "observe":
        print("The cat stares at you intensely but not aggressively. It doesn't look like it's going to attack you immediately.")

      case "reason":
        print("You try to reason with the cat, saying 'Let's not do that', but it doesn't react.")

      case "item":
        print("Inventory: " + inventory.join(", "))
        print("What item do you want to use?")
        item = str(input())

        if item == ("cue") and "pool cue" in inventory:
          print("You brandish the pool cue, and the cat backs off.")
          cat2(inventory, health)
        else:
          useItem(item)

      case _:
        print("Unknown Command. Lock In!!")
    if common(userInput, inventory, description):
      continue

    print(f"\nThe cat stares at you. You have {health} health. (attack, dodge, item, observe, reason)")


    if health < 1:
      print("Having sustained minor scratches to the leg, you begin to feel woozy and pass out on the ground.")
      badEnd()




  # Battle with the second pipecat. This cat will be defeated by dodging its attack. If the player attempts to attack, use an item, or reason, which is signified by the "retaliate" variable, the cat will attack the player for 1-3 damage.
def cat2(inventory, health):
    if dmqUsed == True: return
    description = f"\nAnother one walks toward you. You have {health} health. What will you do? (attack, dodge, item, observe, reason)"
    print(description)
    while True:
      retaliate = False
      userInput = input("> ").strip().lower()
      match userInput:
        case "attack":
          print("You try to attack the cat with the pool cue, but it dodges.")
          retaliate = True

        case "dodge":
          print("You wait as the cat charges towards you, then quickly dart out of the way. You poke it with the pool cue and it runs off.")
          cat3(inventory, health)
          #return
        case "observe":
          print("The cat looks aggressively at you.")

        case "reason":
          print("You try to reason with the cat, saying 'Let's not do that', but it doesn't react.")
          retaliate = True

        case "item":
          print("Inventory: " + inventory.join(", "))
          print("What item do you want to use?")
          item = str(input())
          useItem(item)
          retaliate = True

        case _:
          print ("Unknown Command")
      if common(userInput, inventory, description):
        continue

      if retaliate:
        num = random.randint[1,3]
        print(f"The cat attacks you for {num} damage.")
        health -= num
        retaliate = False

      if health < 1:
        print("Having sustained minor scratches to the leg, you begin to feel woozy and pass out on the ground.")
        badEnd()

    #return if $dmqUsed


# These variables keep track of the player's progress towards completing the ending. The DMQ can only be used if the Ajax is used, and the Ajax can only be used after the bucket has been used. Once $bucketUsed = true, the player gets the good ending.
bucketUsed = False
ajaxUsed = False
dmqUsed = False

# Battle with the third pipecat. This cat will not attack the player. If the player chooses to reason, they will either get the bad end or the selfish end.
def cat3(inventory, health):
  description = "\nA third cat approaches you. You have {health} health. What will you do? (attack, dodge, item, observe, reason)"
  print(description)
  while True:
    userInput = input("> ").strip().lower()
    match userInput:
      case "attack":
        print("You lunge forward to attack the cat, but it jumps aside.")

      case "dodge":
        print("You brace for the cat to attack you, but it remains still.")

      case "item":
        print("Inventory: " + inventory.join(", "))
        print("What item do you want to use?")
        item = str(input())
        useItem(item)

      case "observe":
        print("It doesn't seem to want to fight you.")

      case "reason":
        print("You try to reason with the cat. It appears afraid of you, and it jumps back in fear as you brandish the pool cue. The other cats back off as you walk towards towards the cages. Do you unlock the cages? (y or n)")
        if input() == "y":
          print("You walk towards the cages to free the students. As you begin unlocking the door, the cats charge you and knock you unconscious on the ground.")
          badEnd()
        else:
          print("\nYou decide to leave the students and faculty behind and return to the surface alone. You then declare yourself the chancellor of NCSSM, recruiting new faculty and staff and starting the admissions process for new students. You seal off the hole to Ground Hunt and hide the evidence you'd collected on your investigation, and you tell the police that you never found them. Glory to Chancellor Parsons.\nYou win?") #Selfish/Joke End
        return

      case _:
        print("Unknwon Command")
    if common(userInput, inventory, description):
      continue
    #return if $dmqUsed
    print("\nThe cat stares at you. You have {health} health. (attack, dodge, item, observe, reason)")

# This method is called when the player uses an item during combat with a cat.
def useItem(input):
  while True:
    match input:
      case "bucket":
        if "bucket" in inventory:
          print("You've already used the bucket.") if bucketUsed == True else print("You take out the bucket and place it on the ground.") and bucketUsed == True

      case "ajax":
        if "ajax can" in inventory:
          if bucketUsed and ajaxUsed == False:
            print("You add Ajax to the bucket.")
            ajaxUsed = True
          elif ajaxUsed == True:
            print("You've already used the Ajax.")
          else:
            print("You don't have anything to put the Ajax in.")

      case "dmq":
        if "dmq" in inventory:
          if bucketUsed == True and ajaxUsed == True and dmqUsed == False:
            print("You start to add DMQ to the bucket.")
            dmqUsed = True
          goodEnd1()

        elif bucketUsed == True and ajaxUsed == False:
          print("There's something else you should put in first.")
        else:
          print("You don't have anything to put the DMQ in.")

      case "cue":
        if "cue" in inventory:
          print("You are already holding the pool cue.")
      case "note":
        print("You can't use a note, but you can examine one.")
      case "key" | "fob" | "twan":
        print("That won't help.")
      case _:
        print(f"You don't have {input}.")

# This occurs if you run out of health or choose to unlock the cages after reasoning with cat 3.
def badEnd():
  print("\nYou wake up with a pang in the back of your head. Standing up, you see that you're behind bars, along with the rest of the staff. The pipecats got you.")
  gameoval()


def goodEnd1():
  print("\nJust before you begin pouring, you hear the frightened yelp of a cat. You look up and see them cowering before you; they know what happens when you mix DMQ and Ajax, and they fear for their lives. Of course, you would never actually mix them, because it would endanger the students and faculty as well, but the threat is enough for the pipecats to flee when you approach them.\n\nWith the cats gone, you unlock the cages to free your fellow Smathers, and you hurry back to the tunnel. As the last of the students are climbing up into the clinic, you hear growling from behind you. In a last ditch effort to repel them, you throw the bucket as far as you can into the tunnel, holding your breath as if you had added the DMQ. The pipecats flee once again, and you manage to escape.\n\nYou are victorious, having saved the students and teachers and avoided demise by the hands of the pipecats. As a reward for your valiant deeds, you are crowned the king of NCSSM, giving you an unlimited budget for SAB and garnering the undying loyalty of the students. Congratulations, Taylor Parsons.\n\nDISCLAIMER: Never actually combine Ajax and DMQ")

def goodEnd2():
  print("you can't get this yet.")
  gameoval()

# If the player does not input any of the commands specific to a room, this function is called. It contains generic commands that work in any room.
def help(input, setting):
  # Tells the player the items in their inventory
  while True:
    match input:
      case " inventory" | "i":
        print("Inventory: " + inventory.join(", "))
  # Gives the player a list of starting commands.
      case "help":
        print("\nHere are some commands that might come in handy:\nlook - tells you the description for the room you're in\ninventory - tells you all the items you currently have\nexamine (item) - gives you the description for an item in your inventory")
  # Gives the description for a given item in the player's inventory

  #   case "examine ":

  #   item = input[2..(input.length-1)] if input.include?("x ")
  #   item = input[8..(input.length-1)] if input.include?("examine ")
  #   if item in inventory
  #      print(itemDescriptions[item])
  #   else:
  #      print(f"You don't have {item}.")
  # Tells the player the description for the room they're in
      case "look" | "l":
        print(setting)
      case _:
        print("Sorry, I don't understand that command.")
    return


startGame(inventory)

#https://pc-python.readthedocs.io/en/latest/python_advanced/match_case.html#id1 
#https://pypi.org/project/colorama/
#