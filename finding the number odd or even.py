n1 = int(input('enter 1st number : '))
n2 = int(input('enter 2nd number : '))
even = 0
odd = 0
for i in range(n1, n2+1) :
    if i%2==0 :
        even += 1
    else:
        odd += 1

print('even:', even)
print('odd: ', odd)
