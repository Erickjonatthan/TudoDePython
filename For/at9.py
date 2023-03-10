num = int(input("Você quer saber a tabuada de qual número? "))
print("Tábuada do ",num)
for i in range(10):
    result = num * (i+1)
    print(num, " X ", (i+1), "= ", result)