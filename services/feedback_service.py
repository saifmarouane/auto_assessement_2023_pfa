import datetime
from gpt.gpt_feedback import get_chatgpt_feedback_response, generate_new_conversation_context
from database.datafuncs import get_user_conversation_session_data, insert_user_data, get_last_summary_context

def handle_feedback(user, session, user_response):
    handle_summary(user, session)
    assistant_response = get_chatgpt_feedback_response(user, session, user_response)
    insert_user_data('feedback', user, session, user_response, 'user')
    insert_user_data('feedback', user, session, assistant_response, 'assistant')

def get_feedback_conversation(user, session):
    return get_user_conversation_session_data('feedback', user, session)

def handle_suggestion(user, session, user_response):
    insert_user_data('feedback', user, session, user_response, 'suggestion')

def handle_summary(user, session):
    last_summary = get_last_summary_context(user)
    now = datetime.datetime.now(datetime.timezone.utc)
    if len(last_summary) == 0 or (last_summary[0][1] - now > datetime.timedelta(hours=6)): #2 days
        response = generate_new_conversation_context(user)
        insert_user_data('feedback', user, session, response, 'summary')