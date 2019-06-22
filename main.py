# Dog simulator
from random import randint
from time import sleep

from names import rand_female_name, rand_gender, rand_male_name, rand_species


# IDEA: Insert vet to increase health to max health.
# IDEA: Add exercise stat.
class Owner:
    def __init__(self):
        self.name = None
        self.money = 10
        self.energy = 3  # This determines how much an owner can do in a day.


class Dog:
    def __init__(self):
        self.gender = rand_gender()
        self.status = True  # This will be turned false when dog is dead.

        # Creates name for dog based on gender.
        if self.gender == 'Male':
            self.name = rand_male_name()
        else:
            self.name = rand_female_name()

        self.species = rand_species()  # Species of the pet
        self.health = randint(4, 10)  # Health of the pet (Take dog to vet to maintain).
        self.exercise = randint(4, 10)  # Exercise of the pet (Take dog to walk to maintain).
        self.social = randint(4, 10)  # Player will have to play with pet or there is a chance RSPCA will remove pet.
        self.hunger = randint(4, 10)  # Dog will have to be fed to alleviate this

        # Temporary stats (these are dynamic and can change)
        self.temp_hunger = self.hunger
        self.temp_health = self.health
        self.temp_exercise = self.exercise
        self.temp_social = self.social

    def stats(self):
        return self.name, self.gender, self.species, self.health, self.social, self.hunger

    def __str__(self):
        return "Name: {} \nGender: {} \nSpecies: {} \nHealth: {} \nExercise: {} \nSocial: {} \nHunger: {}".format(
            self.name,
            self.gender,
            self.species,
            self.health,
            self.exercise,
            self.social,
            self.hunger)


# Prints out the dog's stats into a UI.
def print_dog_stats_ui():
    health_bar = '[{0:{1:}}]'.format('-' * OwnerDog.temp_health, OwnerDog.health)
    exercise_bar = '[{0:{1:}}]'.format('-' * OwnerDog.temp_exercise, OwnerDog.exercise)
    social_bar = '[{0:{1:}}]'.format('-' * OwnerDog.temp_social, OwnerDog.social)
    hunger_bar = '[{0:{1:}}]'.format('-' * OwnerDog.temp_hunger, OwnerDog.hunger)

    dog_name_ui = "Name    : {}".format(OwnerDog.name)
    gender_ui = "Gender  : {}".format(OwnerDog.gender)
    species_ui = "Species : {}".format(OwnerDog.species)
    health_ui = "Health  : {0:14} {1:}/{2:}".format(health_bar, OwnerDog.temp_health, OwnerDog.health)
    exercise_ui = "Exercise: {0:14} {1:}/{2:}".format(exercise_bar, OwnerDog.temp_exercise, OwnerDog.exercise)
    social_ui = "Social  : {0:14} {1:}/{2:}".format(social_bar, OwnerDog.temp_social, OwnerDog.social)
    hunger_ui = "Hunger  : {0:14} {1:}/{2:}".format(hunger_bar, OwnerDog.temp_hunger, OwnerDog.hunger)

    print("{}\n{}\n{}\n{}\n{}\n{}\n{}".format(dog_name_ui, gender_ui, species_ui, health_ui, exercise_ui, social_ui,
                                              hunger_ui))


# Prints out prompt for the player.
def print_prompt():
    print("\nWhat Will You Do Today? {}/3 (You Have £{})".format(player_owner.energy, player_owner.money))
    print("[1] Walk {0:} \n[2] Feed {0:} (£1) \n[3] Play with {0:} \n[4] Take {0:} to Vet (£5) \n[5] Go to Work".format(
        OwnerDog.name))


# IDEA: Don't let health decrease? Or too easy?
def simulate_day():
    if randint(1, 2) == 1:
        OwnerDog.temp_health -= randint(1, 3)
    if OwnerDog.temp_health <= 0:
        OwnerDog.temp_health = 0

    if randint(1, 2) == 1:
        OwnerDog.temp_exercise -= randint(1, 3)
    if OwnerDog.temp_exercise <= 0:
        OwnerDog.temp_exercise = 0
        OwnerDog.temp_health -= 1

    if randint(1, 2) == 1:
        OwnerDog.temp_social -= randint(1, 3)
    if OwnerDog.temp_social <= 0:
        OwnerDog.temp_social = 0

    OwnerDog.temp_hunger -= randint(1, 3)
    if OwnerDog.temp_hunger <= 0:
        OwnerDog.temp_hunger = 0
        OwnerDog.temp_health -= 1
    player_owner.energy = 3


if __name__ == "__main__":
    print("Christopher's Dog Owner Simulator 2019")
    player_owner = Owner()
    OwnerDog = Dog()
    player_owner.name = input(str("Enter your Name:"))

    # Player selects which dog they want
    while True:
        PlayerSelection = input("{}\n[1] Select Dog [2] Change Dog\n".format(OwnerDog))
        if PlayerSelection == '1':
            break
        elif PlayerSelection == '2':
            OwnerDog = Dog()
        else:
            print("Invalid Selection\n")
            sleep(0.5)

    # IDEA: Put bottom stuff at the top?
    Day = 1
    while OwnerDog.status:
        print("Day {}".format(Day))
        while player_owner.energy > 0:
            print_dog_stats_ui()
            print_prompt()
            player_input = str(input())

            if player_input == '1':  # Walk
                OwnerDog.temp_exercise += randint(1, 3)
                if OwnerDog.temp_exercise > OwnerDog.exercise:
                    OwnerDog.temp_exercise = OwnerDog.exercise
                player_owner.energy -= 1

            elif player_input == '2':  # Feed
                if player_owner.money < 1:
                    print("Insufficient Funds")
                    continue
                OwnerDog.temp_hunger += randint(1, 3)
                if OwnerDog.temp_hunger > OwnerDog.hunger:
                    OwnerDog.temp_hunger = OwnerDog.hunger
                player_owner.money -= 1
                player_owner.energy -= 1

            elif player_input == '3':  # Play
                OwnerDog.temp_social += randint(1, 3)
                if OwnerDog.temp_social > OwnerDog.social:
                    OwnerDog.temp_social = OwnerDog.social
                player_owner.energy -= 1

            elif player_input == '4':  # Vet
                if player_owner.money < 5:
                    print("Insufficient Funds")
                    continue
                OwnerDog.temp_health = OwnerDog.health
                player_owner.money -= 5
                player_owner.energy -= 1

            elif player_input == '5':  # Work
                money_earned = randint(1, 3)
                print("You Earned £{}!".format(money_earned))
                player_owner.money += money_earned
                player_owner.energy -= 1

            else:
                print("Invalid Input")
                continue

        simulate_day()
        Day += 1
        if OwnerDog.temp_social == 0 or OwnerDog.temp_health == 0:
            OwnerDog.status = False
            print_dog_stats_ui()
            print('You Lose!!!')
