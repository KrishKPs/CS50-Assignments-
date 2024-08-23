def main():

    amount = float(input("How much was the Meal ? $"))
    percentage = float(input("What Percentage would you like to Tip ? ")) 

    x = (percentage/100)*amount

    

    print(f"Leave: ${x:.2f}")

main() 