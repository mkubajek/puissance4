from tkinter import * 

# dimensions fenetre
fenWidth = 1645
fenHeight = 700

fenWidth = 800
fenHeight = 400

nCols = 7
nRows = 6
nAlign = 4

# dimensions cellule

couleurStructure = 'green'
couleurFond = 'grey'
couleurJ1 = 'blue'
couleurJ2 = 'red'
couleurWin = 'yellow'
widthWin = 3

curseur = 3
joueurActu = 1
win = False

class p4Structure():

	reductionCellule = 0.75
	canvas = None

	def __init__(self, canvas, width, height, nCols, nRows):
		self.canvas = canvas
		self.aff = 0

		self.windowWidth = width
		self.windowHeight = height
		self.nCols = nCols
		self.nRows = nRows
		self.nAlign = nAlign

		self.elemWidth = self.elemHeight = self.windowHeight / (self.nRows + 2) # 2 = 1 haut + 1 bas
		self.epaisseurPieds = self.elemWidth / 3
		self.startWidth = (self.windowWidth - (self.elemWidth * self.nCols)) / 2
		self.endWidth= self.startWidth + (self.elemWidth * self.nCols)

	def coor_calcul(self):
		self.pGx0 = self.startWidth - self.epaisseurPieds
		self.pGy0 = self.elemHeight
		self.pGx1 = self.startWidth
		self.pGy1 = self.windowHeight

		self.pDx0 = self.endWidth
		self.pDy0 = self.elemHeight
		self.pDx1 = self.endWidth + self.epaisseurPieds
		self.pDy1 = self.windowHeight

		self.gx0 = self.startWidth
		self.gy0 = self.elemHeight
		self.gx1 = self.endWidth
		self.gy1 = self.windowHeight - self.elemHeight

	def aff_creer(self):
		self.elemPiedGauche = self.canvas.create_rectangle(self.pGx0, self.pGy0, self.pGx1, self.pGy1, fill=couleurStructure)
		self.elemPiedDroite = self.canvas.create_rectangle(self.pDx0, self.pDy0, self.pDx1, self.pDy1, fill=couleurStructure)
		self.elemGrille = self.canvas.create_rectangle(self.gx0, self.gy0, self.gx1, self.gy1, fill=couleurStructure)
		self.aff = 1

	def aff_modifier(self):
		self.canvas.coords(self.elemPiedGauche, self.pGx0, self.pGy0, self.pGx1, self.pGy1)
		self.canvas.coords(self.elemPiedDroite, self.pDx0, self.pDy0, self.pDx1, self.pDy1)
		self.canvas.coords(self.elemGrille, self.gx0, self.gy0, self.gx1, self.gy1)

	def afficher(self):
		self.coor_calcul()
		if self.aff == 0:
			self.aff_creer()
		else:
			self.aff_modifier()

