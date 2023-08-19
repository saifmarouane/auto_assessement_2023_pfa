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
# Recruitment
#############
@app.route("/Recruitment", methods=("GET", "POST"))
def Recruitment():
    user = request.cookies.get('user')
    session = request.cookies.get('session')
    
    if request.method == "POST":
        user_response = request.form["jawab"]
        handle_feedback("Recruitment",user, session, user_response)
        return redirect(url_for("Recruitment"))
    else:
        if not user or not session:
            return check_set_cookies(request, make_response(render_template("Recruitment.html")))
        return make_response(render_template("Recruitment.html", chat=get_feedback_conversation("Recruitment",user, session)))



#############
# Technologie
#############
@app.route("/Technologie", methods=("GET", "POST"))
def Technologie():
    user = request.cookies.get('user')
    session = request.cookies.get('session')
    
    print(user,session)
    if request.method == "POST":
        user_response = request.form["jawab"]
        handle_feedback("Technologie",user, session, user_response)
        return redirect(url_for("Technologie"))
    else:
        if not user or not session:
            return check_set_cookies(request, make_response(render_template("Technologie.html")))
        return make_response(render_template("Technologie.html", chat=get_feedback_conversation("Technologie",user, session)))



#############
# Management
#############
@app.route("/Management", methods=("GET", "POST"))
def Management():
    user = request.cookies.get('user')
    session = request.cookies.get('session')
    
    print(user,session)
    if request.method == "POST":
        user_response = request.form["jawab"]
        handle_feedback("Management",user, session, user_response)
        return redirect(url_for("Management"))
    else:
        if not user or not session:
            return check_set_cookies(request, make_response(render_template("Management.html")))
        return make_response(render_template("Management.html", chat=get_feedback_conversation("Management",user, session)))


#############
# Business
#############
@app.route("/Business", methods=("GET", "POST"))
def Business():
    user = request.cookies.get('user')
    session = request.cookies.get('session')
    
    print(user,session)
    if request.method == "POST":
        user_response = request.form["jawab"]
        handle_feedback("Business",user, session, user_response)
        return redirect(url_for("Business"))
    else:
        if not user or not session:
            return check_set_cookies(request, make_response(render_template("Business.html")))
        return make_response(render_template("Business.html", chat=get_feedback_conversation("Business",user, session)))


#############
# Communication
#############
@app.route("/Communication", methods=("GET", "POST"))
def Communication():
    user = request.cookies.get('user')
    session = request.cookies.get('session')
    
    print(user,session)
    if request.method == "POST":
        user_response = request.form["jawab"]
        handle_feedback("Communication",user, session, user_response)
        return redirect(url_for("Communication"))
    else:
        if not user or not session:
            return check_set_cookies(request, make_response(render_template("Communication.html")))
        return make_response(render_template("Communication.html", chat=get_feedback_conversation("Communication",user, session)))


#############
# Membership
#############
@app.route("/Membership", methods=("GET", "POST"))
def Membership():
    user = request.cookies.get('user')
    session = request.cookies.get('session')
    
    print(user,session)
    if request.method == "POST":
        user_response = request.form["jawab"]
        handle_feedback("Membership",user, session, user_response)
        return redirect(url_for("Membership"))
    else:
        if not user or not session:
            return check_set_cookies(request, make_response(render_template("Membership.html")))
        return make_response(render_template("Membership.html", chat=get_feedback_conversation("Membership",user, session)))


#############
# Ownership
#############
@app.route("/Ownership", methods=("GET", "POST"))
def Ownership():
    user = request.cookies.get('user')
    session = request.cookies.get('session')
    
    print(user,session)
    if request.method == "POST":
        user_response = request.form["jawab"]
        handle_feedback("Ownership",user, session, user_response)
        return redirect(url_for("Ownership"))
    else:
        if not user or not session:
            return check_set_cookies(request, make_response(render_template("Ownership.html")))
        return make_response(render_template("Ownership.html", chat=get_feedback_conversation("Ownership",user, session)))


