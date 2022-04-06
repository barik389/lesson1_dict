def fun_tegs(tag):
    for i in products.get(tag):
        with open('C:\\Users\\Barik\\Desktop\\Foxmided\\Lesson1\\tegs.txt', 'a') as f:
            f.write(x + " is " + i +"\n")
        print("Product found. The tags are in file tags.txt.")
    products.pop(tag) 
products = {
"bread"  : ["white", "fresh", "warm"], 
"milk"   : ["white", "fresh", "cold"], 
"butter" : ["yellow", "freezed", "cold"],  
"eggs"   : ["brown", "fresh", "cold"]
}
while products != {}:
    x = input("Enter the product name:")
    if x in products:
        fun_tegs(x)    
    else:
        print("There is no such product")
else:
    print("There are no products left")
