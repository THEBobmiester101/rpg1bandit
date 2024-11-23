from typing import Callable


class Item:

    # item name
    name: str = ""

    # item description to briefly describe its effects
    description: str = ""

    # whether the item no longer has any effects
    used_up: bool = False

    # dictionary mapping the name of a function to be 
    # wrapped to an effect called before the function
    callbacks: dict[str, Callable] = {}

    def __init__(self, name, description, callbacks: dict[str, Callable]):
        self.name = name
        self.description = description
        self.callbacks = callbacks
