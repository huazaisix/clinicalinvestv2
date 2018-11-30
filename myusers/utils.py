import requests
import json

from django.conf import settings


def get_user_token(user_data):

    url = settings.REQUEST_URL

    my_dict = {
        "grant_type": settings.GRANT_TYPE,
        "client_id": settings.CLIENT_ID,
        "username": user_data.get("email"),
        "password": user_data.get("password")
    }

    try:
        r = requests.post(url, data=my_dict)
    except Exception as e:

        raise e

    data = r.content.decode()

    d = json.loads(data)

    # print(d)

    token = d.get("access_token", None)

    return token

