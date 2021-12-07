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

