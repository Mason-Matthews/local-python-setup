def hello():
    print("Hello World")

hello()


def pack(x,y,z):
    myList = [x,y,z]
    return myList

print(pack("Apple", "Banana", "Grapes"))

def eat_lunch(food):
    if(len(food) == 0):
        print("My lunchbox is empty.")
    else:
        for x in range(len(food)):
            if(x == 0):
                print("First I eat " + food[0])
            else:
                print("Next I eat " + food[x])


eat_lunch(["Apple", "Banana", "Grapes", "Cheese", "Turkey leg", "Cupcake"])