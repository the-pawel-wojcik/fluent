import unicodedata

name="Paweł Wójcik"

for letter in name:
    print(f"{letter}: {unicodedata.name(letter)}")


name_NFC = unicodedata.normalize('NFC', name)
name_NFD = unicodedata.normalize('NFD', name)
name_NFKC = unicodedata.normalize('NFKC', name)
name_NFKD = unicodedata.normalize('NFKD', name)

print("\n\n Normalized unicode")
print(f"{"name":>22}: {name.encode("utf-8")}")
print(f"{"normalized 'NFC' name":>22}: {name_NFC.encode("utf-8")}")
print(f"{"normalized 'NFKC' name":>22}: {name_NFKC.encode("utf-8")}")
print(f"{"normalized 'NFD' name":>22}: {name_NFD.encode("utf-8")}")
print(f"{"normalized 'NFKD' name":>22}: {name_NFKD.encode("utf-8")}")
