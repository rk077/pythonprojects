from Queue import QueueADT


def play_game(player_queue, magic_number):
    count = 0
    while player_queue.size() > 1:
        if count == magic_number:
            player_queue.dequeue()
            count = 0
        else:
            player_queue.enqueue(player_queue.dequeue())
            count += 1
    x = player_queue.dequeue()
    print(x)


def take_input():
    no_players = int(input("Enter the number of players: "))
    players = QueueADT()
    index = 0
    while index < no_players:
        players.enqueue(input("Who is player %d? " % (index+1)))
        index += 1

    magic_num = int(input("Enter the magic number"))
    play_game(players, magic_num)

if __name__=="__main__":
    take_input()
