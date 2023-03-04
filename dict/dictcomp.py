'''Example One: Basics'''

# Attaching the phrase "man" to the end of each hero 
# Manipulating the dictionary so that in the case it is "superman", the corresponding value is "journalist"

'''my_dict = {
    "Spider" : "photographer",
    "Bat" : "philanthropist",
    "Wonder Wo" : "nurse"
}

my_dict = {

(key + "man" if key != "Spider" else "Superman"):

(val if val != "photographer" else "journalist") 

for (key, val) in my_dict.items()

}
print(my_dict)'''


'''Example Two: DNA (ditionary of lists)'''

# Adenine(A) can only be paired with Thymine(T)
# Cytosine(C) can only be paired with Guanine(G)

# Attempting to mirror these pairings with code

'''import random

bases = ["A", "T", "C", "G"]

strand1 = random.choices(bases, k = 10)

print(strand1)

dna = {
key:[val, ("T" if val == "A" else "A" if val == "T" else "C" if val == "G" else "G")] 
for (key, val) in enumerate(strand1)
}

print(dna)'''

'''Example Three: Users (list of dictionaries)'''

import random 
import string

keys = ["id", "username", "password"]
users = ["MaryJane", "You know how it is"]

data = [
{
    key: 
(i if key == "id" else users[i] if key == "username" else "".join(random.choices(string.printable, k=8))) for key in keys
} 

for i in range(len(users))

]

# password = "".join(random.choices(string.printable, k=8)) # This function creates a random password

print(data)
  


