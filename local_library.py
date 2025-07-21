def sum_of_even_numbers(x):
    ll=[]
    sum=0
    for i in range(0, x+1):
        if i % 2 == 0:
            ll.append(i)       
    for j in ll:
        sum +=j            
    return sum 

#-----------------------------------------------------------------------------------------------

def reverse(x):
    return x[::-1]  

#-----------------------------------------------------------------------------------------------

def count_vowels(word):
    count = 0
    word=word.lower()
    vowels="eauio"
    for char in word :
        if char in vowels:
            count += 1
    return count

#-----------------------------------------------------------------------------------------------

def factorial(x):
    for i in range (1 , x):
        x *= i
    return x    

#-----------------------------------------------------------------------------------------------

def is_palindrome(x):
    return x == x[::-1]

#-----------------------------------------------------------------------------------------------

def FizzBuzz(x):
    ll=[]
    for i in range(1, x+1):
        if i%3 == 0 and i%5 == 0:
            ll.append("FizzBuzz")
        elif i%3 == 0:
            ll.append("Fizz")
        elif i%5 == 0:
            ll.append("Buzz")
        else:
            ll.append(i)
    return ll            

#-----------------------------------------------------------------------------------------------

def FindMax(x):
    max=0
    for i in x:
        if i > max:
            max = i
    return max

#-----------------------------------------------------------------------------------------------
    
def SumNum(x):
    x=str(x)
    sum=0
    for i in x:
        sum += (int(i))
    return sum    

#-----------------------------------------------------------------------------------------------

def is_prime(x):
    if x < 3:
        return False
    for i in range (2,x):
        if x%i == 0 :
            return False
    return True
    
#-----------------------------------------------------------------------------------------------

def fibonacci(x):
    fib = [0, 1] 
    while len(fib) < x:
        fib.append(fib[-1] + fib[-2])
    return fib    

def fibonacci(x):
    fib = [0, 1] 
    for i in range(0, x-2):
        fib.append(fib[-1] + fib[-2])
    return fib  

#-----------------------------------------------------------------------------------------------

def RemoveDuplicates(x):
    return list(dict.fromkeys(x))

def RemoveDuplicates(x):
    ll=dict.fromkeys(x, 0)
    for i in x:
        ll[i]+=1

    return list(ll.keys())    
                    
#-----------------------------------------------------------------------------------------------

def MissingNum(x):
    letters=[]
    count=x[0]
    for i in x:
        i+=1
        count+=1
        print(i)
        print(count)
        if count not in x:
            letters.append(count)
        else:
            x.remove(count)

    return letters    

#-----------------------------------------------------------------------------------------------

def anagram(x, y):
    #  return sorted(x) == sorted(y)
    l1=dict.fromkeys(x,0)
    l2=dict.fromkeys(y,0)
    for i in x:
        l1[i]+=1
    for j in y:
        l2[j]+=1

    return l1 == l2

#-----------------------------------------------------------------------------------------------

def RotateArray(array, k):
    final=[]
    final.extend(array[-k:])
    for i in range(len(array)-k):
        final.append(array[i])
    return final    
    
#-----------------------------------------------------------------------------------------------

def LongestWord(x):
    words=x.split(' ')
    long=words[0]
    for char in words:
        if len(char) > len(long):
            long=char
    return long

#-----------------------------------------------------------------------------------------------

def count(word):
    key=dict.fromkeys(word,0)
    for i in word:
        key[i]+=1
    return key
key = count("hello")

#-----------------------------------------------------------------------------------------------

def title(x):
    return x.title()

#-----------------------------------------------------------------------------------------------

def SecLarge(x):
    # x.sort()
    # return x[-2]
    final=[]
    max=0
    for j in range(len(x)):
        for i in x:
            if i>max:
                max=i
        final.append(max)
        x.remove(max)
        max=0
    return final[1]

#-----------------------------------------------------------------------------------------------

def SumOfPairs(l, target):
    final=[]
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i] + l[j] == target and i != j:
                final.append(l[i])
                final.append(l[j])
    return list(dict.fromkeys(final))            

#-----------------------------------------------------------------------------------------------

def GCD(x,y):
    while(x%y !=0):
        num=x%y
        x=y
        y=num
    return y 

#-----------------------------------------------------------------------------------------------

def even_numbers(x):
    even = []
    for i in range(x+1):
        if i %2 == 0:
            even.append(i)
    return even  

#-----------------------------------------------------------------------------------------------

def age(x):
    if x >= 18 :
        return "You are an adult"
    else:
        return "You are a minor"
    
#-----------------------------------------------------------------------------------------------

def operations(x,y):
    if y == 0:
        return("error, {num2 can't be 0}")
    else:
        return f"{x} + {y} = {x+y}\n{x} - {y} = {x-y}\n{x} * {y} = {x*y}\n{x} / {y} = {x/y}"

#-----------------------------------------------------------------------------------------------    

def pyramid(x):
    count=0
    while count <= x:
        print("*"*count)
        count+=1

#-----------------------------------------------------------------------------------------------
 
def center_window(window, width, height):
     screen_width = window.winfo_screenwidth() 
     screen_height = window.winfo_screenheight() 
     x = (screen_width // 2) - (width // 2) 
     y = (screen_height // 2) - (height // 2) 
     window.geometry(f'{width}x{height}+{x}+{y}')
        