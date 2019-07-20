class Color:
    def __init__(self, red: int = 0, green: int = 0, blue: int = 0, hexa: str = None):
        self._hex: str = ""
        if hexa is None:
            red = ('0' if red < 16 else "") + hex(red).split("x")[1]
            green = ('0' if green < 16 else "") + hex(green).split("x")[1]
            blue = ('0' if blue < 16 else "") + hex(blue).split("x")[1]
            self._hex = f"#{red}{green}{blue}"
        else:
            if hexa[0] == '#':
                self._hex = hexa
            elif hexa == "white":
                self.__init__(255, 255, 255)
            elif hexa == "black":
                self.__init__(0, 0, 0)
            elif hexa == "red":
                self.__init__(255, 0, 0)
            elif hexa == "green":
                self.__init__(0, 255, 0)
            elif hexa == "blue":
                self.__init__(0, 0, 255)

    def hex(self):
        return self._hex

    def color(self):
        return self._hex

    def __repr__(self):
        return self._hex
