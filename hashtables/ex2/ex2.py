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
    route = [None] * length

    # Loop through the tickets array and create a hash table with the information
    # The starting location is the key, the destination is the value
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
        # the ticket with source as none is the first ticket in the list
        route[0] = hash_table_retrieve(hashtable, "NONE")
        # starting location is the key each time
        # destination is the value
        # loop through the tickets for the rest of the length of the array
        for index in range(1, len(tickets)):
            # then add each route to the array according to the previous entry's location
            route[index] = hash_table_retrieve(hashtable, route[index - 1])

        return route    

        
            





    """
    YOUR CODE HERE
    """

   

