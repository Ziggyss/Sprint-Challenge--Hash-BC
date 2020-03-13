#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    # store each weight in the input list as keys, and the weight's list index as the value in hash_table_insert(table, key, value )
    for index in range(len(weights)):
        hash_table_insert(ht, weights[index], index)

    # loop through the weights
    for index in range(len(weights)):
        # assign each value to weight
        weight = weights[index]
        # calculate the difference between the limit and each weight
        difference = limit - weight
        # look to see if there is a value in the table equal to the difference
        second_value = hash_table_retrieve(ht, difference)
        if second_value is not None:
            # return the higher value first each time
            if second_value > index:
                return (second_value, index)
            else:
                return (index, second_value) 
        # if the second_value is None, return None           
        
    return None    





    """
    YOUR CODE HERE
    """


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
