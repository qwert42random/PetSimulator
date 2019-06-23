# Dog simulator
from random import randint
from time import sleep

from names import rand_female_name, rand_gender, rand_male_name, rand_species


class Owner:
    def __init__(self):
        self.name = None
        self.money = 5
        self.energy = 3  # This determines how much an owner can do in a day.

        # Stats for the end of the game.
        self.times_vet = 0
        self.vet_bill = 0
        self.times_walk = 0
        self.times_play = 0
        self.times_fed = 0
        self.food_bill = 0
        self.income = 0


class Dog:
    def __init__(self):
        self.gender = rand_gender()
        self.alive = True  # This will turn false when dog is dead.
        self.status = None

        # Creates name for dog based on gender.
        if self.gender == 'Male':
            self.name = rand_male_name()
        else:
            self.name = rand_female_name()

        # Some stats on the dog.
        self.species = rand_species()  # Species of the pet
        self.health = 5  # Health of the pet (Take dog to vet to maintain).
        self.exercise = 5  # Exercise of the pet (Take dog to walk to maintain).
        self.social = 5  # Player will have to play with pet or there is a chance RSPCA will remove pet.
        self.hunger = 5  # Dog will have to be fed to alleviate this

        # Temporary stats (these are dynamic and can change)
        self.temp_hunger = self.hunger
        self.temp_health = self.health
        self.temp_exercise = self.exercise
        self.temp_social = self.social

    def print_stat(self):
        return "Name: {} \nGender: {} \nSpecies: {}".format(
            self.name,
            self.gender,
            self.species)

    # Decreases stat of the dog.
    def simulate_day(self):
        self.temp_exercise -= randint(0, 2)
        if self.temp_exercise <= 0:
            self.temp_exercise = 0
            self.temp_health -= 1

        self.temp_social -= randint(0, 2)
        if self.temp_social <= 0:
            self.temp_social = 0

        self.temp_hunger -= randint(1, 2)
        if self.temp_hunger <= 0:
            self.temp_hunger = 0
            self.temp_health -= 1

        if randint(1, 10) == 1:
            self.temp_health -= randint(1, 2)
        if self.temp_health <= 0:
            self.temp_health = 0


# Prints out the dog's stats into a UI.
def print_dog_stats_ui():
    # Stat bars.
    health_bar = '[{0:{1:}}]'.format('-' * OwnerDog.temp_health, OwnerDog.health)
    exercise_bar = '[{0:{1:}}]'.format('-' * OwnerDog.temp_exercise, OwnerDog.exercise)
    social_bar = '[{0:{1:}}]'.format('-' * OwnerDog.temp_social, OwnerDog.social)
    hunger_bar = '[{0:{1:}}]'.format('-' * OwnerDog.temp_hunger, OwnerDog.hunger)

    # Full UI.
    dog_name_ui = "Name    : {}".format(OwnerDog.name)
    gender_ui = "Gender  : {}".format(OwnerDog.gender)
    species_ui = "Species : {}".format(OwnerDog.species)
    health_ui = "Health  : {0:7} {1:}/{2:}".format(health_bar, OwnerDog.temp_health, OwnerDog.health)
    exercise_ui = "Exercise: {0:7} {1:}/{2:}".format(exercise_bar, OwnerDog.temp_exercise, OwnerDog.exercise)
    social_ui = "Social  : {0:7} {1:}/{2:}".format(social_bar, OwnerDog.temp_social, OwnerDog.social)
    hunger_ui = "Hunger  : {0:7} {1:}/{2:}".format(hunger_bar, OwnerDog.temp_hunger, OwnerDog.hunger)

    print("{}\n{}\n{}\n{}\n{}\n{}\n{}".format(dog_name_ui, gender_ui, species_ui, health_ui, exercise_ui, social_ui,
                                              hunger_ui))


# Prints out prompt for the player.
def print_prompt():
    print("\nWhat Will You Do Today? {}/3 (You Have £{})".format(player_owner.energy, player_owner.money))
    print("\n[1] Take {0:} to Vet (£5)\n[2] Walk {0:}\n[3] Play with {0:}\n[4] Feed {0:} (£1)\n[5] Go to Work".format(
        OwnerDog.name))


