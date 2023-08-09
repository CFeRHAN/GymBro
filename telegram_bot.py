import telebot
from bard_interaction import talk_to_bard

BOT = telebot.TeleBot('6670968645:AAErNrbl3EKT486Gz2T3uj-Ex-pivmSWAyk')

# Global dictionary to store user data
user_data = {}

# Buttons
gym_button = telebot.types.KeyboardButton("Gym Workout")
home_button = telebot.types.KeyboardButton("Home Workout")
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(gym_button, home_button)

# States
GENDER, AGE, HEIGHT, WEIGHT = range(4)

@BOT.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    user_data[user_id] = {'user_id': user_id}  # Add user_id directly to the user data dictionary
    BOT.send_message(message.chat.id, "Hello! Please choose your workout type:", reply_markup=keyboard)

@BOT.message_handler(func=lambda message: message.text == "Gym Workout")
def request_gender_gym(message):
    user_id = message.from_user.id
    user_data[user_id]['workout_type'] = 'Gym Workout'  # Set the workout_type to 'Gym Workout'
    BOT.send_message(message.chat.id, "Great! Please tell me your gender (Male/Female/Others).")
    BOT.register_next_step_handler(message, save_gender_gym, user_id)

def save_gender_gym(message, user_id):
    user_data[user_id]['gender'] = message.text
    BOT.send_message(message.chat.id, "Thanks! Now, please tell me your age.")
    BOT.register_next_step_handler(message, save_age_gym, user_id)

def save_age_gym(message, user_id):
    try:
        age = int(message.text)
        user_data[user_id]['age'] = age
        BOT.send_message(message.chat.id, "Got it! Next, please tell me your height in centimeters.")
        BOT.register_next_step_handler(message, save_height_gym, user_id)
    except ValueError:
        BOT.send_message(message.chat.id, "Please provide a valid age (a number).")
        BOT.register_next_step_handler(message, save_age_gym, user_id)

def save_height_gym(message, user_id):
    try:
        height = float(message.text)
        user_data[user_id]['height'] = height
        BOT.send_message(message.chat.id, "Almost there! Please tell me your weight in kilograms.")
        BOT.register_next_step_handler(message, save_weight_gym, user_id)
    except ValueError:
        BOT.send_message(message.chat.id, "Please provide a valid height (a number).")
        BOT.register_next_step_handler(message, save_height_gym, user_id)

def save_weight_gym(message, user_id):
    try:
        weight = float(message.text)
        user_data[user_id]['weight'] = weight

        # All information collected, print and reply the data
        print(user_data[user_id])
        reply_text = f"Thank you for providing your information, User {user_id}:\n" \
                     f"Workout Type: Gym Workout\n" \
                     f"Gender: {user_data[user_id]['gender']}\n" \
                     f"Age: {user_data[user_id]['age']}\n" \
                     f"Height: {user_data[user_id]['height']} cm\n" \
                     f"Weight: {user_data[user_id]['weight']} kg"

        BOT.send_message(message.chat.id, reply_text)

        # Call the talk_to_bard function and reply with the bard_output
        reply_text2 = talk_to_bard(user_data[user_id])
        BOT.send_message(message.chat.id, reply_text2)

    except ValueError:
        BOT.send_message(message.chat.id, "Please provide a valid weight (a number).")
        BOT.register_next_step_handler(message, save_weight_gym, user_id)

@BOT.message_handler(func=lambda message: message.text == "Home Workout")
def request_gender_home(message):
    user_id = message.from_user.id
    user_data[user_id]['workout_type'] = 'Home Workout'  # Set the workout_type to 'Home Workout'
    BOT.send_message(message.chat.id, "Great! Please tell me your gender (Male/Female/Others).")
    BOT.register_next_step_handler(message, save_gender_home, user_id)

def save_gender_home(message, user_id):
    user_data[user_id]['gender'] = message.text
    BOT.send_message(message.chat.id, "Thanks! Now, please tell me your age.")
    BOT.register_next_step_handler(message, save_age_home, user_id)

def save_age_home(message, user_id):
    try:
        age = int(message.text)
        user_data[user_id]['age'] = age
        BOT.send_message(message.chat.id, "Got it! Next, please tell me your height in centimeters.")
        BOT.register_next_step_handler(message, save_height_home, user_id)
    except ValueError:
        BOT.send_message(message.chat.id, "Please provide a valid age (a number).")
        BOT.register_next_step_handler(message, save_age_home, user_id)

def save_height_home(message, user_id):
    try:
        height = float(message.text)
        user_data[user_id]['height'] = height
        BOT.send_message(message.chat.id, "Almost there! Please tell me your weight in kilograms.")
        BOT.register_next_step_handler(message, save_weight_home, user_id)
    except ValueError:
        BOT.send_message(message.chat.id, "Please provide a valid height (a number).")
        BOT.register_next_step_handler(message, save_height_home, user_id)

def save_weight_home(message, user_id):
    try:
        weight = float(message.text)
        user_data[user_id]['weight'] = weight

        # All information collected, print and reply the data
        print(user_data[user_id])
        reply_text = f"Thank you for providing your information, User {user_id}:\n" \
                     f"Workout Type: Home Workout\n" \
                     f"Gender: {user_data[user_id]['gender']}\n" \
                     f"Age: {user_data[user_id]['age']}\n" \
                     f"Height: {user_data[user_id]['height']} cm\n" \
                     f"Weight: {user_data[user_id]['weight']} kg"

        BOT.send_message(message.chat.id, reply_text)

        # Call the talk_to_bard function and reply with the bard_output
        talk_to_bard(user_data[user_id])

    except ValueError:
        BOT.send_message(message.chat.id, "Please provide a valid weight (a number).")
        BOT.register_next_step_handler(message, save_weight_home, user_id)

if __name__ == '__main__':
    print('Bot Starting...')
    BOT.infinity_polling()
