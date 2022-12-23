from __future__ import annotations
import random as rd
from eatEntry import eatEntry
class species():

    def __init__(self, name, eatsList: list(eatEntry), diesProb: float, movesProb: float, birthsProb: float, position: list, **kwargs) -> None:
        self.name = name
        self.eatsList = eatsList
        self.diesProb = diesProb
        self.movesProb = movesProb
        self.birthsProb = birthsProb
        self.position = position
        self.color = 'red'

    def eat(self, creature: species) -> bool:
        for entry in self.eatsList:
            if entry.eatName == creature.name:
                rollDice = rd.rand