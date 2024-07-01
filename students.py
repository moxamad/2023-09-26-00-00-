grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a=sorted(students)
z=sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),sum(grades[3])/len(grades[3]),sum(grades[-1])/len(grades[-1])
v={a[0]: z[0], a[1]: z[1], a[2]: z[2], a[3]: z[3],a[-1]:z[-1] }
print(v)
