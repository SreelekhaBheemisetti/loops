a=int(input("enter the a:"))
b=int(input("enter the b:"))
even_sum=0
odd_sum=0
while a<=b:
     if a%2==0:
          even_sum=even_sum+a
     elif a%2!=0:
          odd_sum=odd_sum+a
     a=a+1
print("even sum:",even_sum,end=" ")
print("odd sum:", odd_sum, end=" ")