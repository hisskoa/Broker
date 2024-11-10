import queue
from Producer import producer
from Consumer import consumer

class Broker:

    def __init__(self):
        self.broker = {}
        
    def put(self, topic, message):
        if topic not in self.broker:
            self.broker[topic] = queue.Queue()
            
        producer(self.broker, topic, message)    
                    
    def consume(self, topic): 
        return consumer(self.broker, topic)
        
broker = Broker()

while(True):
    
    userInput = input("1 - consume/2 - produce, Email/Phone number, Value: \n")
    
    choice, topic, *message = userInput.split()
    message = message[0] if message else None
       
    if choice == "1":
        print(broker.consume(topic))
        
    elif choice == "2":       
        broker.put(topic, message)


