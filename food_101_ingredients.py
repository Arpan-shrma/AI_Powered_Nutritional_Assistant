import json

def create_food101_database():
    """Create comprehensive database for all Food-101 categories"""
    
    food_db = {
        "apple_pie": {
            "ingredients": [
                {"name": "apples", "amount": "6 cups", "category": "fruit"},
                {"name": "flour", "amount": "2.5 cups", "category": "grain"},
                {"name": "butter", "amount": "0.5 cup", "category": "dairy"},
                {"name": "sugar", "amount": "1 cup", "category": "sweetener"},
                {"name": "cinnamon", "amount": "1 tsp", "category": "spice"}
            ],
            "nutrition_per_100g": {
                "calories": 237,
                "protein": 2.4,
                "carbs": 41.5,
                "fat": 11.2,
                "fiber": 1.7
            },
            "allergens": ["gluten", "dairy"],
            "serving_size": "1 slice (100g)",
            "category": "dessert"
        },
        "baby_back_ribs": {
            "ingredients": [
                {"name": "pork ribs", "amount": "2 racks", "category": "protein"},
                {"name": "bbq sauce", "amount": "1 cup", "category": "condiment"},
                {"name": "brown sugar", "amount": "1/4 cup", "category": "sweetener"},
                {"name": "paprika", "amount": "2 tbsp", "category": "spice"},
                {"name": "garlic powder", "amount": "1 tbsp", "category": "spice"}
            ],
            "nutrition_per_100g": {
                "calories": 238,
                "protein": 27,
                "carbs": 8,
                "fat": 13,
                "fiber": 0
            },
            "allergens": [],
            "serving_size": "3-4 ribs (250g)",
            "category": "main_course"
        },
        "baklava": {
            "ingredients": [
                {"name": "phyllo dough", "amount": "1 package", "category": "grain"},
                {"name": "walnuts", "amount": "2 cups", "category": "nuts"},
                {"name": "butter", "amount": "1 cup", "category": "dairy"},
                {"name": "honey", "amount": "1 cup", "category": "sweetener"},
                {"name": "cinnamon", "amount": "1 tsp", "category": "spice"}
            ],
            "nutrition_per_100g": {
                "calories": 403,
                "protein": 6.2,
                "carbs": 43.3,
                "fat": 25.1,
                "fiber": 2.4
            },
            "allergens": ["gluten", "nuts", "dairy"],
            "serving_size": "1 piece (50g)",
            "category": "dessert"
        },
        "beef_carpaccio": {
            "ingredients": [
                {"name": "beef tenderloin", "amount": "400g", "category": "protein"},
                {"name": "olive oil", "amount": "2 tbsp", "category": "oil"},
                {"name": "arugula", "amount": "2 cups", "category": "vegetable"},
                {"name": "capers", "amount": "2 tbsp", "category": "condiment"},
                {"name": "parmesan cheese", "amount": "50g", "category": "dairy"}
            ],
            "nutrition_per_100g": {
                "calories": 213,
                "protein": 28,
                "carbs": 0.5,
                "fat": 11,
                "fiber": 0.2
            },
            "allergens": ["dairy"],
            "serving_size": "1 portion (120g)",
            "category": "appetizer"
        },
        "beef_tartare": {
            "ingredients": [
                {"name": "beef tenderloin", "amount": "200g", "category": "protein"},
                {"name": "egg yolk", "amount": "1", "category": "protein"},
                {"name": "dijon mustard", "amount": "1 tbsp", "category": "condiment"},
                {"name": "capers", "amount": "1 tbsp", "category": "condiment"},
                {"name": "shallots", "amount": "2 tbsp", "category": "vegetable"}
            ],
            "nutrition_per_100g": {
                "calories": 200,
                "protein": 25,
                "carbs": 1,
                "fat": 12,
                "fiber": 0.3
            },
            "allergens": ["eggs"],
            "serving_size": "1 portion (150g)",
            "category": "appetizer"
        },
        "beet_salad": {
            "ingredients": [
                {"name": "beets", "amount": "4 medium", "category": "vegetable"},
                {"name": "goat cheese", "amount": "100g", "category": "dairy"},
                {"name": "walnuts", "amount": "1/2 cup", "category": "nuts"},
                {"name": "arugula", "amount": "4 cups", "category": "vegetable"},
                {"name": "balsamic vinegar", "amount": "2 tbsp", "category": "condiment"}
            ],
            "nutrition_per_100g": {
                "calories": 156,
                "protein": 5.2,
                "carbs": 12.3,
                "fat": 10.1,
                "fiber": 3.2
            },
            "allergens": ["dairy", "nuts"],
            "serving_size": "1 serving (200g)",
            "category": "salad"
        },
        "beignets": {
            "ingredients": [
                {"name": "flour", "amount": "3 cups", "category": "grain"},
                {"name": "sugar", "amount": "1/4 cup", "category": "sweetener"},
                {"name": "yeast", "amount": "1 tbsp", "category": "leavening"},
                {"name": "milk", "amount": "1 cup", "category": "dairy"},
                {"name": "powdered sugar", "amount": "2 cups", "category": "sweetener"}
            ],
            "nutrition_per_100g": {
                "calories": 280,
                "protein": 4.5,
                "carbs": 48,
                "fat": 8.2,
                "fiber": 1.1
            },
            "allergens": ["gluten", "dairy"],
            "serving_size": "2 pieces (80g)",
            "category": "dessert"
        },
        "bibimbap": {
            "ingredients": [
                {"name": "rice", "amount": "2 cups", "category": "grain"},
                {"name": "beef", "amount": "200g", "category": "protein"},
                {"name": "spinach", "amount": "1 cup", "category": "vegetable"},
                {"name": "carrots", "amount": "1 cup", "category": "vegetable"},
                {"name": "egg", "amount": "1", "category": "protein"},
                {"name": "gochujang", "amount": "2 tbsp", "category": "condiment"}
            ],
            "nutrition_per_100g": {
                "calories": 215,
                "protein": 12,
                "carbs": 28,
                "fat": 7,
                "fiber": 2.5
            },
            "allergens": ["eggs", "soy"],
            "serving_size": "1 bowl (400g)",
            "category": "main_course"
        },
        "bread_pudding": {
            "ingredients": [
                {"name": "bread", "amount": "6 cups", "category": "grain"},
                {"name": "milk", "amount": "2 cups", "category": "dairy"},
                {"name": "eggs", "amount": "4", "category": "protein"},
                {"name": "sugar", "amount": "1 cup", "category": "sweetener"},
                {"name": "vanilla extract", "amount": "1 tsp", "category": "flavoring"}
            ],
            "nutrition_per_100g": {
                "calories": 265,
                "protein": 8.5,
                "carbs": 38,
                "fat": 9.2,
                "fiber": 0.8
            },
            "allergens": ["gluten", "dairy", "eggs"],
            "serving_size": "1 serving (150g)",
            "category": "dessert"
        },
        "breakfast_burrito": {
            "ingredients": [
                {"name": "tortilla", "amount": "1 large", "category": "grain"},
                {"name": "eggs", "amount": "2", "category": "protein"},
                {"name": "cheese", "amount": "50g", "category": "dairy"},
                {"name": "potatoes", "amount": "100g", "category": "vegetable"},
                {"name": "salsa", "amount": "2 tbsp", "category": "condiment"}
            ],
            "nutrition_per_100g": {
                "calories": 250,
                "protein": 12,
                "carbs": 30,
                "fat": 10,
                "fiber": 2
            },
            "allergens": ["gluten", "dairy", "eggs"],
            "serving_size": "1 burrito (300g)",
            "category": "breakfast"
        },
        "bruschetta": {
            "ingredients": [
                {"name": "baguette", "amount": "1", "category": "grain"},
                {"name": "tomatoes", "amount": "4 medium", "category": "vegetable"},
                {"name": "garlic", "amount": "3 cloves", "category": "vegetable"},
                {"name": "basil", "amount": "1/2 cup", "category": "herb"},
                {"name": "olive oil", "amount": "1/4 cup", "category": "oil"}
            ],
            "nutrition_per_100g": {
                "calories": 170,
                "protein": 5,
                "carbs": 25,
                "fat": 6,
                "fiber": 1.5
            },
            "allergens": ["gluten"],
            "serving_size": "2 pieces (120g)",
            "category": "appetizer"
        },
        "caesar_salad": {
            "ingredients": [
                {"name": "romaine lettuce", "amount": "1 head", "category": "vegetable"},
                {"name": "parmesan cheese", "amount": "1/2 cup", "category": "dairy"},
                {"name": "croutons", "amount": "1 cup", "category": "grain"},
                {"name": "caesar dressing", "amount": "1/2 cup", "category": "condiment"},
                {"name": "anchovies", "amount": "4 fillets", "category": "protein"}
            ],
            "nutrition_per_100g": {
                "calories": 180,
                "protein": 8,
                "carbs": 12,
                "fat": 13,
                "fiber": 2.5
            },
            "allergens": ["gluten", "dairy", "fish"],
            "serving_size": "1 bowl (200g)",
            "category": "salad"
        },
        "cannoli": {
            "ingredients": [
                {"name": "ricotta cheese", "amount": "2 cups", "category": "dairy"},
                {"name": "flour", "amount": "2 cups", "category": "grain"},
                {"name": "powdered sugar", "amount": "1 cup", "category": "sweetener"},
                {"name": "chocolate chips", "amount": "1/2 cup", "category": "sweet"},
                {"name": "vanilla extract", "amount": "1 tsp", "category": "flavoring"}
            ],
            "nutrition_per_100g": {
                "calories": 360,
                "protein": 10,
                "carbs": 35,
                "fat": 20,
                "fiber": 0.5
            },
            "allergens": ["gluten", "dairy"],
            "serving_size": "1 cannoli (80g)",
            "category": "dessert"
        },
        "caprese_salad": {
            "ingredients": [
                {"name": "tomatoes", "amount": "4 large", "category": "vegetable"},
                {"name": "fresh mozzarella", "amount": "200g", "category": "dairy"},
                {"name": "fresh basil", "amount": "1 cup", "category": "herb"},
                {"name": "olive oil", "amount": "3 tbsp", "category": "oil"},
                {"name": "balsamic glaze", "amount": "2 tbsp", "category": "condiment"}
            ],
            "nutrition_per_100g": {
                "calories": 140,
                "protein": 7,
                "carbs": 3,
                "fat": 11,
                "fiber": 1
            },
            "allergens": ["dairy"],
            "serving_size": "1 serving (150g)",
            "category": "salad"
        },
        "carrot_cake": {
            "ingredients": [
                {"name": "carrots", "amount": "3 cups", "category": "vegetable"},
                {"name": "flour", "amount": "2 cups", "category": "grain"},
                {"name": "cream cheese", "amount": "8 oz", "category": "dairy"},
                {"name": "walnuts", "amount": "1 cup", "category": "nuts"},
                {"name": "cinnamon", "amount": "2 tsp", "category": "spice"}
            ],
            "nutrition_per_100g": {
                "calories": 390,
                "protein": 6,
                "carbs": 45,
                "fat": 21,
                "fiber": 2
            },
            "allergens": ["gluten", "dairy", "nuts"],
            "serving_size": "1 slice (120g)",
            "category": "dessert"
        },
        "ceviche": {
            "ingredients": [
                {"name": "white fish", "amount": "1 lb", "category": "protein"},
                {"name": "lime juice", "amount": "1 cup", "category": "citrus"},
                {"name": "red onion", "amount": "1 medium", "category": "vegetable"},
                {"name": "cilantro", "amount": "1/2 cup", "category": "herb"},
                {"name": "chili pepper", "amount": "1", "category": "spice"}
            ],
            "nutrition_per_100g": {
                "calories": 120,
                "protein": 20,
                "carbs": 4,
                "fat": 3,
                "fiber": 1
            },
            "allergens": ["fish"],
            "serving_size": "1 serving (150g)",
            "category": "appetizer"
        },
        "cheesecake": {
            "ingredients": [
                {"name": "cream cheese", "amount": "32 oz", "category": "dairy"},
                {"name": "graham crackers", "amount": "2 cups", "category": "grain"},
                {"name": "sugar", "amount": "1.5 cups", "category": "sweetener"},
                {"name": "eggs", "amount": "4", "category": "protein"},
                {"name": "sour cream", "amount": "1 cup", "category": "dairy"}
            ],
            "nutrition_per_100g": {
                "calories": 320,
                "protein": 7,
                "carbs": 25,
                "fat": 23,
                "fiber": 0.3
            },
            "allergens": ["gluten", "dairy", "eggs"],
            "serving_size": "1 slice (150g)",
            "category": "dessert"
        },
        "cheese_plate": {
            "ingredients": [
                {"name": "brie cheese", "amount": "100g", "category": "dairy"},
                {"name": "cheddar cheese", "amount": "100g", "category": "dairy"},
                {"name": "blue cheese", "amount": "100g", "category": "dairy"},
                {"name": "grapes", "amount": "1 cup", "category": "fruit"},
                {"name": "crackers", "amount": "200g", "category": "grain"},
                {"name": "nuts", "amount": "1/2 cup", "category": "nuts"}
            ],
            "nutrition_per_100g": {
                "calories": 350,
                "protein": 20,
                "carbs": 12,
                "fat": 28,
                "fiber": 0.5
            },
            "allergens": ["dairy", "gluten", "nuts"],
            "serving_size": "1 plate (300g)",
            "category": "appetizer"
        },
        "chicken_curry": {
            "ingredients": [
                {"name": "chicken", "amount": "500g", "category": "protein"},
                {"name": "coconut milk", "amount": "400ml", "category": "dairy"},
                {"name": "curry powder", "amount": "2 tbsp", "category": "spice"},
                {"name": "onions", "amount": "2 medium", "category": "vegetable"},
                {"name": "tomatoes", "amount": "2 large", "category": "vegetable"}
            ],
            "nutrition_per_100g": {
                "calories": 165,
                "protein": 15,
                "carbs": 8,
                "fat": 10,
                "fiber": 2
            },
            "allergens": [],
            "serving_size": "1 serving (250g)",
            "category": "main_course"
        },
        "chicken_quesadilla": {
            "ingredients": [
                {"name": "tortillas", "amount": "2 large", "category": "grain"},
                {"name": "chicken breast", "amount": "200g", "category": "protein"},
                {"name": "cheese", "amount": "100g", "category": "dairy"},
                {"name": "bell peppers", "amount": "1 medium", "category": "vegetable"},
                {"name": "onion", "amount": "1 medium", "category": "vegetable"}
            ],
            "nutrition_per_100g": {
                "calories": 242,
                "protein": 18,
                "carbs": 20,
                "fat": 12,
                "fiber": 1.5
            },
            "allergens": ["gluten", "dairy"],
            "serving_size": "1 quesadilla (200g)",
            "category": "main_course"
        },
        "chicken_wings": {
            "ingredients": [
                {"name": "chicken wings", "amount": "1kg", "category": "protein"},
                {"name": "hot sauce", "amount": "1 cup", "category": "condiment"},
                {"name": "butter", "amount": "1/2 cup", "category": "dairy"},
                {"name": "garlic powder", "amount": "1 tbsp", "category": "spice"},
                {"name": "celery", "amount": "4 stalks", "category": "vegetable"}
            ],
            "nutrition_per_100g": {
                "calories": 290,
                "protein": 27,
                "carbs": 0,
                "fat": 20,
                "fiber": 0
            },
            "allergens": ["dairy"],
            "serving_size": "6 wings (180g)",
            "category": "appetizer"
        },
        "chocolate_cake": {
            "ingredients": [
                {"name": "flour", "amount": "2 cups", "category": "grain"},
                {"name": "cocoa powder", "amount": "3/4 cup", "category": "sweet"},
                {"name": "eggs", "amount": "2", "category": "protein"},
                {"name": "milk", "amount": "1 cup", "category": "dairy"},
                {"name": "sugar", "amount": "2 cups", "category": "sweetener"}
            ],
            "nutrition_per_100g": {
                "calories": 367,
                "protein": 5,
                "carbs": 50,
                "fat": 18,
                "fiber": 2
            },
            "allergens": ["gluten", "dairy", "eggs"],
            "serving_size": "1 slice (100g)",
            "category": "dessert"
        },
        "chocolate_mousse": {
            "ingredients": [
                {"name": "dark chocolate", "amount": "200g", "category": "sweet"},
                {"name": "heavy cream", "amount": "2 cups", "category": "dairy"},
                {"name": "eggs", "amount": "4", "category": "protein"},
                {"name": "sugar", "amount": "1/4 cup", "category": "sweetener"},
                {"name": "vanilla extract", "amount": "1 tsp", "category": "flavoring"}
            ],
            "nutrition_per_100g": {
                "calories": 310,
                "protein": 4,
                "carbs": 25,
                "fat": 22,
                "fiber": 1
            },
            "allergens": ["dairy", "eggs"],
            "serving_size": "1 serving (120g)",
            "category": "dessert"
        },
        "churros": {
            "ingredients": [
                {"name": "flour", "amount": "1 cup", "category": "grain"},
                {"name": "water", "amount": "1 cup", "category": "liquid"},
                {"name": "butter", "amount": "1/2 cup", "category": "dairy"},
                {"name": "sugar", "amount": "1/4 cup", "category": "sweetener"},
                {"name": "cinnamon", "amount": "1 tbsp", "category": "spice"}
            ],
            "nutrition_per_100g": {
                "calories": 262,
                "protein": 3,
                "carbs": 45,
                "fat": 8,
                "fiber": 1
            },
            "allergens": ["gluten", "dairy"],
            "serving_size": "2 churros (80g)",
            "category": "dessert"
        },
        "clam_chowder": {
            "ingredients": [
                {"name": "clams", "amount": "4 cups", "category": "seafood"},
                {"name": "potatoes", "amount": "2 cups", "category": "vegetable"},
                {"name": "heavy cream", "amount": "2 cups", "category": "dairy"},
                {"name": "bacon", "amount": "4 slices", "category": "protein"},
                {"name": "celery", "amount": "2 stalks", "category": "vegetable"}
            ],
            "nutrition_per_100g": {
                "calories": 201,
                "protein": 12,
                "carbs": 13,
                "fat": 15,
                "fiber": 1
            },
            "allergens": ["dairy", "shellfish"],
            "serving_size": "1 bowl (250g)",
            "category": "soup"
        },
        "club_sandwich": {
            "ingredients": [
                {"name": "bread", "amount": "3 slices", "category": "grain"},
                {"name": "turkey", "amount": "100g", "category": "protein"},
                {"name": "bacon", "amount": "3 slices", "category": "protein"},
                {"name": "lettuce", "amount": "2 leaves", "category": "vegetable"},
                {"name": "tomato", "amount": "2 slices", "category": "vegetable"},
                {"name": "mayonnaise", "amount": "2 tbsp", "category": "condiment"}
            ],
            "nutrition_per_100g": {
                "calories": 250,
                "protein": 15,
                "carbs": 23,
                "fat": 12,
                "fiber": 1.5
            },
            "allergens": ["gluten", "eggs"],
            "serving_size": "1 sandwich (250g)",
            "category": "main_course"
        },
        "crab_cakes": {
            "ingredients": [
                {"name": "crab meat", "amount": "1 pound", "category": "seafood"},
                {"name": "breadcrumbs", "amount": "1 cup", "category": "grain"},
                {"name": "mayonnaise", "amount": "1/4 cup", "category": "condiment"},
                {"name": "egg", "amount": "1", "category": "protein"},
                {"name": "mustard", "amount": "1 tbsp", "category": "condiment"}
            ],
            "nutrition_per_100g": {
                "calories": 185,
                "protein": 20,
                "carbs": 10,
                "fat": 8,
                "fiber": 0.5
            },
            "allergens": ["shellfish", "gluten", "eggs"],
            "serving_size": "2 cakes (120g)",
            "category": "main_course"
        },
        "creme_brulee": {
            "ingredients": [
                {"name": "heavy cream", "amount": "2 cups", "category": "dairy"},
                {"name": "egg yolks", "amount": "4", "category": "protein"},
                {"name": "vanilla bean", "amount": "1", "category": "flavoring"},
                {"name": "sugar", "amount": "1/4 cup", "category": "sweetener"},
                {"name": "brown sugar", "amount": "1/4 cup", "category": "sweetener"}
            ],
            "nutrition_per_100g": {
                "calories": 292,
                "protein": 4,
                "carbs": 20,
                "fat": 23,
                "fiber": 0
            },
            "allergens": ["dairy", "eggs"],
            "serving_size": "1 ramekin (120g)",
            "category": "dessert"
        },
        "croque_madame": {
            "ingredients": [
                {"name": "bread", "amount": "2 slices", "category": "grain"},
                {"name": "ham", "amount": "100g", "category": "protein"},
                {"name": "gruyere cheese", "amount": "50g", "category": "dairy"},
                {"name": "bechamel sauce", "amount": "1/2 cup", "category": "sauce"},
                {"name": "egg", "amount": "1", "category": "protein"}
            ],
            "nutrition_per_100g": {
                "calories": 280,
                "protein": 15,
                "carbs": 22,
                "fat": 16,
                "fiber": 1
            },
            "allergens": ["gluten", "dairy", "eggs"],
            "serving_size": "1 sandwich (200g)",
            "category": "main_course"
        },
        "cup_cakes": {
            "ingredients": [
                {"name": "flour", "amount": "1.5 cups", "category": "grain"},
                {"name": "sugar", "amount": "1 cup", "category": "sweetener"},
                {"name": "butter", "amount": "1/2 cup", "category": "dairy"},
                {"name": "eggs", "amount": "2", "category": "protein"},
                {"name": "vanilla extract", "amount": "1 tsp", "category": "flavoring"}
            ],
            "nutrition_per_100g": {
                "calories": 305,
                "protein": 4,
                "carbs": 45,
                "fat": 12,
                "fiber": 0.5
            },
            "allergens": ["gluten", "dairy", "eggs"],
            "serving_size": "1 cupcake (60g)",
            "category": "dessert"
        },
        "deviled_eggs": {
            "ingredients": [
                {"name": "eggs", "amount": "6", "category": "protein"},
                {"name": "mayonnaise", "amount": "1/4 cup", "category": "condiment"},
                {"name": "mustard", "amount": "1 tsp", "category": "condiment"},
                {"name": "paprika", "amount": "1/4 tsp", "category": "spice"},
                {"name": "chives", "amount": "2 tbsp", "category": "herb"}
            ],
            "nutrition_per_100g": {
                "calories": 155,
                "protein": 11,
                "carbs": 1,
                "fat": 12,
                "fiber": 0
            },
            "allergens": ["eggs"],
            "serving_size": "2 halves (50g)",
            "category": "appetizer"
        },
         "donuts": {
            "ingredients": [
                {"name": "flour", "amount": "2 cups", "category": "grain"},
                {"name": "milk", "amount": "3/4 cup", "category": "dairy"},
                {"name": "yeast", "amount": "2.25 tsp", "category": "leavening"},
                {"name": "sugar", "amount": "1/4 cup", "category": "sweetener"},
                {"name": "eggs", "amount": "2", "category": "protein"}
            ],
            "nutrition_per_100g": {
                "calories": 350,
                "protein": 6,
                "carbs": 55,
                "fat": 12,
                "fiber": 1
            },
            "allergens": ["gluten", "dairy", "eggs"],
            "serving_size": "1 donut (60g)",
            "category": "dessert"
        },
        "dumplings": {
            "ingredients": [
                {"name": "flour", "amount": "2 cups", "category": "grain"},
                {"name": "ground pork", "amount": "1/2 pound", "category": "protein"},
                {"name": "cabbage", "amount": "2 cups", "category": "vegetable"},
                {"name": "green onions", "amount": "1/4 cup", "category": "vegetable"},
                {"name": "soy sauce", "amount": "2 tbsp", "category": "condiment"}
            ],
            "nutrition_per_100g": {
                "calories": 225,
                "protein": 12,
                "carbs": 30,
                "fat": 7,
                "fiber": 2
            },
            "allergens": ["gluten", "soy"],
            "serving_size": "4 dumplings (120g)",
            "category": "main_course"
        },
        "edamame": {
            "ingredients": [
                {"name": "edamame pods", "amount": "2 cups", "category": "vegetable"},
                {"name": "sea salt", "amount": "1 tsp", "category": "seasoning"},
                {"name": "water", "amount": "4 cups", "category": "liquid"}
            ],
            "nutrition_per_100g": {
                "calories": 122,
                "protein": 11,
                "carbs": 10,
                "fat": 5,
                "fiber": 5
            },
            "allergens": ["soy"],
            "serving_size": "1 cup (120g)",
            "category": "appetizer"
        },
        "eggs_benedict": {
            "ingredients": [
                {"name": "english muffins", "amount": "2", "category": "grain"},
                {"name": "eggs", "amount": "4", "category": "protein"},
                {"name": "canadian bacon", "amount": "4 slices", "category": "protein"},
                {"name": "butter", "amount": "1/2 cup", "category": "dairy"},
                {"name": "egg yolks", "amount": "3", "category": "protein"}
            ],
            "nutrition_per_100g": {
                "calories": 280,
                "protein": 15,
                "carbs": 18,
                "fat": 22,
                "fiber": 1
            },
            "allergens": ["gluten", "eggs", "dairy"],
            "serving_size": "1 serving (250g)",
            "category": "breakfast"
        },
        "escargots": {
            "ingredients": [
                {"name": "snails", "amount": "12", "category": "protein"},
                {"name": "garlic", "amount": "4 cloves", "category": "vegetable"},
                {"name": "butter", "amount": "1/2 cup", "category": "dairy"},
                {"name": "parsley", "amount": "1/4 cup", "category": "herb"},
                {"name": "white wine", "amount": "2 tbsp", "category": "alcohol"}
            ],
            "nutrition_per_100g": {
                "calories": 90,
                "protein": 16,
                "carbs": 2,
                "fat": 4,
                "fiber": 0
            },
            "allergens": ["dairy", "mollusks"],
            "serving_size": "6 snails (90g)",
            "category": "appetizer"
        },
        "falafel": {
            "ingredients": [
                {"name": "chickpeas", "amount": "2 cups", "category": "legume"},
                {"name": "onion", "amount": "1", "category": "vegetable"},
                {"name": "garlic", "amount": "4 cloves", "category": "vegetable"},
                {"name": "parsley", "amount": "1/2 cup", "category": "herb"},
                {"name": "cumin", "amount": "2 tsp", "category": "spice"}
            ],
            "nutrition_per_100g": {
                "calories": 333,
                "protein": 13,
                "carbs": 31,
                "fat": 18,
                "fiber": 4
            },
            "allergens": [],
            "serving_size": "4 balls (100g)",
            "category": "main_course"
        },
        "filet_mignon": {
            "ingredients": [
                {"name": "beef tenderloin", "amount": "8 oz", "category": "protein"},
                {"name": "butter", "amount": "2 tbsp", "category": "dairy"},
                {"name": "garlic", "amount": "2 cloves", "category": "vegetable"},
                {"name": "rosemary", "amount": "2 sprigs", "category": "herb"},
                {"name": "black pepper", "amount": "1 tsp", "category": "spice"}
            ],
            "nutrition_per_100g": {
                "calories": 267,
                "protein": 26,
                "carbs": 0,
                "fat": 17,
                "fiber": 0
            },
            "allergens": ["dairy"],
            "serving_size": "1 steak (230g)",
            "category": "main_course"
        },
        "fish_and_chips": {
            "ingredients": [
                {"name": "white fish", "amount": "500g", "category": "protein"},
                {"name": "potatoes", "amount": "4 large", "category": "vegetable"},
                {"name": "flour", "amount": "2 cups", "category": "grain"},
                {"name": "beer", "amount": "1 cup", "category": "liquid"},
                {"name": "vegetable oil", "amount": "2 cups", "category": "oil"}
            ],
            "nutrition_per_100g": {
                "calories": 295,
                "protein": 12,
                "carbs": 30,
                "fat": 15,
                "fiber": 2
            },
            "allergens": ["gluten", "fish"],
            "serving_size": "1 portion (300g)",
            "category": "main_course"
        },
        "foie_gras": {
            "ingredients": [
                {"name": "duck liver", "amount": "200g", "category": "protein"},
                {"name": "salt", "amount": "1 tsp", "category": "seasoning"},
                {"name": "white pepper", "amount": "1/4 tsp", "category": "spice"},
                {"name": "cognac", "amount": "2 tbsp", "category": "alcohol"},
                {"name": "shallots", "amount": "2 tbsp", "category": "vegetable"}
            ],
            "nutrition_per_100g": {
                "calories": 462,
                "protein": 11,
                "carbs": 4,
                "fat": 44,
                "fiber": 0
            },
            "allergens": [],
            "serving_size": "50g portion",
            "category": "appetizer"
        },
        "french_fries": {
            "ingredients": [
                {"name": "potatoes", "amount": "4 large", "category": "vegetable"},
                {"name": "vegetable oil", "amount": "4 cups", "category": "oil"},
                {"name": "salt", "amount": "2 tsp", "category": "seasoning"}
            ],
            "nutrition_per_100g": {
                "calories": 312,
                "protein": 3.4,
                "carbs": 41,
                "fat": 15,
                "fiber": 3.8
            },
            "allergens": [],
            "serving_size": "1 serving (150g)",
            "category": "side_dish"
        },
        "french_onion_soup": {
            "ingredients": [
                {"name": "onions", "amount": "6 large", "category": "vegetable"},
                {"name": "beef broth", "amount": "6 cups", "category": "liquid"},
                {"name": "bread", "amount": "4 slices", "category": "grain"},
                {"name": "gruyere cheese", "amount": "200g", "category": "dairy"},
                {"name": "butter", "amount": "1/4 cup", "category": "dairy"}
            ],
            "nutrition_per_100g": {
                "calories": 170,
                "protein": 8,
                "carbs": 16,
                "fat": 9,
                "fiber": 1.5
            },
            "allergens": ["gluten", "dairy"],
            "serving_size": "1 bowl (300ml)",
            "category": "soup"
        },
        "french_toast": {
            "ingredients": [
                {"name": "bread", "amount": "8 slices", "category": "grain"},
                {"name": "eggs", "amount": "4", "category": "protein"},
                {"name": "milk", "amount": "1 cup", "category": "dairy"},
                {"name": "vanilla extract", "amount": "1 tsp", "category": "flavoring"},
                {"name": "cinnamon", "amount": "1 tsp", "category": "spice"}
            ],
            "nutrition_per_100g": {
                "calories": 242,
                "protein": 9,
                "carbs": 28,
                "fat": 11,
                "fiber": 1
            },
            "allergens": ["gluten", "eggs", "dairy"],
            "serving_size": "2 slices (150g)",
            "category": "breakfast"
        },
        "fried_calamari": {
            "ingredients": [
                {"name": "squid", "amount": "500g", "category": "seafood"},
                {"name": "flour", "amount": "1 cup", "category": "grain"},
                {"name": "eggs", "amount": "2", "category": "protein"},
                {"name": "vegetable oil", "amount": "4 cups", "category": "oil"},
                {"name": "marinara sauce", "amount": "1 cup", "category": "sauce"}
            ],
            "nutrition_per_100g": {
                "calories": 175,
                "protein": 15,
                "carbs": 13,
                "fat": 8,
                "fiber": 0.5
            },
            "allergens": ["gluten", "eggs", "mollusks"],
            "serving_size": "1 portion (150g)",
            "category": "appetizer"
        },
        "fried_rice": {
            "ingredients": [
                {"name": "rice", "amount": "3 cups", "category": "grain"},
                {"name": "eggs", "amount": "2", "category": "protein"},
                {"name": "peas", "amount": "1 cup", "category": "vegetable"},
                {"name": "carrots", "amount": "1 cup", "category": "vegetable"},
                {"name": "soy sauce", "amount": "3 tbsp", "category": "condiment"}
            ],
            "nutrition_per_100g": {
                "calories": 200,
                "protein": 6,
                "carbs": 40,
                "fat": 4,
                "fiber": 2
            },
            "allergens": ["eggs", "soy"],
            "serving_size": "1 serving (250g)",
            "category": "main_course"
        },
        "frozen_yogurt": {
            "ingredients": [
                {"name": "yogurt", "amount": "4 cups", "category": "dairy"},
                {"name": "sugar", "amount": "1/2 cup", "category": "sweetener"},
                {"name": "vanilla extract", "amount": "1 tsp", "category": "flavoring"},
                {"name": "berries", "amount": "1 cup", "category": "fruit"}
            ],
            "nutrition_per_100g": {
                "calories": 159,
                "protein": 4,
                "carbs": 30,
                "fat": 3,
                "fiber": 0.5
            },
            "allergens": ["dairy"],
            "serving_size": "1 cup (120g)",
            "category": "dessert"
        },
        "garlic_bread": {
            "ingredients": [
                {"name": "baguette", "amount": "1", "category": "grain"},
                {"name": "butter", "amount": "1/2 cup", "category": "dairy"},
                {"name": "garlic", "amount": "6 cloves", "category": "vegetable"},
                {"name": "parsley", "amount": "1/4 cup", "category": "herb"},
                {"name": "parmesan", "amount": "1/4 cup", "category": "dairy"}
            ],
            "nutrition_per_100g": {
                "calories": 350,
                "protein": 8,
                "carbs": 45,
                "fat": 15,
                "fiber": 2
            },
            "allergens": ["gluten", "dairy"],
            "serving_size": "2 slices (80g)",
            "category": "side_dish"
        },
        "gnocchi": {
            "ingredients": [
                {"name": "potatoes", "amount": "2 lbs", "category": "vegetable"},
                {"name": "flour", "amount": "2 cups", "category": "grain"},
                {"name": "egg", "amount": "1", "category": "protein"},
                {"name": "salt", "amount": "1 tsp", "category": "seasoning"},
                {"name": "nutmeg", "amount": "1/4 tsp", "category": "spice"}
            ],
            "nutrition_per_100g": {
                "calories": 201,
                "protein": 6,
                "carbs": 42,
                "fat": 1,
                "fiber": 2
            },
            "allergens": ["gluten", "eggs"],
            "serving_size": "1 cup (160g)",
            "category": "main_course"
        },
        "greek_salad": {
            "ingredients": [
                {"name": "cucumber", "amount": "1 large", "category": "vegetable"},
                {"name": "tomatoes", "amount": "4 medium", "category": "vegetable"},
                {"name": "red onion", "amount": "1 medium", "category": "vegetable"},
                {"name": "feta cheese", "amount": "200g", "category": "dairy"},
                {"name": "olives", "amount": "1/2 cup", "category": "vegetable"},
                {"name": "olive oil", "amount": "1/4 cup", "category": "oil"}
            ],
            "nutrition_per_100g": {
                "calories": 130,
                "protein": 4,
                "carbs": 6,
                "fat": 11,
                "fiber": 2
            },
            "allergens": ["dairy"],
            "serving_size": "1 bowl (200g)",
            "category": "salad"
        },
        "grilled_cheese_sandwich": {
            "ingredients": [
                {"name": "bread", "amount": "2 slices", "category": "grain"},
                {"name": "cheddar cheese", "amount": "2 slices", "category": "dairy"},
                {"name": "butter", "amount": "2 tbsp", "category": "dairy"}
            ],
            "nutrition_per_100g": {
                "calories": 350,
                "protein": 13,
                "carbs": 26,
                "fat": 22,
                "fiber": 1
            },
            "allergens": ["gluten", "dairy"],
            "serving_size": "1 sandwich (120g)",
            "category": "main_course"
        },
        "grilled_salmon": {
            "ingredients": [
                {"name": "salmon fillet", "amount": "200g", "category": "protein"},
                {"name": "lemon", "amount": "1", "category": "fruit"},
                {"name": "olive oil", "amount": "2 tbsp", "category": "oil"},
                {"name": "garlic", "amount": "2 cloves", "category": "vegetable"},
                {"name": "dill", "amount": "2 tbsp", "category": "herb"}
            ],
            "nutrition_per_100g": {
                "calories": 208,
                "protein": 22,
                "carbs": 0,
                "fat": 13,
                "fiber": 0
            },
            "allergens": ["fish"],
            "serving_size": "1 fillet (200g)",
            "category": "main_course"
        },
        "guacamole": {
            "ingredients": [
                {"name": "avocados", "amount": "3 ripe", "category": "fruit"},
                {"name": "lime juice", "amount": "2 tbsp", "category": "citrus"},
                {"name": "onion", "amount": "1/2 cup", "category": "vegetable"},
                {"name": "tomatoes", "amount": "1 medium", "category": "vegetable"},
                {"name": "cilantro", "amount": "1/4 cup", "category": "herb"}
            ],
            "nutrition_per_100g": {
                "calories": 160,
                "protein": 2,
                "carbs": 8,
                "fat": 14.7,
                "fiber": 6.7
            },
            "allergens": [],
            "serving_size": "1/4 cup (60g)",
            "category": "appetizer"
        },
        "gyoza": {
            "ingredients": [
                {"name": "ground pork", "amount": "1/2 pound", "category": "protein"},
                {"name": "cabbage", "amount": "2 cups", "category": "vegetable"},
                {"name": "gyoza wrappers", "amount": "30 pieces", "category": "grain"},
                {"name": "green onions", "amount": "2", "category": "vegetable"},
                {"name": "ginger", "amount": "1 tbsp", "category": "spice"},
                {"name": "soy sauce", "amount": "2 tbsp", "category": "condiment"}
            ],
            "nutrition_per_100g": {
                "calories": 225,
                "protein": 9,
                "carbs": 25,
                "fat": 10,
                "fiber": 1
            },
            "allergens": ["gluten", "soy"],
            "serving_size": "6 pieces (150g)",
            "category": "appetizer"
        },
        "hamburger": {
            "ingredients": [
                {"name": "ground beef", "amount": "200g", "category": "protein"},
                {"name": "hamburger bun", "amount": "1", "category": "grain"},
                {"name": "lettuce", "amount": "1 leaf", "category": "vegetable"},
                {"name": "tomato", "amount": "2 slices", "category": "vegetable"},
                {"name": "onion", "amount": "2 slices", "category": "vegetable"},
                {"name": "cheese", "amount": "1 slice", "category": "dairy"}
            ],
            "nutrition_per_100g": {
                "calories": 295,
                "protein": 17,
                "carbs": 24,
                "fat": 14,
                "fiber": 1.3
            },
            "allergens": ["gluten", "dairy"],
            "serving_size": "1 burger (250g)",
            "category": "main_course"
        },
        "hot_and_sour_soup": {
            "ingredients": [
                {"name": "tofu", "amount": "200g", "category": "protein"},
                {"name": "mushrooms", "amount": "1 cup", "category": "vegetable"},
                {"name": "bamboo shoots", "amount": "1/2 cup", "category": "vegetable"},
                {"name": "eggs", "amount": "2", "category": "protein"},
                {"name": "vinegar", "amount": "3 tbsp", "category": "condiment"},
                {"name": "soy sauce", "amount": "2 tbsp", "category": "condiment"}
            ],
            "nutrition_per_100g": {
                "calories": 90,
                "protein": 6,
                "carbs": 10,
                "fat": 3,
                "fiber": 1.5
            },
            "allergens": ["soy", "eggs"],
            "serving_size": "1 bowl (300ml)",
            "category": "soup"
        },
        "hot_dog": {
            "ingredients": [
                {"name": "hot dog", "amount": "1", "category": "protein"},
                {"name": "hot dog bun", "amount": "1", "category": "grain"},
                {"name": "mustard", "amount": "1 tbsp", "category": "condiment"},
                {"name": "ketchup", "amount": "1 tbsp", "category": "condiment"},
                {"name": "onions", "amount": "2 tbsp", "category": "vegetable"}
            ],
            "nutrition_per_100g": {
                "calories": 290,
                "protein": 11,
                "carbs": 32,
                "fat": 13,
                "fiber": 1.1
            },
            "allergens": ["gluten"],
            "serving_size": "1 hot dog (150g)",
            "category": "main_course"
        },
        "huevos_rancheros": {
            "ingredients": [
                {"name": "eggs", "amount": "2", "category": "protein"},
                {"name": "tortillas", "amount": "2", "category": "grain"},
                {"name": "black beans", "amount": "1 cup", "category": "legume"},
                {"name": "salsa", "amount": "1/2 cup", "category": "sauce"},
                {"name": "cheese", "amount": "1/4 cup", "category": "dairy"}
            ],
            "nutrition_per_100g": {
                "calories": 260,
                "protein": 14,
                "carbs": 28,
                "fat": 12,
                "fiber": 6
            },
            "allergens": ["eggs", "dairy"],
            "serving_size": "1 serving (300g)",
            "category": "breakfast"
        },
        "hummus": {
            "ingredients": [
                {"name": "chickpeas", "amount": "2 cups", "category": "legume"},
                {"name": "tahini", "amount": "1/3 cup", "category": "condiment"},
                {"name": "lemon juice", "amount": "1/4 cup", "category": "citrus"},
                {"name": "olive oil", "amount": "1/4 cup", "category": "oil"},
                {"name": "garlic", "amount": "2 cloves", "category": "vegetable"}
            ],
            "nutrition_per_100g": {
                "calories": 177,
                "protein": 8,
                "carbs": 20,
                "fat": 9,
                "fiber": 4
            },
            "allergens": ["sesame"],
            "serving_size": "1/4 cup (60g)",
            "category": "appetizer"
        },
        "ice_cream": {
            "ingredients": [
                {"name": "heavy cream", "amount": "2 cups", "category": "dairy"},
                {"name": "milk", "amount": "1 cup", "category": "dairy"},
                {"name": "sugar", "amount": "2/3 cup", "category": "sweetener"},
                {"name": "vanilla extract", "amount": "1 tsp", "category": "flavoring"},
                {"name": "egg yolks", "amount": "4", "category": "protein"}
            ],
            "nutrition_per_100g": {
                "calories": 207,
                "protein": 3.5,
                "carbs": 24,
                "fat": 11,
                "fiber": 0
            },
            "allergens": ["dairy", "eggs"],
            "serving_size": "1/2 cup (66g)",
            "category": "dessert"
        },
         "lasagna": {
            "ingredients": [
                {"name": "lasagna noodles", "amount": "12 sheets", "category": "grain"},
                {"name": "ground beef", "amount": "1 pound", "category": "protein"},
                {"name": "ricotta cheese", "amount": "15 oz", "category": "dairy"},
                {"name": "mozzarella", "amount": "1 pound", "category": "dairy"},
                {"name": "tomato sauce", "amount": "24 oz", "category": "sauce"},
                {"name": "parmesan", "amount": "1/2 cup", "category": "dairy"}
            ],
            "nutrition_per_100g": {
                "calories": 285,
                "protein": 16,
                "carbs": 22,
                "fat": 14,
                "fiber": 2
            },
            "allergens": ["gluten", "dairy"],
            "serving_size": "1 piece (250g)",
            "category": "main_course"
        },
        "lobster_bisque": {
            "ingredients": [
                {"name": "lobster", "amount": "2 pounds", "category": "seafood"},
                {"name": "heavy cream", "amount": "2 cups", "category": "dairy"},
                {"name": "shallots", "amount": "2", "category": "vegetable"},
                {"name": "cognac", "amount": "1/4 cup", "category": "alcohol"},
                {"name": "fish stock", "amount": "4 cups", "category": "liquid"}
            ],
            "nutrition_per_100g": {
                "calories": 185,
                "protein": 12,
                "carbs": 8,
                "fat": 11,
                "fiber": 0.5
            },
            "allergens": ["shellfish", "dairy"],
            "serving_size": "1 bowl (240ml)",
            "category": "soup"
        },
        "lobster_roll": {
            "ingredients": [
                {"name": "lobster meat", "amount": "1 pound", "category": "seafood"},
                {"name": "mayonnaise", "amount": "1/4 cup", "category": "condiment"},
                {"name": "celery", "amount": "2 stalks", "category": "vegetable"},
                {"name": "hot dog buns", "amount": "4", "category": "grain"},
                {"name": "lemon juice", "amount": "1 tbsp", "category": "citrus"}
            ],
            "nutrition_per_100g": {
                "calories": 220,
                "protein": 19,
                "carbs": 18,
                "fat": 9,
                "fiber": 1
            },
            "allergens": ["shellfish", "gluten", "eggs"],
            "serving_size": "1 roll (170g)",
            "category": "main_course"
        },
        "macaroni_and_cheese": {
            "ingredients": [
                {"name": "macaroni", "amount": "1 pound", "category": "grain"},
                {"name": "cheddar cheese", "amount": "3 cups", "category": "dairy"},
                {"name": "milk", "amount": "2 cups", "category": "dairy"},
                {"name": "butter", "amount": "1/4 cup", "category": "dairy"},
                {"name": "flour", "amount": "1/4 cup", "category": "grain"}
            ],
            "nutrition_per_100g": {
                "calories": 370,
                "protein": 14,
                "carbs": 43,
                "fat": 18,
                "fiber": 1.7
            },
            "allergens": ["gluten", "dairy"],
            "serving_size": "1 cup (200g)",
            "category": "main_course"
        },
        "macarons": {
            "ingredients": [
                {"name": "almond flour", "amount": "1 cup", "category": "nut"},
                {"name": "powdered sugar", "amount": "2 cups", "category": "sweetener"},
                {"name": "egg whites", "amount": "3", "category": "protein"},
                {"name": "granulated sugar", "amount": "1/4 cup", "category": "sweetener"},
                {"name": "food coloring", "amount": "as needed", "category": "other"}
            ],
            "nutrition_per_100g": {
                "calories": 400,
                "protein": 8,
                "carbs": 75,
                "fat": 9,
                "fiber": 2
            },
            "allergens": ["nuts", "eggs"],
            "serving_size": "2 cookies (25g)",
            "category": "dessert"
        },
        "miso_soup": {
            "ingredients": [
                {"name": "dashi stock", "amount": "4 cups", "category": "liquid"},
                {"name": "miso paste", "amount": "3 tbsp", "category": "condiment"},
                {"name": "tofu", "amount": "200g", "category": "protein"},
                {"name": "seaweed", "amount": "2 sheets", "category": "vegetable"},
                {"name": "green onions", "amount": "2", "category": "vegetable"}
            ],
            "nutrition_per_100g": {
                "calories": 40,
                "protein": 3,
                "carbs": 5,
                "fat": 1,
                "fiber": 1
            },
            "allergens": ["soy"],
            "serving_size": "1 bowl (240ml)",
            "category": "soup"
        },
        "mussels": {
            "ingredients": [
                {"name": "mussels", "amount": "2 pounds", "category": "seafood"},
                {"name": "white wine", "amount": "1 cup", "category": "alcohol"},
                {"name": "garlic", "amount": "4 cloves", "category": "vegetable"},
                {"name": "butter", "amount": "2 tbsp", "category": "dairy"},
                {"name": "parsley", "amount": "1/4 cup", "category": "herb"}
            ],
            "nutrition_per_100g": {
                "calories": 172,
                "protein": 24,
                "carbs": 7,
                "fat": 5,
                "fiber": 0
            },
            "allergens": ["shellfish", "dairy"],
            "serving_size": "1 pound (450g)",
            "category": "main_course"
        },
        "nachos": {
            "ingredients": [
                {"name": "tortilla chips", "amount": "400g", "category": "grain"},
                {"name": "cheddar cheese", "amount": "2 cups", "category": "dairy"},
                {"name": "refried beans", "amount": "1 cup", "category": "legume"},
                {"name": "jalapenos", "amount": "1/2 cup", "category": "vegetable"},
                {"name": "sour cream", "amount": "1/2 cup", "category": "dairy"},
                {"name": "guacamole", "amount": "1 cup", "category": "condiment"}
            ],
            "nutrition_per_100g": {
                "calories": 346,
                "protein": 10,
                "carbs": 32,
                "fat": 20,
                "fiber": 4
            },
            "allergens": ["dairy", "gluten"],
            "serving_size": "1 portion (250g)",
            "category": "appetizer"
        },
        "omelette": {
            "ingredients": [
                {"name": "eggs", "amount": "3", "category": "protein"},
                {"name": "milk", "amount": "2 tbsp", "category": "dairy"},
                {"name": "cheese", "amount": "1/2 cup", "category": "dairy"},
                {"name": "butter", "amount": "1 tbsp", "category": "dairy"},
                {"name": "herbs", "amount": "1 tbsp", "category": "herb"}
            ],
            "nutrition_per_100g": {
                "calories": 154,
                "protein": 13,
                "carbs": 1,
                "fat": 11,
                "fiber": 0
            },
            "allergens": ["eggs", "dairy"],
            "serving_size": "1 omelette (150g)",
            "category": "breakfast"
        },
        "onion_rings": {
            "ingredients": [
                {"name": "onions", "amount": "2 large", "category": "vegetable"},
                {"name": "flour", "amount": "1.5 cups", "category": "grain"},
                {"name": "buttermilk", "amount": "1 cup", "category": "dairy"},
                {"name": "vegetable oil", "amount": "4 cups", "category": "oil"},
                {"name": "seasonings", "amount": "2 tbsp", "category": "spice"}
            ],
            "nutrition_per_100g": {
                "calories": 332,
                "protein": 4,
                "carbs": 41,
                "fat": 17,
                "fiber": 2
            },
            "allergens": ["gluten", "dairy"],
            "serving_size": "6 rings (120g)",
            "category": "side_dish"
        },
        "oysters": {
            "ingredients": [
                {"name": "oysters", "amount": "12", "category": "seafood"},
                {"name": "lemon", "amount": "1", "category": "fruit"},
                {"name": "mignonette sauce", "amount": "1/4 cup", "category": "condiment"},
                {"name": "hot sauce", "amount": "to taste", "category": "condiment"},
                {"name": "horseradish", "amount": "2 tbsp", "category": "condiment"}
            ],
            "nutrition_per_100g": {
                "calories": 69,
                "protein": 9,
                "carbs": 4,
                "fat": 2,
                "fiber": 0
            },
            "allergens": ["shellfish"],
            "serving_size": "6 oysters (100g)",
            "category": "appetizer"
        },
        "pad_thai": {
            "ingredients": [
                {"name": "rice noodles", "amount": "8 oz", "category": "grain"},
                {"name": "shrimp", "amount": "1/2 pound", "category": "seafood"},
                {"name": "tofu", "amount": "200g", "category": "protein"},
                {"name": "bean sprouts", "amount": "2 cups", "category": "vegetable"},
                {"name": "peanuts", "amount": "1/2 cup", "category": "nut"},
                {"name": "tamarind sauce", "amount": "3 tbsp", "category": "sauce"}
            ],
            "nutrition_per_100g": {
                "calories": 300,
                "protein": 15,
                "carbs": 40,
                "fat": 10,
                "fiber": 2
            },
            "allergens": ["shellfish", "peanuts", "soy"],
            "serving_size": "1 plate (300g)",
            "category": "main_course"
        },
        "paella": {
            "ingredients": [
                {"name": "rice", "amount": "2 cups", "category": "grain"},
                {"name": "chicken", "amount": "500g", "category": "protein"},
                {"name": "shrimp", "amount": "250g", "category": "seafood"},
                {"name": "mussels", "amount": "500g", "category": "seafood"},
                {"name": "saffron", "amount": "1 pinch", "category": "spice"},
                {"name": "peas", "amount": "1 cup", "category": "vegetable"}
            ],
            "nutrition_per_100g": {
                "calories": 255,
                "protein": 18,
                "carbs": 30,
                "fat": 8,
                "fiber": 2
            },
            "allergens": ["shellfish"],
            "serving_size": "1 portion (350g)",
            "category": "main_course"
        },
        "pancakes": {
            "ingredients": [
                {"name": "flour", "amount": "1.5 cups", "category": "grain"},
                {"name": "milk", "amount": "1.25 cups", "category": "dairy"},
                {"name": "eggs", "amount": "1", "category": "protein"},
                {"name": "butter", "amount": "3 tbsp", "category": "dairy"},
                {"name": "maple syrup", "amount": "1/4 cup", "category": "sweetener"}
            ],
            "nutrition_per_100g": {
                "calories": 227,
                "protein": 6,
                "carbs": 38,
                "fat": 6,
                "fiber": 1
            },
            "allergens": ["gluten", "dairy", "eggs"],
            "serving_size": "3 pancakes (150g)",
            "category": "breakfast"
        },
        "panna_cotta": {
            "ingredients": [
                {"name": "heavy cream", "amount": "2 cups", "category": "dairy"},
                {"name": "sugar", "amount": "1/4 cup", "category": "sweetener"},
                {"name": "vanilla bean", "amount": "1", "category": "flavoring"},
                {"name": "gelatin", "amount": "2.5 tsp", "category": "gelatin"},
                {"name": "berry sauce", "amount": "1/2 cup", "category": "sauce"}
            ],
            "nutrition_per_100g": {
                "calories": 295,
                "protein": 2,
                "carbs": 15,
                "fat": 25,
                "fiber": 0
            },
            "allergens": ["dairy"],
            "serving_size": "1 serving (120g)",
            "category": "dessert"
        },
        "peking_duck": {
            "ingredients": [
                {"name": "whole duck", "amount": "4-5 lbs", "category": "protein"},
                {"name": "hoisin sauce", "amount": "1/2 cup", "category": "sauce"},
                {"name": "scallions", "amount": "1 bunch", "category": "vegetable"},
                {"name": "cucumber", "amount": "1", "category": "vegetable"},
                {"name": "pancakes", "amount": "16 pieces", "category": "grain"}
            ],
            "nutrition_per_100g": {
                "calories": 401,
                "protein": 25,
                "carbs": 8,
                "fat": 32,
                "fiber": 1
            },
            "allergens": ["gluten", "soy"],
            "serving_size": "200g with pancakes",
            "category": "main_course"
        },
        "pho": {
            "ingredients": [
                {"name": "rice noodles", "amount": "1 pound", "category": "grain"},
                {"name": "beef brisket", "amount": "1 pound", "category": "protein"},
                {"name": "beef broth", "amount": "8 cups", "category": "liquid"},
                {"name": "bean sprouts", "amount": "2 cups", "category": "vegetable"},
                {"name": "thai basil", "amount": "1 cup", "category": "herb"},
                {"name": "star anise", "amount": "3", "category": "spice"}
            ],
            "nutrition_per_100g": {
                "calories": 215,
                "protein": 15,
                "carbs": 30,
                "fat": 5,
                "fiber": 2
            },
            "allergens": [],
            "serving_size": "1 bowl (500g)",
            "category": "soup"
        },
        "pizza": {
            "ingredients": [
                {"name": "pizza dough", "amount": "1 pound", "category": "grain"},
                {"name": "tomato sauce", "amount": "1 cup", "category": "sauce"},
                {"name": "mozzarella", "amount": "2 cups", "category": "dairy"},
                {"name": "olive oil", "amount": "2 tbsp", "category": "oil"},
                {"name": "basil", "amount": "1/4 cup", "category": "herb"}
            ],
            "nutrition_per_100g": {
                "calories": 266,
                "protein": 11,
                "carbs": 33,
                "fat": 10,
                "fiber": 2
            },
            "allergens": ["gluten", "dairy"],
            "serving_size": "1 slice (100g)",
            "category": "main_course"
        },
        "pork_chop": {
            "ingredients": [
                {"name": "pork chop", "amount": "8 oz", "category": "protein"},
                {"name": "garlic", "amount": "3 cloves", "category": "vegetable"},
                {"name": "rosemary", "amount": "2 sprigs", "category": "herb"},
                {"name": "butter", "amount": "2 tbsp", "category": "dairy"},
                {"name": "olive oil", "amount": "2 tbsp", "category": "oil"}
            ],
            "nutrition_per_100g": {
                "calories": 242,
                "protein": 26,
                "carbs": 0,
                "fat": 15,
                "fiber": 0
            },
            "allergens": ["dairy"],
            "serving_size": "1 chop (225g)",
            "category": "main_course"
        },
        "poutine": {
            "ingredients": [
                {"name": "french fries", "amount": "4 cups", "category": "vegetable"},
                {"name": "cheese curds", "amount": "2 cups", "category": "dairy"},
                {"name": "gravy", "amount": "2 cups", "category": "sauce"},
                {"name": "vegetable oil", "amount": "for frying", "category": "oil"}
            ],
            "nutrition_per_100g": {
                "calories": 365,
                "protein": 12,
                "carbs": 35,
                "fat": 22,
                "fiber": 3
            },
            "allergens": ["dairy"],
            "serving_size": "1 serving (300g)",
            "category": "main_course"
        },
        "pulled_pork_sandwich": {
            "ingredients": [
                {"name": "pork shoulder", "amount": "4 lbs", "category": "protein"},
                {"name": "bbq sauce", "amount": "2 cups", "category": "sauce"},
                {"name": "burger buns", "amount": "8", "category": "grain"},
                {"name": "coleslaw", "amount": "2 cups", "category": "vegetable"},
                {"name": "spice rub", "amount": "1/4 cup", "category": "seasoning"}
            ],
            "nutrition_per_100g": {
                "calories": 250,
                "protein": 18,
                "carbs": 25,
                "fat": 12,
                "fiber": 1
            },
            "allergens": ["gluten"],
            "serving_size": "1 sandwich (200g)",
            "category": "main_course"
        },
         "ramen": {
            "ingredients": [
                {"name": "ramen noodles", "amount": "200g", "category": "grain"},
                {"name": "pork belly", "amount": "200g", "category": "protein"},
                {"name": "soy sauce", "amount": "2 tbsp", "category": "condiment"},
                {"name": "soft boiled egg", "amount": "2", "category": "protein"},
                {"name": "nori", "amount": "2 sheets", "category": "vegetable"},
                {"name": "green onions", "amount": "1/4 cup", "category": "vegetable"}
            ],
            "nutrition_per_100g": {
                "calories": 436,
                "protein": 18,
                "carbs": 65,
                "fat": 15,
                "fiber": 3
            },
            "allergens": ["gluten", "eggs", "soy"],
            "serving_size": "1 bowl (500g)",
            "category": "main_course"
        },
        "ravioli": {
            "ingredients": [
                {"name": "pasta dough", "amount": "1 pound", "category": "grain"},
                {"name": "ricotta cheese", "amount": "2 cups", "category": "dairy"},
                {"name": "parmesan", "amount": "1/2 cup", "category": "dairy"},
                {"name": "spinach", "amount": "2 cups", "category": "vegetable"},
                {"name": "marinara sauce", "amount": "2 cups", "category": "sauce"}
            ],
            "nutrition_per_100g": {
                "calories": 290,
                "protein": 14,
                "carbs": 42,
                "fat": 8,
                "fiber": 2
            },
            "allergens": ["gluten", "dairy", "eggs"],
            "serving_size": "1 serving (250g)",
            "category": "main_course"
        },
        "red_velvet_cake": {
            "ingredients": [
                {"name": "flour", "amount": "2.5 cups", "category": "grain"},
                {"name": "cocoa powder", "amount": "2 tbsp", "category": "sweet"},
                {"name": "cream cheese", "amount": "16 oz", "category": "dairy"},
                {"name": "buttermilk", "amount": "1 cup", "category": "dairy"},
                {"name": "red food coloring", "amount": "2 oz", "category": "other"}
            ],
            "nutrition_per_100g": {
                "calories": 385,
                "protein": 5,
                "carbs": 55,
                "fat": 17,
                "fiber": 1
            },
            "allergens": ["gluten", "dairy", "eggs"],
            "serving_size": "1 slice (125g)",
            "category": "dessert"
        },
        "risotto": {
            "ingredients": [
                {"name": "arborio rice", "amount": "2 cups", "category": "grain"},
                {"name": "mushrooms", "amount": "8 oz", "category": "vegetable"},
                {"name": "parmesan", "amount": "1 cup", "category": "dairy"},
                {"name": "white wine", "amount": "1/2 cup", "category": "alcohol"},
                {"name": "chicken broth", "amount": "6 cups", "category": "liquid"}
            ],
            "nutrition_per_100g": {
                "calories": 170,
                "protein": 5,
                "carbs": 29,
                "fat": 4,
                "fiber": 1
            },
            "allergens": ["dairy"],
            "serving_size": "1 serving (200g)",
            "category": "main_course"
        },
        "samosa": {
            "ingredients": [
                {"name": "flour", "amount": "2 cups", "category": "grain"},
                {"name": "potatoes", "amount": "3 medium", "category": "vegetable"},
                {"name": "peas", "amount": "1 cup", "category": "vegetable"},
                {"name": "onion", "amount": "1 large", "category": "vegetable"},
                {"name": "garam masala", "amount": "2 tbsp", "category": "spice"}
            ],
            "nutrition_per_100g": {
                "calories": 262,
                "protein": 6,
                "carbs": 36,
                "fat": 11,
                "fiber": 3
            },
            "allergens": ["gluten"],
            "serving_size": "2 samosas (120g)",
            "category": "appetizer"
        },
        "sashimi": {
            "ingredients": [
                {"name": "fresh tuna", "amount": "200g", "category": "protein"},
                {"name": "fresh salmon", "amount": "200g", "category": "protein"},
                {"name": "wasabi", "amount": "2 tsp", "category": "condiment"},
                {"name": "soy sauce", "amount": "1/4 cup", "category": "condiment"},
                {"name": "pickled ginger", "amount": "50g", "category": "condiment"}
            ],
            "nutrition_per_100g": {
                "calories": 130,
                "protein": 26,
                "carbs": 0,
                "fat": 2,
                "fiber": 0
            },
            "allergens": ["fish", "soy"],
            "serving_size": "6 pieces (100g)",
            "category": "main_course"
        },
        "scallops": {
            "ingredients": [
                {"name": "sea scallops", "amount": "1 pound", "category": "seafood"},
                {"name": "butter", "amount": "2 tbsp", "category": "dairy"},
                {"name": "garlic", "amount": "3 cloves", "category": "vegetable"},
                {"name": "lemon", "amount": "1", "category": "fruit"},
                {"name": "parsley", "amount": "1/4 cup", "category": "herb"}
            ],
            "nutrition_per_100g": {
                "calories": 105,
                "protein": 20,
                "carbs": 3,
                "fat": 2,
                "fiber": 0
            },
            "allergens": ["shellfish", "dairy"],
            "serving_size": "3-4 scallops (100g)",
            "category": "main_course"
        },
        "seaweed_salad": {
            "ingredients": [
                {"name": "wakame seaweed", "amount": "2 oz", "category": "vegetable"},
                {"name": "sesame oil", "amount": "2 tbsp", "category": "oil"},
                {"name": "rice vinegar", "amount": "2 tbsp", "category": "condiment"},
                {"name": "soy sauce", "amount": "1 tbsp", "category": "condiment"},
                {"name": "sesame seeds", "amount": "1 tbsp", "category": "seed"}
            ],
            "nutrition_per_100g": {
                "calories": 130,
                "protein": 3,
                "carbs": 15,
                "fat": 7,
                "fiber": 4
            },
            "allergens": ["sesame", "soy"],
            "serving_size": "1 serving (120g)",
            "category": "salad"
        },
        "shrimp_and_grits": {
            "ingredients": [
                {"name": "shrimp", "amount": "1 pound", "category": "seafood"},
                {"name": "grits", "amount": "1 cup", "category": "grain"},
                {"name": "cheddar cheese", "amount": "1 cup", "category": "dairy"},
                {"name": "bacon", "amount": "4 slices", "category": "protein"},
                {"name": "butter", "amount": "1/4 cup", "category": "dairy"}
            ],
            "nutrition_per_100g": {
                "calories": 265,
                "protein": 18,
                "carbs": 22,
                "fat": 12,
                "fiber": 1
            },
            "allergens": ["shellfish", "dairy"],
            "serving_size": "1 serving (250g)",
            "category": "main_course"
        },
        "spaghetti_bolognese": {
            "ingredients": [
                {"name": "spaghetti", "amount": "1 pound", "category": "grain"},
                {"name": "ground beef", "amount": "1 pound", "category": "protein"},
                {"name": "tomato sauce", "amount": "28 oz", "category": "sauce"},
                {"name": "onion", "amount": "1 large", "category": "vegetable"},
                {"name": "parmesan", "amount": "1/2 cup", "category": "dairy"}
            ],
            "nutrition_per_100g": {
                "calories": 285,
                "protein": 12,
                "carbs": 42,
                "fat": 9,
                "fiber": 2
            },
            "allergens": ["gluten", "dairy"],
            "serving_size": "1 serving (300g)",
            "category": "main_course"
        },
        "spaghetti_carbonara": {
            "ingredients": [
                {"name": "spaghetti", "amount": "1 pound", "category": "grain"},
                {"name": "eggs", "amount": "4", "category": "protein"},
                {"name": "pancetta", "amount": "8 oz", "category": "protein"},
                {"name": "pecorino romano", "amount": "1 cup", "category": "dairy"},
                {"name": "black pepper", "amount": "2 tsp", "category": "spice"}
            ],
            "nutrition_per_100g": {
                "calories": 310,
                "protein": 14,
                "carbs": 40,
                "fat": 12,
                "fiber": 2
            },
            "allergens": ["gluten", "dairy", "eggs"],
            "serving_size": "1 serving (250g)",
            "category": "main_course"
        },
        "spring_rolls": {
            "ingredients": [
                {"name": "rice paper", "amount": "12 sheets", "category": "grain"},
                {"name": "shrimp", "amount": "1/2 pound", "category": "seafood"},
                {"name": "rice noodles", "amount": "4 oz", "category": "grain"},
                {"name": "carrots", "amount": "2", "category": "vegetable"},
                {"name": "lettuce", "amount": "1 head", "category": "vegetable"}
            ],
            "nutrition_per_100g": {
                "calories": 145,
                "protein": 8,
                "carbs": 22,
                "fat": 3,
                "fiber": 2
            },
            "allergens": ["shellfish"],
            "serving_size": "2 rolls (120g)",
            "category": "appetizer"
        },
        "steak": {
            "ingredients": [
                {"name": "ribeye steak", "amount": "16 oz", "category": "protein"},
                {"name": "butter", "amount": "2 tbsp", "category": "dairy"},
                {"name": "garlic", "amount": "4 cloves", "category": "vegetable"},
                {"name": "rosemary", "amount": "2 sprigs", "category": "herb"},
                {"name": "black pepper", "amount": "1 tbsp", "category": "spice"}
            ],
            "nutrition_per_100g": {
                "calories": 252,
                "protein": 25,
                "carbs": 0,
                "fat": 17,
                "fiber": 0
            },
            "allergens": ["dairy"],
            "serving_size": "1 steak (225g)",
            "category": "main_course"
        },
        "strawberry_shortcake": {
            "ingredients": [
                {"name": "flour", "amount": "2 cups", "category": "grain"},
                {"name": "strawberries", "amount": "1 pound", "category": "fruit"},
                {"name": "heavy cream", "amount": "2 cups", "category": "dairy"},
                {"name": "sugar", "amount": "1/2 cup", "category": "sweetener"},
                {"name": "butter", "amount": "1/2 cup", "category": "dairy"}
            ],
            "nutrition_per_100g": {
                "calories": 275,
                "protein": 3,
                "carbs": 35,
                "fat": 14,
                "fiber": 2
            },
            "allergens": ["gluten", "dairy"],
            "serving_size": "1 serving (150g)",
            "category": "dessert"
        },
        "sushi": {
            "ingredients": [
                {"name": "sushi rice", "amount": "2 cups", "category": "grain"},
                {"name": "nori sheets", "amount": "6", "category": "vegetable"},
                {"name": "fresh fish", "amount": "1/2 pound", "category": "protein"},
                {"name": "avocado", "amount": "1", "category": "vegetable"},
                {"name": "cucumber", "amount": "1", "category": "vegetable"},
                {"name": "rice vinegar", "amount": "1/4 cup", "category": "condiment"}
            ],
            "nutrition_per_100g": {
                "calories": 150,
                "protein": 6,
                "carbs": 30,
                "fat": 2,
                "fiber": 1
            },
            "allergens": ["fish", "soy"],
            "serving_size": "6 pieces (150g)",
            "category": "main_course"
        },
        "tacos": {
            "ingredients": [
                {"name": "corn tortillas", "amount": "8", "category": "grain"},
                {"name": "ground beef", "amount": "1 pound", "category": "protein"},
                {"name": "lettuce", "amount": "2 cups", "category": "vegetable"},
                {"name": "cheese", "amount": "1 cup", "category": "dairy"},
                {"name": "tomatoes", "amount": "2", "category": "vegetable"}
            ],
            "nutrition_per_100g": {
                "calories": 210,
                "protein": 12,
                "carbs": 18,
                "fat": 11,
                "fiber": 3
            },
            "allergens": ["dairy"],
            "serving_size": "2 tacos (200g)",
            "category": "main_course"
        },
        "takoyaki": {
            "ingredients": [
                {"name": "flour", "amount": "1 cup", "category": "grain"},
                {"name": "octopus", "amount": "1/2 pound", "category": "seafood"},
                {"name": "green onion", "amount": "1/4 cup", "category": "vegetable"},
                {"name": "dashi", "amount": "1 cup", "category": "liquid"},
                {"name": "takoyaki sauce", "amount": "1/4 cup", "category": "sauce"}
            ],
            "nutrition_per_100g": {
                "calories": 180,
                "protein": 8,
                "carbs": 25,
                "fat": 6,
                "fiber": 1
            },
            "allergens": ["gluten", "mollusks"],
            "serving_size": "6 pieces (120g)",
            "category": "appetizer"
        },
        "tiramisu": {
            "ingredients": [
                {"name": "ladyfingers", "amount": "24", "category": "grain"},
                {"name": "mascarpone", "amount": "16 oz", "category": "dairy"},
                {"name": "coffee", "amount": "1 cup", "category": "beverage"},
                {"name": "eggs", "amount": "4", "category": "protein"},
                {"name": "cocoa powder", "amount": "2 tbsp", "category": "sweet"}
            ],
            "nutrition_per_100g": {
                "calories": 350,
                "protein": 6,
                "carbs": 30,
                "fat": 23,
                "fiber": 1
            },
            "allergens": ["gluten", "dairy", "eggs"],
            "serving_size": "1 piece (120g)",
            "category": "dessert"
        },
        "tuna_tartare": {
            "ingredients": [
                {"name": "fresh tuna", "amount": "1 pound", "category": "protein"},
                {"name": "avocado", "amount": "1", "category": "vegetable"},
                {"name": "soy sauce", "amount": "2 tbsp", "category": "condiment"},
                {"name": "sesame oil", "amount": "1 tbsp", "category": "oil"},
                {"name": "green onions", "amount": "1/4 cup", "category": "vegetable"}
            ],
            "nutrition_per_100g": {
                "calories": 185,
                "protein": 25,
                "carbs": 2,
                "fat": 9,
                "fiber": 1
            },
            "allergens": ["fish", "soy", "sesame"],
            "serving_size": "1 serving (120g)",
            "category": "appetizer"
        },
        "waffles": {
            "ingredients": [
                {"name": "flour", "amount": "2 cups", "category": "grain"},
                {"name": "milk", "amount": "1.75 cups", "category": "dairy"},
                {"name": "eggs", "amount": "2", "category": "protein"},
                {"name": "butter", "amount": "1/2 cup", "category": "dairy"},
                {"name": "maple syrup", "amount": "1/2 cup", "category": "sweetener"}
            ],
            "nutrition_per_100g": {
                "calories": 290,
                "protein": 8,
                "carbs": 40,
                "fat": 12,
                "fiber": 1
            },
            "allergens": ["gluten", "dairy", "eggs"],
            "serving_size": "2 waffles (150g)",
            "category": "breakfast"
        }
    }
    return food_db

