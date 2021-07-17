# Write your code here
import random


class Game:
    def __init__(self):
        self.user_score = 0
        self.robot_score = 0
        self.draws = 0

    def print_stats(self):
        print("You won: {},".format(self.user_score))
        print("The robot won: {},".format(self.robot_score))
        print("Draws: {}.".format(self.draws))


class RPSGame(Game):
    def __init__(self):
        super().__init__()
        self.variants = ["rock", "paper", "scissors"]
        self.combinations = {"rock": "paper", "paper": "scissors", "scissors": "rock"}


    def make_round(self, user_, robot_):
        if self.combinations.get(user_) == robot_:
            self.robot_score += 1
            self.result(robot_, "The robot won!")
        elif user_ == robot_:
            self.draws += 1
            self.result(robot_, "It's a draw!")
        elif self.combinations.get(robot_) == user_:
            self.user_score += 1
            self.result(robot_, "You won!")

    def result(self, robot_, result_):
        print("The robot chose {}.".format(robot_))
        print(result_)

    def check_user_input(self):
        while True:
            print("What is your move?")
            option_ = input()
            if option_ == "exit game":
                return option_
            if option_ not in self.variants:
                print("No such option! Try again!")
                continue
            return option_


class NumbersGame(Game):
    def __init__(self, seed):
        super().__init__()
        random.seed(seed)
        self.goal = random.randint(0, 1000000)

    def generate_goal(self):
        self.goal = random.randint(0, 1000000)


    def make_round(self, player_, robot_):
        player_ = int(player_)
        delta_player = abs(self.goal - player_)
        delta_robot = abs(self.goal - robot_)
        if delta_robot == delta_player:
            self.draws += 1
            self.result(robot_, "It's a draw!")
        if delta_robot > delta_player:
            self.user_score += 1
            self.result(robot_, "You won!")
        if delta_robot < delta_player:
            self.robot_score += 1
            self.result(robot_, "The robot won!")

    def result(self, robot_, result_):
        print("The robot entered the number {}.".format(robot_))
        print("The goal number is {}.".format(self.goal))
        print(result_)

    def check_user_input(self):
        while True:
            print("What is your number?")
            option_ = input()
            if option_ == "exit game":
                return option_
            if not (option_.strip("-")).isdigit():
                print("A string is not a valid input!")
                continue
            if int(option_) < 0:
                print("The number can't be negative!")
                continue
            if int(option_) > 1000000:
                print("Invalid input! The number can't be bigger than 1000000")
                continue
            return option_