#############
# BrandEvangelism
#############
@app.route("/BrandEvangelism", methods=("GET", "POST"))
def BrandEvangelism():
    user = request.cookies.get('user')
    session = request.cookies.get('session')
    
    print(user,session)
    if request.method == "POST":
        user_response = request.form["jawab"]
        handle_feedback("BrandEvangelism",user, session, user_response)
        return redirect(url_for("BrandEvangelism"))
    else:
        if not user or not session:
            return check_set_cookies(request, make_response(render_template("BrandEvangelism.html")))
        return make_response(render_template("BrandEvangelism.html", chat=get_feedback_conversation("BrandEvangelism",user, session)))


#############
# Process
#############
@app.route("/Process", methods=("GET", "POST"))
def Process():
    user = request.cookies.get('user')
    session = request.cookies.get('session')
    
    print(user,session)
    if request.method == "POST":
        user_response = request.form["jawab"]
        handle_feedback("Process",user, session, user_response)
        return redirect(url_for("Process"))
    else:
        if not user or not session:
            return check_set_cookies(request, make_response(render_template("Process.html")))
        return make_response(render_template("Process.html", chat=get_feedback_conversation("Process",user, session)))



#############
# Community
#############
@app.route("/Community", methods=("GET", "POST"))
def Community():
    user = request.cookies.get('user')
    session = request.cookies.get('session')
    
    print(user,session)
    if request.method == "POST":
        user_response = request.form["jawab"]
        handle_feedback("Community",user, session, user_response)
        return redirect(url_for("Community"))
    else:
        if not user or not session:
            return check_set_cookies(request, make_response(render_template("Community.html")))
        return make_response(render_template("Community.html", chat=get_feedback_conversation("Community",user, session)))



#############
# Methodology
#############
@app.route("/Methodology", methods=("GET", "POST"))
def Methodology():
    user = request.cookies.get('user')
    session = request.cookies.get('session')
    
    print(user,session)
    if request.method == "POST":
        user_response = request.form["jawab"]
        handle_feedback("Methodology",user, session, user_response)
        return redirect(url_for("Methodology"))
    else:
        if not user or not session:
            return check_set_cookies(request, make_response(render_template("Methodology.html")))
        return make_response(render_template("Methodology.html", chat=get_feedback_conversation("Methodology",user, session)))





#############
# Mentorship
#############
@app.route("/Mentorship", methods=("GET", "POST"))
def Mentorship():
    user = request.cookies.get('user')
    session = request.cookies.get('session')
    
    print(user,session)
    if request.method == "POST":
        user_response = request.form["jawab"]
        handle_feedback("Mentorship",user, session, user_response)
        return redirect(url_for("Mentorship"))
    else:
        if not user or not session:
            return check_set_cookies(request, make_response(render_template("Mentorship.html")))
        return make_response(render_template("Mentorship.html", chat=get_feedback_conversation("Mentorship",user, session)))


#############
# NEUTRAL
#############

###########
#test neutral
##########
@app.route("/testindex", methods=["GET"])
def testindex():
    return check_set_cookies(request, make_response(render_template("testindex.html")))




@app.route("/", methods=["GET"])
def index():
    return check_set_cookies(request, make_response(render_template("index.html")))
@app.route("/nexindex", methods=["GET"])
def nexindex():
    return check_set_cookies(request, make_response(render_template("nexindex.html")))
@app.route("/reinit/<redirection>", methods=["GET"])
def reset_session_cookie(redirection):
    assert redirection in ['index','Mentorship','Methodology','Process', 'Community','Recruitment','Management','Technologie','Ownership','Communication','Business','Membership','testindex','BrandEvangelism']
    resp = make_response(redirect(url_for(redirection)))
    resp.set_cookie('session', '', expires=0)
    return resp