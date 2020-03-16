#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length-1)

    """
    YOUR CODE HERE
    """
    current_ticket = None
    # insert tickets into the hashtable
    for i in range(length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

        if tickets[i].source == "NONE":
            current_ticket = tickets[i].destination
            route[0] = current_ticket

    for i in range(1, length):
        next_destination = hash_table_retrieve(hashtable, current_ticket)
        if next_destination == "NONE":
            return route
        else:
            route[i] = next_destination
            current_ticket = next_destination
    return route


print(reconstruct_trip([
    Ticket("PIT", "ORD"),
    Ticket("XNA", "CID"),
    Ticket("SFO", "BHM"),
    Ticket("FLG", "XNA"),
    Ticket("NONE", "LAX"),
    Ticket("LAX", "SFO"),
    Ticket("CID", "SLC"),
    Ticket("ORD", "NONE"),
    Ticket("SLC", "PIT"),
    Ticket("BHM", "FLG")
], 10))
