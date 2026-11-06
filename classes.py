class YouTubeChannel:

    def __init__(self,name):
        self.name = name
        self.subscribers = 0

    def subscribe(self):
        self.subscribers += 1
        print(f"Thanks for subscribing! Total: {self.subscribers}")

    def unsubscribe(self):
        if self.subscribers > 1:
            self.subscribers -= 1
            print(f"Total: {self.subscribers}")

    def show(self):
        print(f"{self.name} has {self.subscribers} subscribers")


codebasics = YouTubeChannel("codebasics")
codepython = YouTubeChannel("codepython")

codebasics.subscribe()
codebasics.subscribe()
codebasics.subscribe()

codepython.subscribe()
codepython.subscribe()
codepython.unsubscribe()
codepython.show()

codebasics.unsubscribe()
codebasics.show()