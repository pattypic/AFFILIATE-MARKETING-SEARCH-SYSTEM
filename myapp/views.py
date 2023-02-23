from flask import render_template, flash, redirect, url_for, request, Blueprint
from .models import Link, db
from .forms import LinkForm


views = Blueprint('views', __name__)

# add a home page
@views.route('/')
def home():
    return render_template("home.html")

# defines a route for a web application. When a [GET/POST] request is made to the /search
# endpoint, the function checks if a 'q' parameter is provided in the request URL using request.args.get('q')
@views.route('/search', methods=['GET', 'POST'])
def search():
    form = LinkForm()
    query = request.args.get('q')
    if query:
        links = Link.query.filter(Link.name.ilike(f'%{query}%')).all()
    else:
        links = []
    return render_template('search.html', form=form, query=query, links=links)


# adds a link
@views.route('/add_link', methods=['GET' , 'POST'])
def add_link():
    form = LinkForm()
    if form.validate_on_submit():
        link = Link(name=form.name.label, url=form.url.label)
        db.session.add(link)
        db.session.commit()
        flash('Link added successfully!', 'success')
        # process form data and save the new link to the database
        return redirect(url_for('views.all_links'))
    return render_template('add_link.html', form=form)

@views.route('/all_links', methods=['GET'])
def all_links():
    links = Link.query.all()
    return render_template('all_links.html', links=links)

