from abc import ABC, abstractmethod


class MailingList:

    def __init__(self, name):
        self.name = name
        self.members = []

    def subscribe(self, user):
        self.members.append(user)

    def notify(self, event):
        for member in self.members:
            member.sendNotification(self.name, event)


class MailingListSubscriber(ABC):

    @abstractmethod
    def sendNotification(self, event):
        pass


class MailingListUser(MailingListSubscriber):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def sendNotification(self, mailing_list, event):
        print(f'{mailing_list} has sent message {event} to recipient {self.name}')


if __name__ == '__main__':
    m1 = MailingList("Monk's cafe")
    m2 = MailingList("United Airlines")
    u1 = MailingListUser('Jerry Seinfeld')
    u2 = MailingListUser('George Costanza')
    u3 = MailingListUser('Elaine Bennes')
    u4 = MailingListUser('Cosmo Kramer')
    m1.subscribe(u1)
    m1.subscribe(u2)
    m1.subscribe(u3)
    m1.subscribe(u4)
    m2.subscribe(u1)
    m2.subscribe(u3)
    m1.notify('Get food on July 5th weekend with coupon jul20 for 20% off')
    m2.notify('New flights from New York to Los Angeles')
