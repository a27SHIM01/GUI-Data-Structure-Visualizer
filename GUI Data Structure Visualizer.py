# Author: Antony (Avery) Shim
# Date: Sep 05, 2023
# Purpose: a basic GUI program to create, manipulate, and visualize data structures
# ================================================================================

# IMPORT
import tkinter as tk
import tkinter.ttk as ttk

# CONSTANTS

# Text Styles
COLOR_THEME_ONE = ["#162129", "#223440", "#23455b"]
COLOR_THEME_TWO = ["#fafafa", "#e4e5f1", "#d2d3db"]
FONT_ONE = "Comic Sans"

# Spacing
WIDTH = 100
HEIGHT = 30
PAD_X = 25
PAD_Y = 25

# Widget Tags
LINKED_LIST = "linked_list"
STACK = "stack"
QUEUE = "queue"


# CLASSES
# =================================================

# Author: Avery
# Date: Sep 05, 2023
# Purpose: Basic node class

# Data Elements:    data: int

# Methods:      __init__: initializes data elements
#               __str__: returns data

class Node:
    def __init__(self, data = 0) -> None:
        """Constructs and initializes data and next.
        """
        self.data = data
        self.next = None

    def __str__(self) -> str:
        """Returns data.
        """
        return self.data


# Author: Avery
# Date: Sep 05, 2023
# Purpose: LinkedList class

# Data Elements:    head: the first node of the linked list, None if linked list is empty
#                   size: number of nodes in the linked list

# Methods:      __init__: initializes data elements
#               __str__: returns the linked list along with the size
#               is_empty: returns True if linked list is empty
#               insert_node: inserts a given node to the beginning of the linked list
#               remove_node: removes a node with the specified data from the linked list

class LinkedList:
    def __init__(self, head: Node = None) -> None:
        """Constructs and initializes head and size.
        """
        self.head = head
        self.size = 0
        print("created linked list")
    
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

    def insert_node(self, new_node_data = 0) -> None:
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


    def remove_node(self, target_node_data = 0) -> bool:
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


# Author: Avery
# Date: Dec 19, 2023
# Purpose: Stack class

# Data Elements:    data: the list of items(int) in the stack

# Methods:      __init__: initializes data elements
#               __str__: returns the items in data as a list
#               is_empty: returns True if data is empty
#               push: inserts an item to the top/front of data
#               pop: removes the top/front item from data and returns it; if data is empty, return False.
class Stack:
    def __init__(self, data: list[int] = []):
        """Initializes data elements.
        """
        self.data = data
        print("created stack")
    
    def __str__(self) -> str:
        """Returns the items in data as a list.
        """
        return "Stack: Top " + str(self.data)
    
    def is_empty(self) -> bool:
        """Returns True if data is empty.
        """
        return self.data==[]
    
    def push(self, item = 0) -> list[int]:
        """Inserts an item to the top/front of data.
        """
        self.data.insert(0, item)
        return self.data
    
    def pop(self):
        """Removes the top/front item from data and returns it. If data is empty, return False.
        """
        if not self.is_empty():
            return self.data.pop(0)
        return False 


# Author: Avery
# Date: Dec 19, 2023
# Purpose: Queue class

# Data Elements:    data: the list of items(int) in the Queue

# Methods:      __init__: initializes data elements
#               __str__: returns the items in data as a list
#               is_empty: returns True if data is empty
#               enqueue: inserts an item to the back of data
#               dequeue: removes the front item from data and returns it; if data is empty, return False.
class Queue:
    def __init__(self, data: list[int] = []) -> None:
        self.data = data
        print("created queue")

    def __str__(self) -> str:
        return "Queue: Front " + str(self.data) + " Back"
    
    def is_empty(self) -> bool:
        """Returns True if data is empty.
        """
        return self.data==[]
    
    def enqueue(self, item = 0) -> list[int]:
        """Inserts an item to the back of data.
        """
        self.data.append(item)
        return self.data
    
    def dequeue(self):
        """Removes the top/front item from data and returns it. If data is empty, return False.
        """
        if not self.is_empty():
            return self.data.pop(0)
        return False



# Author: Avery
# Date: Nov 06, 2023
# Purpose: Creates visual representation of data structures in a GUI

