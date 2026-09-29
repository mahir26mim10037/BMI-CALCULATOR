from statistics import NormalDist
import math
def intro():
    print("Welcome to BMI calculator.")
    b=int(input("Enter you age :"))
    if b>=20:
        bmi_adult()
    elif b<=2:
        print("bmi is not calculated for this age group.")
    else:
        bmi_child()

def bmi_adult():
  c=float(input("Enter your height in m :"))
  d=float(input("Enter your weight in kg :"))
  if c<=0 and d<=0:
    print("Invalid input")
  else:
    e=d/(c**2)
  if e<18.5:
      print("Your bmi is :",e,"\n You are underweight.\n You need to include more calories in your diet!")
  elif e<=24.5:
        print("Your bmi is :",e,"\n You are fit.\nCongratulations!You are leading a healthy lifestyle. Continue with that.")
  elif e<=29.9:
        print("Your bmi is :",e,"\n You are overweight., \n You need to start exercising and eat a balanced diet.")
  elif e>30:
        print("Your bmi is :",e,"\n You are obese. \n Oops!Looks like someone needs to start exercising and eat healthy food.")
def bmi_child():
    gen=input("Enter whether you are a boy or a girl :")
    f=float(input("Enter your height in m :"))
    g=float(input("Enter your weight in kg :"))
    age=int(input("Please enter your age again. :"))
    if f<=0 and g<=0:
        print("Invalid input")
    else:
        bmi=g/(f**2)
    boys={ 2: [14.0, 14.7, 16.0, 17.0], 3: [13.9, 14.6, 15.8, 16.9],
           4: [13.8, 14.5, 15.7, 16.8], 5: [13.8, 14.4, 15.6, 16.8],
           6: [13.8, 14.5, 15.7, 17.0], 7: [13.8, 14.5, 15.8, 17.2],
           8: [13.8, 14.6, 15.9, 17.5], 9: [13.9, 14.7, 16.1, 17.8],
           10: [14.0, 14.8, 16.3, 18.2], 11: [14.1, 15.0, 16.5, 18.6],
           12: [14.3, 15.2, 16.8, 19.0], 13: [14.5, 15.4, 17.1, 19.4],
           14: [14.7, 15.6, 17.4, 19.8], 15: [14.9, 15.8, 17.7, 20.2], 16: [15.1, 16.0, 18.0, 20.6],
           17: [15.3, 16.2, 18.3, 21.0], 18: [15.5, 16.4, 18.6, 21.4], 19: [15.7, 16.6, 18.9, 21.8] }
    girls = { 2: [13.7, 14.4, 15.7, 16.9], 3: [13.6, 14.3, 15.6, 16.8],
              4: [13.6, 14.2, 15.5, 16.7], 5: [13.5, 14.2, 15.5, 16.8], 
              6: [13.5, 14.2, 15.6, 17.0], 7: [13.6, 14.3, 15.8, 17.3], 
              8: [13.7, 14.4, 16.0, 17.6], 9: [13.8, 14.5, 16.2, 18.0], 
              10: [14.0, 14.7, 16.4, 18.4], 11: [14.2, 14.9, 16.7, 18.8], 
              12: [14.4, 15.1, 17.0, 19.2], 13: [14.6, 15.3, 17.3, 19.6], 
              14: [14.8, 15.5, 17.6, 20.0], 15: [15.0, 15.7, 17.9, 20.4], 
              16: [15.2, 15.9, 18.2, 20.8], 17: [15.4, 16.1, 18.5, 21.2], 
              18: [15.6, 16.3, 18.8, 21.6], 19: [15.8, 16.5, 19.1, 22.0] } 
    if gen=="boy": 
        data=boys 
    elif gen=="girl": 
        data=girls 
    else: 
        print("Please enter either boy or girl.") 
        exit()
    age=round(age) 
    p5, p50, p85, p95=data[age] 
    if bmi<p5: 
        percentile=4.0 
        cat="Underweight" 
    elif bmi<p50: 
        percentile =5+((bmi-p5)/(p50 - p5))*45
        cat="Healthy Weight" 
    elif bmi<p85: 
        percentile=50+((bmi-p50)/(p85-p50))*35 
        cat="Healthy Weight" 
    elif bmi<p95: 
        percentile=85+((bmi-p85)/(p95-p85))*10 
        cat="Overweight" 
    else: 
        percentile=95+((bmi-p95)/p95)*5 
        cat="Obese"

intro()
print("Thank You.")
ask=input("Do you want to check again?(Yes/No) :").lower()
if ask=="yes":
   intro()
else:
    print("Thank You for using our BMI calculator.")

