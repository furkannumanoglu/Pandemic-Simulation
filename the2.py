
# WRITE YOUR CODE HERE AND SEND ONLY THIS FILE TO US.
#
# DO NOT DEFINE get_data() here. Check before submitting
from evaluator import *    # get_data() will come from this import
import math
import random
M = get_data()[0]
N = get_data()[1]
D = get_data()[2]
K = get_data()[3]
LAMBDA = get_data()[4]
MU = get_data()[5]
universalState = get_data()[6:][0]
green=(1/2)*MU
yellow=(1/8)*MU
blue= (1/2)*(1-MU-MU**2)
purple=(2/5)*MU**2
gray=(1/5)*MU**2
l = len(universalState)
#buraya kadar gerekli sabitleri tanımladım

def new_move():
	global universalState
	# o = old   n = new
	omovelst = []
	ostatelst = []
	nmovelst = []
	nstatelst = []
	masklst = []
	#her çağrıldığında bu listeleri boş listeye çeviriyorum
	for i in range(l):
		masklst.append(universalState[i][2])
	for i in range(l):
		omovelst.append(universalState[i][1])  #last move'ları koydum
		ostatelst.append(universalState[i][0]) #(x,y) formatında konumları ekledim
	for i in range(l):
		#bu döngüde yardımcı fonksiyonlarla yeni lastmove ve konumlarını ekliyorum
		x = universalState[i][0][0]
		y = universalState[i][0][1]
		d = next_move(universalState[i][1])
		nmovelst.append(d)
		func2(universalState[i][1], x, y)
		nstatelst.append(func2(nmovelst[i], x, y))  #yeni konumlar eklendi

	for i in range(l):
		# bu for döngüsünde problemsiz çıkanlar devam ediyor. eğer üstüste gelme, evrenin dışına çıkma gibi bir durum varsa eski konumlarında kalıyorlar
		x = nstatelst[i][0]
		y = nstatelst[i][1]
		if x > -1 and y > -1:
			if x < N and y < M:
				for j in range(l):
					if i>j and nstatelst[i] == nstatelst[j]:
						nstatelst[i] = ostatelst[i]
						nmovelst[i] = omovelst[i]

					if i<j and nstatelst[i] == ostatelst[j]:
						nstatelst[i] = ostatelst[i]
						nmovelst[i] = omovelst[i]
			else:
				nstatelst[i] = ostatelst[i]
				nmovelst[i] = omovelst[i]
		else:
			nstatelst[i] = ostatelst[i]
			nmovelst[i] = omovelst[i]

	new_infections = []
	for i in range(l):
		new_infections.append(universalState[i][3])

	for i in range(l):
		#Bu uzun for döngüsünde tüm olabilecek tüm durumları dahil etmeye çalıştım.
		if universalState[i][3] == "infected":
			x1 = nstatelst[i][0]
			y1 = nstatelst[i][1]
			for j in range(i + 1, l):
				x2 = nstatelst[j][0]
				y2 = nstatelst[j][1]
				distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

				if distance <= D:
					if masklst[i] == "masked" and masklst[j] == "masked":
						if new_infections[j] == "infected" and universalState[j][3] == "notinfected":
							random.choices(["infected","notinfected"],weights=[0,1])

						if new_infections[j] == "notinfected":
							ratio = min(1, (K / distance ** 2) / LAMBDA ** 2)
							status = random.choices(["infected", "notinfected"], weights=[ratio, 1 - ratio])[0]
							if status == "infected":
								new_infections[j] = "infected"
							else:
								new_infections[j] = "notinfected"

					if masklst[i] == "notmasked" and masklst[j] == "masked":
						if new_infections[j] == "infected" and universalState[j][3] == "notinfected":
							random.choices(["infected","notinfected"],weights=[0,1])

						if new_infections[j] == "notinfected":
							ratio = min(1, (K / distance ** 2) / LAMBDA)
							status = random.choices(["infected", "notinfected"], weights=[ratio, 1 - ratio])[0]
							if status == "infected":
								new_infections[j] = "infected"
							else:
								new_infections[j] = "notinfected"
					if masklst[i] == "masked" and masklst[j] == "notmasked":
						if new_infections[j] == "infected" and universalState[j][3] == "notinfected":
							random.choices(["infected","notinfected"],weights=[0,1])

						if new_infections[j] == "notinfected":
							ratio = min(1, (K / distance ** 2) / LAMBDA)
							status = random.choices(["infected", "notinfected"], weights=[ratio, 1 - ratio])[0]
							if status == "infected":
								new_infections[j] = "infected"
							else:
								new_infections[j] = "notinfected"
					if masklst[i] == "notmasked" and masklst[j] == "notmasked":
						if new_infections[j] == "infected" and universalState[j][3] == "notinfected":
							random.choices(["infected","notinfected"],weights=[0,1])

						if new_infections[j] == "notinfected":
							ratio = min(1, (K / distance ** 2))
							status = random.choices(["infected", "notinfected"], weights=[ratio, 1 - ratio])[0]
							if status == "infected":
								new_infections[j] = "infected"
							else:
								new_infections[j] = "notinfected"

		if universalState[i][3] == "notinfected":
			x1 = nstatelst[i][0]
			y1 = nstatelst[i][1]
			for j in range(i + 1, l):
				x2 = nstatelst[j][0]
				y2 = nstatelst[j][1]
				distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

				if distance <= D:
					if masklst[i] == "masked" and masklst[j] == "masked":
						if universalState[j][3] == "infected":
							ratio = min(1, (K / distance ** 2)) / LAMBDA ** 2
							status = random.choices(["infected","notinfected"], weights=[ratio, 1-ratio])[0]
							if status == "infected":
								new_infections[i] = "infected"

					if masklst[i] == "notmasked" and masklst[j] == "masked":
						if universalState[j][3] == "infected":
							ratio = min(1, (K / distance ** 2)) / LAMBDA
							status = random.choices(["infected", "notinfected"], weights=[ratio, 1 - ratio])[0]
							if status == "infected":
								new_infections[i] = "infected"

					if masklst[i] == "masked" and masklst[j] == "notmasked":
						if universalState[j][3] == "infected":
							ratio = min(1, (K / distance ** 2)) / LAMBDA
							status = random.choices(["infected", "notinfected"], weights=[ratio, 1 - ratio])[0]
							if status == "infected":
								new_infections[i] = "infected"

					if masklst[i] == "notmasked" and masklst[j] == "notmasked":
						if universalState[j][3] == "infected":
							ratio = min(1, (K / distance ** 2))
							status = random.choices(["infected", "notinfected"], weights=[ratio, 1 - ratio])[0]
							if status == "infected":
								new_infections[i] = "infected"
	universalState = []
	#universalState'i kullanmıştım fonksiyon içerisinde. Artık işim bitti, yeni verileri ekliyorum.
	for i in range(l):
		universalState.append([nstatelst[i], nmovelst[i], masklst[i], new_infections[i]])

	return universalState


