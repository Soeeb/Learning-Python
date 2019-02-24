class Spoon():
    def __init__(self,useTimes = 100):
        self.useTimes = useTimes

    def useSpoon(self, use = 1):
        self.useTimes -= use
        if self.useTimes <= 0:
            return True
        else:
            return False


def main():
    loop = True
    Spoon1 = Spoon()
    while loop:
        timeUse = int(input("How many times would you like to use the spoon?"))
        if Spoon1.useSpoon(timeUse):
            print("You've used the spoon to many times!")
            loop = False
        else:
            print("You've used the spoon!")
main()
("\n\nPress the enter key to exit")