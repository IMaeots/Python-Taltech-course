"""Spaceship OP Tests."""

from spaceship import Crewmate, Impostor
from spaceship_op import OPSpaceship


def test__kill_crewmate_less_votes_than_skips():
    """Test kill crewmate."""
    spaceship = OPSpaceship("easy")
    aru = Crewmate("red", "guardian aNGEl")
    taru = Crewmate("yellow", "crewmate")
    maru = Crewmate("green", "sheriff")
    karu = Impostor("blue")
    spaceship.add_crewmate(aru)
    spaceship.add_crewmate(taru)
    spaceship.add_crewmate(maru)
    spaceship.add_impostor(karu)
    spaceship.start_game()
    spaceship.kill_crewmate(karu, "green")
    spaceship.report_dead_body(aru, maru)
    spaceship.cast_vote(aru, "blue")
    spaceship.cast_vote(taru, "")
    spaceship.cast_vote(karu, "")
    assert spaceship.end_meeting() == "No one was ejected. (Skipped)"


def test__add_crewmate_sheriff():
    """Test adding crewmate as sheriff."""
    spaceship = OPSpaceship("easy")
    crewmate2 = Crewmate("Red", "Sheriff")
    spaceship.add_crewmate(crewmate2)
    assert spaceship.get_role_of_player("red") == "Sheriff"


def test__end_game_no_impostors_left():
    """Test game ending with no impostors left."""
    spaceship = OPSpaceship("easy")
    crewmate1 = Crewmate("red", "sheriff")
    crewmate2 = Crewmate("blue", "crewmate")
    impostor = Impostor("yellow")
    spaceship.add_crewmate(crewmate1)
    spaceship.add_crewmate(crewmate2)
    spaceship.add_impostor(impostor)
    spaceship.start_game()
    assert spaceship.kill_impostor(crewmate1, "yellow") == "Crewmates won."


def test__end_game_equal_impostors_crewmates():
    """Test game ending with equal impostors and crewmates."""
    spaceship = OPSpaceship("easy")
    crewmate1 = Crewmate("red", "crewmate")
    crewmate2 = Crewmate("blue", "crewmate")
    crewmate3 = Crewmate("white", "sheriff")
    impostor1 = Impostor("yellow")
    impostor2 = Impostor("green")
    spaceship.add_crewmate(crewmate1)
    spaceship.add_crewmate(crewmate2)
    spaceship.add_crewmate(crewmate3)
    spaceship.add_impostor(impostor1)
    spaceship.add_impostor(impostor2)
    spaceship.start_game()
    assert spaceship.kill_crewmate(impostor1, "red") == "Impostors won."


def test__meeting_voting_tie():
    """Test meeting voting resulting in a tie."""
    spaceship = OPSpaceship("easy")
    crewmate1 = Crewmate("red", "crewmate")
    crewmate2 = Crewmate("blue", "crewmate")
    crewmate3 = Crewmate("black", "crewmate")
    impostor1 = Impostor("yellow")
    spaceship.add_crewmate(crewmate1)
    spaceship.add_crewmate(crewmate2)
    spaceship.add_crewmate(crewmate3)
    spaceship.add_impostor(impostor1)
    spaceship.start_game()
    spaceship.kill_crewmate(impostor1, "red")
    spaceship.report_dead_body(impostor1, crewmate1)
    spaceship.cast_vote(crewmate2, "yellow")
    spaceship.cast_vote(crewmate3, "blue")
    spaceship.cast_vote(impostor1, "black")
    assert spaceship.end_meeting() == "No one was ejected. (Tie)"


def test__get_vote_for_non_existing_player():
    """Test getting vote for a player that hasn't voted."""
    spaceship = OPSpaceship("hard")
    crewmate = Crewmate("red", "crewmate")
    impostor = Impostor("yellow")
    spaceship.add_crewmate(crewmate)
    spaceship.add_impostor(impostor)
    spaceship.start_game()
    spaceship.report_dead_body(crewmate, impostor)
    spaceship.cast_vote(crewmate, "yellow")
    assert spaceship.get_vote(impostor.color) == "No vote found"


def test__hard_meeting_vote_player_off():
    """Test ejecting a player in hard mode."""
    spaceship = OPSpaceship("hard")
    crewmate1 = Crewmate("red", "crewmate")
    crewmate2 = Crewmate("yellow", "crewmate")
    crewmate3 = Crewmate("blue", "crewmate")
    crewmate4 = Crewmate("white", "crewmate")
    impostor1 = Impostor("purple")
    spaceship.add_crewmate(crewmate1)
    spaceship.add_crewmate(crewmate2)
    spaceship.add_crewmate(crewmate3)
    spaceship.add_crewmate(crewmate4)
    spaceship.add_impostor(impostor1)
    spaceship.start_game()
    spaceship.kill_crewmate(impostor1, "red")
    spaceship.report_dead_body(impostor1, crewmate1)
    spaceship.cast_vote(crewmate2, "yellow")
    spaceship.cast_vote(crewmate3, "yellow")
    spaceship.cast_vote(crewmate4, "yellow")
    spaceship.cast_vote(impostor1, "yellow")
    assert spaceship.end_meeting() == "Yellow was ejected."


def test__imposter_voted_out():
    """Test ejecting a player in hard mode."""
    spaceship = OPSpaceship("easy")
    crewmate1 = Crewmate("red", "crewmate")
    crewmate2 = Crewmate("yellow", "crewmate")
    crewmate3 = Crewmate("blue", "crewmate")
    crewmate4 = Crewmate("white", "crewmate")
    impostor1 = Impostor("purple")
    impostor2 = Impostor("gray")
    spaceship.add_crewmate(crewmate1)
    spaceship.add_crewmate(crewmate2)
    spaceship.add_crewmate(crewmate3)
    spaceship.add_crewmate(crewmate4)
    spaceship.add_impostor(impostor1)
    spaceship.add_impostor(impostor2)
    spaceship.start_game()
    spaceship.kill_crewmate(impostor1, "red")
    spaceship.report_dead_body(impostor1, crewmate1)
    spaceship.cast_vote(crewmate2, "purple")
    spaceship.cast_vote(crewmate3, "purple")
    spaceship.cast_vote(crewmate4, "purple")
    spaceship.cast_vote(impostor1, "purple")
    assert spaceship.end_meeting() == "Purple was an Impostor. 1 Impostor remains."
