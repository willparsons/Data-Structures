from bst import BST

if __name__ == "__main__":
    tree = BST(10)
    tree.insert(5)
    tree.insert(15)
    
    tree.preOrder()
    print()
    tree.inOrder()
    