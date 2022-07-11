#Binary Serach Tree
# Code based in Eduarda's code created in the Algorithms and Data Structures II course

from Node import Node


class Tree:
    
    def __init__(self):
        self.root = None
    
    # Return tree root
    def getRoot(self):
        return self.root

    # Insert a node in the tree
    def insert(self, label):
        node = Node(label)

        ## Check if the Tree is empty
        if self.empty(): 
            self.root = node
        ## Check if the node/number already exists, if it exists will not add
        elif self.search(label, False):
            print("Node already exists, it will not be added!\n")
        else:
            current_node = self.root
            parent_node = None

            ## We search until the node is equal to null
            while True: 
                if current_node != None:
                    parent_node = current_node

                    # Check if the new node is bigger or smaller than current_node
                    if node.getLabel() < current_node.getLabel():
                        current_node = current_node.getLeft()
                    else:
                        current_node = current_node.getRight()
                else: 
                    # Check if will insert in the right or left
                    if node.getLabel() < parent_node.getLabel(): 
                        parent_node.setLeft(node)
                    else:
                        parent_node.setRight(node)
                    break
    
    # Check if the tree is empty
    def empty(self):
        if self.root == None:
            return True
        return False

    # Print message when tree is empty
    def emptyMessage(self):
        print("The tree is empty!")

    # Print the Tree sorted from: root, left, right
    def showTree(self, current_node):
        if self.getRoot() != None:
            if current_node != None:
                print('%d' % current_node.getLabel(), end=' ')
                self.showTree(current_node.getLeft())
                self.showTree(current_node.getRight())
        else:
            self.emptyMessage()
    
    # Print the Tree sorted from: left, right, root
    def showTreePostOrder(self, current_node):
        if self.getRoot() != None:
            if current_node != None:
                self.showTreePostOrder(current_node.getLeft())
                self.showTreePostOrder(current_node.getRight())
                print('%d' % current_node.getLabel(), end=' ')
        else:
            self.emptyMessage()

    # Print the Tree sorted from: left, root, right
    def showTreeInOrder(self, current_node):
        if self.getRoot() != None:
            if current_node != None:
                self.showTreeInOrder(current_node.getLeft())
                print('%d' % current_node.getLabel(), end=' ')
                self.showTreeInOrder(current_node.getRight())
        else:
            self.emptyMessage()

    # Remove an element
    def remove(self, label):
        # Check if the tree is empty
        if self.empty():
            self.emptyMessage()
        else:
            node = Node(label)
            current_node = self.root
            parent_node = None

            while True:
                # Check if the node doesn't exist
                if current_node == None:
                    print('The node was not found.')
                    break
                # Search for the node
                if current_node.getLabel() != node.getLabel():
                    parent_node = current_node
                    if node.getLabel() < current_node.getLabel():
                        current_node = current_node.getLeft()
                    else:
                        current_node = current_node.getRight()
                # Node found
                else:
                    # If the Node doesn't have children
                    if current_node.getLeft() == None and current_node.getRight() == None:
                        if node.getLabel() == self.getRoot().getLabel():
                            self.root = None
                        else:
                            if node.getLabel() > parent_node.getLabel():
                                parent_node.setRight(None)
                            else:
                                parent_node.setLeft(None)
                    
                    # If the Node have 2 children
                    elif current_node.getLeft() != None and current_node.getRight() != None:
                        min_node = current_node.getRight()
                        min_node_parent = current_node

                        while True:
                            if min_node.getLeft() != None:
                                min_node_parent = min_node
                                min_node = min_node.getLeft()
                            else:
                                current_node.setLabel(min_node.getLabel())
                                if min_node.getLabel() < min_node_parent.getLabel():
                                    min_node_parent.setLeft(None)
                                else:
                                    min_node_parent.setRight(None)
                                min_node = None
                                break
                        break
                        
                    # If the Node has just one child
                    else:
                        if current_node.getLeft() != None:
                            current_node.setLabel(current_node.getLeft().getLabel()) 
                            current_node.setLeft(None)
                        else:
                            current_node.setLabel(current_node.getRight().getLabel()) 
                            current_node.setRight(None)
                    current_node = None
                    break
    
    # Search for an element
    def search(self, label, printMessage = True):

        ##Check if the Tree is empty
        if self.empty(): 
            self.emptyMessage()
        else:
            current_node = self.root
            while True:
                if current_node == None:
                    if printMessage:
                        print('Number not found!')
                    return False

                if current_node.getLabel() == label:
                    if printMessage:
                        print('Number found: ', label)
                    return True
                else:
                    if label < current_node.getLabel():
                        current_node = current_node.getLeft()
                    else:
                        current_node = current_node.getRight()

    # Print Node Journey Pre-Order Tree
    def printShowTree(self, current_node, previous_node):
        if current_node != None:
            if previous_node != None:
                print(f'{previous_node.getLabel()} -> {current_node.getLabel()}')
            self.printShowTree(current_node.getLeft(), current_node)
            self.printShowTree(current_node.getRight(), current_node)

    # Print Node Journey Post-Order Tree
    def printShowTreePostOrder(self, current_node, previous_node):
        if current_node != None:
            self.printShowTreePostOrder(current_node.getLeft(), current_node)
            self.printShowTreePostOrder(current_node.getRight(), current_node)
            if previous_node != None:
                print(f'{current_node.getLabel()} -> {previous_node.getLabel()}')

    # Print Node Journey In-Order Tree
    def printShowTreeInOrder(self, current_node, previous_node):
        if current_node != None:
            self.printShowTreeInOrder(current_node.getLeft(), current_node)
            if previous_node != None:
                print(f'{current_node.getLabel()} -> {previous_node.getLabel()}')
            self.printShowTreeInOrder(current_node.getRight(), current_node)