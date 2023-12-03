"""Spaceship."""


class Crewmate:
    """Crewmate class."""

    def __init__(self, color: str, role: str, tasks: int = 10):
        """Construct the class."""
        self.color = color.capitalize()

        possible_roles = ["CREWMATE", "SHERIFF", "GUARDIAN ANGEL", "ALTRUIST"]
        if role.upper() in possible_roles:
            self.role = role.title()
        else:
            self.role = possible_roles[0].title()

        self.tasks = tasks
        self.protected = False

    def __repr__(self):
        """Magic method repr for string representation."""
        return f"{self.color}, role: {self.role}, tasks left: {self.tasks}."

    def complete_task(self):
        """Subtract task from tasks list."""
        if self.tasks > 1:
            self.tasks -= 1
        else:
            return


class Impostor:
    """Impostor class."""

    def __init__(self, color: str):
        """Construct the class."""
        self.color = color.title()
        self.kills = 0

    def __repr__(self):
        """Magic method repr for string representation."""
        return f"Impostor {self.color}, kills: {self.kills}."


class Spaceship:
    """Spaceship class."""

    def __init__(self):
        """Construct the class."""
        self.crewmate_list = []
        self.impostor_list = []
        self.dead_players = []

    def get_crewmate_list(self):
        """Get list of crewmates."""
        return self.crewmate_list

    def add_crewmate(self, crewmate: Crewmate):
        """Add a crewmate."""
        if isinstance(crewmate, Crewmate) and self.check_if_new_player(crewmate):
            self.crewmate_list.append(crewmate)

    def get_impostor_list(self):
        """Get list of impostors."""
        return self.impostor_list

    def add_impostor(self, impostor: Impostor):
        """Add an impostor."""
        if isinstance(impostor, Impostor) and len(self.impostor_list) < 3 and self.check_if_new_player(impostor):
            self.impostor_list.append(impostor)
        else:
            return

    def get_dead_players(self):
        """Get list of dead players."""
        return self.dead_players

    def check_if_new_player(self, player):
        """Control if the body-color is not already in use."""
        for crewmate in self.crewmate_list:
            if player.color.title() == crewmate.color:
                return False

        for impostor in self.impostor_list:
            if player.color.title() == impostor.color:
                return False

        for dead in self.dead_players:
            if player.color.title() == dead.color:
                return False

        return True

    def kill_impostor(self, sheriff: Crewmate, color: str):
        """Murder an imposter if the chosen color is correct."""
        if sheriff in self.crewmate_list and sheriff.role == "Sheriff":
            person_to_remove = None
            for person in self.impostor_list:
                if person.color == color.title():
                    person_to_remove = person

            if person_to_remove:
                self.impostor_list.remove(person_to_remove)
                self.dead_players.append(person_to_remove)
            else:
                self.crewmate_list.remove(sheriff)
                self.dead_players.append(sheriff)

        return

    def revive_crewmate(self, altruist: Crewmate, dead_crewmate: Crewmate):
        """Help a friend in need."""
        if altruist in self.crewmate_list and altruist.role == "Altruist" \
                and dead_crewmate in self.dead_players:
            self.dead_players.remove(dead_crewmate)
            self.crewmate_list.append(dead_crewmate)
            self.crewmate_list.remove(altruist)
            self.dead_players.append(altruist)

    def protect_crewmate(self, guardian_angel: Crewmate, crewmate_to_protect: Crewmate):
        """Enable protection for crewmate."""
        if guardian_angel.role == "Guardian Angel" and crewmate_to_protect.role != "Guardian Angel":
            for person in self.crewmate_list:
                person.protected = False

            crewmate_to_protect.protected = True

    def kill_crewmate(self, impostor: Impostor, color: str):
        """Simulate killing a crewmate."""
        the_person = None
        for person in self.crewmate_list:
            if person.color == color.title():
                the_person = person

        if the_person:
            if the_person.protected:
                the_person.protected = False
            else:
                self.dead_players.append(the_person)
                self.crewmate_list.remove(the_person)
                impostor.kills += 1

    def sort_crewmates_by_tasks(self):
        """Sort crewmates by tasks."""
        return sorted(self.crewmate_list, key=lambda x: x.tasks)

    def sort_impostors_by_kills(self):
        """Sort impostors by kills."""
        return sorted(self.impostor_list, key=lambda x: -x.kills)

    def get_regular_crewmates(self):
        """Return a list of regular crewmates."""
        regulars = []
        for i in self.crewmate_list:
            if i.role == "Crewmate":
                regulars.append(i)

        return regulars

    def get_role_of_player(self, color: str):
        """Return the role of player."""
        for player in self.crewmate_list:
            if player.color == color.title():
                return player.role

        for player in self.impostor_list:
            if player.color == color.title():
                return "Impostor"

    def get_crewmate_with_most_tasks_done(self):
        """Return crewmate with the most tasks done."""
        the_one = self.crewmate_list[0]
        for crewmate in self.crewmate_list:
            if crewmate.tasks < the_one.tasks:
                the_one = crewmate

        return the_one

    def get_impostor_with_most_kills(self):
        """Return the impostor with most kills."""
        the_one = self.impostor_list[0]
        for imposter in self.impostor_list:
            if imposter.kills > the_one.kills:
                the_one = imposter

        return the_one


