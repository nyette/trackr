from flask import Blueprint, flash, redirect, render_template, url_for
from trackr.db import db, Item
from trackr.forms import SaveItemForm, DeleteItemForm
from datetime import datetime

bp = Blueprint("items", __name__)

@bp.route("/")
def index():
    items = Item.query.filter_by(in_trash = False).all()
    trash = Item.query.filter_by(in_trash = True).all()
    return render_template("items/index.html", items = items, trash = trash)

@bp.route("/create", methods = ["GET", "POST"])
def create():
    form = SaveItemForm()
    if form.validate_on_submit():
        item = Item(name = form.name.data, description = form.description.data, price = form.price.data, count = form.count.data)
        db.session.add(item)
        db.session.commit()
        flash(f"Created {form.name.data}!")
        return redirect(url_for("index"))
    return render_template("items/save.html", form = form)

@bp.route("/<int:id>")
def get(id):
    item = Item.query.get_or_404(id)
    return render_template("items/get.html", item = item)

@bp.route("/<int:id>/update", methods = ["GET", "POST"])
def update(id):
    item = Item.query.get_or_404(id)
    form = SaveItemForm(obj = item)
    if form.validate_on_submit():
        form.populate_obj(item)
        db.session.commit()
        flash(f"Updated {form.name.data}!")
        return redirect(url_for("index"))
    return render_template("items/save.html", form = form)

@bp.route("/<int:id>/delete", methods = ["GET", "POST"])
def delete(id):
    item = Item.query.get_or_404(id)
    form = DeleteItemForm()
    if form.validate_on_submit():
        item.in_trash = True
        item.deletion_date = datetime.now()
        item.deletion_comment = form.deletion_comment.data
        db.session.commit()
        flash(f"Deleted {item.name}!")
        return redirect(url_for("index"))
    return render_template("items/delete.html", form = form)

@bp.route("/<int:id>/restore")
def restore(id):
    item = Item.query.get_or_404(id)
    flash(f"Restored {item.name}!")
    item.in_trash = False
    item.deletion_date = None
    item.deletion_comment = None
    db.session.commit()
    return redirect(url_for("index"))

@bp.route("/<int:id>/purge")
def purge(id):
    item = Item.query.get_or_404(id)
    flash(f"Purged {item.name}!")
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for("index"))
