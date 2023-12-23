"""Nutrition facts preparation"""

import pandas as pd
import math

food_name_list = [
  'Apple w skin av',
  'Strawberries',
  'Apricots w skin',
  'Pineapple',
  'Banana',
  'Blueberries',
  'Redcurrants',
  'Lemon',
  'Grapes w skin av',
  'Raspberries',
  'Grapefruit',
  'Cherries',
  'Gooseberries',
  'Manderins',
  'Plums w skin',
  'Orange',
  'Coconut meat',
  'Avocado',
  'Guava (pink fleshed)',
  'Lime',
  'Mango',
  'Papaya',
  'Pomegranate',
  'Figs fresh',
  'Kaki / Sharon fruit',
  'Passion fruit',
  'Lychees',
  'Kumquat',
  'Melon water',
  'Nectarine',
  'Dates fresh',
  'Carambola',
  'Pear w skin',
  'Melon cantaloupe',
  'Mulberries raw',
  'Peach w skin',
  'Kiwi fruit av',
  'Melon av',
  'Ginger root',
  'Beans soya dried',
  'Hazelnuts unsalted',
  'Chestnuts raw',
  'Walnuts unsalted',
  'Pecan nuts unroasted unsalted',
  'Potatoes raw',
  'Potato sweet raw',
  'Aubergine/eggplant raw',
  'Beetroot raw',
  'Cauliflower raw',
  'Peas raw',
  'Turnip tops raw',
  'Spinach raw',
  'Sweetcorn boiled',
  'Onions raw',
  'Cabbage white raw',
  'Carrot raw av',
  'Radish raw',
  'Kohlrabi raw',
  'Garlic raw',
  'Lettuce av raw',
  'Chili pepper raw',
  'Tomato cherry raw',
  'Tomato beef raw',
  'Tomato av raw',
  'Cucumber w skin raw',
  'Sweet pepper av raw'
]

fldrs2nutrition_map = {
  'apple': 'Apple w skin av', 
  'apricot': 'Apricots w skin',
  'avocado': 'Avocado',
  'banana': 'Banana',
  'beetroot': 'Beetroot raw',
  'bell_pepper': 'Sweet pepper av raw',
  'blueberry': 'Blueberries',
  'cabbage': 'Cabbage white raw',     
  'cantaloupe': 'Melon cantaloupe', 
  'carrot': 'Carrot raw av',
  'cauliflower': 'Cauliflower raw',
  'cherry_black': 'Cherries', 
  'chestnut': 'Chestnuts raw',
  'chilli_pepper': 'Chili pepper raw',
  'clementine': 'Manderins',  
  'coconut': 'Coconut meat',
  'corn': 'Sweetcorn boiled',
  'cucumber': 'Cucumber w skin raw',
  'dates': 'Dates fresh',
  'eggplant': 'Aubergine/eggplant raw',
  'fig': 'Figs fresh',
  'garlic': 'Garlic raw', 
  'ginger': 'Ginger root',	
  'granadilla': 'Passion fruit',
  'grapefruit_pink': 'Grapefruit',
  'grapes': 'Grapes w skin av',
  'guava': 'Guava (pink fleshed)',
  'hazelnut': 'Hazelnuts unsalted',
  'kaki': 'Kaki / Sharon fruit',
  'kiwi':	'Kiwi fruit av',
  'kohlrabi': 'Kohlrabi raw',
  'kumquats': 'Kumquat',
  'lemon': 'Lemon',
  'lettuce': 'Lettuce av raw',
  'limes': 'Lime',
  'lychee': 'Lychees',
  'mango': 'Mango',
  'melon_or_piel_de_sapo': 'Melon av',
  'mulberry': 'Mulberries raw',
  'nectarine': 'Nectarine',
  'onion': 'Onions raw',
  'orange': 'Orange',
  'papaya': 'Papaya',
  'peach': 	'Peach w skin',
  'pear': 'Pear w skin',
  'peas': 'Peas raw',
  'pecan_nut': 	'Pecan nuts unroasted unsalted',
  'physalis_or_gooseberry': 'Gooseberries',
  'pineapple': 'Pineapple',
  'plum': 'Plums w skin',
  'pomegranate': 'Pomegranate',
  'potato': 'Potatoes raw',
  'potato_sweet': 'Potato sweet raw',
  'raddish': 'Radish raw',
  'raspberry': 'Raspberries',
  'redcurrant': 'Redcurrants',
  'soy_beans': 'Beans soya dried',
  'spinach': 'Spinach raw',
  'star_fruit_or_carambola': 'Carambola',
  'strawberry': 'Strawberries',
  'tomato': 'Tomato av raw',
  'tomato_beefsteak': 'Tomato beef raw',
  'tomato_cherry_red': 'Tomato cherry raw',
  'turnip': 'Turnip tops raw',
  'walnut': 'Walnuts unsalted',
  'watermelon': 'Melon water'
}

