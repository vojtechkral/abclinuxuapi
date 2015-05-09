#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
import os.path

import pytest

import abclinuxuapi


# Fixtures ====================================================================
@pytest.fixture
def username_password():
    local_dir = os.path.dirname(__file__)
    pwd_file_path = os.path.join(local_dir, "login")

    if not os.path.exists(pwd_file_path):
        raise IOError(
            "Please create file `login` in tests/ directory.\n"
            "First line is username, second password for test user."
        )

    with open(pwd_file_path) as f:
        return f.read().splitlines()[:2]


@pytest.fixture
def username():
    return username_password()[0]


@pytest.fixture
def password():
    return username_password()[-1]


# Tests =======================================================================
def test_register_blog(username, password):
    u = abclinuxuapi.User(username, password)

    if u.has_blog():
        return

    u.register_blog("Test user's blog")
    assert u.has_blog()


def test_login(username, password):
    u = abclinuxuapi.User(username, password)
    u.login()

    with pytest.raises(UserWarning):
        u = abclinuxuapi.User(username, "bad password")
        u.login()


def test_get_blogposts():
    posts = abclinuxuapi.User("bystroushaak").get_blogposts()

    assert len(posts) >= 56
    assert posts[0].title == "Google vyhledávání"
    assert posts[55].title == "Dogecoin"


def test_add_concept(username, password):
    u = abclinuxuapi.User(username, password)

    old_concept_list = u.get_concepts()

    u.add_concept("Text of the new concept", "Title of the concept")

    new_concept_list = u.get_concepts()

    assert len(old_concept_list) < len(new_concept_list)

    assert new_concept_list[-1].title == "Title of the concept"
    content = new_concept_list[-1].get_content()

    assert len(content) > 0

    # print content

    # assert  == "Text of the new concept"


def test_get_user_id(username, password):
    u = abclinuxuapi.User(username, password)
    u.login()

    assert u._get_user_id()
    assert int(u._get_user_id())
