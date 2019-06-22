# Dog simulator
from random import randint
from time import sleep

from names import rand_female_name, rand_gender, rand_male_name, rand_species


# IDEA: Insert vet to increase health to max health. Can vet increase stat?
# IDEA:
class Owner:
    def __init__(self):
        self.name = None
        self.money = 100
        self.energy = None  # This determines how much an owner can do in a day.


class Dog:
    def __init__(self):
        self.gender = rand_gender()

        # Creates name for dog based on gender.
        if self.gender == 'Male':
            self.name = rand_male_name()
        else:
            self.name = rand_female_name()

        self.species = rand_species()  # Species of the pet
        self.health = randint(1, 10)  # Health of the pet (Dog will need to be walked for this to be maintained.)
        self.social = randint(1, 10)  # Player will have to play with pet or there is a chance RSPCA will remove pet.
        self.hunger = randint(1, 10)  # Dog will have to be fed to alleviate this

        # Temporary stats (these are dynamic and can change)
        self.temp_hunger = self.hunger
        self.temp_health = self.health
        self.temp_social = self.social

    def stats(self):
        return self.name, self.gender, self.species, self.health, self.social, self.hunger

    def __str__(self):
        return "Name: {} \nGender: {} \nSpecies: {} \nHealth: {} \nSocial: {} \nHunger: {}".format(self.name,
                                                                                                   self.gender,
                                                                                                   self.species,
                                                                                                   self.health,
                                                                                                   self.social,
                                                                                                   self.hunger)


if __name__ == "__main__":
    print("Christopher's Dog Owner Simulator 2019")
    player_owner = Owner()
    OwnerDog = Dog()
    player_owner.name = "Bob"  # input(str("Enter your Name:")) TODO: Change this prompt back later

    # Player selects which dog they want
    while True:
        PlayerSelection = "1"  # input("{}\n[1] Select Dog [2] Change Dog\n".format(OwnerDog)) TODO: Change this back
        if PlayerSelection == '1':
            break
        elif PlayerSelection == '2':
            OwnerDog = Dog()
        else:
            print("Invalid Selection\n")
            sleep(0.5)

    Day = 0


    def print_ui():
        health_bar = '[{0:{1:}}]'.format('-' * OwnerDog.temp_health, OwnerDog.health)
        social_bar = '[{0:{1:}}]'.format('-' * OwnerDog.temp_social, OwnerDog.social)
        hunger_bar = '[{0:{1:}}]'.format('-' * OwnerDog.temp_hunger, OwnerDog.hunger)

        dog_name_ui = "Name    : {}".format(OwnerDog.name)
        species_ui = "Species : {}".format(OwnerDog.species)
        health_ui = "Health  : {0:12} {1:}/{2:}".format(health_bar, OwnerDog.temp_health, OwnerDog.health)
        social_ui = "Social  : {0:12} {1:}/{2:}".format(social_bar, OwnerDog.temp_social, OwnerDog.social)
        hunger_ui = "Hunger  : {0:12} {1:}/{2:}".format(hunger_bar, OwnerDog.temp_hunger, OwnerDog.hunger)

        print("{}\n{}\n{}\n{}\n{}".format(dog_name_ui, species_ui, health_ui, social_ui, hunger_ui))


    print_ui()
