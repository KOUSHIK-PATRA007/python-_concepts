#
# print("1. Numbers from 1 to 10:")
# num = 1
# while num <= 10:
#     print(num, end=" ")
#     num = num + 1
# print()
# print()
#
# print("2. Even numbers from 1 to 50:")
# n = 1
# while n <= 50:
#     if n % 2 == 0:
#         print(n, end=" ")
#     n = n + 1
# print()
# print()
#
# print("3. Odd numbers from 1 to 50:")
# number = 1
# while number <= 50:
#     if number % 2 == 1:
#         print(number, end=" ")
#     number = number + 1
# print()
# print()
#
# print("4. Numbers from 100 to 1:")
# a = 100
# while a >= 1:
#     print(a, end=" ")
#     a = a - 1
# print()
# print()
#
# print("5. Sum of first 10 natural numbers:")
# total = 0
# val = 1
# while val <= 10:
#     total = total + val
#     val = val + 1
# print("Sum is", total)
# print()
#
# print("6. Multiplication table of a given number:")
# table_num = 3
# i = 1
# while i <= 10:
#     print(table_num, "x", i, "=", table_num*i)
#     i = i + 1
# print()
#
# print("7. Count digits in a number:")
# given_num = 4862
# cnt = 0
# temp = given_num
# while temp > 0:
#     cnt = cnt + 1
#     temp = temp // 10
# print("Number of digits in", given_num, "is", cnt)
# print()
#
# print("8. Sum of digits of a number:")
# num2 = 345
# sum_d = 0
# temp2 = num2
# while temp2 > 0:
#     r = temp2 % 10
#     sum_d = sum_d + r
#     temp2 = temp2 // 10
# print("Sum of digits of", num2, "is", sum_d)
# print()
#
# print("9. Reverse a number:")
# n1 = 789
# rev = 0
# tt = n1
# while tt > 0:
#     y = tt % 10
#     rev = rev * 10 + y
#     tt = tt // 10
# print("The reverse of", n1, "is", rev)
# print()
#
# print("10. Check if a number is a palindrome:")
# org = 131
# rev2 = 0
# check = org
# while check > 0:
#     s = check % 10
#     rev2 = rev2 * 10 + s
#     check = check // 10
# if rev2 == org:
#     print(org, "is a palindrome")
# else:
#     print(org, "is not a palindrome")
# print()
#
# print("11. Find the factorial of a number")
# fact_num = 4
# big = 1
# mul = 1
# while mul <= fact_num:
#     big = big * mul
#     mul = mul + 1
# print("Factorial of", fact_num, "is", big)
# print()
#
# print("12. Count digit 5 in a number:")
# num5 = 155555215
# count5 = 0
# tryme = num5
# while tryme > 0:
#     if tryme % 10 == 5:
#         count5 = count5 + 1
#     tryme = tryme // 10
# print("Digit 5 was found", count5, "times in", num5)
# print()
#
# print("13. Product of digits of a number:")
# num3 = 321
# prod = 1
# tmp3 = num3
# while tmp3 > 0:
#     prod = prod * (tmp3 % 10)
#     tmp3 = tmp3 // 10
# print("Product of digits of", num3, "is", prod)
# print()
#
# print("14. Smallest digit in a number:")
# nu = 78542
# tiny = 9
# copy = nu
# while copy > 0:
#     uu = copy % 10
#     if uu < tiny:
#         tiny = uu
#     copy = copy // 10
# print("Smallest digit in", nu, "is", tiny)
# print()
#
# print("15. Largest digit in a number:")
# nm = 78542
# biggest = 0
# cpy = nm
# while cpy > 0:
#     dd = cpy % 10
#     if dd > biggest:
#         biggest = dd
#     cpy = cpy // 10
# print("Largest digit in", nm, "is", biggest)
# print()
#
# print("16. Armstrong number check:")
# number = 153
# temp = number
# result = 0
# digits = 0
# t = temp
# while t > 0:
#     digits = digits + 1
#     t = t // 10
# t = temp
# while t > 0:
#     rem = t % 10
#     result = result + rem ** digits
#     t = t // 10
# if result == number:
#     print(number, "is an Armstrong number")
# else:
#     print(number, "is not an Armstrong number")
# print()
#
# print("17. Numbers from 1 to N divisible by 3 and 5:")
# N = 100
# x = 1
# while x <= N:
#     if x % 3 == 0 and x % 5 == 0:
#         print(x, end=" ")
#     x = x + 1
# print()
# print()
#
# print("20. How many times can number be divided by 2 before it's 0:")
# num = 40
# count = 0
# while num > 0:
#     num = num // 2
#     count = count + 1
# print("It can be divided", count, "times before it becomes 0")
# print()
#
# print("22. Count numbers from 1 to 100 divisible by 7:")
# counter = 0
# for val in range(1, 101):
#     if val % 7 == 0:
#         counter = counter + 1
# print("Count is", counter)
# print()
#
# print("23. Series of squares (first N terms):")
# N = 10
# k = 1
# while k <= N:
#     print(k * k, end=" ")
#     k = k + 1
# print()
# print()
#
# print("24. Series of cubes (first N terms):")
# N = 10
# j = 1
# while j <= N:
#     print(j ** 3, end=" ")
#     j = j + 1
# print()
#
#
# print("28. Check whether all digits of a number are even")
# num = 482604
# temp = num
# even = True
#
# while temp > 0:
#     digit = temp % 10
#     if digit % 2 != 0:
#         even = False
#         break
#     temp = temp // 10
#
# if even:
#     print("All digits of", num, "are even")
# else:
#     print("All digits of", num, "are not even")

































