def main():

  camelcase = input("Camel Case: ")

  print(case(camelcase))

def case (camelcase): 
  

 snakecase = ""

 for char in camelcase:

    if char.isupper():
      snakecase += "_" + char.lower() 
    else:
      snakecase += char 

 return snakecase
      

main()