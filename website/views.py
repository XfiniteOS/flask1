from flask import Blueprint,render_template,request,flash,jsonify
from flask_login import login_user,logout_user,current_user
from flask_login import login_required
from .models import User,Note
from . import db

import json

views = Blueprint('views', __name__)

@views.route('/',methods=['GET','POST'])
@login_required
def home():
    if request.method=='POST':
        text=request.form.get('text')
        note = request.form.get('note')
        if len(note)<1:
            flash("Note is too short",category="error")
        else:
            new_note=Note(title=text,content=note,user_id=current_user.id)
                     
            db.session.add(new_note)
            db.session.commit()
            flash("Note added",category="success")

    notes=Note.query.filter_by(user_id=current_user.id).all()
        
    return render_template("home.html",user=current_user)
    
@views.route('/delete-note',methods=['POST'])
def delete_note():
    note=json.loads(request.data)
    noteId = note['noteId']
    note=Note.query.get(id=noteId)
    if note:
        if note.user_id==current_user:
            db.session.delete(note)
            db.session.commit()
            flash("Note deleted",category="success")
            
    return jsonify({})

