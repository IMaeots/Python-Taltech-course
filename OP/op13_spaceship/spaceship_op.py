"""Spaceship OP."""
import spaceship


def get_object_by_color(color, object_list):
    """Return object from color."""
    for obj in object_list:
        if obj.color == color:
            return obj
    return None


class OPSpaceship(spaceship.Spaceship):
    """OP version of spaceship."""

    def __init__(self, difficulty: str):
        """Initialize the class."""
        super().__init__()
        if difficulty.lower() in ["easy", "hard"]:
            self.difficulty = difficulty.lower()
        else:
            self.difficulty = "hard"

        self.ejected_players = []
        self.meeting = False
        self.votes = {}
        self.game = False

    def add_crewmate(self, crewmate: spaceship.Crewmate):
        """Add crewmate."""
        if self.game is False:
            super().add_crewmate(crewmate)

    def add_impostor(self, impostor: spaceship.Impostor):
        """Add impostor."""
        if self.game is False:
            super().add_impostor(impostor)

    def kill_impostor(self, sheriff: spaceship.Crewmate, color: str):
        """Kill impostor."""
        if self.game is True and self.meeting is False:
            super().kill_impostor(sheriff, color)
            return self.check_if_game_over()

    def kill_crewmate(self, impostor: spaceship.Impostor, color: str):
        """Kill crewmate."""
        if self.game is True and self.meeting is False:
            super().kill_crewmate(impostor, color)
            return self.check_if_game_over()

    def check_if_game_over(self):
        """Check if the game is over."""
        if self.game is True:
            win_message = None
            if len(self.impostor_list) < 1:
                win_message = "Crewmates won."
            elif len(self.crewmate_list) == len(self.impostor_list) and len(self.impostor_list) <= 3:
                win_message = "Impostors won."

            if win_message is not None:
                self.ejected_players = []
                self.impostor_list = []
                self.crewmate_list = []
                self.votes = {}
                self.game = False
                self.meeting = False

                return win_message
        return

    def start_game(self):
        """Start the game."""
        if self.game is False:
            if 0 < len(self.impostor_list) < len(
                    self.crewmate_list) and len(self.crewmate_list) >= 2:
                self.game = True

    def report_dead_body(self, reporting_player: spaceship.Crewmate | spaceship.Impostor,
                         dead_body: spaceship.Crewmate | spaceship.Impostor):
        """Report a dead body."""
        if reporting_player not in self.dead_players or reporting_player not in self.ejected_players:
            if dead_body in self.dead_players:
                self.meeting = True

    def cast_vote(self, player: spaceship.Crewmate | spaceship.Impostor, target_player_color: str):
        """Cast vote in the meeting."""
        if self.game is True and self.meeting is True:
            if player in self.crewmate_list or player in self.impostor_list:
                if player.color not in self.votes:
                    if any(target_player_color == obj.color for obj in self.crewmate_list + self.impostor_list):
                        self.votes[player.color] = target_player_color

    def end_meeting(self):
        """End meeting."""
        for person in self.dead_players:
            self.ejected_players.append(person)
            self.dead_players.remove(person)

        if self.game is True and self.meeting is True:
            if len(self.votes) == 0:
                self.meeting = False
                return "No one was ejected. (Skipped)"
            else:
                vote_count = {}
                for color in self.votes.values():
                    if color not in vote_count:
                        vote_count[color] = 1
                    else:
                        vote_count[color] += 1

                max_value = max(vote_count.values())
                max_keys = [key for key, value in vote_count.items() if value == max_value]
                if len(max_keys) != 1:
                    self.meeting = False
                    self.votes = {}
                    return "No one was ejected. (Tie)"

                eliminated_person = max_keys[0]
                if self.difficulty == "easy":
                    if eliminated_person in self.impostor_list:
                        self.impostor_list.remove(eliminated_person)
                        self.ejected_players.append(eliminated_person)
                        impostors_left = len(self.impostor_list)
                        if impostors_left > 1:
                            self.meeting = False
                            self.votes = {}
                            end = self.check_if_game_over()
                            if self.game:
                                return f"{eliminated_person.color} was an Impostor. {impostors_left} Impostors remains."
                            return end
                        else:
                            self.meeting = False
                            self.votes = {}
                            end = self.check_if_game_over()
                            if self.game:
                                return f"{eliminated_person.color} was an Impostor. {impostors_left} Impostor remain."
                            return end
                    elif eliminated_person in self.crewmate_list:
                        self.crewmate_list.remove(eliminated_person)
                        self.ejected_players.append(eliminated_person)
                        impostors_left = len(self.impostor_list)
                        if impostors_left > 1:
                            self.meeting = False
                            self.votes = {}
                            end = self.check_if_game_over()
                            if self.game:
                                return f"{eliminated_person.color} was not an Impostor. {impostors_left} Impostors remains."
                            return end
                        else:
                            self.meeting = False
                            self.votes = {}
                            end = self.check_if_game_over()
                            if self.game:
                                return f"{eliminated_person.color} was not an Impostor. {impostors_left} Impostor remain."
                            return end
                else:
                    if eliminated_person in self.impostor_list:
                        self.impostor_list.remove(eliminated_person)
                        self.ejected_players.append(eliminated_person)
                    elif eliminated_person in self.crewmate_list:
                        self.crewmate_list.remove(eliminated_person)
                        self.ejected_players.append(eliminated_person)

                    self.meeting = False
                    self.votes = {}
                    end = self.check_if_game_over()
                    if self.game:
                        return f"{eliminated_person.color} was ejected."
                    return end
        else:
            self.meeting = False
            self.votes = {}
            return

    def get_vote(self, color: str):
        """Return who a player voted for."""
        if color.title() in self.votes.keys():
            return self.votes[color.title()]
        else:
            return "No vote found"

    def get_ejected_players(self):
        """Get ejected players."""
        return self.ejected_players

    def get_votes(self):
        """Get votes."""
        return self.votes

    def is_meeting(self):
        """Return if there is a meeting going on."""
        return self.meeting
