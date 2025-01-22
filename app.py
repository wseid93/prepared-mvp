from flask import Flask, render_template, request, jsonify
import phonenumbers
from mock_data import USERS, CHEFS, MENUS

app = Flask(__name__)

def validate_phone_number(phone):
    try:
        # Add '+' if not present
        if not phone.startswith('+'):
            phone = '+' + phone
        parsed = phonenumbers.parse(phone, "US")
        return phonenumbers.is_valid_number(parsed), phone
    except:
        return False, None

def get_recommended_chefs(user_data):
    recommended = []
    for chef in CHEFS:
        if any(specialty in user_data["preferences"] for specialty in chef["specialties"]):
            recommended.append(chef)
    return recommended[:2]  # Return top 2 matches

def get_recommended_menus(user_data, chef_ids):
    recommended = []
    for menu in MENUS:
        if menu["chef_id"] in chef_ids:
            recommended.append(menu)
    return recommended

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '').strip()
    phone_number = data.get('phone_number')
    
    # If no phone number provided yet, check if message contains one
    if not phone_number and any(char.isdigit() for char in message):
        # Try to extract phone number from message
        for word in message.split():
            # Remove any non-digit characters except '+'
            cleaned_number = ''.join(c for c in word if c.isdigit() or c == '+')
            if cleaned_number:
                is_valid, formatted_number = validate_phone_number(cleaned_number)
                if is_valid:
                    phone_number = formatted_number
                    break
    
    if not phone_number:
        return jsonify({
            "response": "Please provide your phone number to get started (e.g., +14155552671).",
            "phone_number": None
        })
    
    # Validate phone number
    is_valid, formatted_number = validate_phone_number(phone_number)
    if not is_valid:
        return jsonify({
            "response": "Please provide a valid phone number in the format: +14155552671",
            "phone_number": None
        })
    
    # Use the formatted number to check user
    user_data = USERS.get(formatted_number)
    if not user_data:
        return jsonify({
            "response": "Sorry, I couldn't find a profile with that phone number.",
            "phone_number": formatted_number
        })
    
    # Process the conversation based on user data
    recommended_chefs = get_recommended_chefs(user_data)
    recommended_menus = get_recommended_menus(user_data, [chef["id"] for chef in recommended_chefs])
    
    response = f"""Hi {user_data['name']}! Based on your profile:
- Daily calorie goal: {user_data['nutrition_goals']['daily_calories']} calories
- Protein: {user_data['nutrition_goals']['protein']}
- Dietary restrictions: {', '.join(user_data['dietary_restrictions'])}

Here are some recommended chefs for you:
{', '.join([chef['name'] + ' (specializing in ' + ', '.join(chef['specialties'][:2]) + ')' for chef in recommended_chefs])}

And some suggested menus:
{', '.join([menu['name'] for menu in recommended_menus])}

Would you like to:
1. See detailed menu options
2. Create a custom meal plan
3. Adjust your nutrition goals"""

    return jsonify({
        "response": response,
        "phone_number": formatted_number
    })

@app.route('/api/chefs')
def get_chefs():
    return jsonify({
        "chefs": CHEFS,
        "menus": MENUS
    })

if __name__ == '__main__':
    app.run(debug=True, port=5005) 