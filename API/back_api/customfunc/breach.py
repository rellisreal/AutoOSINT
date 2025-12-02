import http.client
import os
import urllib.parse

from dotenv import load_dotenv

# Refernce : https://breachdirectory.com/api_documentation
# ToDO: Accept API from Database & Pass data back into database

load_dotenv()


class BreachAPI:
    def __init__(self, target_email):
        self.url = "breachdirectory.p.rapidapi.com"
        self.api = os.getenv("BREACH_DIRECTORY_API")
        self.target = target_email

    def getBreachData(self):
        self.constructConnection()
        self.constructHeader()
        self.sendRequest()
        return self.readResponse()

    def constructConnection(self):
        self.conn = http.client.HTTPSConnection(self.url)

    def constructHeader(self):
        self.headers = {
            "x-rapidapi-key": self.api,
            "x-rapidapi-host": self.url,
            "User-Agent": "Python",
        }

    def sendRequest(self):
        self.conn.request(
            "GET", f"/?func=auto&term={self.target}", body=None, headers=self.headers
        )
        self.res = self.conn.getresponse()
        if self.res.status in (301, 302, 303, 304, 306, 307, 308):
            self.handleRedirect()

    def handleRedirect(self):
        redirect_url = dict(self.res.getheaders()).get("Location")
        self.url = urllib.parse.urlsplit(redirect_url).netloc
        self.path = urllib.parse.urlsplit(redirect_url).path
        self.query = urllib.parse.urlsplit(redirect_url).query
        self.constructConnection()
        self.conn.request("GET", self.path + ("?" + self.query), headers=self.headers)
        self.res = self.conn.getresponse()

    def readResponse(self):
        data = self.res.read()
        return data.decode("utf-8")