class p4curseur():

	reductionFlecheWidth1 = 0.20
	reductionFlecheWidth2 = 0.50
	reductionFlecheHeight = 0.7

	def __init__(self, p4Structure):
		self.canvas = p4Structure.canvas
		self.aff = 0

		self.position = 3
		self.pcolor = 'blue'
		self.joueur = 1

		self.elemWidth = p4Structure.elemWidth
		self.elemHeight = p4Structure.elemHeight
		self.startWidth = p4Structure.startWidth
		self.reductionCellule = p4Structure.reductionCellule

	def coor_calcul(self):
		self.Rx0 = self.startWidth + (self.position * self.elemWidth) + (self.elemWidth * (1 - self.reductionCellule) / 2)
		self.Ry0 = self.elemHeight * (1 - self.reductionCellule) / 2
		self.Rx1 = self.startWidth + ((self.position + 1) * self.elemWidth) - (self.elemWidth * (1 - self.reductionCellule) / 2)
		self.Ry1 = self.elemHeight - (self.elemHeight * (1 - self.reductionCellule) / 2)

		self.fAx0 = self.startWidth + (self.position * self.elemWidth) + (self.elemWidth * (1 - (self.reductionCellule * self.reductionFlecheWidth1)) / 2)
		self.fAy0 = self.elemHeight * (1 - (self.reductionCellule * self.reductionFlecheHeight)) / 2
		self.fAx1 = self.startWidth + ((self.position + 1) * self.elemWidth) - (self.elemWidth * (1 - (self.reductionCellule * self.reductionFlecheWidth1)) / 2)
		self.fAy1 = self.elemHeight / 2

		self.fBx0 = self.startWidth + (self.position * self.elemWidth) + (self.elemWidth * (1 - (self.reductionCellule * self.reductionFlecheWidth2)) / 2)
		self.fBy0 = self.elemHeight / 2
		self.fBx1 = self.startWidth + ((self.position + 1) * self.elemWidth) - (self.elemWidth * (1 - (self.reductionCellule * self.reductionFlecheWidth2)) / 2)
		self.fBy1 = self.elemHeight / 2
		self.fBx2 = self.startWidth + (self.position * self.elemWidth) + (self.elemWidth / 2)
		self.fBy2 = self.elemHeight - (self.elemHeight * (1 - (self.reductionCellule * self.reductionFlecheHeight)) / 2)

	def aff_creer(self):
		self.flecheC = canvas.create_oval(self.Rx0, self.Ry0, self.Rx1, self.Ry1, fill=self.pcolor)
		self.flecheA = canvas.create_rectangle(self.fAx0, self.fAy0, self.fAx1, self.fAy1, fill="black")
		self.flecheB = canvas.create_polygon(self.fBx0, self.fBy0, self.fBx1, self.fBy1, self.fBx2, self.fBy2, fill="black")
		self.aff = 1

	def aff_modifier(self):
		self.canvas.delete(self.flecheC)
		self.flecheC = canvas.create_oval(self.Rx0, self.Ry0, self.Rx1, self.Ry1, fill=self.pcolor)
		self.canvas.tag_lower(self.flecheC, self.flecheA)
		#self.canvas.coords(self.flecheC, self.Rx0, self.Ry0, self.Rx1, self.Ry1)
		self.canvas.coords(self.flecheA, self.fAx0, self.fAy0, self.fAx1, self.fAy1)
		self.canvas.coords(self.flecheB, self.fBx0, self.fBy0, self.fBx1, self.fBy1, self.fBx2, self.fBy2)

	def afficher(self):
		self.coor_calcul()
		if self.aff == 0:
			self.aff_creer()
		else:
			self.aff_modifier()

	def joueursuivant(self):
		if self.joueur == 1:
			self.joueur = 2
			self.pcolor = 'red'
		else:
			self.joueur = 1
			self.pcolor = 'blue'

