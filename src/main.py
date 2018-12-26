def comp(p, r, t):
    return p*((1+r)**t)

def main():
    p = int(input("Amount saved per month: "))*12
    r = int(input("percentage interest per annum: "))/100
    t = int(input("number of years to save for: "))

    total = 0
    for i in range(1, t+1):
        total += comp(p, r, i)

    print("Amount saved after {:d} years: €{:0.2f}".format(t, total))

if __name__ == "__main__":
    main()
