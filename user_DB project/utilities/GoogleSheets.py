import requests


class Client:

    def __init__(self):
        pass

    def reading_data(self, sheet, range_term):
        self.end_point = "https://sheets.googleapis.com/v4/spreadsheets/"
        self.key = "AIzaSyDDeOBJwKD1do-ZoZtheo4TtnckuNvtFFE"
        self.sheet_id = "1vyRZ2pv2Wg0rSZmVBwJsy4aH4m4Icyb1Msi1X5NZBcs"
        self.data = requests.get(
            f"{self.end_point}{self.sheet_id}/values/{sheet}!A1:{range_term}?key={self.key}").json()
        self.parsed_data = {}

        rows = self.data['values']
        for row in rows:
            if rows.index(row) == 0:
                rows[rows.index(row)].pop(0)
                continue
            currentID = row.pop(0)
            self.parsed_data[currentID] = dict(zip(rows[0], row))

            # {
            #     'id1': {
            #         'header1' : 'value1'
            #         'header2' : 'value2'
            #     },
            #     'id2': {
            #         'header1' : 'value1'
            #         'header2' : 'value2'
            #     }
            # }

    def Adding_new_data(self, sheet, data_lists):
        self.data_dictionary = {"range": f"{sheet}!A2:E2",
                                "majorDimension": "ROWS",
                                "values": [data_lists],
                                }
        # self.token = requests.post("https://accounts.google.com/o/oauth2/auth?"
        self.end_point = "https://sheets.googleapis.com/v4/spreadsheets/"
        self.key = "AIzaSyDDeOBJwKD1do-ZoZtheo4TtnckuNvtFFE"
        self.sheet_id = "1vyRZ2pv2Wg0rSZmVBwJsy4aH4m4Icyb1Msi1X5NZBcs"
        self.data = requests.put(
            f"{self.end_point}{self.sheet_id}/values/{sheet}!A1:E1?key={self.key}", data=self.data_dictionary).json()


gs = Client()
gs.Adding_new_data("users", [1006, 21, 22, 23, 24])
print(gs.data)
# gs.reading_data("users", "D5")
# print(gs.parsed_data)


# client ID: 930374724466-ofi8ca9fl70ujtjrug07busejkbs9qag.apps.googleusercontent.com
# client secret: 8O8adrt0A_1qznAQ5uYWddTk