class Robot:
    actions = ["exit", "info", "recharge", "sleep", "play", "work", "oil", "learn"]
    games = ["rock-paper-scissors", "numbers"]

    def __init__(self, seed, name):
        random.seed(seed)
        self.guess = random.randint(0, 1000000)
        self.is_game_over = False
        self.name = name
        self.battery = 100
        self.overheat = 0
        self.skills = 0
        self.boredom = 0
        self.rust = 0
        self.prev_battery = 100
        self.prev_overheat = 0
        self.prev_skills = 0
        self.prev_boredom = 0
        self.prev_rust = 0

    def robot_menu(self):
        while True:
            if self.overheat >= 100:
                print()
                print("The level of overheat reached 100, {} has blown up. Game over. Try again?".format(self.name))
                break
            if self.rust >= 100:
                print()
                print("{} is too rusty! Game over. Try again?".format(self.name))
                break
            print("Available interactions with {}:".format(self.name))
            print("exit - Exit")
            print("info - Check the vitals")
            print("work - Work")
            print("play - Play")
            print("oil - Oil")
            print("recharge - Recharge")
            print("sleep - Sleep mode")
            print("learn - Learn skills")
            print()
            print("Choose:")
            choice_ = input()
            print()
            if self.battery == 0 and choice_ != "recharge":
                print("The level of the battery is 0, {} needs recharging!".format(self.name))
                continue
            if self.boredom == 100 and choice_ != "play":
                print("{} is too bored! {} needs to have fun!".format(self.name, self.name))
                continue
            if choice_ not in self.actions:
                print("Invalid input, try again!")
                continue
            if choice_ == "exit":
                print("Game over.")
                return
            if choice_ == "info":
                self.robot_stats()
                continue
            if choice_ == "recharge":
                self.robot_recharge()
                continue
            if choice_ == "sleep":
                self.robot_sleep()
                continue
            if choice_ == "play":
                self.robot_play()
                continue
            if choice_ == "work":
                self.robot_work()
                continue
            if choice_ == "learn":
                self.robot_learn()
                continue
            if choice_ == "oil":
                self.robot_oil()
                continue

    def change_battery(self, value_):
        self.prev_battery = self.battery
        self.battery += value_
        if self.battery < 0:
            self.battery = 0
        if self.battery > 100:
            self.battery = 100

    def change_overheat(self, value_):
        self.prev_overheat = self.overheat
        self.overheat += value_
        if self.overheat < 0:
            self.overheat = 0
        if self.overheat > 100:
            self.overheat = 100

    def change_boredom(self, value_):
        self.prev_boredom = self.boredom
        self.boredom += value_
        if self.boredom < 0:
            self.boredom = 0
        if self.boredom > 100:
            self.boredom = 100

    def change_skills(self, value_):
        self.prev_skills = self.skills
        self.skills += value_
        if self.skills < 0:
            self.skills = 0
        if self.skills > 100:
            self.skills = 100

    def change_rust(self, value_):
        self.prev_rust = self.rust
        self.rust += value_
        if self.rust < 0:
            self.rust = 0
        if self.rust > 100:
            self.rust = 100

    def change_print(self, param_, prev_, next_):
        print("{}'s level of {} was {}. Now it is {}.".format(self.name, param_, prev_, next_))

    def make_accident(self):
        events_ = ["", "puddle", "sprinkler", "pool"]
        events_desc_ = {"puddle": "Oh no, {} stepped into a puddle!".format(self.name),
                        "sprinkler": "Oh, {} encountered a sprinkler!".format(self.name),
                        "pool": "Guess what! {} fell into the pool!".format(self.name)}
        event_ = random.choice(events_)
        if event_ == "puddle":
            self.change_rust(10)
            print(events_desc_.get("puddle"))
            self.change_print("rust", self.prev_rust, self.rust)
        if event_ == "sprinkler":
            self.change_rust(30)
            print(events_desc_.get("sprinkler"))
            self.change_print("rust", self.prev_rust, self.rust)
        if event_ == "pool":
            self.change_rust(50)
            print(events_desc_.get("pool"))
            self.change_print("rust", self.prev_rust, self.rust)

    def robot_learn(self):
        if self.skills == 100:
            print("There's nothing for {} to learn!".format(self.name))
            return
        self.change_skills(10)
        self.change_battery(-10)
        self.change_overheat(10)
        self.change_boredom(5)
        self.change_print("skill", self.prev_skills, self.skills)
        self.change_print("overheat", self.prev_overheat, self.overheat)
        self.change_print("the battery", self.prev_battery, self.battery)
        self.change_print("boredom", self.prev_boredom, self.boredom)
        print()
        print("{} has become smarter!".format(self.name))

    def robot_oil(self):
        if self.rust == 0:
            print("{} is fine, no need to oil!".format(self.name))
            return
        self.change_rust(-20)
        print("{}'s level of rust was {}. Now it is {}. {} is less rusty!"
              .format(self.name, self.prev_rust, self.rust, self.name))

    def robot_work(self):
        if self.skills < 50:
            print("{} has got to learn before working!".format(self.name))
            return
        self.change_battery(-10)
        self.change_boredom(10)
        self.change_overheat(10)
        print("{} did well!".format(self.name))
        self.change_print("boredom", self.prev_boredom, self.boredom)
        self.change_print("overheat", self.prev_overheat, self.overheat)
        self.change_print("the battery", self.prev_battery, self.battery)
        self.make_accident()

    def robot_recharge(self):
        if self.battery == 100:
            print("{} is charged!".format(self.name))
            return
        self.change_overheat(-5)
        self.change_print("overheat", self.prev_overheat, self.overheat)
        self.change_battery(10)
        self.change_print("the battery", self.prev_battery, self.battery)
        self.change_boredom(5)
        self.change_print("boredom", self.prev_boredom, self.boredom)
        print("{} is recharged!".format(self.name))

    def robot_sleep(self):
        if self.overheat == 0:
            print("{} is cool!".format(self.name))
            return
        self.change_overheat(-20)
        self.change_print("overheat", self.prev_overheat, self.overheat)
        if self.overheat == 0:
            print("{} is cool!".format(self.name))
        else:
            print("Daneel cooled off!")

    def robot_stats(self):
        print("{}'s stats are: the battery is {},".format(self.name, self.battery))
        print("overheat is {},".format(self.overheat))
        print("skill level is {},".format(self.skills))
        print("boredom is {},".format(self.boredom))
        print("rust is {}.".format(self.rust))
        print()

    def guess_number(self):
        self.guess = random.randint(0, 1000000)
        return self.guess

    def guess_rps(self):
        self.guess = random.choice(["rock", "paper", "scissors"])
        return self.guess

    def robot_move(self, game_):
        if game_ == "rock-paper-scissors":
            return self.guess_rps()
        if game_ == "numbers":
            return self.guess_number()

    def robot_play(self):
        choice = self.check_game()
        game = Game()
        if choice == "rock-paper-scissors":
            game = RPSGame()
        if choice == "numbers":
            game = NumbersGame(100500)
        while True:
            player_input = game.check_user_input()
            robot_move = self.robot_move(choice)
            if player_input == "exit game":
                break
            game.make_round(player_input, robot_move)
        game.print_stats()
        self.change_boredom(-20)
        self.change_overheat(10)
        if self.overheat == 100:
            print("The level of overheat reached 100, {} has blown up! Game over. Try again?".format(self.name))
            self.is_game_over = True
            return
        self.change_print("boredom", self.prev_boredom, self.boredom)
        self.change_print("overheat", self.prev_overheat, self.overheat)
        if self.boredom == 0:
            print("{} is in a great mood!".format(self.name))
        self.make_accident()
        # self.change_battery(10)

    def check_game(self):
        print("Which game would you like to play?")
        while True:
            choice_ = input().lower()
            if choice_ in self.games:
                return choice_
            print("Please choose a valid option: Numbers or Rock-paper-scissors?")


print("How will you call your robot?")
robot = Robot(100500, input())
robot.robot_menu()
