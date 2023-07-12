from flask import Response, Request
import random
import string

def get_random_str():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(64))

def check_set_cookies(req: Request, resp: Response):
    if not req.cookies.get('user'):
        resp.set_cookie('user', get_random_str(), max_age=3600*24*365*10) # 10 years of user cookie
    if not req.cookies.get('session'):
        resp.set_cookie('session', get_random_str(), max_age=3600*6) # 6 hours of session cookie
    return resp