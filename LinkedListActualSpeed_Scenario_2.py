# Name: Trent Adams
# Date:  2024-Jan-13


from LinkedList import LinkedList
from Client import Client
from datetime import date
import time  # Used to time for code executions.
import random
import sys  # Used to terminate application.

# Display name and date in output.
print("Name: ", "Trent Adams")
print("Date: ", date.today())
print()

# Read records from client data via ClientData.csv file
# into client object and place the client objects into the list.

input_file_name = 'ClientData.csv'
clients = []  # Ensure this is defined before the loop

with open(input_file_name) as infile:
    for line in infile:
        fileData = line.split(',')
        client_id = int(fileData[0])  # Convert to integer.
        f_name = fileData[1]
        l_name = fileData[2]
        phone = fileData[3]
        email = fileData[4]

        # Create client objects using the data from the file.
        clientObject = Client(client_id, f_name, l_name, phone, email)

        # Add client objects to list
        clients.append(clientObject)

    # Add client objects to list
    clients.append(clientObject)

numRecords = len(clients)

my_linked_list = LinkedList()


# Scenario 2: Customer Service Center
section_title = "Scenario: Customer Service Center"
print(section_title)
print("-" * len(section_title))

# Add records to the LinkedList
for i in range(numRecords):
    my_linked_list.add_last(clients[i])

start_time = time.time()

for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + numRecords
    random_id = random.randint(smallest_id, largest_id)
    print(my_linked_list.search(Client(random_id)))

end_time = time.time()
total_time = end_time - start_time

print("There are {} records in the list.".format(numRecords))
print("Seconds to display random records: {:.6f}".format(total_time))