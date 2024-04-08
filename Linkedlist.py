class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
class Linkedlist:
    
    def traverse (self):
        
        first = self.head
        while first:
            print(first.data)
            first = first.next
            
    def insert_at_beginning(self,new_node):
        new_data = Node(new_node)
        new_data.next = self.head
        self.head  = new_data
        
        
    def find(self,data):
        temp = self.head
        
        while temp is not None:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def delete_node(self,data):
        temp = self.head
        prev = None
        
        if temp is not None:
            if temp.data == data:
                if prev is not None:
                    prev.next = temp.next
                else:
                    self.head = temp.next
            else:
                prev = temp
                temp = temp.next
                
    
                    




        
    
            
            
family = Linkedlist()
family.head = Node('Lebone')
wife = Node('Ortega')
first_born = Node('Emily')
sec_born = Node('David')


family.head.next = wife
wife.next = first_born
first_born.next = sec_born
            
    
family.traverse()
family.insert_at_beginning('Gabriel')
family.traverse()
print(family.find('dan'))
print("")
family.delete_node('Gabriel')
family.traverse()