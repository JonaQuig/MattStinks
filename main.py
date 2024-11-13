import random
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
BLUE = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"
ORANGE = "\033[48;2;255;165;0m"
x = 100

print(YELLOW + "Enter \'start\' to begin")
start = input()
while x == 100:
    if start == 'start':
        print(RESET +"Welcome to Scotland Yard!")
        print("In this game, you will chase down a criminal known by Mr.X as a detective")
        if x == 100:
          x += 1
        print(BLUE + "Enter \'ticket\' to continue")
        ticket = input()
        if ticket == 'ticket':
          class Player:
              def __init__(self, player_type):
                  self.type = player_type
                  self.tickets = {'taxi': 20, 'double': 2}
                  if player_type == "mr_x":
                      self.tickets['taxi'] = 1
                      self.tickets['double'] = 2
                  if player_type in ("detective1", "detective2"):
                      self.tickets['taxi'] = 20
                      self.tickets['double'] = 0
          detective1 = Player('detective1')
          detective2 = Player('detective2')
          mr_x = Player('mr_x')
          print(RESET + "Each role has a different amount and type of tickets")
          print("Detective 1's tickets:", detective1.tickets)
          print("Detective 2's tickets:", detective2.tickets)
          print("Mr.X's tickets:", mr_x.tickets)

          locations = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
          print(BLUE + "Enter \'location\' to to be assigned a position")
          location = input()
          if location == 'location':
              location_detective1 = random.choice(locations)
              location_detective2 = random.choice(locations)
              location_mr_x = random.choice(locations)
              print(RESET + "You have been placed at", location_detective1)
              if location_detective2 == location_detective1:
                  location_detective2 = random.choice(locations)
              print("Detective2 has been placed at", location_detective2)
              if location_mr_x == location_detective1 and location_detective2:
                 location_mr_x = random.choice(locations)
              print("Mr.X has been placed at", RED + "Unknown")
              print(RESET + " ")

          board = {
              "A": ["C", "D", "E"],
              "B": ["D", "E", "I"],
              "C": ["A", "D"],
              "D": ["A", "B", "C", "O"],
              "E": ["A", "B", "F"],
              "F": ["E", "G", "H"],
              "G": ["F", "I", "J"],
              "H": ["F", "J"],
              "I": ["B", "G", "K", "N"],
              "J": ["G", "H", "K"],
              "K": ["I", "J", "L", "M"],
              "L": ["K", "M"],
              "M": ["K", "N"],
              "N": ["I", "M", "O"],
              "O": ["D", "N"]
          }
          detective1.position = location_detective1
          detective2.position = location_detective2
          mr_x.position = location_mr_x
