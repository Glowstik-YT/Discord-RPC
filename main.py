from pypresence import Presence
import time

client_id = "application id here"
RPC = Presence(client_id)

RPC.connect()

RPC.update(
    state="Small Text",
    large_image="asset name here",
    buttons=[{"label": "Button Text","url": "Button Link"}]
        )

while True:
    time.sleep(60)
