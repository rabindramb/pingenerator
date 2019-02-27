print("""
  _____ _        _____                           _             
 |  __ (_)      / ____|                         | |            
 | |__) | _ __ | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 |  ___/ | '_ \| | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
 | |   | | | | | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
 |_|   |_|_| |_|\_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|                                                                                                                                
""")
x = int(input('Enter the starting number[~]:'))
y = int(input('Enter the ending number[~]:'))
y +=1
filen = input('Enter file name without extension where you want to save pins[~]:')
filename = filen+'.txt'

save = open(filename,'w')
for numbers in range(x,y): #This will generate no. of pins ranging from x to y
 pins = str(numbers)
 save.write(pins)
 save.write('\n')
save.close()
print('Pins from '+str(x)+' to '+str(y)+' have been saved in '+filename)

