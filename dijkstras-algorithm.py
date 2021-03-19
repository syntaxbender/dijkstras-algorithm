from numpy import inf
graph = {
	'Kirklareli': {'Edirne':67,'Tekirdag':50},
	'Edirne':{'Kirklareli':67,'Tekirdag':115,'Canakkale':228},
	'Tekirdag':{'Kirklareli':86,'Edirne':115,'Canakkale':171,'Istanbul':148},
	'Canakkale':{'Edirne':228,'Tekirdag':171,'Balikesir':144},
	'Istanbul':{'Tekirdag':148,'Izmit':118,'Yalova':92},
	'Balikesir':{'Bursa':152,'Canakkale':144},
	'Bursa':{'Balikesir':152,'Yalova':68,'Bilecik':98},
	'Yalova':{'Istanbul':92,'Izmit':65,'Bursa':68,'Bilecik':111},
	'Izmit':{'Istanbul':118,'Yalova':65,'Sakarya':43},
	'Bilecik':{'Sakarya':105,'Yalova':111,'Bursa':98},
	'Sakarya':{'Izmit':43,'Bilecik':105}
}
costs = {'Kirklareli': 0, 'Edirne': inf, 'Tekirdag': inf, 'Canakkale': inf, 'Istanbul': inf, 'Balikesir': inf, 'Bursa': inf, 'Yalova': inf, 'Izmit': inf, 'Bilecik': inf, 'Sakarya': inf}
parents = {}
def search(source, target, graph, costs, parents):
    nextNode = source
    #ziyaret edilecek node başlangıç için source olarak işaretleniyor.
    while nextNode != target:
    	#hedef node'a ulaşana kadar sonsuz döngü devam edecek.
        for neighbor in graph[nextNode]:
        	#ziyaret edilecek olarak işaretlenen başlangıç node'sinden başlanarak her while döngüsü iterasyonunda nextNode değişkenine set edilen nodenin ilişkili olduğu diğer nodeler for döngüsü ile her iterasyonda işlenir.
            if graph[nextNode][neighbor] + costs[nextNode] < costs[neighbor]:
            	#nextNode nodesinin başlangıç nodesine olan uzaklığı ile for döngüsünde işlenen nextNode nodesinin ilişkiği olduğu diğer nodelerin nextNode nodesine olan uzaklığı toplamı mesafeleri sakladığımız cost dizesinde tanımlı olan mesafeden az ise kod bloğu çalışır.
                costs[neighbor] = graph[nextNode][neighbor] + costs[nextNode]
                #daha az olan mesafe değeri tanımlanır.
                parents[neighbor] = nextNode
                #parent dizisine şuan itere edilen izlenen path eklenir.
            del graph[neighbor][nextNode]
            #graph dizisinden path tersine gidilmemesi için tam ters yol silinir.
        del costs[nextNode]
        #en küçük cost/mesafe şuan üzerinde bulunduğumuz nextNode'nin olacağı için diziden çıkarılır. aşağı satırdaki kodda en küçük cost değeri alınacaktır.
        nextNode = min(costs, key=costs.get)
        #en küçük cost değerine sahip olan node nextNode olarak seçilir.
    return parents
    #izlenen yol dönüş yapılır.
def backpedal(source, target, searchResult):
	#bu metod sayesinde parents değişkeninde izlenen yol geriye dönük olarak çözümlenir.
    node = target
    backpath = [target]
    path = []
    while node != source:
        backpath.append(searchResult[node])
        node = searchResult[node]
    for i in range(len(backpath)):
        path.append(backpath[-i - 1])
    return path

result = search('Kirklareli', 'Balikesir', graph, costs, parents)
print('parent dictionary={}'.format(result))
print('longest path={}'.format(backpedal('Kirklareli', 'Balikesir', result)))