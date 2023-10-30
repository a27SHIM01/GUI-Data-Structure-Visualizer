# Author: Antony (Avery) Shim
# Date: Sept 05, 2023
# Purpose: a basic GUI program to create, manipulate, and visualize data structures
# ================================================================================

# IMPORT
from tkinter import *

# CONSTANTS
COLOR_ONE = "#162129"
COLOR_TWO = "#223440"
COLOR_THREE = "#23455b"
FONT_ONE = "Verdana"


# CLASSES
# =================================================

# Author: Avery
# Date: Sept 05, 2023
# Purpose: Basic node class

# Data Elements:    data: str

# Methods:      __init__: initializes data elements
#               __str__: returns data

class Node:
    def __init__(self, data = '') -> None:
        """Constructs and initializes data and next.
        """
        self.data = data
        self.next = None

    def __str__(self) -> str:
        """Returns data.
        """
        return self.data


# Author: Avery
# Date: Sept 05, 2023
# Purpose: LinkedList class

# Data Elements:    head: the first node of the linked list, None if linked list is empty
#                   size: number of nodes in the linked list

# Methods:      __init__: initializes data elements
#               __str__: returns the linked list along with the size
#               is_empty: returns True if linked list is empty
#               insert_node: inserts a given node to the beginning of the linked list
#               remove_node: removes a node with the specified data from the linked list

class LinkedList:
    def __init__(self) -> None:
        """Constructs and initializes head and size.
        """
        self.head = None
        self.size = 0
    
    def __str__(self) -> str:
        """Returns the linked list as a string.
        """
        temp_pointer = self.head
        str_list = 'Head'
        while temp_pointer != None:
            str_list += ' -> ' + temp_pointer.data
            temp_pointer = temp_pointer.next
        str_list += ' Size: ' + str(self.size)
        return str_list
        
    def is_empty(self) -> bool:
        """Returns True if the linked list is empty.
        """
        return self.head == None

    def insert_node(self, new_node_data = '') -> None:
        """Inserts a node with data new_node_data into the beginning (head) of the linked list.
        """
        self.size += 1
        
        new_node = Node(new_node_data)
        # Case 1: empty list
        if self.is_empty():
            self.head = new_node
        # Case 2: 1+ node(s) in LL
        else:
            new_node.next = self.head
            self.head = new_node


    def remove_node(self, target_node_data = '') -> bool:
        """Removes the first node with data target_node_data in the linked list and returns True.
        If there is no node with target_node_data, return False. 
        """
        removed = False
        if not self.is_empty():
            if self.head.data == target_node_data:
                self.head = self.head.next
                removed = True
                self.size -= 1
            else:
                prev_node = self.head
                current_node = self.head.next
                while current_node != None:
                    if current_node.data == target_node_data:
                        prev_node.next = current_node.next
                        removed = True
                        self.size -= 1
                        break
                    prev_node = current_node
                    current_node = current_node.next
        return removed


#Author: Avery
#Date: Sept 25, 2023
#Parameters: given_val -> int, min_val -> int, max_val -> int, default_val -> int
#Return: default_val if given_val not in [min_val, max_val]; otherwise, given_val
#=================================
def check_int(given_val = 0, min_val = 0, max_val = 0, default_val = 0) -> int:
    """Returns default_val if given_val is not between min_val and max_val;
    otherwise returns given_val.
    """
    if (given_val < min_val) or (given_val > max_val):
        return default_val
    return given_val


#Author: Avery
#Date: Sept 05, 2023
#Parameters: none
#Return: none
#=================================
def exit_GUI() -> None:
    """Exits the GUI.
    """
    form.destroy()


#Author: Avery
#Date: Oct 22, 2023
#Parameters: linked_list -> LinkedList(), prompt -> str, choice -> int
#Return: none
#=================================
def create_prompt_GUI(linked_list = None, prompt = "", choice = 0) -> None:
    """Creates an Entry with a prompt allowing user input on data to add to or remove from linked_list, depending on choice.
    """
    prompt_label = Label(form, text = prompt)

    data_var = StringVar()
    input_entry = Entry(form, textvariable = data_var, font = (FONT_ONE, 11))
    input_entry.grid(row = 0, column = 5, sticky = W + E, padx = 10, pady = 10)
    
    input_button = Button(form, text = "Enter", command = lambda:enter_data_GUI(linked_list, data_var.get(), choice, [prompt_label, input_entry, input_button]))
    input_button.grid(row = 1, column = 5, sticky = W + E, padx = 10, pady = 10)
    data_var.set("")


