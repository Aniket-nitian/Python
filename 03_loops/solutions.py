# 1st sol

numbers = [1, 2, 3, -4, 5, -6, -7, 8, 9, 10]
count = 0

for number in numbers:
    if number > 0:
        count = count + 1
print(count)

# 2nd sol
sum = 0
for number in numbers:
    if number % 2 == 0:
        sum += number
print(sum)

n=10
sum_even=0
for i in range(1,n+1):
    if i%2==0:
        sum_even+=i
print(sum_even)

# 4rd sol -->string reverse
str = "Hello World"
reversed_str = ""
for char in str:
    reversed_str = char + reversed_str
print(reversed_str)
  






