data_panen = {
    "lokasi1": {
        "nama_lokasi": "kebun A",
        "hasil_panen": {"padi": 1200, "jagung": 800, "kedelai": 500},
    },
    "lokasi2": {
        "nama_lokasi": "kebun B",
        "hasil_panen": {"padi": 1500, "jagung": 900, "kedelai": 450},
    },
    "lokasi3": {
        "nama_lokasi": "kebun C",
        "hasil_panen": {"padi": 1100, "jagung": 750, "kedelai": 600},
    },
    "lokasi4": {
        "nama_lokasi": "kebun D",
        "hasil_panen": {"padi": 1300, "jagung": 850, "kedelai": 550},
    },
    "lokasi5": {
        "nama_lokasi": "kebun E",
        "hasil_panen": {"padi": 1400, "jagung": 950, "kedelai": 480},
    },
}

for i, j in data_panen.items():
    print(f"{i}")
    print(f"nama lokasi : {j['nama_lokasi']}")
    print(f"hasil panen padi: {j['hasil_panen']['padi']}")
    print(f"hasil panen jagung: {j['hasil_panen']['jagung']}")
    print(f"hasil panen kedelai: {j['hasil_panen']['kedelai']}")

hasil_jagung2 = data_panen["lokasi2"]["hasil_panen"]["jagung"]
print(f"hasil panen jagung lokasi2: {hasil_jagung2}")

nama_lokasi3 = data_panen["lokasi3"]["nama_lokasi"]
print(f"nama lokasi 3 : {nama_lokasi3}")

padi = []
kedelai = []
for i, j in data_panen.items():
    padi.append(j["hasil_panen"]["padi"])
    kedelai.append(j["hasil_panen"]["kedelai"])
print(f"data hasil panen padi: {padi}")
print(f"data hasil panen kedelai: {kedelai}")

for i in range(5):
    print(f"hasil panen padi lokasi {i+1} :{padi[i]}")
    print(f"hasil panen kedelai lokasi {i+1}: {kedelai[i]}")

for i, j in data_panen.items():
    padi = j["hasil_panen"]["padi"]
    jagung = j["hasil_panen"]["jagung"]
    if padi > 1300 or jagung > 800:
        print(f"{i} perlu perhatian khusus")
    else:
        print(f"{i} dalam kondisi baik")

# coba
