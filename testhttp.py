import logging
import sys
import requests
import json

from requests.exceptions import (
    SSLError,
    ConnectionError,
    HTTPError,
    InvalidSchema,
)

sut_url = "http://10.102.120.119:8080/is_ready"

sidecar_url = "http://10.102.120.119:8080/is_ready"
def is_system_live(URL):
    try:
       result = requests.get(
                url = URL,
                params = {},
            )

       print(
                f"Received while getting system state: {result}, "
                f"{result.text}"
            )
       return True

    except (SSLError, ConnectionError, HTTPError, InvalidSchema) as ex:
            print(f"Exception encountered while getting system state: {ex}")
            return False
	
result2 = is_system_live(sut_url)
print(f"The result is: {result2}")