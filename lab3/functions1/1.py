def grams_to_ounces(grams):
    return grams * 0.03527396195

grams = 100
ounces = grams_to_ounces(grams)
print(f"{grams} граммов = {ounces:.2f} унций")