def add_health_info(food_db):
    """Add health information and warnings to each food item"""
    
    allergens_check = {
        "lactose": ["milk", "cheese", "cream", "butter", "yogurt"],
        "gluten": ["wheat", "flour", "pasta", "bread", "phyllo"],
        "histamine": ["avocado", "tomatoes", "spinach", "eggplant"],
        "salicylate": ["pineapple", "spinach", "eggplant", "strawberry"],
        "eggs": ["egg", "mayonnaise"],
        "nuts": ["peanut", "almond", "walnut", "cashew", "pistachio"],
        "shellfish": ["shrimp", "crab", "lobster", "mussel"],
        "soy": ["soy", "tofu", "soybean"]
    }
    
    for food_name, food_info in food_db.items():
        # Add dietary classifications
        food_info["dietary_info"] = []
        
        calories = food_info["nutrition_per_100g"]["calories"]
        if calories < 200:
            food_info["dietary_info"].append("low-calorie")
        elif calories > 400:
            food_info["dietary_info"].append("high-calorie")
            
        protein = food_info["nutrition_per_100g"]["protein"]
        if protein > 20:
            food_info["dietary_info"].append("high-protein")
            
        carbs = food_info["nutrition_per_100g"]["carbs"]
        if carbs < 10:
            food_info["dietary_info"].append("low-carb")
        
        # Check for allergens in ingredients
        detected_allergens = set()
        for ingredient in food_info["ingredients"]:
            for allergen_type, triggers in allergens_check.items():
                if any(trigger in ingredient["name"].lower() for trigger in triggers):
                    detected_allergens.add(allergen_type)
        
        food_info["allergens"] = list(detected_allergens)
    
    return food_db

if __name__ == "__main__":
    # Create initial database
    food_db = create_food101_database()
    
    # Add health information
    food_db = add_health_info(food_db)
    
    # Save to file
    with open('food101_database.json', 'w') as f:
        json.dump(food_db, f, indent=4)
    
    # Print sample entry
    print("\nSample database entry:")
    print(json.dumps(list(food_db.items())[0], indent=2))