#!/usr/bin/env python3

import requests

if __name__ == "__main__":

    resp = \
            requests.get(
                "http://files.vladstudio.com/joy/where_tahrs_live/wall/vladstudio_where_tahrs_live_2880x1800_signed.jpg")

    if resp.status_code == 200:

        print(resp.headers["Content-Length"])

        with open("test_normal.jpg", "wb") as f:

            f.write(resp.content)
