"""
Test addition of players::

    >>> maguire = ManUtdPlayer("Harry McGuire", ["Sheffield", "Man Utd"], shirt_number=5)
    >>> new_defender = ManUtdPlayer("Who Knows", ["Madrid"], shirt_number=5)
    Traceback (most recent call last):
    ...
    ValueError: Player with number 5 is already part of the team.
"""
from dataclasses import dataclass, field

@dataclass
class Athlete:
    name: str
    teams_played: list[str] = field(default_factory=list)
    starting_lineup: bool = field(default=False, repr=False)


defender = Athlete(
    name="McGuire",
    teams_played=["Sheffield Utd", "Man Utd"],
    starting_lineup=True,
)

print(defender)


@dataclass
class ManUtdPlayer(Athlete):
    all_numbers = set()
    shirt_number: int | None = None

    def __post_init__(self):
        cls = self.__class__
        if len(cls.all_numbers) >= 99:
            raise ValueError("No more than 99 players can be registered.")

        if self.shirt_number is None:
            for num in range(1, 99):
                if num in cls.all_numbers:
                    continue
                self.shirt_number = num
                break

        if self.shirt_number in cls.all_numbers:
            raise ValueError(
                f"Player with number {self.shirt_number} is already part of"
                " the team."
            )

        cls.all_numbers.add(self.shirt_number)