def next_move(lastmove):
	#yön sırasına uyarak numaralaştırdım, olasılıklar dahilinde seçiyor.
	if lastmove == 0:
		return random.choices([0,1,2,3,4,5,6,7], weights=[green, yellow, blue, purple, gray, purple, blue, yellow])[0]
	if lastmove == 1:
		return random.choices([1,2,3,4,5,6,7,0], weights=[green, yellow, blue, purple, gray, purple, blue, yellow])[0]
	if lastmove == 2:
		return random.choices([2,3,4,5,6,7,0,1], weights=[green, yellow, blue, purple, gray, purple, blue, yellow])[0]
	if lastmove == 3:
		return random.choices([3,4,5,6,7,0,1,2], weights=[green, yellow, blue, purple, gray, purple, blue, yellow])[0]
	if lastmove == 4:
		return random.choices([4,5,6,7,0,1,2,3], weights=[green, yellow, blue, purple, gray, purple, blue, yellow])[0]
	if lastmove == 5:
		return random.choices([5,6,7,0,1,2,3,4], weights=[green, yellow, blue, purple, gray, purple, blue, yellow])[0]
	if lastmove == 6:
		return random.choices([6,7,0,1,2,3,4,5], weights=[green, yellow, blue, purple, gray, purple, blue, yellow])[0]
	if lastmove == 7:
		return random.choices([7,0,1,2,3,4,5,6], weights=[green, yellow, blue, purple, gray, purple, blue, yellow])[0]

