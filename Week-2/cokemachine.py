def main():
  
  amount = 50; 


  while amount > 0:
    print("Amount Due: " , amount)
    due = int(input("Insert Coin: "))
    amount = amount - due 

  print("Amount Due: " , amount) 


   
main() 