def truth_values(val1, val2):
    A = True if val1 == 1 else False
    B = True if val2 == 1 else False

    return {'conjunction': A & B, 
            'disjunction': A | B,
            'negation': A == False,
            'implication': not ((A == True) & (B == False)),
            'biconditional': (A & B) | ((A == False) & (B == False)),
            }

def main():

    print('You can either show a full truth table or choose the truth value of each statement')
    print('Enter 1 to see the full truth table, 0 to enter your own values')

    fullTruthTable = bool(input())

    if (fullTruthTable):
        print('full truth table')
        print('-------------------------')
        print(f"{'Value of A':^12} | {'Value of B':^12} | {'Conjunction':^12} | {'Disjunction':^12} | {'Negation':^12} | {'Implication':^12} | {'Biconditional':^15}")


        # get the truth values
        combos = [[1,1], [0,0], [1,0], [0,1]]

        for pair in combos:
            vals = truth_values(pair[0], pair[1])
            print(f"{str(pair[0]):^12} | {str(pair[1]):^12} | {str(vals['conjunction']):^12} | {str(vals['disjunction']):^12} | {str(vals['negation']):^12} | {str(vals['implication']):^12} | {str(vals['biconditional']):^15}")
        return

    print("Enter the truth of two statements")
    print("------")
    print("Is statement A true? Enter 1 for true, 0 for false:")
    print("------")

    valueA = int(input())

    while (valueA != 0 | valueA != 1):
        print('please enter either 0 or 1: ')
        valueA = input()
    

    print("------")
    print("Is statement B true? Enter 1 for true, 0 for false:")
    print("------")

    valueB = int(input())

    while (valueB != 0 | valueB != 1):
        print('please enter either 0 or 1: ')
        valueB = input()
    
    results = truth_values(valueA, valueB)

    # print truth table
    for key, value in results.items():
        print(key + ": " + str(value))
        print("--------------")




if __name__ == '__main__':  
    main()