def func2(move,x,y):
	#(x,y) formatında yeni konumu veriyor.
	if move == 0:
		y = y+1
	if move == 1:
		y = y+1
		x = x-1
	if move == 2:
		x = x-1
	if move == 3:
		y = y-1
		x = x-1
	if move == 4:
		y = y-1
	if move == 5:
		y = y-1
		x = x+1
	if move == 6:
		x = x+1
	if move == 7:
		y = y+1
		x = x+1
	return (x, y)

print(new_move())
print(new_move())
print(new_move())
print(new_move())
print(new_move())
print(new_move())
print(new_move())
print(new_move())
print(new_move())
print(new_move())
print([[(37, 7), 4, 'notmasked', 'infected'], [(41, 9), 0, 'masked', 'infected'], [(45, 9), 7, 'notmasked', 'infected'], [(46, 8), 2, 'masked', 'infected'], [(49, 8), 2, 'notmasked', 'notinfected'], [(53, 7), 4, 'masked', 'infected'], [(55, 9), 0, 'notmasked', 'notinfected'], [(38, 11), 6, 'notmasked', 'infected'], [(55, 10), 4, 'masked', 'infected'], [(38, 13), 6, 'notmasked', 'infected'], [(56, 13), 6, 'notmasked', 'notinfected'], [(37, 17), 0, 'notmasked', 'infected'], [(55, 15), 4, 'masked', 'infected'], [(38, 18), 6, 'notmasked', 'infected'], [(53, 18), 2, 'notmasked', 'notinfected'], [(55, 22), 7, 'masked', 'infected'], [(37, 21), 4, 'notmasked', 'infected'], [(38, 26), 7, 'notmasked', 'infected'], [(54, 26), 0, 'notmasked', 'notinfected'], [(53, 27), 3, 'masked', 'infected'], [(36, 28), 3, 'notmasked', 'infected'], [(38, 32), 6, 'notmasked', 'infected'], [(55, 31), 5, 'notmasked', 'notinfected'], [(37, 36), 0, 'notmasked', 'infected'], [(54, 36), 0, 'masked', 'infected'], [(36, 36), 3, 'notmasked', 'infected'], [(52, 37), 2, 'notmasked', 'infected'], [(38, 40), 6, 'notmasked', 'infected'], [(54, 39), 5, 'masked', 'infected'], [(38, 43), 6, 'notmasked', 'infected'], [(52, 43), 2, 'notmasked', 'notinfected']]
==[[(37, 7), 4, 'notmasked', 'infected'], [(41, 9), 0, 'masked', 'infected'], [(45, 9), 7, 'notmasked', 'infected'], [(46, 8), 2, 'masked', 'infected'], [(49, 8), 2, 'notmasked', 'notinfected'], [(53, 7), 4, 'masked', 'infected'], [(55, 9), 0, 'notmasked', 'notinfected'], [(38, 11), 6, 'notmasked', 'infected'], [(55, 10), 4, 'masked', 'infected'], [(38, 13), 6, 'notmasked', 'infected'], [(56, 13), 6, 'notmasked', 'notinfected'], [(37, 17), 0, 'notmasked', 'infected'], [(55, 15), 4, 'masked', 'infected'], [(38, 18), 6, 'notmasked', 'infected'], [(53, 18), 2, 'notmasked', 'notinfected'], [(55, 22), 7, 'masked', 'infected'], [(37, 21), 4, 'notmasked', 'infected'], [(38, 26), 7, 'notmasked', 'infected'], [(54, 26), 0, 'notmasked', 'notinfected'], [(53, 27), 3, 'masked', 'infected'], [(36, 28), 3, 'notmasked', 'infected'], [(38, 32), 6, 'notmasked', 'infected'], [(55, 31), 5, 'notmasked', 'notinfected'], [(37, 36), 0, 'notmasked', 'infected'], [(54, 36), 0, 'masked', 'infected'], [(36, 36), 3, 'notmasked', 'infected'], [(52, 37), 2, 'notmasked', 'notinfected'], [(38, 40), 6, 'notmasked', 'infected'], [(54, 39), 5, 'masked', 'infected'], [(38, 43), 6, 'notmasked', 'infected'], [(52, 43), 2, 'notmasked', 'notinfected']]
	  )








