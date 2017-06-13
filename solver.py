import math

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

grid = '''
MRKFFRKTIAHYPDQWYTRKGUR
XGEFRUDLGVMACYRLYEZMRXE
FYNIKAYKLZMCSNLYIKRGACP
TLBVTSCNYWMRPAEKAZIWTUR
HBTDQENTPMMBCCLROBISITE
YVHRQGRYUXOIEAGCENLXFSS
NFQJWCEAMRGSBNLXDHDEYIC
LOFPELCJTRAYUJREFEOYNRR
NWMKINYBUEJBWVTECGTCMYI
GCLTEELSCCAOLAINIXIFNLB
OHIIJBOBMSWHNEENFDNCVOE
BCOJVRXUQMXODULKFDTCYCN
NLUSTFVNUDIGLRLUNIEYFJN
DMLCUGMXASXFNAMBUTRLIXS
WTESUPERSENSUALITYPLCYH
XLMSIGEADIPIREETVURALNM
ECJJCZPREEUOZDXONJOVUKE
RJUDPEHRPZCEIVBPTTXEDON
ANIRZSGFGOBABLAPRAIOSYB
EXILENHIIJSDFGLIOSMCOYJ
UDETNEMIDEPIEACABOAHXIA
HYLKFTDBLZIDTHOSCPLDLDH
NDAHYNWTZAADLIDIOSMOSED
IFLUKIERUTJOOSOSESUEREC
YWRIGRMBJARNUVHNHMVOYCG
GILTHEADEIRBIOOONIGLPNR
VWBKTPBNDRSIDRAXOTUWPUM
HDXGXUOEZPTGABBRIAJQOVH
LBTJBSZFEQEAILDYTLETUKM
YLTHGINCUSBTJUCNAOLJWGA
OEETAMILCOTPYRCJGPHACRT
HANTTAIGECOFSRITIHYVOVU
WLWCLFLIRTATIOUSMIONPOP
FIHILGTDSLOVCHKZULOWRZO
XFZEFOCLOFPMCQQNFEMCIML
RELIOHSGLEVLJASDLTUXNEE
WGLTUNNEHGHGLAQEPLCCTJV
'''

words = ['BEZEL', 'SUPERPOSITION', 'DRYABLE', 'PEDIMENTED', 'CALLIOPEAN', 'FLIRTATIOUS', 'INTERPROXIMAL', 'SHOA', 'GRATIFY', 'EXILE', 'UNPAGED', 'DIOSMOSED', 'SUBSPECIALIZE', 'ELECTROSURGICALLY', 'FUMIGATION', 'NONCOHERENCY', 'PYELITIC', 'RINA', 'FRACTURABLE', 'REITERATE', 'NYX', 'COSSACK', 'SUPERINTENSE', 'UNRESCISSABLE', 'HODGES', 'REPRESCRIBE', 'NIGHTLY', 'SUPERSENSUALITY', 'BRINJAL', 'MOTE', 'CEREUSES', 'DULCIFY', 'CLAIRAUT', 'PASSIONATE', 'CRYPTOCLIMATE', 'BALKIER', 'TUBMAN', 'FLUKIER', 'AFACED', 'ENCLOSE', 'BERTA', 'TUPOLEV', 'PRINT', 'TRICHLORIDE', 'LYRIST', 'ITALOPHIL', 'COEVALLY', 'ELEONORA', 'REINFLUENCED', 'GILTHEAD']

def roundUp(x, base):
	return ((x / base)+1) * base - 1

grid = grid.strip()

height = len(grid.split('\n'))
width = len(grid.split('\n')[0].strip())

letters = []
for y, line in enumerate(grid.split('\n')):
	for x, char in enumerate(line):
		letters.append([char, y * width + x, x, y, None])
total = len(letters)

## Get lines
down = []
for i in range(width):
	line = []
	for j in range(i, total, width):
		line.append(letters[j])
	down.append(line)

downRight = []
for i in range(width):
	line = []
	edge = roundUp(i, width) + width * (width - i - 1)
	for j in range(i, min(total, edge) + 1, width + 1):
		line.append(letters[j])
	downRight.append(line)
for i in range(width, total, width):
	line = []
	for j in range(i, total, width + 1):
		line.append(letters[j])
	downRight.append(line)

right = []
for i in range(0, total, width):
	line = []
	for j in range(i, roundUp(i, width) + 1):
		line.append(letters[j])
	right.append(line)

upRight = []
for i in range(0, total, width):
	line = []
	for j in range(i, -1, 1 - width):
		line.append(letters[j])
	upRight.append(line)
