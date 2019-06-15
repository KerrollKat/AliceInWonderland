class Character:
    def __init__(self):
        self.power = "power"
        self.hp = "hp"
        self.madness = "madness"
        self.time = "time"

    def attack(self, character):
        character.hp -= 5
        character.power -= 5


class Hero(Character):
    def __init__(self, name):
        Character.__init__(self)
        self.name = name

    def say_name(self):
        print(self.name)

    def show_info(self):
        if self.hp == 0 or self.madness == 0 or self.time == 0:
            info = "{}:"
            print(info.format(self.name), "Dead")
        else:
            inf = "{}: power={}, hp={}, madness={}, time={}\n"
            print(inf.format(self.name, self.power, self.hp, self.madness, self.time))


class NPC(Character):
    def __init__(self):
        Character.__init__(self)

    def show_info(self):
        var = self.x
        if self.hp == 0 or self.madness == 0 or self.time == 0:
            i = "{}:"
            print(i.format(var), "Dead")
        else:
            inf = "{}: power={}, hp={}, madness={}, time={}\n"
            print(inf.format(var, self.power, self.hp, self.madness, self.time))


class WhiteQueen(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.power = 50
        self.hp = 100
        self.madness = 100
        self.time = 50

    def heal(self, character):
        character.hp += 5
        self.power = self.power - 5


class Alice(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.power = 100
        self.hp = 100
        self.madness = 80
        self.time = 50

    def sword(self, character):
        character.hp -= 25
        self.power = self.power - 5


class Hatter(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.power = 50
        self.hp = 80
        self.madness = 100
        self.time = 40

    def mad(self, character):
        character.madness += 5
        self.power = self.power - 5


class RedQueen(NPC):
    x = "Red Queen"

    def __init__(self):
        super().__init__()
        self.power = 100
        self.hp = 50
        self.madness = 100
        self.time = 50

    def head(self, character):
        character.hp = 0


class Jake(NPC):
    x = "Jake"

    def __init__(self):
        super().__init__()
        self.power = 100
        self.hp = 100
        self.madness = 50
        self.time = 50

    def attack(self, character):
        character.hp -= 10
        self.power = self.power - 5


class TimeMan(NPC):
    x = 'Time Man'

    def __init__(self):
        super().__init__()
        self.power = 100
        self.hp = 100
        self.madness = 100
        self.time = 100

    def old(self, character):
        character.time -= 5
        self.power = self.power - 5

    def young(self, character):
        character.time += 5
        self.power = self.power - 5


class Human(NPC):
    x = "Human"

    def __init__(self):
        super().__init__()
        self.power = 80
        self.hp = 80
        self.madness = 20
        self.time = 50

    def reality(self, character):
        character.madness -= 5
        self.power = self.power - 5


a = WhiteQueen('Player1')
b = RedQueen()
b.head(a)
a.show_info()
b.show_info()

e = Alice('Player2')
d = TimeMan()
d.old(e)
e.show_info()
d.show_info()




