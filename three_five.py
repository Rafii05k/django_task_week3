sum=0
replaced_sum=0
count=0

for num in range(51):
    if num%2==0:
        sum+=num #sum of even numbers 

   #print all even numbers between 1 and 51 except 3 and 5 multiples
        if num%3==0:
            num_str="Three"
            count+=1
            replaced_sum+=num
        elif num%5==0:
            num_str="Five"
            count+=1
            replaced_sum+=num
        else:
            num_str=num
        print(num_str)

    #print the sum of the multiple of 3 and 5 and their count
print(f"the sum of numbers replaced by 'three' or 'five' is {replaced_sum} & there are {count} numbers that got replaced")
print(f"The sum of all even numbers between 0 and 50 is {sum}")


















    #print the sum of even numbers between 1 and 50(inclusive)
print(f"The sum of even numbers between 1 and 50 is {sum}")
    
    
    
    