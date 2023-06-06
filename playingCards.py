def can_play_card(table_card, hand_cards):
    table_rank, table_suit = table_card[0], table_card[1]
    for card in hand_cards:
        if card[0] == table_rank or card[1] == table_suit:
            return "YES"
    return "NO"


t = int(input())
for i in range(t):
    table_card = input()
    hand_cards = input().strip().split()
    result = can_play_card(table_card, hand_cards)
    print(result)
