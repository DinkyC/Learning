'''Purpose'''

# This function takes an input and indexes it in a dictionary 
# After it index's the input as a key it takes more input and counts the instances of each key that's inputed
# Finally the function outputs a capitalized string that is a key and value pair (Ex. 2 ICE CREAM)


def grocery():
    grocerylst= dict()

    while True:
        i = 1
        
        try:
            store = input()

            if store in grocerylst:
                grocerylst.update({store:i + 1})

            elif store not in grocerylst:
                grocerylst[store] = 1

        except KeyboardInterrupt:
            for k, v in grocerylst.items():
                j = str(v), k.upper()
                joined = " ".join(j)
                print(f"\n{joined}")
            break

grocery()



