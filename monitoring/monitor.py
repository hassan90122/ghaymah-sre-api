import requests
import time
from datetime import datetime


URL = "https://ghaymah-sre-api-20e343cababc.hosted.ghaymah.systems/health"


while True:

    try:
        start = time.time()

        response = requests.get(URL)

        end = time.time()

        response_time = round(end - start, 3)


        if response.status_code == 200:

            print(
                datetime.now(),
                "UP",
                "Response time:",
                response_time,
                "seconds"
            )

        else:

            print(
                datetime.now(),
                "DOWN",
                response.status_code
            )


    except Exception as e:

        print(
            datetime.now(),
            "ERROR",
            e
        )


    time.sleep(30)
