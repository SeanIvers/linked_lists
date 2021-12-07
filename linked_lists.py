# Linked List Data Structure

# Node Class
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    # Get methods
    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    # Set method
    def set_next_node(self, next_node):
        self.next_node = next_node

# Linked List Class
class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    # Inserts a value at the beginning
    def insert_beginning(self, new_value):
        new_node = Node(new_value)
        new_node.set_next_node(self.head_node)
        self.head_node = new_node

    # Shows string representation of the list
    def stringify_list(self):
        string = ""
        current_node = self.head_node
        while current_node != None:
            string += str(current_node.get_value()) + "\n"
            current_node = current_node.get_next_node()
        return string

    # Remove node with given value
    def remove_node(self, value_to_remove):
        current_node = self.head_node
        if self.head_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            current_node = current_node.get_next_node()
            while current_node != None:
                if current_node.get_next_node().get_value() == value_to_remove:
                    current_node.set_next_node(current_node.next_node.get_next_node())
                    current_node = None

    # Remove all nodes with given value
    def remove_all_nodes(self, value_to_remove):
        current_node = self.head_node.get_next_node()
        prev_node = self.head_node
        while current_node:
            if prev_node.get_value() == value_to_remove:
                self.head_node = current_node
                prev_node = self.head_node
                current_node = prev_node.get_next_node()
            elif current_node.get_value() == value_to_remove:
                prev_node.set_next_node(current_node.get_next_node)
                current_node = current_node.get_next_node()
            else:
                prev_node = current_node
                current_node = current_node.get_next_node()

