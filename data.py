from datetime import datetime, timedelta

# Тело запроса для создания нового заказа
order_body = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d"),  # Дата автоматически завтрашняя
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK"]
}