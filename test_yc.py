import unittest
import yc
import json


class MyTestCase(unittest.TestCase):
    def git_push(self):
        self.assertEqual(yc.tg, False)  # add assertion here


git_push = json.loads("""{
  "object_kind": "push",
  "event_name": "push",
  "before": "f07892dbed6affc8fd79664c3652848cc72b1d88",
  "after": "afb22d3517c07cb56cc2d34c6a51f8cc50714725",
  "ref": "refs/heads/main",
  "checkout_sha": "afb22d3517c07cb56cc2d34c6a51f8cc50714725",
  "message": null,
  "user_id": 2,
  "user_name": "Алексей Присяжный",
  "user_username": "prisyazhnyj",
  "user_email": "prisyazhnyj@starkovgrp.ru",
  "user_avatar": "http://git.starkovgrp.local/uploads/-/system/user/avatar/2/avatar.png",
  "project_id": 140,
  "project": {
    "id": 140,
    "name": "Work",
    "description": "",
    "web_url": "http://git.starkovgrp.local/cicd-tfoms/work",
    "avatar_url": null,
    "git_ssh_url": "ssh://git@git.starkovgrp.local:2224/cicd-tfoms/work.git",
    "git_http_url": "http://git.starkovgrp.local/cicd-tfoms/work.git",
    "namespace": "cicd-tfoms",
    "visibility_level": 0,
    "path_with_namespace": "cicd-tfoms/work",
    "default_branch": "main",
    "ci_config_path": "",
    "homepage": "http://git.starkovgrp.local/cicd-tfoms/work",
    "url": "ssh://git@git.starkovgrp.local:2224/cicd-tfoms/work.git",
    "ssh_url": "ssh://git@git.starkovgrp.local:2224/cicd-tfoms/work.git",
    "http_url": "http://git.starkovgrp.local/cicd-tfoms/work.git"
  },
  "commits": [
    {
      "id": "afb22d3517c07cb56cc2d34c6a51f8cc50714725",
      "message": "Update .gitlab-ci.yml file",
      "title": "Update .gitlab-ci.yml file",
      "timestamp": "2023-02-10T12:29:22+00:00",
      "url": "http://git.starkovgrp.local/cicd-tfoms/work/-/commit/afb22d3517c07cb56cc2d34c6a51f8cc50714725",
      "author": {
        "name": "Егоров Егор",
        "email": "egorov@starkovgrp.ru"
      },
      "added": [

      ],
      "modified": [

      ],
      "removed": [

      ]
    },
    {
      "id": "1b81918600e81e0a3d969f70d697d76073d05121",
      "message": "Update _ConfigSettings.xml",
      "title": "Update _ConfigSettings.xml",
      "timestamp": "2023-02-09T09:10:47+00:00",
      "url": "http://git.starkovgrp.local/cicd-tfoms/work/-/commit/1b81918600e81e0a3d969f70d697d76073d05121",
      "author": {
        "name": "Егоров Егор",
        "email": "egorov@starkovgrp.ru"
      },
      "added": [
        "_ConfigSettings.xml"
      ],
      "modified": [

      ],
      "removed": [

      ]
    },
    {
      "id": "f07892dbed6affc8fd79664c3652848cc72b1d88",
      "message": "Update .gitlab-ci.yml file",
      "title": "Update .gitlab-ci.yml file",
      "timestamp": "2023-02-09T09:06:17+00:00",
      "url": "http://git.starkovgrp.local/cicd-tfoms/work/-/commit/f07892dbed6affc8fd79664c3652848cc72b1d88",
      "author": {
        "name": "Егоров Егор",
        "email": "egorov@starkovgrp.ru"
      },
      "added": [

      ],
      "modified": [
        ".gitlab-ci.yml"
      ],
      "removed": [

      ]
    }
  ],
  "total_commits_count": 3,
  "push_options": {
  },
  "repository": {
    "name": "Work",
    "url": "ssh://git@git.starkovgrp.local:2224/cicd-tfoms/work.git",
    "description": "",
    "homepage": "http://git.starkovgrp.local/cicd-tfoms/work",
    "git_http_url": "http://git.starkovgrp.local/cicd-tfoms/work.git",
    "git_ssh_url": "ssh://git@git.starkovgrp.local:2224/cicd-tfoms/work.git",
    "visibility_level": 0
  }
}""")


