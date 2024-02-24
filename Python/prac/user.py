class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

        self.is_rewards_member = False
        self.gold_card_points = 0
    
    def display_info(self):
        print(f"First Name - {self.first_name}")
        print(f"Last Name - {self.last_name}")
        print(f"Email - {self.email}")
        print(f"Age - {self.age}")
        print(f"Rewards Member - {self.is_rewards_member}")
        print(f"Gold Card Points - {self.gold_card_points}")

    def enroll(self):
        if self.is_rewards_member == True:
            print(f"{self.first_name} already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            print(f"{self.first_name} has become a rewards member and now have {self.gold_card_points} gold card points to spend!")
            return True

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print(f"{self.first_name} does not have enough gold points.")
            return False
        else:
            self.gold_card_points = self.gold_card_points - (amount)
            print(f"{self.first_name} now has {self.gold_card_points} gold card points left.")
            return True

garret = User("Garret", "Cuadra", "cuadragarret@gmail.com", 22)
nathan = User("Nathan", "Cuadra", "abc@gmail.com", 24)
kyle = User("Kyle", "Cuadra", "abcd@gmail.com", 26)
garret.display_info()
garret.enroll()
nathan.enroll()
garret.spend_points(50)
nathan.spend_points(80)
garret.display_info()
nathan.display_info()
kyle.display_info()
