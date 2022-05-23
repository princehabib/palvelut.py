import random
from typing import List


class Asiakas:
    __nimi: str
    __asiakasnro: List[int]
    __ika: int

    def __init__(self, nimi, age) -> None:
        self.__nimi = nimi
        self.__age = age
        self.__luo_nro()

    def set_nimi(self, nimi):
        if nimi == False:
            raise ValueError("Give a new name")
        if nimi == True:
            self_nimi = nimi

    def get_nimi(self):
        return self.__nimi
    
    def set_age(self,newage):
        if newage == False:
            raise ValueError("Give a new age")
        if newage == True:
            self.__age = newage

    def get_age(self):
        return self.__age
        
    def get_asiakasnro(self):
        return f"{str(self.__asiakasnro[0:2])}-{self.__asiakasnro[2:5]}-{self.__asiakasnro[5:9]}"

    def _randfixed_digit(self, digits):
        return ''.join(["{}".format(random.randint(0, 9)) for num in range(0, digits)])

    def __luo_nro(self):
        self.__asiakasnro = [self._randfixed_digit(
            2), self._randfixed_digit(3), self._randfixed_digit(3)]


class Palvelu():
    tuotenimi: str
    __asiakkaat: List[Asiakas]

    def __init__(self, tuotenimi: str):
        self.tuotenimi = tuotenimi
        self.__asiakkaat = []

    def _luo_asiakasrivi(self, asiakas: Asiakas) -> str:
        text = f"{asiakas.get_nimi()} {asiakas.get_asiakasnro()} on {asiakas.get_age()}-vuotias"
        print(text)

    def lisaa_asiakas(self, asiakas: Asiakas):
        if(asiakas == False):
            raise ValueError("Sorry, client is required!")
        else:
            self.__asiakkaat.append(asiakas)
            

    def poista_asiakas(self, asiakas: Asiakas):
        try:
            if asiakas == False:
                raise ValueError("Sorry, client is required!")
            else:
                self.__asiakkaat.remove(asiakas)
        except:
            pass

    def tulosta_asiakkaat(self):
        for asiakas in self.__asiakkaat:
            self._luo_asiakasrivi(asiakas)


class ParempiPalvelu(Palvelu):
    __edut: List[str]

    def __init__(self, tuotenimi):
        super().__init__(tuotenimi)
        self.__edut = []

    def lisaa_etu(self, a: str):
        if(a):
            self.__edut.append(a)
        else:
            raise Exception("Sorry, edut is required!")

    def poista_etu(self, a: str):
        try:
            if a == False:
                raise ValueError("Sorry, edut is required!")
            else:
                self.__edut.remove(a)
        except:
            pass

    def tulosta_edut(self):
        for etu in self.__edut:
            print(etu)

# p1 = Asiakas("Habib",18)
# # print(p1._luo_nro())
