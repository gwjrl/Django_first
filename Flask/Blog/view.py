from flask_restful import Resource, marshal

from .model import Blog

from Blog.fields_template import blog_fields


class BlogsResource(Resource):

    def get(self):

        blogs = Blog.query.all()

        return marshal(blogs, blog_fields)

    def post(self):
        blog_title = "哈哈"
        blog_conent = "哈哈，O(∩_∩)O哈哈~"

        blog = Blog()
        blog.blog_title = blog_title
        blog.blog_content = blog_conent

        if blog.save():
            return marshal(blog, blog_fields)
        return {"msg": "create fail"}
