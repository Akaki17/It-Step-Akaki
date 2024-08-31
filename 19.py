# Node class represents each element in the LinkedList or Stack
class Node:
    def __init__(self, data=None):
        self.data = data  # Store data
        self.next = None  # Pointer to the next node

# LinkedList class to handle operations on the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list as None
        
    # Append a new node to the end of the linked list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        
        if self.head is None:
            self.head = new_node  # If list is empty, set head to the new node
            return
        
        last_node = self.head  # Start from the head of the list
        
        # Traverse to the last node
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = new_node  # Link the last node to the new node
        
    # Remove a node at a specific index from the linked list
    def remove_at(self, index):
        if index < 0 or self.head is None:
            return  # Invalid index or empty list
        
        if index == 0:
            self.head = self.head.next  # Remove the head node
            return
       
        current_node = self.head 
        current_position = 0
        
        # Traverse to the node before the one to be removed
        while current_node.next and current_position < index - 1:
            current_node = current_node.next
            current_position += 1
        
        if current_node.next:
            current_node.next = current_node.next.next  # Skip the node to be removed

    # Display the elements of the linked list
    def display(self):
        current_node = self.head
        
        while current_node is not None:
            print(current_node.data, end=' -> ')  # Print the data of the current node
            current_node = current_node.next  # Move to the next node
    
# Example usage of LinkedList
linked_list = LinkedList()
linked_list.append('Hello')
linked_list.append(10)
linked_list.append(True)
linked_list.append(5.5)

linked_list.display()  # Output the linked list
print()

linked_list.remove_at(2)  # Remove the third element
linked_list.remove_at(0)  # Remove the first element
linked_list.display()  # Output the modified linked list


# Stack class to implement a stack data structure using linked list nodes
class Stack:
    def __init__(self): 
        self.top_node = None  # Initialize the top of the stack as None
        self.length = 0  # Initialize stack size as 0
    
    # Check if the stack is empty
    def empty(self):
        return self.length == 0
    
    # Return the size of the stack
    def size(self):
        return self.length
    
    # Push a new node onto the stack
    def push(self, data):
        new_node = Node(data)  # Create a new node with the given data
        new_node.next = self.top_node  # Link new node to the current top node
        self.top_node = new_node  # Update the top to the new node
        self.length += 1  # Increase the stack size
    
    # Peek at the top node's data without removing it
    def top(self):
        if not self.empty():
            return self.top_node.data
        else:
            raise IndentationError('Stack Is Empty')
        
    # Pop the top node from the stack and return its data
    def pop(self):
        if not self.empty():
            popped_item = self.top_node.data  # Get the data of the top node
            self.top_node = self.top_node.next  # Move top to the next node
            self.length -= 1  # Decrease the stack size
            return popped_item
        else:
            raise IndentationError('Stack is empty')

# Example usage of Stack
stack = Stack()

print(f'Stack is Empty: {stack.empty()}')  # Check if stack is empty
print(f'Stack Size: {stack.size()}')  # Get stack size

stack.push(10)
stack.push(5)
stack.push(20)
stack.push(50)

print(f'Stack is Empty: {stack.empty()}')  # Check if stack is empty after pushing
print(f'Stack Size: {stack.size()}')  # Get stack size after pushing

print(stack.top())  # Peek at the top of the stack
print(stack.pop())  # Pop the top of the stack
print(f'Stack size: {stack.size()}')  # Get stack size after popping
print(stack.pop())  # Pop again
print(f'Stack size: {stack.size()}')  # Get stack size again
print(stack.pop())  # Continue popping
print(f'Stack size: {stack.size()}')  # Check final size

print(stack.top())  # Try peeking at the now-empty stack (will raise an error)

# Example comparing an empty list and an empty stack
empty_lst = list()
empty_lst.append(10)

empty_stack = Stack()
empty_stack.push(10)
