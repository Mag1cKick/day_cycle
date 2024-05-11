import random

def prime(fn):
    """Decorator for states to send input"""
    def wrapper(*args, **kwargs):
        v = fn(*args, **kwargs)
        v.send(None)
        return v
    return wrapper

class MyDay:
    """How my day goes"""
    hung = [100, 80, 60, 40, -50, -20, -10, 0]
    tire = [100, 80, 60, 40]
    e_st = [0, 20, 40, 80]
    def __init__(self):
        self.wake_up = self._wake_up()
        self.eat = self._eat()
        self.sleep = self._sleep()
        self.take_a_shower = self._shower()
        self.rest = self._rest()
        self.programming = self._programming()
        self.shopping = self._shopping()
        self.sport = self._sport()
        self.reading = self._read()
        print("choose your difficulty {1:'easy', 2:'average', 3:'hard', 4:'Asian'}")
        try:
            self.difficulty = int(input())
        except TypeError:
            print('you lost')
            self.end = True

        self.current_time = 7
        self.tiredness = 0
        self.hunger = 20
        self.e_stability = 95
        self.current_state = self.sleep
        self.end = False
        self.win = False

    def check(self):
        """surving check"""
        if self.hunger > self.hung[self.difficulty-1]:
            print('You starved to death')
            self.end = True
            return False
        if self.hunger < self.hung[3+self.difficulty]:
            print('Obbesity killed you')
            self.end = True
            return False
        if self.tiredness > self.tire[self.difficulty-1]:
            print('You are so tired you died')
            self.end = True
            return False
        if self.e_stability < self.e_st[self.difficulty-1]:
            if self.difficulty == 4:
                print('You died with Emotional dammage')
            else:
                print('Your mental health is entirely damaged')
            self.end = True
            return False
        return True

    def send(self, action):
        """Sends actions"""
        try:
            self.current_state.send(action)
        except Exception:
            self.end = True

    @prime
    def _sleep(self):
        while True:
            action = yield

            if self.current_time >= 24:
                self.win = True
                self.end = True

            elif action == "wake_up":
                print("You woke up, it's time to be productive!")
                print("You can: 'sleep', 'eat' or 'take a shower':")
                self.current_time += 0.25
                self.current_state = self.wake_up
                self.hunger += 5
                self.check()

            elif action == "sleep":
                print("You can: 'wake_up' or 'sleep':")
                self.current_time += 0.5
                self.hunger += 5
                self.tiredness -= 10
                self.check()
            else:
                print("You can't do it right now, try to do it later")
                print("You can: 'wake_up' or 'sleep':")

    @prime
    def _wake_up(self):
        while True:
            action = yield

            if self.current_time >= 24:
                self.win = True
                self.end = True

            elif action == "sleep":
                print("It was so dark when you woke up so wou went to bed")
                print("You can: 'wake_up' or 'sleep':")
                self.current_time += 0.5
                self.current_state = self.sleep
                self.hunger += 5
                self.tiredness -= 10
                self.check()

            elif action == "take a shower":
                print("Time to sing a song")
                print("You can: 'eat', 'programming' or 'rest':")
                self.current_time += 0.5
                self.current_state = self.take_a_shower
                self.hunger += 7
                self.tiredness += 5
                self.e_stability = min(self.e_stability + 5, 100)
                self.check()

            elif action == "eat":
                print("Niam niam")
                print("You can: 'eat', 'programming' or 'rest':")
                self.current_time += 0.5
                self.current_state = self.eat
                self.tiredness += 5
                self.hunger -= 20
                self.e_stability = min(self.e_stability + 5, 100)
                self.check()

            else:
                print("You can't do it right now, try to do it later")
                print("You can:'sleep', 'eat' or 'take a shower':")
    @prime
    def _shower(self):
        while True:
            action = yield

            if self.current_time >= 24:
                self.win = True
                self.end = True

            elif action == "eat":
                print("Niam niam")
                print("You can: 'eat', 'programming' or 'rest':")
                self.current_time += 0.5
                self.current_state = self.eat
                self.hunger -= 20
                self.e_stability = min(self.e_stability + 5, 100)
                self.check()

            elif action == "programming":
                print("We are programming baby!")
                print("You can: 'eat', 'programming' or 'rest':")
                self.current_time += 1
                self.current_state = self.programming
                self.hunger += 15
                self.tiredness += 10
                self.e_stability = self.e_stability - 10
                self.check()

            elif action == "rest":
                print("It is time to rest")
                print("You can: 'eat', 'programming', 'shopping', 'read', 'sleep' or 'sport':")
                self.current_time += 0.25
                self.current_state = self.rest
                self.hunger += 5
                self.e_stability = min(self.e_stability + 5, 100)
                self.check()

            else:
                print("You can't do it right now, try to do it later")
                print("You can: 'eat', 'programming' or 'rest':")

    @prime
    def _eat(self):
        while True:
            action = yield

            if self.current_time >= 24:
                self.win = True
                self.end = True

            elif action == "eat":
                print("Niam niam")
                print("You can: 'eat', 'programming' or 'rest':")
                self.current_time += 0.5
                self.hunger -= 20
                self.e_stability = min(self.e_stability + 5, 100)
                self.check()

            elif action == "programming":
                print("We are programming baby!")
                print("You can: 'eat', 'programming' or 'rest':")
                self.current_time += 1
                self.current_state = self.programming
                self.hunger += 15
                self.tiredness += 15
                self.e_stability = self.e_stability - 10
                self.check()

            elif action == "rest":
                print("time to rest")
                print("You can: 'eat', 'programming', 'shopping', 'sleep' 'read' or 'sport':")
                self.current_time += 0.25
                self.current_state = self.rest
                self.hunger += 5
                self.e_stability = min(self.e_stability + 5, 100)
                self.check()

            else:
                print("You can't do it right now, try to do it later")
                print("You can: 'eat', 'programming' or 'rest':")

    @prime
    def _programming(self):
        while True:
            action = yield

            if self.current_time >= 24:
                self.win = True
                self.end = True

            elif action == "eat":
                print("Niam niam")
                print("You can: 'eat', 'programming' or 'rest':")
                self.current_time += 0.5
                self.current_state = self.eat
                self.hunger -= 20
                self.e_stability = min(self.e_stability + 5, 100)
                self.check()

            elif action == "programming":
                print("We are programming baby!")
                print("You can: 'eat', 'programming' or 'rest':")
                self.current_time += 1
                self.hunger += 15
                self.tiredness += 15
                self.e_stability = self.e_stability - 10
                self.check()

            elif action == "rest":
                print("Pomodoro timer said to rest")
                print("You can: 'eat', 'programming', 'shopping', 'read', 'sleep' or 'sport':")
                self.current_time += 0.25
                self.current_state = self.rest
                self.hunger += 5
                self.e_stability = min(self.e_stability + 5, 100)
                self.check()

            else:
                print("You can't do it right now, try to do it later")
                print("You can: 'eat', 'programming' or 'rest':")

    @prime
    def _rest(self):
        while True:
            action = yield

            if self.current_time >= 24:
                self.win = True
                self.end = True

            elif action == "eat":
                print("Niam niam")
                print("You can: 'eat', 'programming' or 'rest':")
                self.current_time += 0.5
                self.current_state = self.eat
                self.hunger -= 20
                self.e_stability = min(self.e_stability + 5, 100)
                self.check()

            elif action == "programming":
                print("We are programming baby!")
                print("You can: 'eat', 'programming' or 'rest':")
                self.current_time += 1
                self.current_state = self.programming
                self.hunger += 15
                self.tiredness += 10
                self.e_stability = self.e_stability - 10
                self.check()

            elif action == "shopping":
                print("we are going to buy something special")
                print("You can: 'rest' or 'sport':")
                self.current_time += 0.5
                self.current_state = self.shopping
                self.hunger += 5
                self.tiredness += 10
                self.e_stability = min(self.e_stability + random.randint(-5, 5), 100)
                self.check()

            elif action == "sport":
                print("We are lifting")
                print("You can: 'eat', 'programming' or 'rest':")
                self.current_time += 1.5
                self.current_state = self.sport
                self.hunger += 15
                self.tiredness += 10
                self.e_stability = min(self.e_stability + random.randint(-5, 5), 100)
                self.check()

            elif action == "read":
                print("My favorite book <333")
                print("You can: 'rest' or 'sleep':")
                self.current_time += 0.5
                self.current_state = self.reading
                self.hunger += 5
                self.tiredness += 5
                self.e_stability = min(self.e_stability + 5, 100)
                self.check()

            elif action == "sleep":
                print("Ok, it's time to work now. Ладно, за работу(Fallout3)")
                print("You can: 'wake_up' or 'sleep':")
                self.current_time += 0.5
                self.current_state = self.sleep
                self.hunger += 5
                self.tiredness -= 10
                self.check()

            else:
                print("You can't do it right now, try to do it later")
                print("You can: 'eat', 'programming', 'shopping', 'read', 'sleep' or 'sport':")

    @prime
    def _shopping(self):
        while True:
            action = yield

            if self.current_time >= 24:
                self.win = True
                self.end = True

            elif random.randint(0, 100) >= (100/self.difficulty*2.5):
                print("You were hit by a truck")
                self.end = True

            elif action == "rest":
                print("Pomodoro timer said to rest")
                print("You can: 'eat', 'programming', 'shopping', 'read', 'sleep' or 'sport':")
                self.current_time += 0.25
                self.current_state = self.rest
                self.hunger += 5
                self.e_stability = min(self.e_stability + 5, 100)
                self.check()

            elif action == "sport":
                print("We are lifting")
                print("You can: 'eat', 'programming' or 'rest':")
                self.current_time += 1.5
                self.current_state = self.sport
                self.hunger += 15
                self.tiredness += 10
                self.e_stability = min(self.e_stability + random.randint(-5, 5), 100)
                self.check()

            else:
                print("You can't do it right now, try to do it later")
                print("You can: 'rest' or 'sport':")

    @prime
    def _read(self):
        while True:
            action = yield

            if self.current_time >= 24:
                self.win = True
                self.end = True

            elif action == "sleep":
                print("Ok, it's time to work now. Ладно, за работу(Fallout3)")
                print("You can: 'wake_up' or 'sleep':")
                self.current_time += 0.5
                self.current_state = self.sleep
                self.hunger += 5
                self.tiredness -= 10
                self.check()

            elif action == "rest":
                print("Pomodoro timer said to rest")
                print("You can: 'eat', 'programming', 'shopping', 'read', 'sleep' or 'sport':")
                self.current_time += 0.25
                self.current_state = self.rest
                self.hunger += 5
                self.e_stability = min(self.e_stability + 5, 100)
                self.check()

            else:
                print("You can't do it right now, try to do it later")
                print("You can: 'rest' or 'sleep':")

    @prime
    def _sport(self):
        while True:
            action = yield

            if self.current_time >= 24:
                self.win = True
                self.end = True

            elif action == "eat":
                print("Niam niam")
                print("You can: 'eat', 'programming' or 'rest':")
                self.current_time += 0.5
                self.current_state = self.eat
                self.hunger -= 20
                self.e_stability = min(self.e_stability + 5, 100)
                self.check()

            elif action == "programming":
                print("We are programming baby!")
                print("You can: 'eat', 'programming' or 'rest':")
                self.current_time += 1
                self.hunger += 15
                self.tiredness += 15
                self.e_stability = self.e_stability - 10
                self.check()

            elif action == "rest":
                print("Pomodoro timer said to rest")
                print("You can: 'eat', 'programming', 'shopping', 'read', 'sleep' or 'sport':")
                self.current_time += 0.25
                self.current_state = self.rest
                self.hunger += 5
                self.e_stability = min(self.e_stability + 5, 100)
                self.check()

            else:
                print("You can't do it right now, try to do it later")
                print("You can: 'eat', 'programming' or 'rest':")
                