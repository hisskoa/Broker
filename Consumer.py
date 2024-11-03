# Функция для извлечения данных из брокера
def consumer(b, userId):
    if not b[userId].empty():        
        return b[userId].get()
    else:
        print("Очередь пуста!")
    
    