test:
	python3 database.py

tedst:
	make solver

solver:
	python3 solver_RUN_THIS.py

bench:
	python3 bench.py

two:
	python3 two_steps_ahead_solver_RUN_THIS.py

game:
	python3 game_RUN_THIS.py

ext:
	python3 external_solver_RUN_THIS.py

auto:
	python3 auto_solver_RUN_THIS.py

auto-anti:
	python3 auto_anti_wordle_RUN_THIS.py

gen:
	python3 outcomes_combination.py

.PHONY: solver two game ext auto auto-anti gen bench test
