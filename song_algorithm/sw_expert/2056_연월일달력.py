# T=int(input())

# for test_case in range(1, T+1):
#   N=input()
#   year=N[:4]
#   month=int(N[4:6])
#   date=int(N[6:])
#   if 1 > month > 12:
#     print(f"#{test_case} -1")
#   else:


rental_book = ["난중일기",'위대한 개츠비','데미안']

rental_book = ["난중일기"*2,'위대한 개츠비','데미안']

missing_book =[]

for each in rental_book:
  if each not in list_book:
    missing_book.append(each)

missing_book = [book for book in rental_book if ]