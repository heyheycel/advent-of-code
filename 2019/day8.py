wide=25
tall=6
image=open('input_day8.txt').read().strip()
layers=[]

for layer in range(len(image)//(wide*tall)):
	layers.append(image[layer*wide*tall:(layer+1)*wide*tall])



def min_layer(layers, num):
	minn=150
	for layer in layers:
		tmp=layer.count(num)
		if tmp<minn:
			minn=tmp
			layer_m=layer

	return layer_m


    

def collapse(layers):
    return [next(filter(lambda v: v != 2, lay)) for lay in zip(*layers)]


def no_transparencies(layer):
	for i in layer:
		if '2' in layer:
			return False

		else:
			return True

def create_img(layers):
	img=[]
	#map each layer with the other layer and so on
	for layer in zip(*layers):
		#filter transparencies with number 2
		layer_f=filter(lambda v: v!='2', layer)
		img.append(next(layer_f))

	return img
	
def create_matr(lista, size):
	img=[]
	for i in range(0, len(lista), size):
		img.append(lista[i:i+size])

	return img
		

	


def draw(img):
    for r in img: 
    	print(*['#' if x == '1' else ' ' for x in r])

# Part 1
best = min_layer(layers, '0')
print("Part 1")
print(best.count('1') * best.count('2'))

# Part 2
print("Part 2")
img = create_matr(create_img(layers), wide)
#print(img)
#print(collapse_(layers))
draw(img)	