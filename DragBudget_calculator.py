# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 09:25:26 2021

@author: Dhruv K
"""

#This is a Drag Budget calculator
print("**********************************************************************************************************************************************************")
print("                                                             NITKRacing Aerodynamics Subsystem")
print("**********************************************************************************************************************************************************")
print("                                                                 Drag Budget Calculator")
print("**********************************************************************************************************************************************************\n")
print("         ############               ######        ###############                                     #########           ##################")                   
print("        ######  ######             ######        ######        ####                                 #####  #####          ######         ######")
print("       ######    ######           ######        ######         #####                               #####    #####         ######          ######")
print("      ######      ######         ######        ######          #####                              #####      #####        ######           ######")
print("     ######        ######       ######        #####################         ############        ###################       ######          ######")
print("    ######          ######     ######        ######         ######                             ######        ######       ######         ######")
print("  ######              ###### ######        ######             ######                          ######          ######      ######        ######")    
print(" ######                ############       ######                #######                      ######            ######      #################")
print("**********************************************************************************************************************************************************\n")
available_power=float(input("Total Available Power from the car (kW) :"))
Cd1=float(input("Drag coefficient of the car :"))
rho=float(input("Density (kg/m3) :"))
A=float(input("Frontal area(m2):"))
vel=float(input("Velocity(m/s):"))
Crr=input("Input the Coefficient of Rolling resistance Crr :")
m=input("Mass of the car(kg):")
t=float(input("Targeted time for acceleration event(s):"))

# Note: remember to give the value of Cd for the case without any aero device
 

g=9.81
m=float(m)
Crr=float(Crr)

rr=0.0
rr=m*g*Crr
print("\nRolling resistance:",rr)

dpower=0.0
dpower= 0.5 * rho * Cd1 * A * (vel ** 3)
print("\nDrag power :",dpower)


car_power=0.0

s=75.0 #75m for acceleration

a1=2*s
a2= t * t
   
a=a1/a2

car_power= m*a*vel
print("\nPower consumed by car for the acceleration event:",car_power)




ad1=car_power+rr+dpower
ad=ad1 / 1000
print (ad)
rem=available_power - ad
print("\nPower available for aero package:",rem)
print("\nRemember to have some excess power to account for other losses ")


