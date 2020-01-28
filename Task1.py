class Marker:
    color = None
    _capacity = 200

    def show(self, str):
        if self._capacity != 0:
            i = 0
            while (self._capacity != 0) and (i < len(str)):
                print(str[i], end="")
                if str[i] != ' ':
                    self._capacity -= 1
                i += 1
            print(" ")
        else:
            print("Нет чернил")

class Reload_Marker(Marker):
    def fill(self):
        self._capacity = 200






m2 = Reload_Marker()
m2.show("123456")
m2.show("78910")
m2.show("123456")
m2.fill()
m2.show("123456")


m = Marker()
m.show("  12")
m.show("3 4")
m.show("12345678 9 10 11 ")
m.show("AA")