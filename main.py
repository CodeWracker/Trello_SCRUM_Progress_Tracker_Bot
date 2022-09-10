from definitions import *
from trello_api import TRELLO_API

from datetime import datetime

def get_cards():
    trello_api = TRELLO_API(TRELLO_BOARD_ID,IGNORE_LIST_IDS,IGNORE_CARDS_IDS, DONE_LIST_ID)
    lists = (trello_api.get_board_lists())
    card_list_not_done = []
    card_list_done = []
    all_cards = []
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
                all_cards.append([card['name'],difficulty,criterias,due])
                if list['id'] == trello_api.done_list_id:
                    card_list_done.append([card['name'],difficulty,criterias,due])
                else:
                    card_list_not_done.append([card['name'],difficulty,criterias,due])
    return all_cards,card_list_not_done, card_list_done


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

def get_crit_activity_list(all_cards):
    crit_activity = {}
    for card in all_cards:
        for crit in card[2]:
            if crit not in crit_activity:
                crit_activity[crit] = []
            crit_activity[crit].append(card[0]) 
    return crit_activity
if __name__ == "__main__":

    all_cards,card_list_not_done, card_list_done = get_cards()
    card_list_not_done, card_list_done = sort_cards(card_list_not_done, card_list_done)
    
    not_done_difficulty_acc, done_difficulty_acc = get_accumulated_difficulty(card_list_not_done, card_list_done)
    
    crit_activity = get_crit_activity_list(all_cards)
    
    for crit in crit_activity:
        print(f'{crit} : {crit_activity[crit]}')
    print()

    for acc in not_done_difficulty_acc:
        print(acc)
    print()
    for acc in done_difficulty_acc:
        print(acc)
