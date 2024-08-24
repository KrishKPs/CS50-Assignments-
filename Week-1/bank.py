def main():


  str = input("Greetings: ").lower()

  

  if str == "hello":
    print("$0")
  elif str.startswith("h"):
    print("$20")
  else:
    print("$0")

main()