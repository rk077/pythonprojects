class Tower:
    def __init__(self):
        self.towers = []
        self.tc = 0
        self.noTow = 0
        self.output = []

        self.getInput()

    def getInput(self):
        self.tcs = int(input())
        for eachTC in range(0, self.tcs):
            self.noTow = int(input())
            self.towers = list(map(int, input().split()))

            count = 1
            active = 1

            self.output.append(1)
            if self.towers[0] <= self.towers[1]:
                count +=1
            self.output.append(count)
            for active in range(2, len(self.towers)):
                itr = active
                count=1
                for itr in range(active-1, -1, -1):
                    if self.towers[itr] > self.towers[active]:
                        break
                    elif self.towers[itr] <= self.towers[active]:
                        count += 1
                self.output.append(count)
            for eachItem in self.output:
                print(eachItem, end=' ')
            print('')
            self.output=[]

soln = Tower()