#Author: Avery
#Date: Oct 23, 2023
#Parameters: linked_list -> LinkedList(), data -> str, choice -> int, widgets_list -> []
#Return: none
#=================================
def enter_data_GUI(linked_list = None, data = "", choice = 0, widgets_list = []) -> None:
    """Adds or removes data to/from linked_list, depending on choice 
    """
    match choice:
        case 1:
            insert_node_GUI(linked_list, data)
        case 2:
            remove_node_GUI(linked_list, data)
        case _:
            print("Error! Invalid option.")

    for widget in widgets_list:
        widget.destroy()


#Author: Avery
#Date: Oct 22, 2023
#Parameters: linked_list -> LinkedList(), new_node_data -> str
#Return: none
#=================================
def insert_node_GUI(linked_list = None, new_node_data = "") -> None:
    """Inserts a new node containing new_node_data into linked_list.
    """
    linked_list.insert_node(new_node_data)
    output_text.insert(END, linked_list)
    output_text.insert(END, "\n")


#Author: Avery
#Date: Oct 22, 2023
#Parameters: linked_list -> LinkedList(), target_node_data -> str
#Return: none
#=================================
def remove_node_GUI(linked_list = None, target_node_data = "") -> None:
    """Removes the first node containing target_node_data from linked_list.
    """
    if linked_list.remove_node(target_node_data):
        print("Successfully rmeoved", target_node_data, "from the linked list.")
    else:
        print("The node", target_node_data, "is not in the linked list.")
    output_text.insert(END, linked_list)
    output_text.insert(END, "\n")


# MAIN

testList = LinkedList()

form = Tk()
form.title('Data Structure Visualizer')
form.config(bg=COLOR_ONE)


output_text = Text(form)
output_text.grid(row = 0, column = 0, rowspan = 3, columnspan = 5, sticky = W + E, padx = 10, pady = 10)

exit_button = Button(form, text = 'EXIT', font = (FONT_ONE, 11), fg = 'white', bg = COLOR_TWO, width = 2, height = 1, command = lambda:exit_GUI())
exit_button.grid(row = 4, column = 4, sticky = W + E, padx = 10, pady = 10)

insert_button = Button(form, text = 'Insert Node', font = (FONT_ONE, 11), fg = 'white', bg = COLOR_TWO, width = 2, height = 1, \
                       command = lambda:create_prompt_GUI(linked_list = testList, prompt = "Enter the data to insert into the linked list:", choice = 1))
insert_button.grid(row = 4, column = 0, sticky = W + E, padx = 10, pady = 10)

remove_button = Button(form, text = 'Remove Node', font = (FONT_ONE, 11), fg = 'white', bg = COLOR_TWO, width = 2, height = 1, \
                       command = lambda:create_prompt_GUI(linked_list = testList, prompt = "Enter the data to remove from the linked list:", choice = 2))
remove_button.grid(row = 4, column = 1, sticky = W + E, padx = 10, pady = 10)


"""
loopBreak = False
while not loopBreak:
    testList = LinkedList()
    print("Empty list: ", testList, "\n")
    
    optionsLoopBreak = False
    while not optionsLoopBreak:
        options = input("="*40 + "\nPress 1 to insert a new node\nPress 2 to remove a node\nPress 3 to print out the LL\
                        \nPress 0 to exit the LL manipulation\n" + "="*40 + "\nWhat do you want to do? ")
        match options:
            case "1":
                new_node_data = input("Enter the data for a node to insert into the Linked List: ")
                testList.insert_node(new_node_data)
                print(testList)
            case "2":
                target_node_data = input("Enter the data for a node to remove from the Linked List: ")
                if testList.remove_node(target_node_data):
                    print("Successfully removed", target_node_data, "from the linked list.")
                else:
                    print("The node", target_node_data, "is not in the linked list.")
                print(testList)
            case "3":
                print(testList)
            case "0":
                optionsLoopBreak = True
            case _:
                print("Invalid input")
    
    print("The finalized Linked List is:", testList)

    stop = input('\nType in anything to restart the program, or type "stop" to exit: ')
    print()
    if stop == 'stop':
        loopBreak = True
"""

form.mainloop()
