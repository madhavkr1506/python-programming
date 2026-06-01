import heapq as hq

mass = 5
asteroids = [4,9,23,4]

data = []
hq.heapify(data)

for i in asteroids:
    if mass>=i:
        mass+=i
        while len(data)>0 and mass>=data[0]:
            mass+=hq.heappop(data)
    else:
        hq.heappush(data, i)

print(len(data) == 0)
