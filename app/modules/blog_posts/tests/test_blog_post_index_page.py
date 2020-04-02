import pytest, re
from django.test import Client

pytestmark = pytest.mark.django_db

client = Client()

def test_blog_post_index_page_gets_created(blog_post_index_page):
    """Test that we have a blog post index page created by the fixture
    """
    assert blog_post_index_page is not None

def test_blog_post_index_page_get_children(blog_post_index_page, blog_posts):
    """Check that blog_post_index_page has 10 children
    """
    assert len(blog_post_index_page.get_children()) == 10

def test_blog_post_index_200(blog_post_index_page):
    """Test that we have a blog post index page created by the fixture
    """
    rv = client.get(blog_post_index_page.url)
    assert rv.status_code == 200

def test_blog_post_index_lists_blog_posts(blog_post_index_page, blog_posts):
    """Test that the index page lists all of the blog posts
    """
    rv = client.get(blog_post_index_page.url)

    for blog_post in blog_posts:
        assert rv.content.find(str.encode(blog_post.title))

