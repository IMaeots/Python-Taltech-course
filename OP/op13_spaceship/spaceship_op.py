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
        self.players_voted = []
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
            self.check_if_game_over()

    def kill_crewmate(self, impostor: spaceship.Impostor, color: str):
        """Kill crewmate."""
        if self.game is True and self.meeting is False:
            super().kill_crewmate(impostor, color)
            self.check_if_game_over()

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
                self.players_voted = []
                self.votes = {}
                self.game = False
                self.meeting = False
                print(win_message)

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
        if player not in self.players_voted:
            self.players_voted.append(player)
            if self.game is True and self.meeting is True:
                if player in self.crewmate_list or player in self.impostor_list:
                    if target_player_color.title() not in self.votes.keys():
                        self.votes[target_player_color.title()] = 1
                    else:
                        self.votes[target_player_color.title()] += 1

    def end_meeting(self):
        """End meeting."""
        if self.game is True and self.meeting is True:
            if len(self.votes) == 0:
                self.meeting = False
                self.players_voted = []
                return "No one was ejected. (Skipped)"
            else:
                max_value = max(self.votes.values())
                eliminated = [key for key, value in self.votes.items() if value == max_value]
                if len(eliminated) != 1:
                    self.meeting = False
                    self.players_voted = []
                    return "No one was ejected. (Tie)"
                else:
                    if self.difficulty == "easy":
                        eliminated_person = get_object_by_color(eliminated, self.impostor_list)
                        if eliminated_person:
                            self.impostor_list.remove(eliminated_person)
                            self.ejected_players.append(eliminated_person)
                            impostors_left = len(self.impostor_list)
                            if impostors_left > 1:
                                self.meeting = False
                                self.players_voted = []
                                self.votes = {}
                                self.check_if_game_over()
                                if self.game:
                                    return f"{eliminated} was an Impostor. {impostors_left} Impostors remains."
                                return
                            else:
                                self.meeting = False
                                self.players_voted = []
                                self.votes = {}
                                self.check_if_game_over()
                                if self.game:
                                    return f"{eliminated} was an Impostor. {impostors_left} Impostor remain."
                                return

                        eliminated_person = get_object_by_color(eliminated, self.crewmate_list)
                        if eliminated_person:
                            self.crewmate_list.remove(eliminated_person)
                            self.ejected_players.append(eliminated_person)
                            impostors_left = len(self.impostor_list)
                            if impostors_left > 1:
                                self.meeting = False
                                self.players_voted = []
                                self.votes = {}
                                self.check_if_game_over()
                                if self.game:
                                    return f"{eliminated} was not an Impostor. {impostors_left} Impostors remains."
                                return
                            else:
                                self.meeting = False
                                self.players_voted = []
                                self.votes = {}
                                self.check_if_game_over()
                                if self.game:
                                    return f"{eliminated} was not an Impostor. {impostors_left} Impostor remain."
                                return
                    else:
                        eliminated_person = get_object_by_color(eliminated, self.impostor_list)
                        if eliminated_person:
                            self.impostor_list.remove(eliminated_person)
                            self.ejected_players.append(eliminated_person)
                        else:
                            eliminated_person = get_object_by_color(eliminated, self.crewmate_list)
                            if eliminated_person:
                                self.crewmate_list.remove(eliminated)
                                self.ejected_players.append(eliminated)

                        self.meeting = False
                        self.players_voted = []
                        self.votes = {}
                        self.check_if_game_over()
                        if self.game:
                            return f"{eliminated} was ejected."
        else:
            self.meeting = False
            self.players_voted = []
            self.votes = {}
            return

    def get_vote(self, color: str):
        """Return who a player voted for."""
        return self.votes[color.title()]

    def get_ejected_players(self):
        """Get ejected players."""
        return self.ejected_players

    def get_votes(self):
        """Get votes."""
        return self.votes

    def is_meeting(self):
        """Return if there is a meeting going on."""
        return self.meeting
