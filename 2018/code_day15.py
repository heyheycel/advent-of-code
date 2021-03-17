with open("input_day15.txt","r") as f:
    data = f.read().strip()

#for row in data.split("\n"):
    #print(row)


def build_board(inp):
	board=[]
	for row_number,row in enumerate(inp.split("\n")):
		board.append([char for char in row])
		#print(board)
		for col_number, col in enumerate(row):
			if col in ["G","E"]:
				#save (player, hit_points, move)
				element=(col,200,False)
				board[row_number][col_number]=element
	return board


def print_board(board):
	for row in board:
		extra = []
		print_row = []
		for char in row:
			if isinstance(char,tuple):
				print_row.append(char[0])
				extra.append(str(char[1]))
			else:
				print_row.append(char)
		print("".join(print_row),"   ", " ".join(extra))

def adjacent_enemy(entrada, row, col, enemy):
	for x in [entrada[row+1][col], entrada[row-1][col], entrada[row][col+1], entrada[row][col-1]]:
		if x[0]==enemy:
			return True
	return False


def get_best_move(posibles_moves):
	#(first_move, number_of_moves, finish_coordinates)
	#print('here '+str(posibles_moves))
	if not posibles_moves:
		return None

	#find the shortest one
	min_moves=min([x[1] for x in posibles_moves])
	posibles_moves=[x for x in posibles_moves if x[1]==min_moves]
	#print('here '+str(posibles_moves))
	#print(posibles_moves[0][2])
	#if min moves is the same for more than one, choose the first tile in reading order
	#to the target
	if len(posibles_moves)>1:
		posibles_moves.sort(key = lambda x:x[2])
		#print('here '+str(posibles_moves))
		posibles_moves = [x for x in posibles_moves if x[2]==posibles_moves[0][2]]
		#print('here '+str(posibles_moves))
	#print('here '+str(posibles_moves))
	#if we still have the same, now for tiles
	#to the first move
	if len(posibles_moves)>1:
		posibles_moves.sort(key=lambda x:x[0])
		posibles_moves=[x for x in posibles_moves if x[0]==posibles_moves[0][0]]
	#print('here '+str(posibles_moves))
	#print(posibles_moves[0][0])
	return posibles_moves[0][0]


def search_enemies(entrada,row,col,hero,enemy):
	if adjacent_enemy(entrada,row,col,enemy):
		return None
	#movimientos adyacentes
	first_moves = [(row+1,col),(row-1,col),(row,col-1),(row,col+1)]
	#movimientos adyacentes validos
	first_moves = [x for x in first_moves if entrada[x[0]][x[1]]=="."]
	#print(entrada[row][col])
	#print("first_moves: " +str(first_moves))
	min_moves=1000000
	next_moves=[]
	#visited={}
	#saves move, number of moves, coordinates of the enemy we found
	for move in first_moves:
		y,x=move
		#if the first child in moves is already near to the enemy, dont move it and add it to the 
		#stack of next move
		if adjacent_enemy(entrada,y,x,enemy):
			next_moves.append((move,1,move))
			#print("adjacent_enemy ")
			#print("next_moves: "+str(next_moves))
			continue
		#we already moved once, so i=1
		i=1
		#visited.update({(row,col):0,(y,x):i})
		visited={(row,col):0,(y,x):1}
		posibles=[(y+1,x),(y-1,x),(y,x-1),(y,x+1)]
		#posibles = [x for x in posibles if entrada[x[0]][x[1]]=="." and (x[0],x[1]) not in visited or( x in visited and visited[x]<i)]
		posibles = [x for x in posibles if entrada[x[0]][x[1]]=="." and (x[0],x[1]) not in visited]
		#print("posibles: "+str(posibles))
		#print("visited: "+str(visited))
		#now that we get the posibles moves of the next child, then loop to know if this is a valid candidate
		
		search=True
		while search:
			i+=1
			#stack for the child of the children that we have already identified
			stack_grandsons=[]

			for child in posibles:
				#if child in visited and visited[child]<i:
				if child in visited:
					continue

				visited[child]=i
				r,c=child
				if adjacent_enemy(entrada,r,c,enemy):
					if i<min_moves:
						next_moves.append((move,i,(r,c)))
					#finish this loop to go to others children that may have the same distance
					search=False
					continue


				#we have not found the one so go to the next children
				new_tiles = [(r+1,c),(r-1,c),(r,c-1),(r,c+1)]
				#stack_grandsons += [x for x in new_tiles if entrada[x[0]][x[1]]=="." and (x[0],x[1]) not in visited or (x in visited and visited[x]<i)]
				stack_grandsons += [x for x in new_tiles if entrada[x[0]][x[1]]=="." and (x[0],x[1]) not in visited]

			posibles = list(set(stack_grandsons))
			#no more sons, end it
			if not posibles:
				search = False

	#print("next_moves: "+str(next_moves))
	#print("best_move "+str(get_best_move(next_moves)))
	return get_best_move(next_moves)
	

def attack(entrada,row,col,enemy,damage=3):
	"""
    Attacks the enemy with less points, if there is one
    I there are many, use the reading order
    return a board modified with the data if an enemy died
    """

	if not adjacent_enemy(entrada,row,col,enemy):
		return entrada,False

	#search all the adjacent enemies
	enemies={}

	for coords in [(row-1,col), (row+1,col), (row,col-1), (row,col+1)]:
		if entrada[coords[0]][coords[1]][0] == enemy:
			#enemy is a tuple, (char_type, hp, already_moved_bool)
			enemies[coords] = entrada[coords[0]][coords[1]][1]

	#print('enemies: '+str(enemies))
	#get the enemies with the min value of hp
	min_value=min(enemies.values())
	enemies = [x for x in enemies if enemies[x]==min_value]
	#print('enemies list: '+str(enemies))

	#sort them to get them in reading order
	enemies.sort()
	#print('enemies after sort: '+str(enemies))
	coords=enemies[0]
	enemy = entrada[coords[0]][coords[1]]
	enemy_pts = enemy[1] - damage
	enemy_tup = (enemy[0], enemy_pts, enemy[2])
	print(enemy_tup)
	#if we killed the moroon
	if enemy_pts <= 0:
		entrada[coords[0]][coords[1]] = "."
		return entrada, True
	else:
		entrada[coords[0]][coords[1]] = enemy_tup
		return entrada, False



