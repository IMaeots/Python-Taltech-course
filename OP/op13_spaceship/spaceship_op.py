"""Spaceship OP."""

import spaceship


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

        return None

    def start_game(self):
        """Start the game."""
        if self.game is False:
            if len(self.impostor_list) and len(self.crewmate_list) >= 2 and len(self.impostor_list) < len(
                    self.crewmate_list):
                self.game = True

    def report_dead_body(self, reporting_player: spaceship.Crewmate | spaceship.Impostor,
                         dead_body: spaceship.Crewmate | spaceship.Impostor):
        """Report a dead body."""
        if reporting_player not in self.dead_players or reporting_player not in self.ejected_players:
            if dead_body in self.dead_players:
                self.meeting = True

    def cast_vote(self, player: spaceship.Crewmate | spaceship.Impostor, target_player_color: str):
        """Cast vote in the meeting."""
        if player in self.crewmate_list or self.impostor_list:
            if player.color not in self.votes and self.game is True and self.meeting is True:
                if target_player_color in [gamer.color for gamer in self.crewmate_list + self.impostor_list]:
                    self.votes[player.color] = target_player_color.title()

    def end_meeting(self):
        """End meeting."""
        if self.game is True and self.meeting is True:
            if self.votes:
                eliminated = max(self.votes, key=self.votes.get)
                if self.difficulty == "easy":
                    if eliminated in self.impostor_list:
                        self.impostor_list.remove(eliminated)
                        self.ejected_players.append(eliminated)
                        impostors_left = len(self.impostor_list)
                        if impostors_left > 1:
                            self.meeting = False
                            return self.check_if_game_over() if not None else (f"{eliminated.color} was an Impostor. \\"
                                                                               f" {impostors_left} Impostors remains.")
                        else:
                            self.meeting = False
                            return self.check_if_game_over() if not None else (f"{eliminated.color} was an Impostor. \\"
                                                                               f"{impostors_left} Impostor remain.")
                    else:
                        self.crewmate_list.remove(eliminated)
                        self.ejected_players.append(eliminated)
                        impostors_left = len(self.impostor_list)
                        if impostors_left > 1:
                            self.meeting = False
                            return self.check_if_game_over() if not None else (f"{eliminated.color} was not an Impostor. \\"
                                                                               f" {impostors_left} Impostors remains.")
                        else:
                            self.meeting = False
                            return self.check_if_game_over() if not None else (f"{eliminated.color} was not an Impostor. \\"
                                                                               f"{impostors_left} Impostor remain.")
                else:
                    if eliminated in self.impostor_list:
                        self.impostor_list.remove(eliminated)
                        self.ejected_players.append(eliminated)
                    else:
                        self.crewmate_list.remove(eliminated)
                        self.ejected_players.append(eliminated)

                    self.meeting = False
                    return self.check_if_game_over() if not None else f"{eliminated.color} was ejected."
            else:
                self.meeting = False
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
