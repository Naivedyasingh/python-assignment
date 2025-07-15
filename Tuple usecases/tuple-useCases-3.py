# 3.you're developing a program to analyze temperature data.write a python function to convert a tuple representing temperture from celsius to fahrenheit
cel=int(input("Enter the celcius:"))
fer=int(input("Enter the fahreheit:"))

cal_cel=(1.8*cel)+32
cal_fer=(fer-32)/(5/9)

print(cal_cel)
print(cal_fer)