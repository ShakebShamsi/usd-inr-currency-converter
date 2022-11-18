def main():
    print("This program coverts USD into INR")
    print("")

    dollars = eval(input("Enter the amount in USD: "))

    rupee =convert_to_rupee(dollars)

    print("That is", rupee, "rupee.") 


convert_to_rupee = lambda dollars: dollars * 80

main()