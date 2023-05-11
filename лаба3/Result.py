mimport numpy
import numpy as np

newfile = open("app.conf", "w")
newfile.write(input("Введите числа a b c через пробел"))
newfile.close()
newfile = open("app.conf", "r")

spisok = newfile.readlines()
celchisl = []
for i in spisok:
    for j in i:
        if j == " ":
            continue
        else:
            celchisl.append(j)

celchisl = list(map(int, celchisl))
ans = [celchisl[1] * i + celchisl[2] for i in range(0, celchisl[0])]
print(ans)

with open("result.dat", "w") as file23:
    file23.write(str(ans))
    file23.close()
    


#Готовая лабораторная