def move_the_piece(entrada,from_row,from_col,to_row,to_col,char,points):
	entrada[from_row][from_col]="."
	entrada[to_row][to_col]=(char,points,True)
	return entrada


def count_pieces(entrada):
	pieces={'G':0,'E':0}
	for row in entrada:
		for col in row:
			if col[0]in pieces.keys():
				pieces[col[0]]+=1
	return pieces



def score_game(entrada,rounds):
	pts=0
	for rowI,row in enumerate(entrada):
		for colI,col in enumerate(row):
			if col[0] in ['G','E']:
				pts+=col[1]
	return rounds*pts

def reset_everyone_moved(entrada):
	'''The third value of the tuple is whether or not we have moved, after a round we reset'''
	for rowI,row in enumerate(entrada):
		for colI,col in enumerate(row):
			if col[0] in ['G','E']:
				col_tuple=(col[0],col[1],False)
				entrada[rowI][colI]=col_tuple

	return entrada


def main1(entrada):
	#import pdb; pdb.set_trace()
	grid=build_board(entrada)
	print_game=False
	rounds=0
	while True:
		'''Count the number of participants in each category
		the count is going to tell us if the round finished in the begining or in the end
		Combat only ends when a unit finds no targets during its turn.'''
		counts=count_pieces(grid)
		print_board(grid)
		for rowI, row in enumerate(grid):
			for colI, col in enumerate(row):
				char=grid[rowI][colI]
				if isinstance(char,tuple):
					#if we have already moved this round, the third value is set to True
					if char[2]:
						continue

					#current coordinates
					y,x=rowI,colI
					hero=char[0]
					enemy='G' if hero=='E' else 'E'
					counts[hero]-=1
					move_to=search_enemies(grid,rowI,colI,hero,enemy)
					print('move to '+str(move_to))
					#if we get adjacent enemies where we can move
					if move_to:
						#update current coordinates to the move
						y,x=move_to
						grid=move_the_piece(grid,rowI,colI,y,x,char[0],char[1])
						#print_board(grid)
		

					
					grid,death=attack(grid,y,x,enemy)
					print('DEATH '+str(death))
					if death:
						#we are going to check if we have more target or we are done
						current_counts=count_pieces(grid)
						end_of_game=any(x==0 for x in current_counts.values())
						if end_of_game:
							#check if was at the mid round
							if counts[hero]>0:
								score=score_game(grid,rounds)
								print_game=True
							else:
								rounds+=1
								score=score_game(grid,rounds)
								print_game=True
							if print_game:
								print('Game Over')
								print("Rounds "+str(rounds))
								print_board(grid)
							
							return score
		#reset rounds
		
		grid=reset_everyone_moved(grid)	
		rounds+=1

		if print_game:
			print_board(grid)



def loop_2(entrada,ataques):
	grid=build_board(entrada)
	print_game=False
	rounds=0
	while True:
		'''Count the number of participants in each category
		the count is going to tell us if the round finished in the begining or in the end
		Combat only ends when a unit finds no targets during its turn.'''
		counts=count_pieces(grid)
		print_board(grid)
		for rowI, row in enumerate(grid):
			for colI, col in enumerate(row):
				char=grid[rowI][colI]
				if isinstance(char,tuple):
					#if we have already moved this round, the third value is set to True
					if char[2]:
						continue

					#current coordinates
					y,x=rowI,colI
					hero=char[0]
					enemy='G' if hero=='E' else 'E'
					counts[hero]-=1
					move_to=search_enemies(grid,rowI,colI,hero,enemy)
					if move_to:
						#update current coordinates to the move
						y,x=move_to
						grid=move_the_piece(grid,rowI,colI,y,x,char[0],char[1])
						#print_board(grid)

					damage=ataques[hero]
					grid,death=attack(grid,y,x,enemy,damage)
					if death and enemy=='E':
						#asi no se puede
						return False
					elif death:
						#check if the goblins are gone
						current_counts=count_pieces(grid)
						end_of_game=any(x==0 for x in current_counts.values())
						if end_of_game:
							#check if was at the mid round
							if counts[hero]>0:
								score=score_game(grid,rounds)
								print_game=True
							else:
								rounds+=1
								score=score_game(grid,rounds)
								print_game=True
							if print_game:
								print('Game Over')
								print_board(grid)
							
							return score
		#reset rounds
		
		grid=reset_everyone_moved(grid)	
		rounds+=1

		if print_game:
			print("Rounds "+str(rounds))
			print("Force: "+str(ataques['E']))
			print_board(grid)



def main2(entrada):
	score=False
	ataques={'G':3,'E':3}
	while not score:
		ataques['E']+=1
		score=loop_2(entrada,ataques)
		print("score "+str(score))
	return score



		


#matrix=build_board(data)
#print_board(matrix)
#search_enemies(matrix,1,1,'E','G')
#print(search_enemies(matrix,1,1,'E','G'))
#print(matrix[1][4])
#attack(matrix,1,4,'G')
#print(count_pieces(matrix))

#print(score_game(matrix,3))
#print(reset_everyone_moved(matrix))

#print(main1(data))
print(main2(data))


















