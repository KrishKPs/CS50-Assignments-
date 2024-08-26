def main():


    print(create("Hello"))

def create(str):
      
      new_str=""
      remove = "aeiouAEIOU"
      for char in str:
           if char not in remove:
                new_str = new_str + char

      return new_str  

           
main()