# Data Elements:    form: a Tk window
#                   canvas: a Canvas object
#                   linked_list: a LinkedList

# Methods:      __init__: initializes data elements
#               exit_GUI: exits the GUI
#               create_prompt_GUI: creates an Entry with a prompt allowing user input on data to add to or remove from linked_list, depending on choice
#               enter_data_GUI: adds or removes data to/from data_struct, depending on choice
#               create_widgets: create the GUI widgets

class DataStructVisualizer:
    def __init__(self, form: tk.Tk, linked_list: LinkedList = None, stack: Stack = None, queue: Queue = None) -> None:
        """Initializes data elements.
        """
        self.form = form
        self.form.state("zoomed")
        self.form.title("GUI Data Structure Visualizer")
        self.form.config(bg = COLOR_THEME_TWO[0])
        
        self.canvas = tk.Canvas(self.form, bg = COLOR_THEME_TWO[2])
        self.canvas.configure(scrollregion=(0,0,2000,2000))

        self.canvas.bind("<ButtonPress-1>", self.begin_scroll)
        self.canvas.bind("<B1-Motion>", self.begin_moving_scroll)
        self.canvas.bind("<Button-3>", self.show_right_click_menu)

        self.linked_list = linked_list
        self.stack = stack
        self.queue = queue

        self.create_widgets()


    def exit_GUI(self) -> None:
        """Exits the GUI.
        """
        self.form.destroy()


    def reset_canvas(self) -> None:
        """Clears the entire canvas and resets the data structures.
        """
        #self.canvas.delete("all")
        
        self.linked_list = LinkedList()
        self.stack.data = []
        self.queue.data = []
        
        self.draw_all_data_structs()



    def begin_scroll(self, event) -> None:
        self.canvas.scan_mark(event.x, event.y)


    def begin_moving_scroll(self, event) -> None:
        self.canvas.scan_dragto(event.x, event.y, gain=1)
    

    def show_right_click_menu(self, event) -> None:
        testMenu = tk.Menu(self.canvas, tearoff = 0) 
        testMenu.add_command(label ="Create/Edit Linked List - Placeholder")
        testMenu.add_command(label ="Create/Edit Stack - Placeholder")
        testMenu.add_command(label ="Create/Edit Queue - Placeholder")
        try: 
            testMenu.tk_popup(event.x_root, event.y_root) 
        finally: 
            testMenu.grab_release()


    def create_prompt_GUI(self, master, prompt = "", data_struct_type = 0, choice = 0, disable_list = []) -> None:
        """Creates a prompt on master form allowing user inputted data to be added to or removed from, depending on choice, 
        a selected data structure represented by data_struct_type. Widgets in disable_list are disabled.
        """
        for object in disable_list:
            object.config(state = tk.DISABLED)
            
        prompt_label = ttk.Label(master, text = prompt, wraplength=WIDTH, justify="center")
        prompt_label.place(width=WIDTH, height=HEIGHT*2, x=10, y=PAD_Y)

        data_var = tk.IntVar()
        data_var.set(0)
        input_entry = ttk.Entry(master, textvariable = data_var)
        input_entry.place(width=WIDTH, height=HEIGHT, x=10, y=HEIGHT+PAD_Y*2)
        
        input_button = ttk.Button(master, text = "Enter", \
            command = lambda:self.enter_data_GUI(data_var.get(), data_struct_type, choice, disable_list, [prompt_label, input_entry, input_button]))
        input_button.place(width=WIDTH, height=HEIGHT, x=10, y=HEIGHT*2+PAD_X*3)


    def enter_data_GUI(self, data = 0, data_struct_type = 0, choice = 0, enable_list = [], remove_widgets_list = []) -> None:
        """Adds or removes data, depending on choice, to/from a selected data structure represented by data_struct_type. 
        Re-enables the widgets in enable_list and deletes widgets in remove_widgets_list.
        """
        print("The data struct val is:", data_struct_type)
        match data_struct_type:
            case 0:
                match choice:
                    case 1:
                        self.linked_list.insert_node(data)
                        print("Successfully inserted", data, "into the linked list.")
                    case 2:
                        if self.linked_list.remove_node(data):
                            print("Successfully removed", data, "from the linked list.")
                        else:
                            print("The node", data, "is not in the linked list.")
                    case _:
                        print("Error! Invalid option.")
            case 1:
                match choice:
                    case 1:
                        self.stack.push(data)
                        print("Successfully pushed", data, "into the stack.")
                    case 2:
                        if self.stack.pop():
                            print("Successfully popped", data, "from the stack.")
                        else:
                            print("Cannot pop from empty stack!")
            case 2:
                match choice:
                    case 1:
                        self.queue.enqueue(data)
                        print("Successfully enqueued", data, "into the queue.")
                    case 2:
                        if self.queue.dequeue():
                            print("Successfully dequeued", data, "from the queue.")
                        else:
                            print("Cannot dequeue from empty queue!")
            case _:
                print("Error! Invalid data structure chosen!")

        for widget in remove_widgets_list:
            widget.destroy()
        
        for object in enable_list:
            object.config(state = tk.NORMAL)

        self.draw_all_data_structs()


    def choose_remove(self, master, prompt = "", data_struct_type = 0, choice = 0, disable_list = []) -> None:
        """Decides whether or not to show a prompt asking for which value to remove from the selected data structure
        depending on data_structure_type.
        """
        if data_struct_type == 0:
            self.create_prompt_GUI(master, prompt, data_struct_type, choice, disable_list)
        else:
            self.enter_data_GUI(data_struct_type = data_struct_type, choice = choice)


    def draw_item(self, start_x = 0, start_y = 0, data = 0, data_struct_tag = "") -> list[int]:
        """Draws a box representing an item in a data structure on the canvas.
        The data text inside the box will be created at (start_x, start_y).
        The entities created are given the tag data_struct_tag, representing the selected data structure.
        Returns the list of coordinates of the box.
        """
        # Box and data
        data_text = self.canvas.create_text(start_x, start_y, fill = "black", text = data, tags = data_struct_tag)
        print(self.canvas.gettags(data_text))
        boundary_coord = list(self.canvas.bbox(data_text))
        print(boundary_coord)
        boundary_coord[0] -= 10
        boundary_coord[1] -= 10
        boundary_coord[2] += 10
        boundary_coord[3] += 10
        rect_box = self.canvas.create_rectangle(tuple(boundary_coord), fill="green", tags = data_struct_tag)
        self.canvas.tag_raise(data_text, rect_box)
        return boundary_coord
    

    def draw_linked_list(self, start_x = 0, start_y = 0) -> None:
        """Draws the linked list on the canvas starting at (start_x, start_y).
        """
        self.canvas.delete(LINKED_LIST)
        self.canvas.create_text(start_x, start_y, text= "Linked List:\n     Head", tags = LINKED_LIST)
        current_node = self.linked_list.head
        curr_coord = [start_x, start_y+HEIGHT+5]
        dist_between_nodes = 70
        while current_node != None:
            boundary_coord = self.draw_item(curr_coord[0], curr_coord[1], current_node.data, LINKED_LIST)
            self.canvas.create_line(boundary_coord[2], (boundary_coord[1]+boundary_coord[3])//2, curr_coord[0]+dist_between_nodes-15, \
                                    curr_coord[1], arrow = "last", tags = LINKED_LIST)
            current_node = current_node.next
            curr_coord[0] += dist_between_nodes
        self.canvas.create_text(curr_coord[0], curr_coord[1], fill = "black", text = "NULL", tags = LINKED_LIST)


    def draw_stack(self, start_x = 0, start_y = 0) -> None:
        """Draws the stack on the canvas starting at (start_x, start_y).
        """
        self.canvas.delete(STACK)
        self.canvas.create_text(start_x, start_y, text= "Stack:\n  Top", tags = STACK)
        curr_y = start_y+HEIGHT+5
        for item in self.stack.data:
            curr_y = (self.draw_item(start_x, curr_y, item, STACK))[3]+20
        #self.canvas.create_line(start_x-20, start_y+25, start_x-20, curr_y-5, tags = STACK)


    def draw_queue(self, start_x = 0, start_y = 0) -> None:
        """Draws the queue on the canvas starting at (start_x, start_y).
        """
        self.canvas.delete(QUEUE)
        self.canvas.create_text(start_x, start_y, text= "Queue:\n  Front", tags = QUEUE)
        curr_x = start_x
        for item in self.queue.data:
            curr_x = (self.draw_item(curr_x, start_y+HEIGHT+5, item, QUEUE))[2]+20
        self.canvas.create_text(curr_x-20, start_y, text= "Back", anchor = tk.NE, tags = QUEUE)


    def draw_all_data_structs(self):
        """Draws all the data structures at hardcoded coordinates.
        """
        self.draw_linked_list(150, 50)
        self.draw_stack(50, 50)
        self.draw_queue(150, 150)


    def create_widgets(self) -> None:
        """Creates and places the widgets for the GUI.
        """
        self.canvas.place(width=self.form.winfo_screenwidth()-WIDTH*2-PAD_X, height=HEIGHT*25, x=WIDTH+PAD_X*2, y=PAD_Y-10)
        

        select_struct_group = ttk.LabelFrame(self.form, text = "Data Structures")
        select_struct_group.place(width=WIDTH+PAD_X, height=HEIGHT*6, x=PAD_X-10, y=PAD_Y-10)
        edit_struct_group = ttk.LabelFrame(self.form, text = "Options")
        edit_struct_group.place(width=WIDTH+PAD_X, height=HEIGHT*7, x=PAD_X-10, y=HEIGHT*10+PAD_Y-10)
        

        data_struct_type = tk.IntVar()
        data_struct_type.set(0)
        

        linked_list_button = ttk.Radiobutton(select_struct_group, text = "Linked List", variable = data_struct_type, value = 0)
        linked_list_button.place(width=WIDTH, height=HEIGHT, x=10, y=PAD_Y)
        
        stack_button = ttk.Radiobutton(select_struct_group, text = "Stack", variable = data_struct_type, value = 1)
        stack_button.place(width=WIDTH, height=HEIGHT, x=10, y=HEIGHT+PAD_Y)
        
        queue_button = ttk.Radiobutton(select_struct_group, text = "Queue", variable = data_struct_type, value = 2)
        queue_button.place(width=WIDTH, height=HEIGHT, x=10, y=HEIGHT+PAD_Y*2)


        insert_button = ttk.Button(edit_struct_group, text = 'Insert Item', command = lambda:self.create_prompt_GUI(edit_struct_group,
            prompt = "Enter the value to insert:", data_struct_type = data_struct_type.get(), choice = 1, \
                disable_list = [linked_list_button, stack_button, queue_button, insert_button, remove_button]))
        insert_button.place(width=WIDTH, height=HEIGHT, x=10, y=PAD_Y)

        remove_button = ttk.Button(edit_struct_group, text = 'Remove Item', command = lambda:self.choose_remove(edit_struct_group,
                prompt = "Enter the value to remove:", data_struct_type = data_struct_type.get(), choice = 2, \
                    disable_list = [linked_list_button, stack_button, queue_button, insert_button, remove_button]))
        remove_button.place(width=WIDTH, height=HEIGHT, x=10, y=HEIGHT+PAD_Y*2)

        clear_button = ttk.Button(self.form, text = 'Reset', command = lambda:self.reset_canvas())
        clear_button.place(width=WIDTH, height=HEIGHT, x=PAD_X+3, y=HEIGHT*24-PAD_Y)
        exit_button = ttk.Button(self.form, text = 'Exit', command = lambda:self.exit_GUI())
        exit_button.place(width=WIDTH, height=HEIGHT, x=PAD_X+3, y=HEIGHT*25-PAD_Y)

        self.draw_all_data_structs()

        


    

#Author: Avery
#Date: Sep 25, 2023
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


# MAIN

testStack = Stack()
print("Initial stack empty?:", testStack.is_empty())
if not testStack.pop():
    print("Empty data!")
testList = LinkedList()

testQueue = Queue()

"""
for i in range(100,120):
    testList.insert_node(i)
    print(testStack.push(i))
    print(testQueue.enqueue(i))
"""

print(testStack.pop())
print(testStack)

print(testQueue.dequeue())
print(testQueue)

form = tk.Tk()
test = DataStructVisualizer(form, testList, testStack, testQueue)
form.mainloop()