# create Array 
planet = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus"]
planet.append("Neptune")
print("Therd planet is : " +planet[2])

print("Here are the planets listed in order of their distance from the Sun: ")
for x in planet:
    print(x)

print("The number of planets is : "+str(len(planet)))
