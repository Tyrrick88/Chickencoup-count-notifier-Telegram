def main():
    #First The capacity of the coup is determined
    coupCount = int(input("Chicken coup count: "))

    if coupCount < 50:
        print("Chicken/Chicks are too few")

    elif coupCount == 50:
        print("All the Chicken/Chicks are in the coups")

if __name__ == "__main__":
    main()
