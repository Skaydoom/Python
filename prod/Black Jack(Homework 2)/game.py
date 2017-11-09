from random import *
class Card(object):
#Инициализация переменных
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

#Начисление очков за определенную карту
    def card_value(self):
        if self.rank in "TJQK":
            return 10
        else:
            return " A23456789".index(self.rank)
        
    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)

#Создание класса диллер
class Dealer(object):
    def __init__(self,name):
        self.name=("Диллер")
        self.cards=[]

#Добор карты для диллера
    def add_card(self, card):
        self.cards.append(card)

#Вычисление очков за карты в руке
    def get_value(self):
        result = 0
        aces = 0
        for card in self.cards:
            result += card.card_value()
            if card.get_rank() == "A":
                aces += 1
        #Подсчет очков за туз
        if result + aces * 10 <= 21:
            result += aces * 10
        return result

#Вывод кол-ва очков в руке
    def __str__(self):
        text = "%s's Рука:\n" % self.name
        for card in self.cards:
            text += str(card) + " "
        text += "\nОчки в руке: " + str(self.get_value())
        return text

#Создание руки игрока с именем "___"
class Hand(object):
    def __init__(self, name):
        self.name = input("Введите имя игрока: ")
        self.cards = []

#Добор карты для игрока
    def add_card(self, card):
        self.cards.append(card)

#Пересчет очков для игрока
    def get_value(self):
        result = 0
        aces = 0
        for card in self.cards:
            result += card.card_value()
            if card.get_rank() == "A":
                aces += 1
        if result + aces * 10 <= 21:
            result += aces * 10
        return result

#Вывод кол-ва очков игрока
    def __str__(self):
        text = "%s's Рука:\n" % self.name
        for card in self.cards:
            text += str(card) + " "
        text += "\nОчки в руке: " + str(self.get_value())
        return text

#Создание класса "Колода". Создание мастей, рангов
class Deck(object):
    def __init__(self):
        # ранги
        ranks = "23456789TJQKA"
        # масти
        suits = "♠♥♣♦"
        #Создание колоды
        self.cards = [Card(r, s) for r in ranks for s in suits]
        #Перетасовка колоды
        shuffle(self.cards)

#Сдача карты
    def deal_card(self):
        return self.cards.pop()

#Главная функция начала игры
def new_game():
    #Создание колоды
    d = Deck()
    #Создание руки
    player_hand = Hand("Player")
    dealer_hand = Dealer("Dealer")
    #Выдача 2 карт игроку и 1 карты диллеру
    player_hand.add_card(d.deal_card())
    player_hand.add_card(d.deal_card())
    dealer_hand.add_card(d.deal_card())
    print(dealer_hand)
    print("="*20)
    print(player_hand)
    in_game = True
    #Добор карты если рука<21
    while player_hand.get_value() < 21:
        ans = input("Добрать или сдать?(y/n)")
        if ans == "y":
            player_hand.add_card(d.deal_card())
            print(player_hand)
            if player_hand.get_value() > 21:
                print("Ты проиграл")
                in_game = False
        elif ans == "n":
            print("Ты сдал")
            break
        else:
            print("Выберите ответ y/n")
    print("=" * 20)
    if in_game:
        #Добор карт диллером
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(d.deal_card())
            print(dealer_hand)
            #Оценка руки диллера
            if dealer_hand.get_value() > 21:
                print("*Диллер(Перебор)")
                in_game = False
    #Победа или поражение
    if in_game:
        if player_hand.get_value() > dealer_hand.get_value():
            print ("Ты выйграл")
        elif player_hand.get_value() == dealer_hand.get_value():
            print("Ничья")
        else:
            print ("Диллер выйграл")
