#!/usr/bin/env python3

import solver
import game
import external_solver

import sys


HELP_TEXT = """Wordle.py

Solve wordle with a smart assistant.

USAGE:
    wordle game        Play the game, vanilla
    wordle solver      Play the game with suggested solutions
    wordle external    Play the game with self-provided outcomes
"""


def main():
    if len(sys.argv) == 1:
        return print(HELP_TEXT)

    cmd = sys.argv[1]

    app = {}

    app["game"] = game.run
    app["solver"] = solver.run
    app["external"] = external_solver.run

    try:
        run = app[cmd]
    except KeyError:
        return print(HELP_TEXT)

    run()


if __name__ == "__main__":
    main()