def print_endgame_report():
    print("""
    RSPCA Owner Report #{:05}
    
    Name:         {}
    Dog Name:     {}
    Dog Status:   {}
    Vet Visits:   {}   (£{})
    Times Walked: {}
    Times Played: {}
    Times Fed:    {}   (£{})
    Owner Income: £{}""".format(randint(1, 99999), player_owner.name, OwnerDog.name, OwnerDog.status,
                                player_owner.times_vet,
                                player_owner.vet_bill, player_owner.times_walk, player_owner.times_play,
                                player_owner.times_fed, player_owner.food_bill, player_owner.income))


if __name__ == "__main__":
    print("Christopher's Dog Owner Simulator 2019")
    player_owner = Owner()
    OwnerDog = Dog()
    player_owner.name = input(str("Enter your Name: "))

    # Player selects which dog they want
    while True:
        print('-' * 20)
        PlayerSelection = input("{}\n[1] Select Dog [2] Change Dog\n".format(OwnerDog.print_stat()))
        if PlayerSelection == '1':
            break
        elif PlayerSelection == '2':
            OwnerDog = Dog()
        else:
            print("Invalid Selection\n")
            sleep(0.5)

    Day = 0
    while OwnerDog.alive is True:

        OwnerDog.simulate_day()
        player_owner.energy = 3
        Day += 1
        print("\nDay {}".format(Day))
        sleep(1)
        print_dog_stats_ui()
        if OwnerDog.temp_social == 0:

            # Simulates chance of dog being taken for neglect by RSPCA.
            if randint(1, 5) == 5:
                if player_owner.money >= 30:
                    print("\nYou bribed the RSPCA £30 to prevent them from taking {} for neglect!".format(
                        OwnerDog.name))
                    player_owner.money -= 30
                else:
                    print("\n{} Was Taken by the RSPCA!".format(OwnerDog.name))
                    OwnerDog.alive = False
                    OwnerDog.status = "Taken to RSPCA shelter"

        # If health of the dog is 0.
        if OwnerDog.temp_health == 0:
            print('\n{} Died of Neglect!'.format(OwnerDog.name))
            OwnerDog.alive = False
            OwnerDog.status = "Died from neglect"

        while player_owner.energy > 0 and OwnerDog.alive is True:
            print_prompt()
            player_input = str(input())

            # Vet
            if player_input == '1':
                if player_owner.money < 5:
                    print("Insufficient Funds!")
                    sleep(1)
                    print_dog_stats_ui()
                else:
                    print("You took {} to the vet and got billed £5!!".format(OwnerDog.name))
                    sleep(0.5)

                    OwnerDog.temp_health = OwnerDog.health
                    player_owner.money -= 5
                    player_owner.energy -= 1

                    player_owner.times_vet += 1
                    player_owner.vet_bill += 5

            # Walk
            elif player_input == '2':
                OwnerDog.temp_exercise += randint(1, 2)
                if OwnerDog.temp_exercise > OwnerDog.exercise:
                    OwnerDog.temp_exercise = OwnerDog.exercise
                print("You took {} for a walk!".format(OwnerDog.name))
                sleep(0.5)

                player_owner.energy -= 1

                player_owner.times_walk += 1

            # Play
            elif player_input == '3':
                OwnerDog.temp_social += randint(1, 2)
                if OwnerDog.temp_social > OwnerDog.social:
                    OwnerDog.temp_social = OwnerDog.social

                print("You played with {}!".format(OwnerDog.name))
                sleep(0.5)

                player_owner.energy -= 1

                player_owner.times_play += 1

            # Feed
            elif player_input == '4':
                if player_owner.money < 1:
                    print("Insufficient Funds")
                    sleep(0.5)
                else:
                    OwnerDog.temp_hunger += randint(1, 2)
                    if OwnerDog.temp_hunger > OwnerDog.hunger:
                        OwnerDog.temp_hunger = OwnerDog.hunger
                    player_owner.money -= 1
                    player_owner.energy -= 1
                    print('You spent £1 to feed {}!'.format(OwnerDog.name))
                    sleep(0.5)

                    player_owner.times_fed += 1
                    player_owner.food_bill += 1

            # Work
            elif player_input == '5':
                money_earned = randint(1, 3)
                print("You Earned £{}!".format(money_earned))
                player_owner.money += money_earned
                player_owner.income += money_earned
                player_owner.energy -= 1
                sleep(0.5)

            else:
                print("Invalid Input")
                sleep(0.5)
            print_dog_stats_ui()
    print("You Lose!")
    print_endgame_report()
