def main(): 

 x = faces (input())
 print(x)

def faces(name): 
   name = name.replace(":)" , "😄")
   name = name.replace(":(" , "🥲")
   return name 

main() 