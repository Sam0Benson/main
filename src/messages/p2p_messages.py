buy = """
Если вы уже покупали товар, то нажмите кнопку "Получить товар",
если нет, то нажмите на кнопку "Оплатить"
"""
wait_message = """
Вы не оплатили товар или оплата еще в пути!
"""
successful_payment = """
Большое спасибо за приобретение
"""

MESSAGES = {
    'successful_payment': successful_payment,
    'buy': buy,
    'wait_message': wait_message,
}