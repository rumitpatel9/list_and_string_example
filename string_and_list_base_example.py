#find the prime number
# check_nu =int(input("Enter a Number."))
# if check_nu <=0:
#     print("Plese enter a valid number.")
# elif check_nu ==1:
#     print("Not prime number")    
# else:    
#     for nu in range(2,check_nu):
#         if check_nu % nu == 0:
#             print(" Not Prime number")
#             continue
#         else:
#             break
#     else:
#         print("Prime number.")



#fibonacci serice
# a,b =0,1
# n =5
# assert n ==5
# fibo_list =[]
# fibo_list.append(a)
# fibo_list.append(b)
# while(n!=0):
#     c =a+b
#     fibo_list.append(c)
#     a =b
#     b =c
#     n-=1       
# print(fibo_list)



#list comprehension

# l1 =[i for i in range(5)]
# print(l1)

# thisdict = {
#   3: "Ford",
#   2: "Mustang",
# }
# # print(thisdict[0])
# first_key = list(thisdict.keys())
# print(first_key)



#list base programs...
# 1)Python program to interchange first and last elements in a list
# l1 =[1,2,3,4,5,6,78]
# l1[-1],l1[0] = l1[0],l1[-1]
# print(l1)

# Python program to swap two elements in a list
# l1 =[29,57,38,29]
# l1[-1],l1[-2] =l1[-2],l1[-1]
# print(l1)

#Python | Ways to find length of list with logic
# l1 =[29,57,38,29]
# count  =0
# for nu in l1:
#   count+=1
# print(count)  

# Different ways to clear a list in Python
# l1.clear()
# print(l1)
# l1 =[29,30,40,58]
# for i in range(len(l1)):
#   l1.pop()
# print(l1) 

# l2 =[9]
# l2.pop()
# print(l2)

# Python | Reversing a List using logic
# l1 = [29,30,40,50,27]
# for n in range(1,len(l1)+1):
#   l1[n-1],l1[-n] = l1[-n],l1[n-1]
# print(l1) 

# Python program to find smallest number in a list
# l1 = [29,30,40,50,27]
# l1.sort(reverse=False)
# print(l1[0])


# Python program to print positive numbers in a list
# l1 = [-29,30,40,-50,-27]
# for nu in l1:
#   if nu<0:
#     print(nu,"nag")
#   else:
#     print(nu,'pos')  

#remover emtey list form a List
# test_list = [5,6,[],5,3,[],[],9]
# for i in test_list:
#   print(i)
#   if i == []:
#     print(i)
#     test_list.pop(test_list.index(i))
# print(test_list)

# ls2=[[],23,456,[],65,[],63]
# ls3=[i for i in ls2 if i!=[]]
# print(ls3)


l1 =[1,2,[3,4,5],[[6],[[[7,[None]],[8,9]]]]]
l2 =[]
for i in l1:
  if type(i) is list:
    for j in i:
      pass
  else:
    l2.append(i)
print(l2)     