if __name__ == "__main__":
    print("Spaceship.")

    spaceship = Spaceship()
    print(spaceship.get_dead_players())  # -> []
    print()

    print("Let's add some crewmates.")
    red = Crewmate("Red", "Crewmate")
    white = Crewmate("White", "Impostor")
    yellow = Crewmate("Yellow", "Guardian Angel", tasks=5)
    green = Crewmate("green", "Altruist")
    blue = Crewmate("BLUE", "Sheriff", tasks=0)

    print(red)  # -> Red, role: Crewmate, tasks left: 10.
    print(white)  # -> White, role: Crewmate, tasks left: 10.
    print(yellow)  # -> Yellow, role: Guardian Angel, tasks left: 5.
    print(blue)  # -> Blue, role: Sheriff, tasks left: 0.
    print()

    print("Let's make Yellow complete a task.")
    yellow.complete_task()
    print(yellow)  # ->  Yellow, role: Guardian Angel, tasks left: 4.
    print()

    print("Adding crewmates to Spaceship:")
    spaceship.add_crewmate(red)
    spaceship.add_crewmate(white)
    spaceship.add_crewmate(yellow)
    spaceship.add_crewmate(green)
    print(spaceship.get_crewmate_list())  # -> Red, White, Yellow and Green

    spaceship.add_impostor(blue)  # Blue cannot be an Impostor.
    print(spaceship.get_impostor_list())  # -> []
    spaceship.add_crewmate(blue)
    print()

    print("Now let's add impostors.")
    orange = Impostor("orANge")
    black = Impostor("black")
    purple = Impostor("Purple")
    spaceship.add_impostor(orange)
    spaceship.add_impostor(black)

    spaceship.add_impostor(Impostor("Blue"))  # Blue player already exists in Spaceship.
    spaceship.add_impostor(purple)
    spaceship.add_impostor(Impostor("Pink"))  # No more than three impostors can be on Spaceship.
    print(spaceship.get_impostor_list())  # -> Orange, Black and Purple
    print()

    print("The game has begun! Orange goes for the kill.")
    spaceship.kill_crewmate(orange, "yellow")
    print(orange)  # -> Impostor Orange, kills: 1.
    spaceship.kill_crewmate(black, "purple")  # You can't kill another Impostor, silly!
    print(spaceship.get_dead_players())  # -> Yellow
    print()

    spaceship.kill_impostor(blue, "black")
    print(spaceship.get_impostor_list())
    print()

    print("Yellow is a Guardian angel, and can protect their allies when dead.")
    spaceship.protect_crewmate(yellow, green)
    print(green.protected)  # -> True
    spaceship.kill_crewmate(orange, "green")
    print(green in spaceship.dead_players)  # -> False
    print(green.protected)  # -> False
    print()

    print("Green revives their ally.")
    spaceship.kill_crewmate(purple, "RED")
    spaceship.revive_crewmate(green, red)
    print(red in spaceship.dead_players)  # -> False
    print()

    print("Let's check if the sorting and filtering works correctly.")

    red.complete_task()
    print(spaceship.get_role_of_player("Blue"))  # -> Sheriff
    spaceship.kill_crewmate(purple, "blue")
    print(spaceship.sort_crewmates_by_tasks())  # -> Red, White
    print(spaceship.sort_impostors_by_kills())  # -> Purple, Orange, Black
    print(spaceship.get_regular_crewmates())  # -> White, Red
