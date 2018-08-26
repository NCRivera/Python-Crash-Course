#Removing an Item by Value.
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

#motorcycles.remove('ducati')
#print(motorcycles)

#You can also use the remove() method to work with a value that’s being 
#removed from a list.

too_expensive = 'ducati'
motorcycles.remove('ducati')
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")
