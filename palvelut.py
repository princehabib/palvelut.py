import random
from typing import List


class Asiakas:
    __nimi: str
    __asiakasnro: List[int]
    __ika: int

    def __init__(self, nimi, ika) -> None:
        self.__nimi = nimi
        self.__ika = ika
        self.__luo_nro()

    @property
    def nimi(self):
        return self.__nimi

    @nimi.setter
    def nimi(self, nimi: str):
        if(nimi):
            self.__nimi = nimi
        else:
            raise Exception("Sorry, nimi is required!")

    @property
    def ika(self):
        return self.__ika

    @ika.setter
    def ika(self, ika: int):
        if(ika):
            self.__ika = ika
        else:
            raise Exception("Sorry, ika is required!")

    @property
    def asiakasnro(self):
        return f"{str(self.__asiakasnro[0:2])}-{self.__asiakasnro[2:5]}-{self.__asiakasnro[5:9]}"

    @asiakasnro.setter
    def asiakasnro(self, asiaksnro: list[int]):
        self.__asiakasnro = asiaksnro

    def _randfixed_digit(self, digits):
        return ''.join(["{}".format(random.randint(0, 9)) for num in range(0, digits)])

    def __luo_nro(self):
        self.__asiakasnro = [self._randfixed_digit(
            2), self._randfixed_digit(3), self._randfixed_digit(3)]


class Palvelu():
    tuotenimi: str
    __asiakkaat: List[Asiakas]

    def __init__(self, tuotenimi: str):
        super()
        self.tuotenimi = tuotenimi
        self.__asiakkaat = []

    def _luo_asiakarivi(self, asiakas: Asiakas) -> str:
        return asiakas.nimi

    def lisaa_asiakas(self, asiakas: Asiakas):
        if(asiakas):
            self.__asiakkaat.append(asiakas)
            return f"{asiakas.nimi} ({asiakas.asiakasnro}) is {asiakas.ika} years old"

        else:
            raise Exception("Sorry, client is required!")

    def poista_asiakas(self, asiakas: Asiakas):
        try:
            self.__asiakkaat.remove(asiakas)
        except:
            print("Client not found")
            pass

    def tulosta_asiakkaat(self):
        pass


class ParempiPalvelu(Palvelu):
    __edut: List[str]

    def __init__(self, tuotenimi):
        super(ParempiPalvelu, self).__init__(tuotenimi)
        self.__edut = []

    def lisaa_etu(self, a: str):
        if(a):
            self.__edut.append(a)
        else:
            raise Exception("Sorry, edut is required!")

    def poista_etu(self, a: str):
        try:
            self.__edut.remove(a)
        except:
            print("edut not found")
            pass

    def tulosta_edut(self):
        pass

# p1 = Asiakas("AHmad",24)
# # print(p1._luo_nro())

