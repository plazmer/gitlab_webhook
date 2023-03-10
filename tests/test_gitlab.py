import json
import unittest
import gitlab


def test_router_push():
    j = json.load(open("push.json"))
    assert gitlab.router(j,'../') == """<b>Administrator</b> pushed to <a href="https://192.168.7.46/dvps/firstproject">dvps/firstproject/</a>\nCommits:\n- Initial commit <a href="https://192.168.7.46/dvps/firstproject/-/commit/acb5f1061a528a37444ac41782bb8c06b4a73f58">&gt;&gt;&gt;</a>"""

def test_router_merge():
    j = json.load(open("merge_request.json"))
    assert gitlab.router(j, '../') == """"""