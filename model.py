from dis import Instruction
import os
from enum import Enum
from secrets import token_urlsafe

class Ingredient:
    def __init__(self, name, amount, unit):
        self.name = name
        self.amount = amount
        self.unit = unit

    # predpostavimo da so enote vedno enake, torej nas zanima samo
    # kolicina. Dodatna komplikacija bi bila dodati pretvorni enot,
    # tako da bi lahko eno izrazili, recimo, z grami, drugo pa z
    # nestandardnimi enotai, recimo "zlicka", "cup" ali podobno
    def have_enough(required_ingredient):
        return self.amount >= required_ingredient.amount
        
    def __init__(self, tokens):
       
        # Primer liste tokens je recimo ['pecilni', 'prasek', '1/2', 'kos']
        self.name =  ' '.join(tokens[0:-2])
        self.amount = tokens[-2]
        self.unit = tokens [-1]

    def __str__(self):
        return ' '.join([self.name, self.amount, self.unit])
        
class Recipe:
    def __init__(self, name):
        self.name = name 
        self.ingredients = []
        self.instructions = ''

    def get_ingredients(self):
        return self.ingredients

    def get_instructions(self):
        return self.instructions 

    def get_name(self):
        return self.name    

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def set_instructions(self, text):
        self.instrucitons = text

    def is_doable(self, list_of_ingredients):

        for ingredient in self.ingredients:
            # najprej v listi sestavin poisci to sestavino. Ce je ne najde potem
            # recept ni izvedljiv
            found_ingredient = None
            for aux in list_of_ingredients:
                if ingredient.name  == aux.name:
                    found_ingredient = aux
                    break
                
             # ce sestavine ni v seznamu recept ni izvedljiv
            if found_ingredient == None:
                return False   
                
            # sestavine mora tudi biti dovolj; odgovor na to vprasanje pa pozna
            # sestavina sama.
            #  found_ingredient je najden sestavina iz mojega seznama
            #  ignredient je trenutna sestavina iz recepta
            if not found_ingredient.have_enough(ingredient):
                return False

        # ce se zunanja zanka konco, to pomeni da so vse sestavine iz recepta
        # najdene v zadnostni kolicini na vhodnem seznamu, torej je recept
        # izvedljiv
        return True
            
    def __str__(self):
        ret = 'Naslov: ' + self.name + "\n\nSestavine:\n"
        for ingredient in self.ingredients:
            ret += str(ingredient) + "\n"
        ret += "\nKoraki:\n" + self.instructions + "\n====================\n\n"
        return ret

class InputState(Enum):
    OUTSIDE = 1
    IN_INGREDIENTS = 2
    IN_INSTRUCTIONS = 3
        
class Cookbook:
    def __init__(self, name):
        self.name = name
        self.recipes = []

    def __str__(self):
        ret = ''
        for recipe in self.recipes:
            ret += str(recipe)
        return ret

    def from_file_read(self, file_name):
        # spremenljivka ki hrani vhodno stanje
        input_state = InputState.OUTSIDE

        # recept ki se trenutno bere
        current_recipe = None

        # priporocam uporabo "with" ki sam zapre datoteko ali kaksen
        # drugi resource ko se konca koda v bloku
        with open(file_name, 'r') as fp:

            # preberemo kar vse vrstice
            all_lines = fp.readlines()

            # sledi iteracija skozi vse vrstice
            for line in all_lines:
                tokens = line.split()

                # prazne vrstice preskocimo
                if len(tokens) == 0:
                    continue
                
                if input_state  == InputState.OUTSIDE:
                    
                    if tokens[0] == 'Naslov:':
                        current_recipe = Recipe(' '.join(tokens[1:]))
                    elif tokens[0] == 'Sestavine:':
                        input_state = InputState.IN_INGREDIENTS
                    elif tokens[0] == 'Koraki':
                        input_state = InputState.IN_INSTRUCTIONS

                elif input_state == InputState.IN_INGREDIENTS:
                    
                        if tokens[0].startswith('Koraki:'):
                            input_state = InputState.IN_INSTRUCTIONS
                        else:
                            current_recipe.ingredients.append(Ingredient(tokens))
                            
                elif input_state == InputState.IN_INSTRUCTIONS:
                    
                        if tokens[0].startswith('====='):
                            # konec recepta, dodaj recept v listo in se postavi v zacetno stanje
                            input_state =InputState.OUTSIDE
                            if current_recipe != None:
                                self.recipes.append(current_recipe)
                                current_recipe = None
                        else:
                            current_recipe.instructions += line
                            
    # get_doable je kar member metoda razreda Cookbook. Zakaj member metoda? Glede na to da objekt Cookbook vsebuje
    # listo receptov, in da se vprasanje omejuje na to listo receptov je  to najbolj smiselno, a ne?
    # sama metoda pa uporablja "deli in vladaj" pristop ... pravzaprav se noce ukvarjati z vprasanjem kdaj je konkreten
    # recept izvedljiv s sestavinami ki so na voljo, ampak jo samo zanima ali je izvedljiv ... zato odgovor na vprasanje
    # o izvedljivosti prepusca receptu samemu:
    def get_doable(self, list_of_ingredients):

        response = []      # zacnemo s prazno listo receptov; ce noben ni izvedljiv je to kar odgovor
        for recipe in self.recipes:
            if recipe.is_doable(list_of_ingredients):
                response.append(recipe)

        return response
    # konec: vidis kako preprosto je to???
 
                            
#def Cookbook.get_doable(list_of_ingredients):
#    list_of_ingredients = Ingredient(tokens)
#
#    if self.name != Recepie(self.ingredients[0:2]):
#        break
#    elif self.name == Recepie(self.ingredients[0:2]) 
#        & self.unit == Recepie(self.ingredients[-1])
#        & self.amount >= Recepie(self.ingredients[-2]):
#
#        Cookbook(self.recepies).append(Recepie(self.name))



                            
# # ustvari novo kuharsko knjigo...
# a = Cookbook('MyRecipes')

# # ... jo preberi iz datoteke
# a.from_file_read('recepti.txt')

# # ... in izpisi na konzolo
# print(a)
