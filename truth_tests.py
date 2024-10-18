from truth import truth_values

# 3 normal tests
print('properly tests conjunction: ', truth_values(1,1)['conjunction'] == True )
print('tests a false implication: ', truth_values(1, 0)['implication'] == False )
print('biconditional is true when both are false: ', truth_values(0, 0)['biconditional'] == True)


# 3 edge cases
