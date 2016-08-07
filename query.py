"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)
# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()
# Get all models that are older than 1960.
Model.query.filter(Model.year < 1960).all()
# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()
# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.startswith('Cor')).all #can this still work without the .all???
# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded==1903,Brand.discontinued.is_(None)).all
# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.
Brand.query.filter(Brand.discontinued is not(None),Brand.founded < 1950).all()
# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all()
# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    all_years = db.session.query(Model.name, Model.brand_name,Brand.headquarters) 
    each_year = all_years.filter(Model.year ==year)

    print each_year.all()


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brand_info = db.session.query(Model.brand_name,Model.name)

    for item in brand_name:
    	print item
# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# its an object
# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
 # an association table bolds forgeign keys with many to many relationships.
# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    brands_information = Brand.query.filter((Brand.name.contains(mystr)) | (Brand.name == mystr)).all()
    print brands_information

def get_models_between(start_year, end_year):
    
    cars_selected = Model.query.filter(Model.year > start_year, Model.year < end_year)
    print cars_selected