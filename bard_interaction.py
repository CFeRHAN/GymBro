import os
from bardapi import Bard

# Set the Bard API key
os.environ['_BARD_API_KEY'] = "YgiVvQmMQqTdWE_GTsL-6mcaWZuGmQKmvCh3QI3WHCJJlzWMjd5VnqNcolh_n117PPPjaw."

def talk_to_bard(user_data):
    input_text = f"give me a {'Gym' if user_data['workout_type'] == 'Gym Workout' else 'Home'} workout plan " \
                 f"for a {user_data['age']} years old {user_data['gender']}, " \
                 f"with {user_data['height']} cm height and {user_data['weight']} kg weight"
    bard_output = Bard().get_answer(input_text)['content']
    return bard_output
