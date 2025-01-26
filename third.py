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
marks.insert(1,100)
print(marks)
marks.remove(97)
marks.pop(3)
print(marks)