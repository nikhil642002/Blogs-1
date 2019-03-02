from flask import render_template,request,redirect,url_for,abort
from ..models import Comment,Blog,User,PhotoProfile
from . import main
from .forms import UpdateProfile,CommentForm,UpdateProfile,AddBlogForm
from ..import db,photos
from flask_login import login_required, current_user
# Views

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - Welcome to The best Pitches Review Website Online'
    all_blogs = Blog.query.all()
    # comments = Comment.query.filter_by(pitch_id = id).all()
 
    return render_template('index.html', title = title, all_blogs= all_blogs)


@main.route('/blog/new/', methods = ['GET','POST'])
@login_required
def create_blogs():
    form = AddBlogForm()


    if form.validate_on_submit():
        category = form.category.data
        content = form.content.data 

        new_blog = Blog(description=content,user=current_user)
        new_blog.save_blog()

        return redirect(url_for('main.index'))

    all_blogs = Blog.query.all()
       
    title = 'Feel free to add a pitch'
    return render_template('blogs.html',title = title, form=form)


@main.route('/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def create_comments(id):
    form = CommentForm()
    blog= Blog.query.filter_by(id=id).first()

    if form.validate_on_submit():

        comment = form.comment.data

        new_comment =Comment(content = comment , blog= blog, user=current_user)
        db.session.add(new_comment)
        db.session.commit()

    comments = Comment.query.filter_by(blog_id = id).all()


    return render_template('comments.html', form=form ,comments=comments)

@main.route('/blog/<int:id>')
def blog(id):
    blog=Blog.get_bloge(id)

    return render_template('blog.html',blog=blog)

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
