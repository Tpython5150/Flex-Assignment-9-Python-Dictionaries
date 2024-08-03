'''

2. Python Programming Challenges for Customer Service Data Handling
Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

Problem Statement: Develop a program that:

Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
  - Implement functions to:
  - Open a new service ticket.
  - Update the status of an existing ticket.
  - Display all tickets or filter by status.
  - Initialize with some sample tickets and include functionality for additional ticket entry.
  
Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
'''

service_tickets = {
  "Ticket01": {"Customer": "Nicole", "Issue": "Derailer Adjustment", "Status": "open"},
  "Ticket02": {"Customer": "Sophia", "Issue": "Brakes ", "Status": "closed"},
  "Ticket03": {"Customer": "Mason", "Issue": "Flat tire", "Status": "closed"}, 
  "Ticket04": {"Customer": "Troy", "Issue": "Broken Chain", "Status": "open"}
}
#next tickets to add 
#"Ticket05:": {"Customer": "David", "Issue": "Bent Frame", "Status": "open"}

def open_new_ticket(ticket, ticket_number):
  if ticket_number not in ticket: # checking ticket number doesnt't exist
    ticket[ticket_number] = {} # if it doesnt adding to ticket
    print(f"Ticket number '{ticket_number}' added.") # conditonal print statement
  else:                                                       
    print(f"Ticket number '{ticket_number}' already exists.")   # conditional print statement #2
    
def add_customer(ticket, ticket_number, customer):
  if ticket_number in ticket:  # making sure ticket now exists
    if customer not in ticket[ticket_number]: # checking if customer is not in dict.
      ticket[ticket_number]["Customer"] = customer  #adding customer  to ticket number
      print(f"Customers name '{customer}' added to '{ticket_number}'.")  # conditional print statements
    else:
      print(f"Customers name '{customer}' already exists in '{ticket_number}'.")
  else:
    print(f"Category '{ticket_number}' does not exist.") 
    
def add_issue(ticket, ticket_number, customer, issue):
  if ticket_number in ticket:
    if issue not in ticket[ticket_number]: #checking for issue = not in ticket
      ticket[ticket_number]["Issue"] = issue # adds issue to tickenumber
      print(f"Issue '{issue}' added to '{ticket_number}' concerning '{customer}'.") # conditional statements
    else:
      print(f"Issue '{issue}' already exists in '{ticket_number}' concerning '{customer}'.")  
  else:
    print(f"Ticket number '{ticket_number}' does not exist.")
    
def add_status(ticket, ticket_number, customer, issue, status):
  if ticket_number in ticket:
    if status not in ticket[ticket_number]: # checking for status = not in ticket
      ticket[ticket_number]["Status"] = status # adding status ticket number
      print(f"Status '{status}' added to '{ticket_number}' concerning '{customer}'.") # conditional statements
    else:
      print(f"Status '{status}' already exists in '{ticket_number}' concerning '{customer}'.") 
  else:
    print(f"Ticket number '{ticket_number}' does not exist.")
      
def display_tickets(ticket):
  for ticket_number, items in ticket.items():  # displaying tickets
    print(f"{ticket_number}:")  # print ticket number
    for key, value in items.items():
        print(f"  - {key}: {value}") # print key, value pairs

def remove_ticket(ticket, ticket_number): # function to remove ticket number for service tickets
  if ticket_number in ticket: # letting us know where to find ticket number = in ticket
    removed_item = ticket.pop(ticket_number) 
    print(f"Item '{ticket_number}' removed from '{ticket}'.") # print statement
  else:
        print(f"Item '{ticket_number}' does not exist.") # condtional print statement
        
def view_tickets_by_status(ticket, status): # function to view ticket by status
    print(f"Tickets with status '{status}':") # print statment status
    for ticket_number, details in ticket.items():
        if details.get("Status") == status:
            print(f"{ticket_number}:")  # print ticket number
            for key, value in details.items(): 
                print(f"  - {key}: {value}") # print key, value


 
open_new_ticket(service_tickets, "Ticket05") 
add_customer(service_tickets, "Ticket05", "David")
add_issue(service_tickets, "Ticket05", "David", "Frame Bent")
add_status(service_tickets, "Ticket05", "David", "Frame Bent", "open")
remove_ticket(service_tickets, "Ticket03")
view_tickets_by_status(service_tickets, "closed")
view_tickets_by_status(service_tickets, "open")
display_tickets(service_tickets)