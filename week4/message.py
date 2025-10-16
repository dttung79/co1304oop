class Message:
    def __init__(self, sender, receiver, content):
        self.__sender = sender
        self.__receiver = receiver
        self.__content = content

    def get_sender(self):
        return self.__sender

    def get_receiver(self):
        return self.__receiver

    def get_content(self):
        return self.__content
    
    def __str__(self):
        return f'{self.__sender} -> {self.__receiver}: {self.__content}'
    
if __name__ == "__main__":
    msg = Message("Alice", "Bob", "Hello, Bob!")
    print(msg)