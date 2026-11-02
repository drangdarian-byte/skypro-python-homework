from address import Address
from mailing import Mailing


from_address = Address("443001", "Самара", "Ленинская", "10", "5")
to_address = Address("101000", "Москва", "Мясницкая", "20", "12")
mailing = Mailing(to_address, from_address, 350, "RU123456789")

sender = mailing.from_address
recipient = mailing.to_address

print(
    f"Отправление {mailing.track} из "
    f"{sender.index}, {sender.city}, {sender.street}, "
    f"{sender.house} - {sender.apartment} в "
    f"{recipient.index}, {recipient.city}, {recipient.street}, "
    f"{recipient.house} - {recipient.apartment}. "
    f"Стоимость {mailing.cost} рублей."
)
