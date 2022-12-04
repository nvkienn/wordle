from base_game_code import colorize_outcome
import threading
import listw
import time
from database import Database

db = Database(5)

start_time = time.time()
turn = 0

# generates answer
# ans = ans_generator()


# to be averaged to find the average number of guesses took to solve all answers
number_of_guess = 0

word_count = 0


def compute(start, end, db):
    print("GOT HERE")
    number_of_guess = 0
    turn = 0
    word_count = start
    # running through all answers
    for i in range(start, start + 2):
        answer = listw.ans[i]
        word_count += 1
        print("Word #" + str(word_count))
        user_guess = []
        ans_list = listw.ans
        # initiating each turn
        for turn in range(6):
            print("Guess #" + str(turn + 1))
            if turn == 0:
                guess = "soare"
            elif len(ans_list) == 1:
                guess = ans_list[0]
            else:
                a = db.best_entropy(ans_list)
                guess = a[0]
                b = db.possible_answers(ans_list)
                if b[0][1] == a[1]:
                    guess = b[0][0]

            # generates outcome
            outcome = db.get_outcome(answer, guess)
            user_guess.append(colorize_outcome(guess, outcome))
            for z in user_guess:
                print(z)

            ans_list = db.reduce_ans_list(guess, outcome, ans_list)
            print("\n-----------------------------")
            if guess == answer:
                break
        number_of_guess += turn + 1
    results[(start, end)] = {"number_of_guess": number_of_guess}


total = len(listw.ans)
chunk_size = 400
b = 0
chunk_counts = []
while b < total:
    chunk_counts.append(b)
    b += chunk_size
chunk_counts.append(total + 1)
db.read_all()

results = {}
threads = []

for i in range(len(chunk_counts) - 1):
    print(chunk_counts[i], chunk_counts[i + 1])
    start = chunk_counts[i]
    end = chunk_counts[i + 1]
    t = threading.Thread(target=compute, args=(start, end, db))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
    # compute(i, i + 1, db)
print(chunk_counts)

print("Average number of guesses:", number_of_guess / 2309)
print(time.time() - start_time)
