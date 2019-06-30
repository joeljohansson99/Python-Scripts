from random import randint
import os
clear = lambda: os.system('cls')

class Deck():
	def __init__(self):
		self.taken = []

	card_values = ['#','Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
	card_colors = ['#','Hearts','Spades','Diamonds','Clubs']
	ace = False

	def get_card(self):
		while True:
			rand_value = randint(1,13)
			rand_color = randint(1,4)

			tup = (rand_value, rand_color)

			if tup != self.taken:
				self.taken += tup
				return tup

	def display_cards(self, card, player):
		print(f"{player} drew "+ self.card_values[card[0]] + " of " + self.card_colors[card[1]])

	def count_sum(self, card):
		if card[0]==1:
			self.ace = True
		if card[0]>=10:
			return 10
		else:
			return card[0]

	def check_bust(self, total):
		return total>21

def run():
	clear()
	win = True
	go = Deck()
	computer_card = go.get_card()
	go.display_cards(computer_card, "Dealer")
	sum_computer = go.count_sum(computer_card)
	computer_card = go.get_card()
	go.display_cards(computer_card, "Dealer")
	sum_computer += go.count_sum(computer_card)
	print('')
	if go.ace == True:
		if sum_computer + 10 <22:
			sum_computer+=10
			go.ace = False

	play_card = go.get_card()
	go.display_cards(play_card, "You")
	sum_play = go.count_sum(play_card)
	play_card = go.get_card()
	go.display_cards(play_card, "You")
	sum_play += go.count_sum(play_card)
	print('')

	while True:
		s = input('Hit or Stay? ')
		if s.lower()=='hit':
			play_card = go.get_card()
			go.display_cards(play_card, "You")
			sum_play += go.count_sum(play_card)
			print('')
		if s.lower()=='stay':
			break

	if go.ace == True:
		if sum_play + 10 <22:
			sum_play+=10

	print(f"Sum of Dealer: {sum_computer} \nSum of Player: {sum_play}")

	if go.check_bust(sum_play):
		win = False
	while win:
		if go.check_bust(sum_computer):
			win = True
		if sum_computer<sum_play and win:
			computer_card = go.get_card()
			go.display_cards(computer_card, "Dealer")
			sum_computer += go.count_sum(computer_card)
			if go.ace == True:
				if sum_computer + 10 <22:
					sum_computer+=10
					go.ace = False
		else:
			break

	if win:
		if sum_computer <22:
			if sum_play>sum_computer:
				print('You won this round!')
			else:
				win = False
		else:
			print('You won this round!')
	if not win:
		print('Dealer won this round!')

if __name__ == '__main__':
	while True:
		run()
		while True:
			again = input('Do you wanna play again?[y/n]: ')
			if again=='n':
				break
			elif again=='y':
				break
		if again != 'y':
			break