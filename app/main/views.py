from flask import render_template,abort,request,redirect,url_for
from . import main
from flask_login import login_required,current_user
from .forms import AddComment,UpdateProfile,PitchesForm
from ..models import User,Pitches,Comments
from .. import db,photos

@main.route('/')
@login_required
def index():
    '''
    View root page function that returns the index page and its data
    '''
    pitches = Pitches.query.order_by(Pitches.date.desc())

    title = 'PITCHES'

    return render_template('index.html', title = title, pitches = pitches)

@main.route('/pitch',methods = ['GET','POST'])
@login_required
def new_pitch():

    form = PitchesForm()
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data

        new_pitch = Pitches(title = title, pitch = pitch, user = current_user)

        new_pitch.save_pitch()
        return redirect(url_for('main.index'))
        
    title = 'New Pitch'
    return render_template('pitch_form.html', title= title,form = form)

@main.route('/pitch/<int:id>/comments',methods = ['GET','POST'])
def comments(id):
    pitch = Pitches.query.filter_by(id = id).first()
    form = AddComment()
    if form.validate_on_submit():
        comment = form.comment.data

        new_comment = Comments(comment = comment,pitch_id = pitch.id, user = current_user)

        new_comment.save_comment()
        return redirect(url_for('main.comments',id = pitch.id))

    comments = Comments.query.filter_by(pitch_id = id).order_by(Comments.date.desc())
    title = 'Comments'
    return render_template('comments.html', title= title,form = form, comments = comments)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))