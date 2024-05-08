# Kursinis darbas
Programa automobilių parkavimo valdymui Python: informacinės sistemos kūrimas ir naudojimas automobilių pridėjimui ir šalinimui

## Paruošė:
Igor Gavrylyuk EDIF23/1

# Įvadas
Šiuolaikiniame pasaulyje automobilių stovėjimo vietų valdymas tampa vis svarbesne užduotimi, atsižvelgiant į didėjantį transporto priemonių skaičių miestuose. Šio kursinio darbo tikslas - „Python“ programavimo kalba sukurti informacinę sistemą, kuri leistų valdyti automobilių pridavimo ir pašalinimo iš stovėjimo aikštelės procesą, taip pat stebėti stovėjimo vietų užimtumo būklę. Sukurtoje programoje numatyta tekstinė sąveikos su vartotoju (naudojant terminalą) sąsaja ir ji įgyvendinta taikant objektinio programavimo principus.
Norint paleisti taikomąją programą, reikia paleisti failą „main.py“, kuriuo paleidžiamas pagrindinis taikomosios programos meniu ir pateikiamos navigacijos parinktys, skirtos įvairioms automobilių stovėjimo vietų valdymo funkcijoms. Pagrindinės naudotojui prieinamos operacijos yra automobilių stovėjimo vietų, kuriose laikomi automobiliai, sukūrimas, naujų automobilių pridėjimas į stovėjimo vietą, automobilių pašalinimas iš stovėjimo vietos ir esamos užimtų ir laisvų vietų būklės peržiūra, taip pat įgyvendinta automobilio paieška pagal valstybinį numerį ir kitos funkcijos. Programa skirta naudoti mažose ir vidutinio dydžio automobilių stovėjimo aikštelėse. 
# Pagrindinė dalis
Siekiant įgyvendinti programos „Programa automobilių parkavimo valdymui Python: informacinės sistemos kūrimas ir naudojimas automobilių pridėjimui ir šalinimui“ funkcinius reikalavimus, buvo suprojektuoti ir įgyvendinti pagrindiniai komponentai ir funkcijos. Programa sukurta taip, kad būtų galima lengvai tvarkyti automobilių stovėjimo vietų ir automobilių duomenis, suteikiant naudotojams galimybę pridėti, ištrinti ir peržiūrėti automobilius per terminalą. Programa suskirstyta į keletą failų, kad būtų lengviau suprasti programos kodą. 
## Pagrindinių programos modulių aprašymas
### Modulio „main.py“aprašymas 
„main.py“ - šis failas yra pagrindinis visos programos modulis. Jame yra klase „main_menu()“, kuri iškviečia pagrindinį programos meniu, kurio pagalba galima iškviesti kitas funkcijas. Meniu įgyvendinamas naudojant ciklą „while“ ir operatorių „if“. Visos funkcijos įgyvendintos kitame modulyje (faile), kad būtų lengviau rašyti kodą, įgyvendinti naujus metodus arba suprasti, kaip parašyta programa. Kad būtų galima iškviesti funkcijas iš failo „main_menu_functions.py“, faile „main.py“ sukurti du objektai „main_menu_methods“, taip pat dar vienas objektas „parking_menu_open“, kuris reikalingas norint iškviesti funkciją iš kito failo „car_manager.py“, ši funkcija leidžia pasirinkti automobilių stovėjimo aikštelę ir pereiti į sąveikos su automobilių stovėjimo aikštele meniu.


