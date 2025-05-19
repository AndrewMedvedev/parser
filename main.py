import asyncio
import time

from schedule import every, run_pending

from parse import send_data


def job() -> None:
    return asyncio.run(send_data())


every(1).hours.do(job)

while True:
    run_pending()
    time.sleep(1)