class p4jeu():

	def __init__(self, p4Structure):
		self.canvas = p4Structure.canvas
		self.aff = 0

		self.nCols = p4Structure.nCols
		self.nRows = p4Structure.nRows
		self.nAlign = p4Structure.nAlign

		if self.nAlign > self.nCols or self.nAlign > self.nRows:
			print('Mauvaise régle, nAlign = ' + str(self.nAlign) + ', nCols = ' + str(self.nCols) + ', nRows = ' + str(self.nRows))
			exit()

		# on crée les cellules vierges
		self.cellVal = []
		self.cellObj = []
		for i in range(self.nCols):
			ligneVal = []
			ligneObj = []
			for j in range(self.nRows):
				ligneVal.append(0)
				ligneObj.append({'id':None, 'x0':0, 'y0':0, 'x1':0, 'y1':0, 'w':1, 'o':'black', 'm':True})
			self.cellVal.append(ligneVal)
			self.cellObj.append(ligneObj)

		self.cellValEx = []
		for i in range(self.nCols):
			self.cellValEx.append(self.cellVal[i][:])

		self.elemWidth = p4Structure.elemWidth
		self.elemHeight = p4Structure.elemHeight
		self.startWidth = p4Structure.startWidth
		self.reductionCellule = p4Structure.reductionCellule

	def coor_calcul(self):
		for i in range(self.nCols):
			for j in range(self.nRows):
				self.cellObj[i][j]['x0'] = self.startWidth + (i * self.elemWidth) + (self.elemWidth * (1 - self.reductionCellule) / 2)
				self.cellObj[i][j]['y0'] = self.elemHeight + (j * self.elemHeight) + (self.elemHeight * (1 - self.reductionCellule) / 2)
				self.cellObj[i][j]['x1'] = self.startWidth + ((i + 1) * self.elemWidth) - (self.elemWidth * (1 - self.reductionCellule) / 2)
				self.cellObj[i][j]['y1'] = self.elemHeight + ((j + 1) * self.elemHeight) - (self.elemHeight * (1 - self.reductionCellule) / 2)

	def afficher(self):
		if self.aff == 0:
			self.coor_calcul()
			self.aff = 1

		for i in range(self.nCols):
			for j in range(self.nRows):
				if False == self.cellObj[i][j]['m']:
					continue

				self.cellObj[i][j]['m'] = False

				if None != self.cellObj[i][j]['id']:
					self.canvas.delete(self.cellObj[i][j]['id'])

				if self.cellVal[i][j] == 1:
					color = couleurJ1
				elif self.cellVal[i][j] == 2:
					color = couleurJ2
				else:
					color = couleurFond

				self.cellObj[i][j]['id'] = canvas.create_oval(self.cellObj[i][j]['x0'], self.cellObj[i][j]['y0'], self.cellObj[i][j]['x1'], self.cellObj[i][j]['y1'], fill=color, width=self.cellObj[i][j]['w'], outline=self.cellObj[i][j]['o'])


	def checkWin(self):
		messageWin = []
		# verticales
		for i in range(self.nCols):
			for j in range(self.nRows - self.nAlign + 1):
				if 0 != self.cellVal[i][j] == self.cellVal[i][j + 1] == self.cellVal[i][j + 2] == self.cellVal[i][j + 3]:
					self.cellObj[i][j]['w'] = self.cellObj[i][j + 1]['w'] = self.cellObj[i][j + 2]['w'] = self.cellObj[i][j + 3]['w'] = widthWin
					self.cellObj[i][j]['o'] = self.cellObj[i][j + 1]['o'] = self.cellObj[i][j + 2]['o'] = self.cellObj[i][j + 3]['o'] = couleurWin
					self.cellObj[i][j]['m'] = self.cellObj[i][j + 1]['m'] = self.cellObj[i][j + 2]['m'] = self.cellObj[i][j + 3]['m'] = True
					messageWin.append('Victoire joueur ' + str(self.cellVal[i][j]) + ' en | coordonnées ' + str(i) + ' : ' + str(j) + ' > ' + str(j + 3))

		for j in range(self.nRows):
			for i in range(self.nCols - self.nAlign + 1):
				if 0 != self.cellVal[i][j] == self.cellVal[i + 1][j] == self.cellVal[i + 2][j] == self.cellVal[i + 3][j]:
					self.cellObj[i][j]['w'] = self.cellObj[i + 1][j]['w'] = self.cellObj[i + 2][j]['w'] = self.cellObj[i + 3][j]['w'] = widthWin
					self.cellObj[i][j]['o'] = self.cellObj[i + 1][j]['o'] = self.cellObj[i + 2][j]['o'] = self.cellObj[i + 3][j]['o'] = couleurWin
					self.cellObj[i][j]['m'] = self.cellObj[i + 1][j]['m'] = self.cellObj[i + 2][j]['m'] = self.cellObj[i + 3][j]['m'] = True
					messageWin.append('Victoire joueur ' + str(self.cellVal[i][j]) + ' en - coordonnées ' + str(i) + ' > ' + str(i + 3) + ' : ' + str(j))

		for i in range(self.nCols - self.nAlign + 1):
			for j in range(self.nRows - self.nAlign + 1):
				if 0 != self.cellVal[i][j] == self.cellVal[i + 1][j + 1] == self.cellVal[i + 2][j + 2] == self.cellVal[i + 3][j + 3]:
					self.cellObj[i][j]['w'] = self.cellObj[i + 1][j + 1]['w'] = self.cellObj[i + 2][j + 2]['w'] = self.cellObj[i + 3][j + 3]['w'] = widthWin
					self.cellObj[i][j]['o'] = self.cellObj[i + 1][j + 1]['o'] = self.cellObj[i + 2][j + 2]['o'] = self.cellObj[i + 3][j + 3]['o'] = couleurWin
					self.cellObj[i][j]['m'] = self.cellObj[i + 1][j + 1]['m'] = self.cellObj[i + 2][j + 2]['m'] = self.cellObj[i + 3][j + 3]['m'] = True
					messageWin.append('Victoire joueur ' + str(self.cellVal[i][j]) + ' en \\ coordonnées ' + str(i) + ' > ' + str(i + 3) + ' : ' + str(j) + ' > ' + str(j + 3))

		for i in range(self.nCols - self.nAlign + 1):
			for j in range(self.nRows - self.nAlign + 1):
				if 0 != self.cellVal[i + 3][j] == self.cellVal[i + 2][j + 1] == self.cellVal[i + 1][j + 2] == self.cellVal[i][j + 3]:
					self.cellObj[i + 3][j]['w'] = self.cellObj[i + 2][j + 1]['w'] = self.cellObj[i + 1][j + 2]['w'] = self.cellObj[i][j + 3]['w'] = widthWin
					self.cellObj[i + 3][j]['o'] = self.cellObj[i + 2][j + 1]['o'] = self.cellObj[i + 1][j + 2]['o'] = self.cellObj[i][j + 3]['o'] = couleurWin
					self.cellObj[i + 3][j]['m'] = self.cellObj[i + 2][j + 1]['m'] = self.cellObj[i + 1][j + 2]['m'] = self.cellObj[i][j + 3]['m'] = True
					messageWin.append('Victoire joueur ' + str(self.cellVal[i + 3][j]) + ' en / coordonnées ' + str(i + 3) + ' > ' + str(i) + ' : ' + str(j) + ' > ' + str(j + 3))

		if 0 != len(messageWin):
			win = True
			for m in messageWin:
				print(m)
		else:
			win = False

		return win