Funkcijų sąrašas:
1.	Sukurti naują automobilių stovėjimo aikštelę. (Iškviečiama funkcija „create_parking()“, kuri paprašo naudotojo įrašyti parkingo pavadinimą ir sukuria aplanke nurodytą pavadinimą, taip pat patikrina, ar yra parkingas panašiu pavadinimu, jei ne, sukuriamas aplankas, jei taip, programa parodo klaidą ir parašo, kad toks parkingas jau egzistuoja. Be to, jei programa paleidžiama pirmą kartą, sukuriamas aplankas pavadinimu „parkings“ (jame saugomos visos parkavimo vietos, kurios bus sukurtos arba jau sukurtos).
2.	Pasirinkti parkingą. (Šiuo punktu iškviečiamas metodas „select_parking(self)“, kuris klausia naudotojo pavadinimo, tada ieško, ar nurodyta stovėjimo aikštelė egzistuoja, jei taip, naudotojui atveriamas kitas meniu, kad jis galėtų bendrauti su nurodyta stovėjimo aikštele, jei ne, programa pateikia klaidą ir rašo, kad stovėjimo aikštelė su nurodytu pavadinimu neegzistuoja).
3.	Visų stovėjimo aikštelių sąrašas (ši parinktis iškviečia funkciją „list_parkings(self)“, kuri parodo visas jau sukurtas automobilių stovėjimo aikšteles ir kiek jose yra automobilių).
4.	Ištrinti automobilių stovėjimo aikštelę (šia parinktimi iškviečiama funkcija „delete_parking(self)“, kuri patikrina, ar egzistuoja nurodyto pavadinimo automobilių stovėjimo aikštelė, ir jei taip, ištrina šios aikštelės aplanką).
5.	Ieškoti automobilio pagal valstybinį numerį (šia parinktimi iškviečiama funkcija „search_car(self)“, kuri visose stovėjimo aikštelėse ieško automobilio pagal valstybinį numerį. Jei pavyks, programa parodys automobilio valstybinį numerį, jo markę ir kurioje stovėjimo aikštelėje jis šiuo metu yra).
6.	Programos užbaigimas (ši parinktis tiesiog naudoja komandą „break“, kad išeitų iš ciklo ir programa būtų išjungta).
Taip pat svarbu paminėti, kad jei bandysite įrašyti bet kokią kitą reikšmę, nesusijusią su meniu (skaitmenys nuo 1 iki 6), programa parašys, kad tokios parinkties nėra, ir paprašys dar kartą įvesti reikšmę.
### Modulio aprašymas „main_menu_functions.py“
Šiame modulyje yra funkcijų, kurios naudojamos pagrindiniame meniu. Pagrindinio meniu funkcijų sąraše aprašiau, ką jos daro, todėl čia parašysiu trumpesnį variantą. Metodų sąrašas:
„create_parkings()“ - sukuria aplanką (parkings) su vartotojo nurodytu pavadinimu. 
„select_parking()“ - Atlieka pavadinimo paiešką ir atidaro sąveikos meniu su naudotojo nurodytu pavadinimu.
„list_parkings()“ - pateikia visų esamų stovėjimo aikštelių sąrašą ir jų užimtumą automobiliais.
„delete_parking()“ - ištrina aplanką (automobilių stovėjimo aikštelę) su naudotojo nurodytu pavadinimu.
„search_car()“ - Ieško automobilio, parodo, kurioje aikštelėje jis yra, su naudotojo nurodytu pavadinimu.
### Modulio aprašymas „car_manager.py“
Šiame faile „car_manager.py“ saugomos funkcijos (metodai), skirtos sąveikai su automobilių stovėjimo aikštelėse esančiais automobiliais. Šis modulis įgyvendina klases „CarManager()“, „CarManagerFactory“ ir „TextCarManager(CarManager)“. Šiame faile įgyvendinami pagrindiniai objektinio programavimo principai, taip pat du pagrindiniai projektavimo modeliai (Design Patterns). Išsamus funkcijų (metodų) aprašymas bus kito modulio „parking_menu_functions.py“, kuriame yra meniu ir iš šio failo iškviečiamos reikiamos funkcijos, aprašyme. 
1.	Abstrakcija (Abstraction):
Klasė „CarManager“ yra abstrakti bazinė klasė (ABC), kuri yra aiškus abstrakcijos pavyzdys. Tai reiškia, kad ji apibrėžia sąsają visoms išvestinėms klasėms ir joje yra abstrakčių metodų, kurie turi būti įgyvendinami įpėdinėse klasėse.

Kodo pavyzdys:
```
class CarManager(ABC):
    @abstractmethod
    def add_car(self, license_plate, brand):
        pass

    @abstractmethod
    def remove_car(self, license_plate):
        pass

    @abstractmethod
    def list_cars(self):
        pass
```
2.	Inkapsuliavimas (Encapsulation):
„TextCarManager“ klasė apima automobilio valdymo logiką, paslėpdama nuo naudotojo įgyvendinimo detales, pvz., failų tvarkymą.
Kodo pavyzdys:
```
	class TextCarManager(CarManager):
    def add_car(self, license_plate, brand):
        file_path = os.path.join(self.storage_dir, f'{license_plate}.txt')
        with open(file_path, 'w') as file:
            file.write(f'{license_plate}, {brand}\n')
```
3.	Paveldėjimas (Inheritance):
„TextCarManager“ paveldi iš „CarManager“, perimdamas abstrakčius metodus ir pridėdamas naujas funkcijas, tokias kaip „edit_car“ ir „find_car_by_plate“.
Kodo pavyzdys:
```
class TextCarManager(CarManager):
    def add_car(self, license_plate, brand):
        # įgyvendinimas čia
```

4.	Polimorfizmas (Polymorphism):
Polimorfizmas įgyvendinamas per paveldėjimo ir metodų perėmimo mechanizmą. Skirtingi „CarManager“ paveldėtojai gali turėti skirtingas automobilių pridėjimo, pašalinimo ir išvardijimo metodų realizacijas, todėl šie objektai gali būti naudojami per bendrą sąsają.
Kodo pavyzdys:
```
def remove_car(self, license_plate):
    file_path = os.path.join(self.storage_dir, f'{license_plate}.txt')
    if os.path.exists(file_path):
        os.remove(file_path)
```
### Dizaino šablonai
1.	Singleton:
„TextCarManager“ naudoja „Singleton“ modelį, kad visoje programoje būtų sukurtas tik vienas šios klasės egzempliorius. Tai pasiekiama naudojant metodą „__new__“, kuris patikrina, ar klasės egzempliorius jau egzistuoja, o jei ne, jį sukuria.
Kodo pavyzdys:
```
class TextCarManager(CarManager):
    _instance = None

    def __new__(cls, storage_dir):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```
2.	Factory Method:
Klasė „CarManagerFactory“ įgyvendina „Factory Method“ projektavimo modelį, pateikdama statinį metodą „get_manager“, kuris sukuria ir grąžina objektą „TextCarManager“ arba kitus galimus tvarkytuvus, priklausomai nuo parametro „manager_type“. Tai leidžia dinamiškai keisti sukurto tvarkytuvo tipą nekeičiant kliento kodo.
      Kodo pavyzdys:
  	```
	class CarManagerFactory:
    @staticmethod
    def get_manager(manager_type, storage_dir):
        if manager_type == 'text':
            return TextCarManager(storage_dir)
        raise ValueError("Unknown manager type")
  	```


### Modulio aprašymas „parking_menu_functions.py“
Šis failas „parking_menu_functions.py“ yra antrasis programos meniu. Šis meniu leidžia sąveikauti su automobiliais pasirinktoje stovėjimo aikštelėje (tam tikrame aplanke). Šis modulis importuoja funkcijas iš failo „car_manager.py“. Šis meniu įgyvendintas tokiu pat principu kaip ir pirmasis, naudojant ciklą „while“ ir loginius operatorius „if“ ir „else“. 
Funkcijų sąrašas:
1.	Pridėti automobilį (šia parinktimi iškviečiama funkcija „add_car()“ ir paprašoma įrašyti automobilio valstybinį numerį ir markę, tada patikrinama, ar panašus automobilis jau egzistuoja, jei ne, sukuriamas .txt failas, kuriame saugoma informacija apie konkretų automobilį).
2.	Pašalinti automobilį (šiuo pasirinkimu iškviečiama funkcija „remove_car()“ ir prašoma įrašyti automobilio valstybinį numerį, kad būtų galima ieškoti automobilio, jei automobilis su nurodytu valstybiniu numeriu egzistuoja, jis bus pašalintas iš automobilių stovėjimo aikštelės).
3.	Automobilių sąrašas (Šiuo pasirinkimu iškviečiama funkcija „list_cars()“, kuri parodo visus automobilius, esančius automobilių stovėjimo aikštelėje, su kuria sąveikauja naudotojas. Rodomas bendras automobilių skaičius, taip pat sąrašas, kuriame nurodomas automobilio numeris ir markė)
4. Redaguoti informaciją (ši parinktis iškviečia funkciją „edit_car()“, kuri paprašo naudotojo nurodyti automobilio numerį, jei jis egzistuoja, paprašo nurodyti naują automobilio numerį ir naują automobilio markę. Šis metodas leidžia redaguoti jau esamus automobilius ir keisti jų informaciją)
5.	Grįžti į pagrindinį meniu (šiame pasirinkime naudojamas operatorius „break“, todėl nutraukiamas ciklas ir naudotojas grąžinamas į pagrindinį meniu)
Be to, kiekvienas pasirinkimas turi klaidų patikrą, jei naudotojas nurodo neteisingą pasirinkimą, kuris nėra skaičius nuo 1 iki 5, programa sugeneruoja klaidą. Taip pat įdiegtos visos funkcijos (metodai), kurios sąveikauja su duomenimis.


### Modulio aprašymas „test_parking_system.py“
Šis modulis naudojamas programai testuoti naudojant „unittest“. Šiame faile atliekamas kiekvienos funkcijos testas, kad būtų aptiktos klaidos. Visi testai atliekami taip, kad funkcija gautų pavyzdinius duomenis, juos apdorotų ir pateiktų rezultatą, kad galėtume patikrinti, ar ji veikia. Šiame faile naudojau pagalbines bibliotekas, kad patikrinčiau, ką funkcija rašo į terminalą. Šiam tikslui panaudojau biblioteką „io“, iš kurios importavau „StringIO“.

# Kursinio darbo rezultatai ir išvados

Pagrindinis darbo rezultatas - sėkmingai sukurta informacinė sistema, skirta sąveikai su automobilių stovėjimo aikštelėmis ir jose esančiais automobiliais. Šis darbas paskatino nuodugniau išstudijuoti įvairias bibliotekas, pavyzdžiui, biblioteką „os“, kurią naudojau sąveikai su sistemos viduje esančiais failais (su .txt formato aplankais ir dokumentais). Kaip man atrodo, pagrindinis šio kursinio darbo sunkumas buvo „unittest“, nes anksčiau nebuvau susidūręs su šia biblioteka, tačiau man pavyko įgyvendinti funkcijų (metodų) testus. Pagrindiniu šios sistemos kūrimo vektoriumi (ką dar galima padaryti) matau grafinės sąsajos sukūrimą, siekiant supaprastinti sąveiką su automobilių stovėjimo aikštelėmis ir automobiliais. Taip pat galima pridėti laiko sistemą, kad būtų galima matyti, kiek laiko automobilis stovi, taip pat apskaičiuoti, kiek automobilio savininkas turės sumokėti už stovėjimą pagal laiką ir kainą už valandą ar minutę. Kita vertus, šią informacinę sistemą galima pertvarkyti į didesnę duomenų bazę, kad būtų patogiau saugoti didelį duomenų kiekį, tai galima įgyvendinti naudojant „MySQL“ arba ieškoti tinkamų „Python“ bibliotekų. Dėl to kursinio darbo tikslas buvo pasiektas.
