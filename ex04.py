scores = [60, 73, 81, 95, 34]
n = 5
i = 0
total = 0
var = 0
Sumsquare = 0
while i < 5 :
    total += scores[i]
    i += 1

avg = total / n

while i > 0:
    i -= 1
    var += (avg-scores[i])**2 
    Sumsquare += scores[i]**2
print('total ' + str(total))
print('average ' + str(avg))
print('var'+str(var))
print('Sumsquare' + str(Sumsquare))
