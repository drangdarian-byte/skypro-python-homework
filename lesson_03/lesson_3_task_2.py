from smartphone import Smartphone


catalog = [
    Smartphone("Samsung", "Galaxy S24", "+79000000001"),
    Smartphone("Apple", "iPhone 15", "+79000000002"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79000000003"),
    Smartphone("Google", "Pixel 8", "+79000000004"),
    Smartphone("Honor", "Magic6", "+79000000005"),
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
