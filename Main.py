import queue
from Producer import producer
from Consumer import consumer

broker = {}

userId = [0, 1, 2];
phoneNumber = ['8920', '112', '+7920']
email = ['geg@gmail.com', 'help@yandex.ru', 'i.ivanov@mail.ru']

for i in range(len(userId)):
    if userId[i] not in broker:
        broker[userId[i]] = queue.Queue()

for i in range(len(userId)): 
    print('Пользователь №', userId[i], ':')
    producer(broker, userId[i], phoneNumber[i])
    producer(broker, userId[i], email[i])
    print(consumer(broker, userId[i]))
    print(consumer(broker, userId[i]), '\n')


