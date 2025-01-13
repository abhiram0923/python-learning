class Person:
  def __init__(self,fname,lname):
    self.fname = fname
    self.lname = lname

class Node:
  def __init__(self, person):
    self.data = person
    self.next = None

class LinkedList:
  def __init__(self):
    self.initialnode = None
    self.lastnode = None
    self.length = 0
  def add(self,node):
    if self.length == 0:
      self.initialnode = node
      self.lastnode = node
    else:
      self.lastnode.next = node
      self.lastnode = node
    self.length = self.length + 1
  def print(self):
    if self.length == 0:
      print("The list is empty.")
      return
    else:
      current_node = self.initialnode
      while current_node is not None:
        print("First Name: "  + current_node.data.fname)
        current_node = current_node.next
  def find(self,node):
    current_node = self.initialnode
    while current_node is not None:
      if current_node.data.fname == node.data.fname:
        return current_node
      else:
        current_node = current_node.next
    return None
  def delete(self,node):
    #Return quickly if list is empty.
    if self.length == 0:
      return None
    
    if self.initialnode.data.fname == node.data.fname:
      self.initialnode = self.initialnode.next
    else:
      previous_node = self.initialnode
      current_node  = self.initialnode.next
      while current_node is not None:
        if current_node.data.fname == node.data.fname:
          if current_node == self.lastnode:
            self.lastnode = previous_node
          
          previous_node.next = current_node.next
          self.length = self.length - 1
          return current_node
        else:
          previous_node = current_node
          current_node  = current_node.next
    return None
        


    

def main():
  linkedlist = LinkedList()
  person1 = Person("Abhiram","Janga")
  person2 = Person("Ravikanth","Janga")
  person3 = Person("Silpa","Akkina")
  linkedlist.add(Node(person1))
  linkedlist.add(Node(person2))
  linkedlist.add(Node(person3))
  person4 = Person("Neha","Akkina")
  node = linkedlist.find(Node(person4))
  if node is not None:
    print("Found: "+node.data.fname)
  else:
    print("Person not found")
  linkedlist.print()
  removed = linkedlist.delete(Node(person3))
  if removed is not None:
    print("Removed: "+removed.data.fname)
  else:
    print("Person not removed")
  linkedlist.print()
  linkedlist.add(Node(person4))
  linkedlist.print()
  

if __name__ == "__main__":
  main()
        
    
