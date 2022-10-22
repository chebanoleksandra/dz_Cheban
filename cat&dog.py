class Pet:
    amount_of_paws = '4 paws'
    amount_of_tails = '1 tail'
    amount_of_ears = '2 ears'

    def __init__(self, animal='Animal', name='Pet', sound='Sound', height='50 cm', weight='5 kg', fur_color='White', eye_color='Blue'):
        self.animal = animal
        self.name = name
        self.sound = sound
        self.height = height
        self.weight = weight
        self.fur_color = fur_color
        self.eye_color = eye_color


cat = Pet('Cat', 'Ghost', 'Meow', '24 cm', '5 kg', 'White fur', 'Blue eyes')
dog = Pet('Dog', 'Sirius', 'Bark', '90 cm', '30 kg', 'Black fur', 'Black eyes')

# cat.animal = 'Cat'
# cat.name = 'Ghost'
# cat.sound = 'Meow'
# cat.height = 24
# cat.weight = 5
# cat.fur_color = 'White'
# cat.eye_color = 'Blue'

print(cat.animal)
print(cat.name)
print(cat.sound)
print(cat.amount_of_paws)
print(cat.amount_of_tails)
print(cat.amount_of_ears)
print(cat.height)
print(cat.weight)
print(cat.fur_color)
print(cat.eye_color)

print(dog.animal)
print(dog.name)
print(dog.sound)
print(dog.amount_of_paws)
print(dog.amount_of_tails)
print(dog.amount_of_ears)
print(dog.height)
print(dog.weight)
print(dog.fur_color)
print(dog.eye_color)