USERS = {
    "+14155552671": {
        "name": "Alice Johnson",
        "nutrition_goals": {
            "daily_calories": 2000,
            "protein": "130g",
            "carbs": "225g",
            "fat": "65g"
        },
        "dietary_restrictions": ["gluten-free"],
        "preferences": ["Mediterranean", "Asian"]
    },
    "+14155552672": {
        "name": "Bob Smith",
        "nutrition_goals": {
            "daily_calories": 2500,
            "protein": "180g",
            "carbs": "275g",
            "fat": "80g"
        },
        "dietary_restrictions": ["dairy-free"],
        "preferences": ["High-protein", "Mexican"]
    }
}

CHEFS = [
    {
        "id": 1,
        "name": "Chef Maria Rodriguez",
        "image": "https://example.com/chef1.jpg",
        "specialties": ["Mediterranean", "Spanish", "Healthy"],
        "rating": 4.8,
        "bio": "Specializing in Mediterranean cuisine with a modern twist. Expert in gluten-free cooking.",
        "years_experience": 12,
        "location": "San Francisco, CA"
    },
    {
        "id": 2,
        "name": "Chef John Lee",
        "image": "https://example.com/chef2.jpg",
        "specialties": ["Asian", "Fusion", "Gluten-free"],
        "rating": 4.9,
        "bio": "Master of Asian fusion cuisine. Trained in Japan and Korea.",
        "years_experience": 15,
        "location": "San Francisco, CA"
    },
    {
        "id": 3,
        "name": "Chef Sarah Williams",
        "image": "https://example.com/chef3.jpg",
        "specialties": ["High-protein", "Keto", "Meal-prep"],
        "rating": 4.7,
        "bio": "Sports nutrition specialist. Former restaurant owner turned personal chef.",
        "years_experience": 8,
        "location": "Oakland, CA"
    },
    {
        "id": 4,
        "name": "Chef Michael Torres",
        "image": "https://example.com/chef4.jpg",
        "specialties": ["Mexican", "Latin American", "Vegan"],
        "rating": 4.8,
        "bio": "Traditional Mexican cuisine with a healthy, modern approach.",
        "years_experience": 10,
        "location": "Berkeley, CA"
    },
    {
        "id": 5,
        "name": "Chef Emily Chen",
        "image": "https://example.com/chef5.jpg",
        "specialties": ["Chinese", "Dim Sum", "Seafood"],
        "rating": 4.9,
        "bio": "Third-generation chef specializing in authentic Chinese cuisine.",
        "years_experience": 20,
        "location": "San Francisco, CA"
    }
]

MENUS = [
    {
        "id": 1,
        "chef_id": 1,
        "name": "Mediterranean Wellness",
        "image": "https://example.com/menu1.jpg",
        "description": "A perfect blend of healthy Mediterranean favorites",
        "price_per_meal": 25,
        "meals": [
            {
                "name": "Greek Salad Bowl",
                "image": "https://example.com/meal1.jpg",
                "calories": 450,
                "protein": "25g",
                "carbs": "35g",
                "fat": "28g",
                "description": "Fresh mixed greens, cherry tomatoes, cucumber, red onion, kalamata olives, and feta cheese"
            },
            {
                "name": "Grilled Chicken Souvlaki",
                "image": "https://example.com/meal2.jpg",
                "calories": 550,
                "protein": "45g",
                "carbs": "40g",
                "fat": "22g",
                "description": "Marinated chicken skewers with quinoa and roasted vegetables"
            }
        ]
    },
    {
        "id": 2,
        "chef_id": 2,
        "name": "Asian Fusion Light",
        "image": "https://example.com/menu2.jpg",
        "description": "Modern Asian cuisine with a healthy twist",
        "price_per_meal": 28,
        "meals": [
            {
                "name": "Tofu Stir-Fry Bowl",
                "image": "https://example.com/meal3.jpg",
                "calories": 400,
                "protein": "22g",
                "carbs": "45g",
                "fat": "18g",
                "description": "Crispy tofu with mixed vegetables in a light ginger sauce"
            },
            {
                "name": "Salmon Poke Bowl",
                "image": "https://example.com/meal4.jpg",
                "calories": 500,
                "protein": "35g",
                "carbs": "48g",
                "fat": "24g",
                "description": "Fresh salmon, avocado, and vegetables over brown rice"
            }
        ]
    },
    {
        "id": 3,
        "chef_id": 3,
        "name": "High Performance Meals",
        "image": "https://example.com/menu3.jpg",
        "description": "Protein-rich meals for active lifestyles",
        "price_per_meal": 30,
        "meals": [
            {
                "name": "Grilled Steak Bowl",
                "image": "https://example.com/meal5.jpg",
                "calories": 600,
                "protein": "45g",
                "carbs": "50g",
                "fat": "25g",
                "description": "Grass-fed steak with sweet potato and grilled vegetables"
            }
        ]
    },
    {
        "id": 4,
        "chef_id": 4,
        "name": "Modern Mexican",
        "image": "https://example.com/menu4.jpg",
        "description": "Healthy takes on Mexican classics",
        "price_per_meal": 26,
        "meals": [
            {
                "name": "Chicken Fajita Bowl",
                "image": "https://example.com/meal6.jpg",
                "calories": 550,
                "protein": "40g",
                "carbs": "45g",
                "fat": "22g",
                "description": "Grilled chicken with bell peppers, onions, and cauliflower rice"
            }
        ]
    },
    {
        "id": 5,
        "chef_id": 5,
        "name": "Authentic Chinese",
        "image": "https://example.com/menu5.jpg",
        "description": "Traditional Chinese dishes with a healthy approach",
        "price_per_meal": 27,
        "meals": [
            {
                "name": "Steamed Fish with Ginger",
                "image": "https://example.com/meal7.jpg",
                "calories": 400,
                "protein": "35g",
                "carbs": "25g",
                "fat": "20g",
                "description": "Fresh fish steamed with ginger, scallions, and light soy sauce"
            }
        ]
    }
] 