    import random
    numbers = (1, 2, 3, 4, 5, 6)
    class dice:
        def roll(self):
            a=random.randint(1, 6)
            b=random.randint(1, 6)
            return (a,b)

    #Rolls the dice!
    print(dice.roll(2))
