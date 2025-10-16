from message import Message
class Person:
    def __init__(self, name):
        self.__name = name
        self.__inbox = []
        self.__sent = []

    def get_name(self):
        return self.__name
    
    def send_message(self, receiver, content):
        # create an object of Message class
        msg = Message(self.__name, receiver.get_name(), content)
        receiver.receive_message(msg)   # deliver the message to receiver
        self.__sent.append(msg)         # save the sent message in sent box

    def receive_message(self, message):
        self.__inbox.append(message)    # save the received message in inbox

    def show_inbox(self):
        print(f"Inbox of {self.__name}:")
        for msg in self.__inbox:
            print(msg)

    def show_sent(self):
        print(f"Sent messages of {self.__name}:")
        for msg in self.__sent:
            print(msg)

if __name__ == "__main__":
    a = Person("Alice")
    b = Person("Bob")
    c = Person("Mike")

    a.send_message(b, "Hi Bob! Are you going to Mike's birthday?")
    b.send_message(a, "Yes! See you there!")
    a.send_message(b, "Can you give me a ride? I don't have a car.")
    b.send_message(a, "Sure, I can pick you up!")
    a.send_message(c, "I can go — Bob’s giving me a lift.")
    c.send_message(a, "Fantastic!")

    a.show_inbox()
    b.show_inbox()
    c.show_inbox()

    a.show_sent()