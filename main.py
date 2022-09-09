from definitions import *
from trello_api import TRELLO_API

from datetime import datetime

def get_cards():
    trello_api = TRELLO_API(TRELLO_BOARD_ID,IGNORE_LIST_IDS,IGNORE_CARDS_IDS, DONE_LIST_ID)
    lists = (trello_api.get_board_lists())
    card_list_not_done = []
    card_list_done = []
    for list in lists:
        if list['id'] not in trello_api.ignore_list_ids:
            print(list['name'])
            cards = trello_api.get_list_cards(list['id'])
            for card in cards:
                if(card['id'] in trello_api.ignore_cards_ids):
                    continue
                difficulty = 0
                criterias = []
                due =int( datetime.fromisoformat(str(card['due']).split("T")[0]).timestamp())
                #print(due)
                labels = card['labels']
                for label in labels:
                    try:
                        difficulty = int(label['name'])
                    except:
                        criterias.append(label['name'])
                if list['id'] == trello_api.done_list_id:
                    card_list_done.append([card['name'],difficulty,criterias,due])
                else:
                    card_list_not_done.append([card['name'],difficulty,criterias,due])
    return card_list_not_done, card_list_done
def sort_cards(card_list_not_done,card_list_done):
    card_list_not_done.sort(key=lambda x: x[3])
    card_list_done.sort(key=lambda x: x[3])
    return card_list_not_done,card_list_done

def get_accumulated_difficulty(card_list_not_done, card_list_done):
    not_done_difficulty_acc = []
    done_difficulty_acc = []
    acc = 0
    for card in card_list_not_done:
        acc = acc + card[1]
        not_done_difficulty_acc.append([card[3],acc])


    acc = 0
    for card in card_list_done:
        acc = acc + card[1]
        done_difficulty_acc.append([card[3],acc])
    return not_done_difficulty_acc, done_difficulty_acc
if __name__ == "__main__":

    card_list_not_done, card_list_done = get_cards()
    card_list_not_done, card_list_done = sort_cards(card_list_not_done, card_list_done)
    
    not_done_difficulty_acc, done_difficulty_acc = get_accumulated_difficulty(card_list_not_done, card_list_done)
    
    for acc in not_done_difficulty_acc:
        print(acc)
    print()
    for acc in done_difficulty_acc:
        print(acc)
