from flask import Flask, redirect, render_template, g, request, url_for, make_response
from toolkit import check_set_cookies
from services.feedback_service import handle_feedback, get_feedback_conversation
from database.dataconn import get_db_conn

app = Flask(__name__)

@app.before_request
def before_request():
    g.db_conn = get_db_conn()

@app.teardown_request
def teardown_request(exception):
    db_conn = getattr(g, 'db_conn', None)
    if db_conn is not None:
        db_conn.close()
        del g._db_conn

#############
# FEEDBACK
#############
@app.route("/feedback", methods=("GET", "POST"))
def feedback():
    user = request.cookies.get('user')
    session = request.cookies.get('session')
    
    print(user,session)
    if request.method == "POST":
        user_response = request.form["jawab"]
        handle_feedback(user, session, user_response)
        return redirect(url_for("feedback"))
    else:
        if not user or not session:
            return check_set_cookies(request, make_response(render_template("feedback.html")))
        return make_response(render_template("feedback.html", chat=get_feedback_conversation(user, session)))

#############
# NEUTRAL
#############
@app.route("/", methods=["GET"])
def index():
    return check_set_cookies(request, make_response(render_template("index.html")))

@app.route("/reinit/<redirection>", methods=["GET"])
def reset_session_cookie(redirection):
    assert redirection in ['index', 'feedback']
    resp = make_response(redirect(url_for(redirection)))
    resp.set_cookie('session', '', expires=0)
    return resp