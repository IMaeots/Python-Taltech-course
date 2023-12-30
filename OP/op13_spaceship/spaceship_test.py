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
    spaceship = OPSpaceship("easy")
    crewmate2 = Crewmate("Red", "Sheriff")
    spaceship.add_crewmate(crewmate2)
    assert spaceship.get_role_of_player("red") == "Sheriff"
