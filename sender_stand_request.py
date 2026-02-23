import configuration
import requests
import data

def post_new_order():
    """Отправка POST-запроса на создание нового заказа"""
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
        json=data.order_body
    )

def get_orders_track(track_id):
    """Отправка GET-запроса для получения заказа по трек-номеру"""
    return requests.get(
        configuration.URL_SERVICE + configuration.RECEIVING_ORDER_BY_ID,
        params={"t": track_id}  # Более правильный способ передачи параметров
    )