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

    # Swap nodes with given values
    def swap_nodes(self, val1, val2):
        # No need to swap if they are the same value
        if val1 == val2:
            print("Elements are the same - no swap needed")
            return
        node1 = self.head_node
        node2 = self.head_node
        node1_prev = None
        node2_prev = None
        # Get the node with value 1 and the previous node
        while node1 is not None:
            if node1.get_value() == val1:
                break
            node1_prev = node1
            node1 = node1.get_next_node()
        # Get the node with value 2 and the previous node
        while node2 is not None:
            if node2.get_value() == val2:
                break
            node2_prev = node2
            node2 = node2.get_next_node()
        # Accounts for if there is no matching node(s)
        if (node1 is None or node2 is None):
            print("Swap not possible - one or more elements is not in the list")
            return
        # Update the preceding nodes pointers
        if node1_prev is None:
            self.head_node = node2
        else:
            node1_prev.set_next_node(node2)
        if node2_prev is None:
            self.head_node = node1
        else:
            node2_prev.set_next_node(node1)
        # Update the nodes next pointers (nodes with the given value)
        temp = node1.get_next_node()
        node1.set_next_node(node2.get_next_node())
        node2.set_next_node(temp)

    # Find nth last element in list
    def list_nth_last(self, n):
        current_node = self.head_node
        nth_last_node = None
        counter = 0
        while current_node != None:
            if nth_last_node != None:
                nth_last_node = nth_last_node.get_next_node()
            elif counter == n:
                nth_last_node = self.head_node
            current_node = current_node.get_next_node()
            counter += 1
        if nth_last_node == None:
            return "There are less than n elements in the list"
        return nth_last_node.get_value()

ll = LinkedList(3)
ll.insert_beginning(2)
ll.insert_beginning(1)
ll.insert_beginning(0)
print(ll.stringify_list())

print(ll.list_nth_last(1))