def get_weight():
    while True:
        try:
            weight=float(input("Enter your weight in pounds: "))
            if not weight>0:
                raise ValueError
            elif weight>0:
                return weight
        except ValueError:
            print("ERROR! Non-accepted value was entered. Enter an integer greater than 0 for weight. ")
def get_feet():
    while True:
        try:
            feet=int(input("Enter your height in feet(only whole numbers): "))
            if not feet>0:
                raise ValueError
            elif feet>0:
                return feet
        except ValueError:
            print("ERROR! Non-accepted value was entered. Enter an integer greater than 0 for feet; only whole numbers. ")

def get_inches():
    while True:
        try:
            inches=float(input("Enter your height for inches;please only enter between 0-12 inches: "))
            if 0<=inches<12:
                return inches
            else:
                raise ValueError
        except ValueError:
            print("ERROR! Non-accepted value was entered. Enter an number between 0 and 12. ")

def BMI(weight,feet,inches):
    height=(12*feet)+inches
    BMI=round((((weight/height**2) *703)),2)
    print("As a reminder, BMI is an estimate and is not a sole factor in determining healthy weight.")
    if(BMI>30.0):
        print("Your BMI is", BMI, "and you are considered obese." )
    elif (25.0<=BMI<30.0):
        print("Your BMI is", BMI, "and you are considered overweight." )
    elif (18.5<=BMI<25.0):
        print("Your BMI is", BMI, "and you are considered a healthy weight." )
    elif(BMI<18.5):
        print("Your BMI is", BMI, "and you are considered underweight." )

def get_sets():
    while True:
        try:
            set=int(input("Enter your sets for a given weight: "))
            if not set>0:
                raise ValueError
            elif set>0:
                return set
        except ValueError:
            print("ERROR! Non-accepted value was entered. Enter an integer greater than 0 for sets. ")

def get_reps():
    while True:
        try:
            reps=int(input("Enter your reps for a given weight: "))
            if not reps>0:
                raise ValueError
            elif reps>0:
                return reps
        except ValueError:
            print("ERROR! Non-accepted value was entered. Enter an integer greater than 0 for reps. ")
def get_weights():
    while True:
        try:
            w=float(input("Enter your weights used on your working sets: "))
            if w>0:
                return w
            else:
                raise ValueError
        except ValueError:
            print("ERROR! Non-accepted value was entered. Enter a number greater than 0. ")
def get_RPE():
    while True:
        try:
            RPE=int(input("Enter your RPE(rate of perceived exertion) for your working sets: "))
            if 1<=RPE<=10:
                return RPE
            else:
                raise ValueError
        except ValueError:
            print("ERROR! Non-accepted value was entered. Enter an integer between 1-10 for RPE ")
def RM(sets,reps,weight,RPE):
    RPE=10/RPE
    reps=reps/30
    RM=(RPE*weight)*(1+reps)
    RM=round(RM,2)
    print("As a reminder, a one rep max is an estimate; a person's 1RM can fluctuate due to nutrition, recovery, or determination. ")
    print("Your estimated one-rep max is", RM)
if __name__ == '__main__':
    w=get_weight()
    f=get_feet()
    i=get_inches()
    BM=BMI(w,f,i)
    s=get_sets()
    r=get_reps()
    gw=get_weights()
    RPE=get_RPE()
    oneRM=RM(s,r,gw,RPE)
