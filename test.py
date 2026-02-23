import sender_stand_request

# Абрамян, 40-ая когорта — Финальный проект. Инженер по тестированию плюс

def test_get_order_by_track():
    """Тест: проверка получения заказа по трек-номеру"""
    # Создаем заказ (подготовка данных)
    create_response = sender_stand_request.post_new_order()
    track = create_response.json()["track"]
    
    # Получаем заказ по треку
    get_response = sender_stand_request.get_orders_track(track)
    
    assert get_response.status_code == 200, f"Ожидался код 200, получен {get_response.status_code}"