import random
import pickle

quests = ["Language", "Coding", "Writing", "Reading Fiction", "Drawing", "Reading Non-Fiction", "Piano", "Cardio",
          "Strength", "Meditation"]

selections = []

def quest_log():
    count = 1
    while count <= 3:
        selection = random.choice(quests)
        selections.append(selection)
        quests.remove(selection)
        count +=1

def one_additional_quest():
    one_more = random.choice(quests)
    selections.append(one_more)


def quest_finished():
    position = input("Enter postion of quest in a list.")
    if position == "1":
        del selections[0]
    elif position == "2":
        del selections[1]
    elif position == "3":
        del selections[2]

def save_and_show():
    pickle_out = open('save.pickle', 'wb')
    pickle.dump(selections, pickle_out)
    pickle_out.close()


def load_and_show():
    selections.clear()
    pickle_in = open("save.pickle", "rb")
    new_selections = pickle.load(pickle_in)
    for i in new_selections:
        selections.append(i)


while True:
    select_type = input("1 - new quest log, 2 - new quest, 3 - finished a quest 4 - save and show current quest log"
                        " 5 - load and show current quest log\n")

    if select_type == "1":
        quest_log()
    elif select_type == "2":
        one_additional_quest()
    elif select_type == "3":
        quest_finished()
    elif select_type == "4":
        save_and_show()
    elif select_type == "5":
        load_and_show()
    print(selections)