from Stack import Stack

class HP:
    def __init__(self):
        self.hp_bag = Stack()
        self.coins = 0
        self.instr = 0
        self.monkValue = 0

    def takeinput(self):
        self.coins = int(input())
        coins_arr =list(map(int, input().split()))

        for eachCoin in range(0, self.coins):
            self.hp_bag.push(coins_arr[eachCoin])

        self.instr, self.monkValue = map(int, input().split())
        self.interact()

    def interact(self):
        monk_bag = Stack()
        coinsum = 0
        coincount = 0
        req_coins = 0
        firsttime = True
        for eachInst in range(0, self.instr):
            instr = input()
            if instr == "Harry":
                v = self.hp_bag.pop()
                monk_bag.push(v)
                coinsum += v
                coincount += 1
            else:
                deval = monk_bag.pop()
                coinsum -=deval
                coincount-=1

            if coinsum == self.monkValue and firsttime:
                req_coins = coincount
                firsttime = False

        print(req_coins)

    def checkBag(self,coinsum):
        if coinsum == self.monkValue:
            return False

solution = HP()
solution.takeinput()