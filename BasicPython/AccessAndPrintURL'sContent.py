
import requests as req

resp = req.get("http://www.facebook.com")

print(resp.text)