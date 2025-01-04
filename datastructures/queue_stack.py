class Queue:
  def __init__(self):
    self.queue_list = []
    self.queue_length = 0
  def enqueue(self,data):
    self.queue_list.append(data)
    self.queue_length = self.queue_length + 1
    return True
  def dequeue(self):
    if self.queue_length == 0:
      return None
    data = self.queue_list.pop(0)
    self.queue_length = self.queue_length - 1
    return data
  def length(self):
    return self.queue_length
  def isempty(self):
    return self.queue_length == 0
class Stack:
  def __init__(self):
    self.stack_list = []
    self.stack_length = 0
  def push(self,data):
    self.stack_list.append(data)
    self.stack_length = self.stack_length + 1
    return True
  def pop(self):
    if self.stack_length == 0:
      return None
    data = self.stack_list.pop(self.stack_length - 1)
    self.stack_length = self.stack_length - 1
    return data
  def length(self):
    return self.stack_length
  def isempty(self):
    return self.stack_length == 0
    
def main():
  print("Define a Queue")
  MyQueue = Queue()
  MyQueue.enqueue(100)
  MyQueue.enqueue(200)
  print(MyQueue.length())
  data = MyQueue.dequeue()
  print(MyQueue.length())
  print(data)

def main1():
  print("Define a Stack")
  mystack = Stack()
  mystack.push(100)
  mystack.push(200)
  mystack.push(900)
  print(mystack.length())
  data = mystack.pop()
  print(mystack.length())
  print(data)
  data = mystack.pop()
  print(mystack.length())
  print(data)
  data = mystack.pop()
  print(mystack.length())
  print(data)
  data = mystack.pop()
  print(mystack.length())
  print(data)


if __name__ == "__main__":
  main1()
