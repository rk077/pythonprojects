from Stack import Stack


class Solution:
    def take_input(self):
        test_cases = int(input())
        passCounter = 0
        eachcase = 0
        backpassCounter=0
        for eachcase in range(0, test_cases):
            s = Stack()
            max_pass, start = map(int, input().split())
            s.push(start)
            for passCounter in range(0, max_pass):
                play = input().split()
                if play[0] == 'P':
                    s.push(int(play[1]))
                    backpassCounter=0
                else:
                    backpassCounter += 1
                    if backpassCounter > 1:
                        lastbut1 = last
                        last = s.pop()
                        s.push(lastbut1)
                    else:
                        last = s.pop()

            print("Player", s.peek())


x = Solution()
x.take_input()
