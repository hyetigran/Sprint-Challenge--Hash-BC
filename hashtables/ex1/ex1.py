#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    if len(weights) <= 1:
        return None

    result = []
    table = {}

    for i in range(0, len(weights)):
        sum_weight = limit - weights[i]

        table[weights[i]] = sum_weight

    for i in range(0, len(weights)):
        if limit - weights[i] in table:
            result.insert(0, i)

    return result
    # index = 0

    # for item in weights:
    #     weights_sum = limit - item
    #     existing_key = hash_table_retrieve(ht, item)

    #     if (existing_key == 0 or existing_key) and (limit - item == weights_sum):
    #         return (index, existing_key)
    #     hash_table_insert(ht, item, index)
    #     index += 1


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
