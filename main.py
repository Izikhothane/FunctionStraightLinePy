# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math

def numx1():
        numx1 = float(input("faka ux wepoyinti yoluqala    :"))
        return numx1

def numy1():
        numy1 = float(input("faka uy wepoyinti yoluqala    :"))
        return numy1

def name():
        name = input("Bhala igama lepoyinti yokuqala      :")
        return name

def numx2():
        numx2 = float(input("faka ux wepoyinti yesibini    :"))
        return numx2

def numy2():
        numy2 = float(input("faka uy wepoyinti yesibini    :"))
        return numy2

def name2():
        name2 = input("Faka igama le poyinti yesibini      :")
        return name2

def calculate_dist(numx1,numy1,numx2,numy2):
        return math.sqrt(math.pow(numx2 - numx1, 2) + math.pow(numy2 - numy1, 2))

def equation(numy2,numy1,numx2,numx1):
        return (numy2 - numy1) / (numx2 - numx1)

def quadrant(numx1,numy1,):
        if numx1 > 0 and numy1 > 0:
            print("Ikwi gumbi elise North est")

        elif numx1 < 0 and numy1 > 0:
            print("Ikwi gumbi elise North west")

        elif numx1 < 0 and numy1 < 0:
            print("Ikwi gumbi elise South west")

        elif numx1 > 0 and numy1 < 0:
            print("Ikwi gumbi elise South est")

        elif numx1 == 0 and numy1 == 0:
            print("isesiphakathini")
        else:
            print("ayikho nakwelinye igumbi")

def ref_pointx(numx1,numy1):

        if (numx1 > 0 and numy1 > 0):
            print("Isithunzi sayo xa uyithelekisa ne x-axis ", numx1, ","+"-", numy1);

        elif numx1 < 0 and numy1 > 0:
            print("Isithunzi sayo xa uyithelekisa ne x-axis  ", numx1, ","+"-", numy1);

        elif numx1 < 0 and numy1 < 0:
            print("Isithunzi sayo xa uyithelekisa ne x-axis  ", numx1, ",", numy1);

        elif numx1 > 0 and numy1 < 0:
            print("Isithunzi sayo xa uyithelekisa ne x-axis ", numx1, ",", numy1);

        elif numx1 == 0 and numy1 == 0:
            print("Isesiphakathini,akho sithunzi")

def ref_pointy(numx1,numy1):

        if numx1 > 0 and numy1 > 0:
            print("Isithunzi sayo xa uyithelekisa ne y-axis "+"-", numx1, ",", numy1)

        elif numx1 < 0 and numy1 > 0:
            print("Isithunzi sayo xa uyithelekisa ne y-axis  ", numx1, ",", numy1)

        elif numx1 < 0 and numy1 < 0:
            print("Isithunzi sayo xa uyithelekisa ne y-axis  ", numx1, ",", numy1)

        elif numx1 > 0 and numy1 < 0:
            print("Isithunzi sayo xa uyithelekisa ne x-axis  "+"-", numx1, ",", numy1)

        elif numx1 == 0 and numy1 == 0:
            print("Isesiphakathini,akho sithunzi ")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
         numx1 = numx1()
         numy1 = numy1()
         name=name()
         numx2=numx2()
         numy2=numy2()
         name2=name2()
         print("umahliko phakathi kwezipoyint ngu :", calculate_dist(numx1,numx2,numy1,numy2),"meters")
         equation(numx1,numy1,numx2,numy2)
         quadrant(numx1,numy1)
         ref_pointx(numx1,numy1)
         ref_pointy(numx1,numy1)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
