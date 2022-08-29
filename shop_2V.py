print("Welcome TO Hell Club")

Name=input("Hello sir can i know your name Please?\n" )

if Name == "Ben":
    yes =input("You are evil ben? \n")
    
    
    if yes =="yes":
        print("get out here ass hole")
        exit()
    else:
        print("Sorry for the ask ")


print("Here is our menu sir " + Name + "\n Kottu 6$| Rice 6$| Tofu 2$ \n Juice 3$| water 1$| tea 3$| coffe 2$ \n")
print("What is your desire sir")
Food=input()

quantity =input("how meny food?\n")
print("Ok Sir " +Name+ " Your "+Food+" Ready soon")

if Food == "coffe":
    coffe = 2
    cost =  coffe  * int(quantity)
if Food =="Kottu":
    Kottu = 6
    cost =Kottu    * int (quantity)
if Food =="Rice":
    Rice = 6
    cost = Rice    * int(quantity)
if Food =="Tofu":
    Tofu =2
    cost = Tofu    * int(quantity)
if Food =="Juice":
    Juice =3
    cost = Juice   * int(quantity)
if Food =="water":
    water =1
    cost = water   * int(quantity)
if Food =="tea":
    tea = 3
    cost = tea     * int(quantity)

print("Your Bill Sir:" + str(cost) +"$")

print("Here Your " + quantity + " " + Food + "`s " +Name)