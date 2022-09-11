from urllib.request import urlopen
import json 
from definitions import *

class TRELLO_API():
    def __init__(self,board_id,ignore_list_ids,ignore_cards_ids,done_list_id):
        self.done_list_id = done_list_id
        self.ignore_cards_ids = ignore_cards_ids
        self.board_id = board_id
        self.ignore_list_ids = ignore_list_ids
    def get_board_lists(self):
        return json.loads(urlopen(f"https://api.trello.com/1/boards/{self.board_id}/lists").read().decode())
    def get_list_cards(self,list_id):
        return json.loads(urlopen(f"https://api.trello.com/1/lists/{list_id}/cards").read().decode())
    def get_card_comments(self,card_id):
        return json.loads(urlopen(f'https://api.trello.com/1/cards/{card_id}/actions?filter=commentCard').read().decode())

if __name__ == "__main__":
    trello_api = TRELLO_API(TRELLO_BOARD_ID,IGNORE_LIST_IDS)
    lists = (trello_api.get_board_lists())
    for list in lists:
        if list['id'] not in trello_api.ignore_list_ids:
            print(list['name'])
            cards = trello_api.get_list_cards(list['id'])
            for card in cards:
                print(f"\t{card['name']}")
