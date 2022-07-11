from Tree import Tree


class Menu():
    def __init__(self):
        self.tree = Tree()

    def options(self):
        return input('''
		=======================================
		TREE
		=======================================
		0 -	Insert
		1 -	Delete
		2 -	Search
		3 -	Show Tree Pre-Order
		4 -	Show Tree Post-Order
		5 -	Show Tree In-Order 
		6 -	Exit 
		
		========================================

		Place the number of your choice: ''')
    
    def invalidChoice(self):
        print('''
                Invalid choice. Try again!''')
    
    def incorrectAnswer(self):
        print('''
                Incorrect answer. You need to place just numbers.''')


    def startMenu(self):
        options = {
            0: self.insert,
            1: self.delete,
            2: self.search,
            3: self.showTreePreOrder,
            4: self.showTreePostOrder,
            5: self.showTreeInOrder,
        }
        while True:
            try:
                choice = int(self.options())
                if 0 <= choice <= 5:
                    options.get(choice)()
                elif choice == 6:
                    break
                else:
                    self.invalidChoice()
            except:
                self.invalidChoice()
    
    def insert(self):
        while True:
            try:
                number = int(input('''
                Insert a number: '''))
                self.tree.insert(number)
                print("The tree:")
                self.tree.showTree(self.tree.getRoot())
                break
            except:
                self.incorrectAnswer()
    
    def delete(self):
        while True:
            try:
                number = int(input('''
                Insert a number to delete: '''))
                self.tree.remove(number)
                
                if self.tree.getRoot() != None:
                    print("The tree:")
                    self.tree.showTree(self.tree.getRoot())

                break
            except:
                self.incorrectAnswer()
    
    def search(self):
        while True:
            try:
                number = int(input('''
                Insert a number to find: '''))
                self.tree.search(number)
                break
            except:
                self.incorrectAnswer()
    
    def showTreePreOrder(self):
        self.tree.showTree(self.tree.getRoot())
    
    def showTreePostOrder(self):
        self.tree.showTreePostOrder(self.tree.getRoot())
    
    def showTreeInOrder(self):
        self.tree.showTreeInOrder(self.tree.getRoot())
    

            