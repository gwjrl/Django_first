from FlaskProject.ext import db


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(128), nullable=False)
    blog_content = db.Column(db.String(4096), nullable=True)
    blog_author_id = db.Column(db.Integer, db.ForeignKey("blog_user.id"), nullable=True)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            return False
        return True