from random import choice
lot = (1, 2, 3, 4,'f', 'g', 'c', 2, 3)
pot = [3, 4, 'g', 'c']
ticket = []

while True:
    no_of_items = 0
    while no_of_items < 4:
        game = choice(lot)
        ticket.append(game)
        no_of_items += 1
    print(ticket)
    if ticket == pot:
        print("Yay!")
        break
    elif ticket != pot:
        del ticket[:4]
        #continue