gt_req = """{
  "object_kind": "push",
  "event_name": "push",
  "before": "f07892dbed6affc8fd79664c3652848cc72b1d88",
  "after": "afb22d3517c07cb56cc2d34c6a51f8cc50714725",
  "ref": "refs/heads/main",
  "checkout_sha": "afb22d3517c07cb56cc2d34c6a51f8cc50714725",
  "message": null,
  "user_id": 2,
  "user_name": "Алексей Присяжный",
  "user_username": "prisyazhnyj",
  "user_email": "prisyazhnyj@starkovgrp.ru",
  "user_avatar": "http://git.starkovgrp.local/uploads/-/system/user/avatar/2/avatar.png",
  "project_id": 140,
  "project": {
    "id": 140,
    "name": "Work",
    "description": "",
    "web_url": "http://git.starkovgrp.local/cicd-tfoms/work",
    "avatar_url": null,
    "git_ssh_url": "ssh://git@git.starkovgrp.local:2224/cicd-tfoms/work.git",
    "git_http_url": "http://git.starkovgrp.local/cicd-tfoms/work.git",
    "namespace": "cicd-tfoms",
    "visibility_level": 0,
    "path_with_namespace": "cicd-tfoms/work",
    "default_branch": "main",
    "ci_config_path": "",
    "homepage": "http://git.starkovgrp.local/cicd-tfoms/work",
    "url": "ssh://git@git.starkovgrp.local:2224/cicd-tfoms/work.git",
    "ssh_url": "ssh://git@git.starkovgrp.local:2224/cicd-tfoms/work.git",
    "http_url": "http://git.starkovgrp.local/cicd-tfoms/work.git"
  },
  "commits": [
    {
      "id": "afb22d3517c07cb56cc2d34c6a51f8cc50714725",
      "message": "Update .gitlab-ci.yml file",
      "title": "Update .gitlab-ci.yml file",
      "timestamp": "2023-02-10T12:29:22+00:00",
      "url": "http://git.starkovgrp.local/cicd-tfoms/work/-/commit/afb22d3517c07cb56cc2d34c6a51f8cc50714725",
      "author": {
        "name": "Егоров Егор",
        "email": "egorov@starkovgrp.ru"
      },
      "added": [

      ],
      "modified": [

      ],
      "removed": [

      ]
    },
    {
      "id": "1b81918600e81e0a3d969f70d697d76073d05121",
      "message": "Update _ConfigSettings.xml",
      "title": "Update _ConfigSettings.xml",
      "timestamp": "2023-02-09T09:10:47+00:00",
      "url": "http://git.starkovgrp.local/cicd-tfoms/work/-/commit/1b81918600e81e0a3d969f70d697d76073d05121",
      "author": {
        "name": "Егоров Егор",
        "email": "egorov@starkovgrp.ru"
      },
      "added": [
        "_ConfigSettings.xml"
      ],
      "modified": [

      ],
      "removed": [

      ]
    },
    {
      "id": "f07892dbed6affc8fd79664c3652848cc72b1d88",
      "message": "Update .gitlab-ci.yml file",
      "title": "Update .gitlab-ci.yml file",
      "timestamp": "2023-02-09T09:06:17+00:00",
      "url": "http://git.starkovgrp.local/cicd-tfoms/work/-/commit/f07892dbed6affc8fd79664c3652848cc72b1d88",
      "author": {
        "name": "Егоров Егор",
        "email": "egorov@starkovgrp.ru"
      },
      "added": [

      ],
      "modified": [
        ".gitlab-ci.yml"
      ],
      "removed": [

      ]
    }
  ],
  "total_commits_count": 3,
  "push_options": {
  },
  "repository": {
    "name": "Work",
    "url": "ssh://git@git.starkovgrp.local:2224/cicd-tfoms/work.git",
    "description": "",
    "homepage": "http://git.starkovgrp.local/cicd-tfoms/work",
    "git_http_url": "http://git.starkovgrp.local/cicd-tfoms/work.git",
    "git_ssh_url": "ssh://git@git.starkovgrp.local:2224/cicd-tfoms/work.git",
    "visibility_level": 0
  }
}"""

tg_req = """{"update_id": 131012139,\n"message": {"message_id": 18,"from": {"id": 157215168,
                "is_bot": false,
                "first_name": "\\u0410\\u043b\\u0435\\u043a\\u0441\\u0435\\u0439",
                "last_name": "\\u041f\\u0440\\u0438\\u0441\\u044f\\u0436\\u043d\\u044b\\u0439",
                "username": "praw2003",
                "language_code": "ru"
            },
            "chat": {
                "id": 157215168,
                "first_name": "\\u0410\\u043b\\u0435\\u043a\\u0441\\u0435\\u0439",
                "last_name": "\\u041f\\u0440\\u0438\\u0441\\u044f\\u0436\\u043d\\u044b\\u0439",
                "username": "praw2003",
                "type": "private"
            },
            "date": 1677778700,
            "text": "/start",
            "entities": [
                {
                    "offset": 0,
                    "length": 6,
                    "type": "bot_command"
                }
            ]
        }
    }
"""

tg_chat = """
{"update_id":131012169,\n"message":{"message_id":82,"from":{"id":157215168,"is_bot":false,"first_name":"\\u0410\\u043b\\u0435\\u043a\\u0441\\u0435\\u0439","last_name":"\\u041f\\u0440\\u0438\\u0441\\u044f\\u0436\\u043d\\u044b\\u0439","username":"praw2003","language_code":"ru"},"chat":{"id":-788400033,"title":"TEST_BOT","type":"group","all_members_are_administrators":true},"date":1678025730,"group_chat_created":true}}"""


if __name__ == '__main__':
    unittest.main()
