class TreeNode:
    def __init__(self,name,designation):
        self.data = {'name':name, 'designation':designation}
        self.children = []
        self.parent = None
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+=1
            p = p.parent
        return level
    
    def print_tree(self,wanted):
        level = self.get_level() 
        prefix = (" " * level * 3) + '|__' if level else ''
        if wanted == 'name' or wanted == 'designation':
            print(prefix + self.data[wanted])
        else:
            print(prefix + self.data['name'],f"  ({self.data['designation']})")
            
        if self.children:
            for child in self.children:
                child.print_tree(wanted)
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
        
    
def build_management_tree():
    root = TreeNode('Nilupul','CEO')                       #Root Node - level 0

    Chinmay = TreeNode("Chinmay",'CTO')                    #level 1 Node - 1
    Vishwa = TreeNode("Vishwa",'Infrastructure Head')      #level 2 Node(1) - 1
    Aamir = TreeNode("Aamir",'Application Head')           #level 2 Node(1) - 2
    
    Chinmay.add_child(Vishwa)
    Chinmay.add_child(Aamir)

    Gels = TreeNode("Gels",'HR Head')                      #level 1 Node - 2
    Peter = TreeNode("Peter",'Recruitment Manager')        #level 2 Node(2) - 1
    Waqas = TreeNode("Waqas",'Policy Manager')             #level 2 Node(2) - 2
    
    Gels.add_child(Peter)
    Gels.add_child(Waqas)
    
    #Creating LEAF NODES
    Vishwa.add_child(TreeNode("Dhaval",'Cloud Manager'))
    Vishwa.add_child(TreeNode("Abhijith","App Manager"))

    root.add_child(Chinmay)
    root.add_child(Gels)

    root.print_tree('')
    
if __name__ == '__main__':
    build_management_tree()