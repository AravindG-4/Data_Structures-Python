#Collision handing using chaining

class HashTable:  
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]
            
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
        if not found:
            self.arr[h].append((key,val))
        
    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del",index)
                del self.arr[arr_index][index]
                
with open('Hashing\weather.csv','r') as f:
    weather = f.read().split('\n')
    weather.pop(0)
for ind,i in enumerate(weather):
    weather[ind] = i.split(',')

Nyc = HashTable()

for i in weather:
    Nyc[i[0]] = int(i[1])
    
days = [i[0] for i in weather]

sum = 0    
for i in range(7): 
    sum+=Nyc[days[i]]
print('Average temp of 1st week of Jan :',format((sum/7),'.2f'))

max = (0,0)
for i in Nyc.arr:
    if i:
        for j in i:
            if j[1]>max[1]:
                max = j    
print(f"The maximum temperature is {max[1]} on {max[0]}")

print(Nyc['Jan 9'])
print(Nyc['Jan 4'])


