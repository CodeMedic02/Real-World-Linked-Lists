# Name: Trent Adams
# Date:  2024-Jan-07


from LinkedList import LinkedList
from Client import Client
from datetime import date
import time  # Used to time for code executions.
import random

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

# Scenario 3: Call Center
section_title = "Scenario: Call Center"
print(section_title)
print("-" * len(section_title))

# How long does it take to add records, randomly display 1000 records, and randomly remove 1000 records from the LinkedList?
for i in range(numRecords):
    my_linked_list.add_last(clients[i])

start_time = time.time()

# Add records
current_id = 100001 + numRecords + 1
for i in range(1000):
    my_linked_list.add_last(Client(current_id))
    current_id += 1

# Display random records
for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + numRecords
    random_id = random.randint(smallest_id, largest_id)
    print(my_linked_list.search(Client(random_id)))

# Remove random records
for i in range(1000):
    smallest_id = 100001
    largest_id = smallest_id + numRecords
    random_id = random.randint(smallest_id, largest_id)
    my_linked_list.search(Client(random_id))

end_time = time.time()
total_time = end_time - start_time
print("Seconds to add, display and, records: {:.6f}".format(total_time))
