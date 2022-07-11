from Tree import Tree

## Creating a Tree instance
tree = Tree()

## Test remove when the tree is empty
print('## Test remove when the tree is empty')
tree.remove(10)
print('\n')

## Test find an element when the tree is empty
print('## Test find an element when the tree is empty')
tree.search(100)
print('\n')

## Test insert element duplicated
print('## Test insert element duplicated')
tree.insert(10)
tree.insert(10)
print('Tree:')
tree.showTree(tree.getRoot())
print('\n')

## Test insert
print('## Test insert elements')
tree.insert(5)
tree.insert(4)
tree.insert(6)
tree.insert(4)
tree.insert(15)
tree.insert(25)
tree.insert(2)
tree.insert(28)
tree.insert(13)
tree.insert(14)
print('Tree:')
tree.showTree(tree.getRoot())
print('\n')

## Test remove when node is not found
print('## Test remove when node is not found')
tree.remove(220)
print('Tree:')
tree.showTree(tree.getRoot())
print('\n')

## Test remove when the node doesn't have children
print("## Test remove when the node doesn't have children")
print('# Remove 6')
tree.remove(6)
tree.showTree(tree.getRoot())
print('\n')
print('# Remove 28')
tree.remove(28)
tree.showTree(tree.getRoot())
print('\n')

## Test remove when the node has just one child
print("## Test remove when the node has just one child")
print('# Remove 4')
tree.remove(4)
tree.showTree(tree.getRoot())
print('\n')
print('# Remove 13')
tree.remove(13)
tree.showTree(tree.getRoot())
print('\n')

## Test remove when the node has 2 children
print("## Test remove when the node has 2 children")
print('# Remove 15')
tree.remove(15)
tree.showTree(tree.getRoot())
print('\n')

## Test to find an element that doesn't exist
print("## Test to find an element that doesn't exist")
print('# Find 150')
tree.search(150)
print('\n')

## Test to find an element that exists
print("## Test to find an element that exists")
print('# Find 2')
tree.search(2)
print('\n')

# print('======= Pre Order: Root, Left, Right ======')
print("======= Pre Order: Root, Left, Right ======")
tree.showTree(tree.getRoot())
print('\n')

# print('======= Post Order: Left, Right, Root ======')
print("======= Post Order: Left, Right, Root ======")
tree.showTreePostOrder(tree.getRoot())
print('\n')

# print('======= In Order: Left, Root, Right ======')
print("======= In Order: Left, Root, Right ======")
tree.showTreeInOrder(tree.getRoot())
print('\n')

# print node journey in Pre Order
print("======= Node Journey Pre Order: Root, Left, Right ======")
tree.printShowTree(tree.getRoot(), None)
print('\n')

# print node journey in Post Order
print("======= Node Journey Post Order: Left, Right, Root ======")
tree.printShowTreePostOrder(tree.getRoot(), None)
print('\n')





