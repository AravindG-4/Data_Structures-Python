class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self,level):
        current_lvl = self.get_level()
        if level >= current_lvl:
            spaces = ' ' * current_lvl * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.data)
            if self.children:
                for child in self.children:
                    child.print_tree(level)
                
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
def build_location_tree():
    root = TreeNode("Globe")                      #Root Node - level 0

    India = TreeNode("India")                     #level 1 Node - 1
    Gujarat = TreeNode("Gujarat")                 #level 2 Node(1) - 1
    Karnataka = TreeNode("Karnataka")             #level 2 Node(1) - 2
    
    India.add_child(Gujarat)
    India.add_child(Karnataka)

    USA = TreeNode("USA")                         #level 1 Node - 2
    New_Jersey = TreeNode("New Jersey")           #level 2 Node(2) - 1
    California = TreeNode("California")           #level 2 Node(2) - 2
    
    USA.add_child(New_Jersey)
    USA.add_child(California)
    
    #Creating LEAF NODES
    Gujarat.add_child(TreeNode("Ahmedabad"))
    Gujarat.add_child(TreeNode("Baroda"))
    
    Karnataka.add_child(TreeNode("Bangalore"))
    Karnataka.add_child(TreeNode("Mysore"))
    
    New_Jersey.add_child(TreeNode("Princeton"))
    New_Jersey.add_child(TreeNode("Trenton"))
    
    California.add_child(TreeNode("San Francisco"))
    California.add_child(TreeNode("Moutain view"))
    California.add_child(TreeNode("Palo Alto"))
    
    root.add_child(India)
    root.add_child(USA)

    root.print_tree(2)

if __name__ == '__main__':
    build_location_tree()