for i in range((height - 1) * width + 1, total, 1):
	line = []
	edge = roundUp(i, width) - width * (width - (i % width) - 1)
	for j in range(i, max(0, edge) - 1, 1 - width):
		line.append(letters[j])
	upRight.append(line)

up = [list(reversed(line)) for line in down]
upLeft = [list(reversed(line)) for line in downRight]
left = [list(reversed(line)) for line in right]
downLeft = [list(reversed(line)) for line in upRight]

allLines = [down, downRight, right, upRight, up, upLeft, left, downLeft]

directions = {
	'down': down,
	'downRight': downRight,
	'right': right,
	'upRight': upRight,
	'up': up,
	'upLeft': upLeft,
	'left': left,
	'downLeft': downLeft
}

colors = {
	'down': bcolors.OKBLUE,
	'up': bcolors.OKBLUE,
	'right': bcolors.OKGREEN,
	'left': bcolors.OKGREEN,
	'downRight': bcolors.WARNING,
	'upLeft': bcolors.WARNING,
	'downLeft': bcolors.FAIL,
	'upRight': bcolors.FAIL
}

# for lines in allLines:
# 	for line in lines:
# 		print ''.join([l[0] for l in line])


for word in words:
	for direction in directions:
		for line in directions[direction]:
			string = ''.join([l[0] for l in line])
			# if word == 'COLBLITZ':
			# 	print string
			if word in string:
				# print word, string
				s = string.index(word)
				for i in range(s, s + len(word)):
					line[i][4] = colors[direction]

for y in range(height):
	line = ''
	for x in range(width):
		i = y * width + x
		l = letters[i]
		if l[4]:
			line += l[4] + l[0] + bcolors.ENDC + ' '
		else:
			line += l[0] + ' '
	print line






# #Make a list of tuples containing each letter and its row and column
# left = [(letter, divmod(index, length+1))
#             for  index, letter in enumerate (puzzle)]
# #Reorder the list to represent each reading direction
# right = [i for i in reversed(left)]

# down = []
# for i in range(length):
#     for j in range(i, len(left), length+1):
#         down.append(left[j])
#     down.append('\n')

# up = [i for i in reversed(down)]

# right_down =[]
# for i in range(length):
#     for j in range(i, len(left), length):
#         right_down.append(left[j])
#     right_down.append('\n')

# left_up = [i for i in reversed(right_down)]

# left_down = []
# for i in range(length):
#     for j in range(i, len(left), length + 2):
#         left_down.append(left[j])
#     left_down.append('\n')

# right_up = [i for i in reversed(left_down)]

# lines =  {'left':left, 'right':right,  'up':up, 'down':down,
#                 'left down':left_down, 'left up':left_up,
#                 'right down':right_down, 'right up':right_up}

# for word in clues:
#     for k,v in lines.items():
#         string = ''.join([i[0] for i in v])
#         if word in string:
#             loc = v[string.index(word)][1]
#             print word, 'row', loc[0]+1, 'column', loc[1]+1, k


# # Just formats the puzzle into a more computer-readable text
# wordgrid = puzzle.replace(' ','')

# # Computers start counting at zero, so...
# length = wordgrid.index('\n')+1


# characters = [(letter, divmod(index, length))
#             for  index, letter in enumerate (wordgrid)]

# wordlines = {}
# # These next lines just  directions so you can tell which direction the word is going
# directions = {'going downwards':0, 'going downwards and left diagonally':-1, 'going downwards and right diagonally':1}

# for word_direction, directions in directions.items():
#     wordlines[word_direction] = []
#     for x in range(length):
#         for i in range(x, len(characters), length + directions):
#             wordlines[word_direction].append(characters[i])
#         wordlines[word_direction].append('\n')

# # Nice neat way of doing reversed directions.
# wordlines['going right'] = characters
# wordlines['going left'] = [i for i in reversed(characters)]
# wordlines['going upwards'] = [i for i in reversed(wordlines['going downwards'])]
# wordlines['going upwards and left diagonally'] = [i for i in reversed(wordlines['going downwards and right diagonally'])]
# wordlines['going upwards and right diagonally'] = [i for i in reversed(wordlines['going downwards and left diagonally'])]


# def printitout(direction, tuple, lines):
#     print "Keep in mind, rows are horizontal and columns are vertical.\n"
#     for direction, tuple in lines.items():
#         string = ''.join([i[0] for i in tuple])
#         for word in solutions:
#             if word in string:
#                 coordinates = tuple[string.index(word)][1]
#                 print word, 'is at row', coordinates[0]+1, 'and column', coordinates[1]+1, direction + "."

# printitout(word_direction, tuple, wordlines)