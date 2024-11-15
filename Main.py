class My_Stack:                 # LIFO — Last In First Out («последним пришел, первым ушел»).
    def __init__(self):
        self.stack = []
        
    def push(self, item):          # Добавить элемент на вершину стека
        self.stack.append(item)
        
    def pop(self):              # Достать самый верхний элемент стека
        return self.stack.pop()
        
class Queue:                    # FIFO - First In First Out («первым пришёл — первым ушёл»)
    def __init__(self):
        self.s1 = My_Stack()
        self.s2 = My_Stack()
        
    def push(self, x):          # Добавить элемент в конец очереди
        self.s1.push(x)
        
    def pop(self):              # Достать элемент из начала очереди
        if not self.s2.stack:
            if not self.s1.stack:
                print("Error!")
            while self.s1.stack:
                self.s2.push(self.s1.pop())
        return self.s2.pop() if self.s2.stack else None
    
class Broker:
    def __init__(self):
        self.broker = {}
        
    def put(self, topic, message):      # Добавить в брокера
        if topic not in self.broker:
            self.broker[topic] = Queue()              
        return self.broker[topic].push(message)     
                    
    def consume(self, topic):           # Достать из брокера       
        return self.broker[topic].pop()            

broker = Broker()

while(True):
    
    userInput = input("1 - consume/2 - produce, Email/Phone number, Value: \n")
    
    choice, topic, *message = userInput.split()
    message = message[0] if message else None
       
    if choice == "1":
        print(broker.consume(topic))
        
    elif choice == "2":       
        broker.put(topic, message)


