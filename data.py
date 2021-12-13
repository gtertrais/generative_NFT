
import json

datas = [{
    "id": 43,
    "fond": "Blanc",
    "œil": "Monocle",
    "chapeau": "Royal",
    "bouche": "Gustave Eiffel",
    "mouche": "Mouche"
},
    {
    "id": 44,
    "fond": "Blanc",
    "œil": "none",
    "chapeau": "Gaulois",
        "bouche": "Mousquetaire",
        "mouche": "none"
}]

linkImage = 'https://gateway.pinata.cloud/ipfs/QmVtf1Z2kd2XLmGK6oTYeoXG7nHackumJ5p4PknvoGWLzK/'

for data in datas:
    input = {"id": str(data["id"]),
             "name": "#" + str(data["id"]) + " Logo Gaspard & Joseph",
             "description": "Notre premier drop NFT",
             "image": linkImage + str(data["id"]),
             "external_url": "https://gaspardetjoseph.fr",
             "editor": "Gaspard & Joseph",
             "type": "Logo",
             "domain": "Art",
             "collection": "Gaspard & Joseph",
             "rarity": "Unique",
             "creator": "Gaspard & Joseph",
             "season": "Season 1",
             "bonus_property_1": "Whitelist pour les drops suivants",
             "bonus_property_1": "Drops exclusifs",
             "bouche": data["bouche"],
             "chapeau": data["chapeau"],
             "œil": (data["œil"], "")[data["œil"]!= ""],
             "mouche": (data["mouche"], "")[data["mouche"]!= ""]
             }
    print(input)