def nutrition_prettyprint(nutrifact: dict):
    del nutrifact['Food_Group']
    nutrifact = {k: float(v.replace(',', '.')) 
                 if (type(v) == str and ',' in v) or (type(v) == str and v.isnumeric()) 
                 else v
                 for k, v in nutrifact.items()}
    nutrifact = {k: v for k, v in nutrifact.items() if v != 0}
    nutrifact = {k: v for k, v in nutrifact.items() if not type(v) == float or not math.isnan(v)}

    return nutrifact
    


def retrieve_nutrition_facts(predicted_class):
    nutri_filename = 'CV_data/NEVO2021_7.1.csv'
    df_nutrition = pd.read_csv(nutri_filename, sep="|")

    df_nutrition = df_nutrition[['Food group', 'Engelse naam/Food name', 'ENERCC (kcal)', 'WATER (g)', 'PROT (g)', 'FAT (g)', 'FACID (g)', 'FASAT (g)', 'CHO (g)', 'SUGAR (g)', 
            'STARCH (g)', 'FIBT (g)', 'NA (mg)', 'K (mg)', 'CA (mg)', 'P (mg)', 'MG (mg)', 'FE (mg)',
            'CU (mg)',	'SE (µg)',	'ZN (mg)',	'ID (µg)',
            'VITA_RAE (µg)', 'VITA_RE (µg)',	'RETOL (µg)', 'CARTBTOT (µg)'	, 'CARTA (µg)',	'LUTN (µg)', 'ZEA (µg)',	'CRYPXB (µg)', 'LYCPN (µg)', #Vitamin A
            'VITD (µg)', 'VITE (mg)', 'VITK (µg)', 'THIA (mg)', 'RIBF (mg)',	'VITB6 (mg)',	'VITB12 (µg)',	'NIA (mg)',
            'VITC (mg)']]

    df_nutrition.columns = ['Food_Group', 'Food Name', 'Energy(kcal)', 'Water(g)', 'Protein(g)', 'Fat(g)', 'Fatty_acids_total(g)', 'Fatty acids saturated total(g)', 'Carbohydrate(g)', 'Sugar(g)',
                'Starch(g)', 'Fiber dietary total(g)', 'Na(mg)', 'K(mg)', 'Ca(mg)', 'P(mg)', 'Mg(mg)', 'Fe(mg)', 'Cu(mg)', 'Se(µg)', 'Zn(mg)', 'Id(µg)',
                'VITA_RAE (µg)', 'VITA_RE (µg)',	'RETOL (µg)', 'CARTBTOT (µg)'	, 'CARTA (µg)',	'LUTN (µg)', 'ZEA (µg)',	'CRYPXB (µg)', 'LYCPN (µg)', #Vitamin A
                'Vitamin_D(µg)', 'Vitamin_E(mg)', 'Vitamin_K(µg)', 'Vitamin_B1(mg)', 'Vitamin_B2(mg)', 'Vitamin_B6(mg)', 'Vitamin_B12(µg)', 'Vitamin_B3(mg)',
                'Vitamin_C(mg)']

    vit_a_list = ['VITA_RAE (µg)', 'VITA_RE (µg)',	'RETOL (µg)', 'CARTBTOT (µg)'	, 'CARTA (µg)',	'LUTN (µg)', 'ZEA (µg)',	'CRYPXB (µg)', 'LYCPN (µg)']
    df_nutrition['Vitamin_A'] = df_nutrition[vit_a_list].sum(axis=1)

    df_nutrition = df_nutrition.drop(columns=vit_a_list)

    df_nutrition = df_nutrition[df_nutrition['Food Name'].isin(food_name_list)]

    output = df_nutrition[df_nutrition['Food Name'] == fldrs2nutrition_map[predicted_class]].copy().to_dict('index')
    return nutrition_prettyprint(output[next(iter(output))])

