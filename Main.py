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
        if topic not in self.broker:
            return "Очередь для этого пользователя не существует!"
        
        return consumer(self.broker, topic)
        
broker = Broker()

while(True):
        
    topic = int(input("Введите ID пользователя: \n"))
    
    choice = input("1 - consume 2 - produce \n")
       
    if choice == "1":
        print(broker.consume(topic))
        
    elif choice == "2":
        
        message = input("Email \n")
        
        broker.put(topic, message)


