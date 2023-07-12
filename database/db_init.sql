CREATE TABLE if not exists log (
    app TEXT NOT NULL, -- service used, feedback, language, skill, manager or assessment for example
    enduser TEXT NOT NULL, -- user whose conversation it is (can be an email or a random string)
    sess TEXT NOT NULL, -- session of the conversation
    msg TEXT NOT NULL, -- stored message
    speaker TEXT NOT NULL, -- who is the origin of the message, either 'user', 'assistant', 'suggestion' or 'evaluation'
    ts TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP -- a basic timestamp
);

GRANT ALL PRIVILEGES ON log TO gpt_family;