# Функция для добавления данных в брокера
def producer(b, userId, mes):      
    return b[userId].put(mes) 
    
    
