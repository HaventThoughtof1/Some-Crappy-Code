import faker

f = faker.Faker()
p = f.simple_profile()
print(f'NAME: {p["name"]}'
      f'\nEMAIL: {p["mail"]}'
      f'\nADDRESS: {p["address"]}'
      f'\nBIRTHDATE: {p["birthdate"]}'
      f'\nSEX: {"Male"if p["sex"] == "M" else "Female"}')
