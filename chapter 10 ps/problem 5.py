from random import randint

class Train:
    TrainNo = 13287
    def __init__(self, TrainNo):
        self.TrainNo = TrainNo
    def book(self, fro, to):
        print(f"The Train is booked in Train No. {self.TrainNo} from {fro} to {to}")
    def status(self):
        print(f"The Train No. {self.TrainNo} is running on time.")
    def fare(self, fro, to):
        print(f"The fare of the Train No. {self.TrainNo} from {fro} to {to} is {randint(1000, 4000)}")

object = Train(13288)
object.book("Patna", "Durg")
object.status()
object.fare("Patna", "Durg")

