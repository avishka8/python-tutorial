#listandtuples

marks=[94,70,86,97,79]
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[4])

#slicing
print(marks[0:2])

#listmethods
marks.append(60)
print(marks)
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)
marks.reverse()
print(marks)