# Début execution

fenetre = Tk()
canvas = Canvas(fenetre, width=fenWidth, height=fenHeight, background=couleurFond)

structure = p4Structure(canvas, fenWidth, fenHeight, nCols, nRows)
structure.afficher()

curseur = p4curseur(structure)
curseur.afficher()

jeu = p4jeu(structure)
jeu.afficher()

def clavier(event):
	global curseur
	global win

	touche = event.keysym

	if touche == 'Right' and curseur.position < (structure.nCols - 1):
		curseur.position += 1
		curseur.afficher()

	elif touche == 'Left' and curseur.position > 0:
		curseur.position -= 1
		curseur.afficher()

	elif touche == 'Return' or touche == 'space':
		if win == False:
			for j in range(structure.nRows - 1, -1, -1):
				if jeu.cellVal[curseur.position][j] == 0:
					jeu.cellVal[curseur.position][j] = curseur.joueur
					jeu.cellObj[curseur.position][j]['m'] = True
					print('Joueur ' + str(curseur.joueur) + ' joue en ' + str(curseur.position + 1))
					win = jeu.checkWin()
					#canvas.unbind('<Key>')
					jeu.afficher()
					curseur.joueursuivant()
					curseur.afficher()
					break

	elif touche == 'Escape':
		exit()

canvas.focus_set()
canvas.bind('<Key>', clavier)
canvas.pack()

fenetre.mainloop()
