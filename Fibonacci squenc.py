
#This program calculates Fibonacci sequence

#Starting main function
def main():

#Collecting user input
    user_input = int(input("How many terms? "))
    print("Fibonacci sequence is :")

#Using for loop to output sequence 
    for i in range( user_input ):
       print( fibSeq(i))

def fibSeq( number ):

#Validating user_input 
   if number <= 1:
       return number  
   else:
#Calculating fibonacci sequence 
       return( fibSeq( number - 1 ) + fibSeq( number - 2 ))
    
   if n <= 0:  
       print("Plese enter a positive integer")


#Calling main function
main()
   

