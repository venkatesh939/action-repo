import json

# Properly formatted JSON data (double quotes and no trailing commas)
json_data = """
{
  "action": "closed",
  "number": 11,
  "pull_request": {
    "url": "https://api.github.com/repos/venkatesh939/action-repo/pulls/11",
    "id": 2053126380,
    "node_id": "PR_kwDOMscaoM56YDjs",
    "html_url": "https://github.com/venkatesh939/action-repo/pull/11",
    "diff_url": "https://github.com/venkatesh939/action-repo/pull/11.diff",
    "patch_url": "https://github.com/venkatesh939/action-repo/pull/11.patch",
    "issue_url": "https://api.github.com/repos/venkatesh939/action-repo/issues/11",
    "number": 11,
    "state": "closed",
    "locked": false,
    "title": "addded all",
    "user": {
      "login": "venkatesh939",
      "id": 32451027,
      "node_id": "MDQ6VXNlcjMyNDUxMDI3",
      "avatar_url": "https://avatars.githubusercontent.com/u/32451027?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/venkatesh939",
      "html_url": "https://github.com/venkatesh939",
      "followers_url": "https://api.github.com/users/venkatesh939/followers",
      "following_url": "https://api.github.com/users/venkatesh939/following{/other_user}",
      "gists_url": "https://api.github.com/users/venkatesh939/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/venkatesh939/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/venkatesh939/subscriptions",
      "organizations_url": "https://api.github.com/users/venkatesh939/orgs",
      "repos_url": "https://api.github.com/users/venkatesh939/repos",
      "events_url": "https://api.github.com/users/venkatesh939/events{/privacy}",
      "received_events_url": "https://api.github.com/users/venkatesh939/received_events",
      "type": "User",
      "site_admin": false
    },
    "body": null,
    "created_at": "2024-09-04T10:46:15Z",
    "updated_at": "2024-09-04T10:51:02Z",
    "closed_at": "2024-09-04T10:51:02Z",
    "merged_at": "2024-09-04T10:51:02Z",
    "merge_commit_sha": "8743d59fec2a7d193ff1cb3632ec211dd07c3f2e",
    "assignee": null,
    "assignees": [],
    "requested_reviewers": [],
    "requested_teams": [],
    "labels": [],
    "milestone": null,
    "draft": false,
    "commits_url": "https://api.github.com/repos/venkatesh939/action-repo/pulls/11/commits",
    "review_comments_url": "https://api.github.com/repos/venkatesh939/action-repo/pulls/11/comments",
    "review_comment_url": "https://api.github.com/repos/venkatesh939/action-repo/pulls/comments{/number}",
    "comments_url": "https://api.github.com/repos/venkatesh939/action-repo/issues/11/comments",
    "statuses_url": "https://api.github.com/repos/venkatesh939/action-repo/statuses/2ed2a7ff911e94327d043eac702ad6e8f5a50189",
    "head": {
      "label": "venkatesh939:temp",
      "ref": "temp",
      "sha": "2ed2a7ff911e94327d043eac702ad6e8f5a50189",
      "user": {
        "login": "venkatesh939",
        "id": 32451027,
        "node_id": "MDQ6VXNlcjMyNDUxMDI3",
        "avatar_url": "https://avatars.githubusercontent.com/u/32451027?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/venkatesh939",
        "html_url": "https://github.com/venkatesh939",
        "followers_url": "https://api.github.com/users/venkatesh939/followers",
        "following_url": "https://api.github.com/users/venkatesh939/following{/other_user}",
        "gists_url": "https://api.github.com/users/venkatesh939/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/venkatesh939/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/venkatesh939/subscriptions",
        "organizations_url": "https://api.github.com/users/venkatesh939/orgs",
        "repos_url": "https://api.github.com/users/venkatesh939/repos",
        "events_url": "https://api.github.com/users/venkatesh939/events{/privacy}",
        "received_events_url": "https://api.github.com/users/venkatesh939/received_events",
        "type": "User",
        "site_admin": false
      },
      "repo": {
        "id": 851909280,
        "node_id": "R_kgDOMscaoA",
        "name": "action-repo",
        "full_name": "venkatesh939/action-repo",
        "private": false,
        "owner": {
          "login": "venkatesh939",
          "id": 32451027,
          "node_id": "MDQ6VXNlcjMyNDUxMDI3",
          "avatar_url": "https://avatars.githubusercontent.com/u/32451027?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/venkatesh939",
          "html_url": "https://github.com/venkatesh939",
          "followers_url": "https://api.github.com/users/venkatesh939/followers",
          "following_url": "https://api.github.com/users/venkatesh939/following{/other_user}",
          "gists_url": "https://api.github.com/users/venkatesh939/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/venkatesh939/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/venkatesh939/subscriptions",
          "organizations_url": "https://api.github.com/users/venkatesh939/orgs",
          "repos_url": "https://api.github.com/users/venkatesh939/repos",
          "events_url": "https://api.github.com/users/venkatesh939/events{/privacy}",
          "received_events_url": "https://api.github.com/users/venkatesh939/received_events",
          "type": "User",
          "site_admin": false
        },
        "html_url": "https://github.com/venkatesh939/action-repo",
        "description": null,
        "fork": false,
        "url": "https://api.github.com/repos/venkatesh939/action-repo",
        "forks_url": "https://api.github.com/repos/venkatesh939/action-repo/forks",
        "keys_url": "https://api.github.com/repos/venkatesh939/action-repo/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/venkatesh939/action-repo/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/venkatesh939/action-repo/teams",
        "hooks_url": "https://api.github.com/repos/venkatesh939/action-repo/hooks",
        "issue_events_url": "https://api.github.com/repos/venkatesh939/action-repo/issues/events{/number}",
        "events_url": "https://api.github.com/repos/venkatesh939/action-repo/events",
        "assignees_url": "https://api.github.com/repos/venkatesh939/action-repo/assignees{/user}",
        "branches_url": "https://api.github.com/repos/venkatesh939/action-repo/branches{/branch}",
        "tags_url": "https://api.github.com/repos/venkatesh939/action-repo/tags",
        "blobs_url": "https://api.github.com/repos/venkatesh939/action-repo/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/venkatesh939/action-repo/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/venkatesh939/action-repo/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/venkatesh939/action-repo/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/venkatesh939/action-repo/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/venkatesh939/action-repo/languages",
        "stargazers_url": "https://api.github.com/repos/venkatesh939/action-repo/stargazers",
        "contributors_url": "https://api.github.com/repos/venkatesh939/action-repo/contributors",
        "subscribers_url": "https://api.github.com/repos/venkatesh939/action-repo/subscribers",
        "subscription_url": "https://api.github.com/repos/venkatesh939/action-repo/subscription",
        "commits_url": "https://api.github.com/repos/venkatesh939/action-repo/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/venkatesh939/action-repo/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/venkatesh939/action-repo/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/venkatesh939/action-repo/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/venkatesh939/action-repo/contents/{+path}",
        "compare_url": "https://api.github.com/repos/venkatesh939/action-repo/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/venkatesh939/action-repo/merges",
        "archive_url": "https://api.github.com/repos/venkatesh939/action-repo/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/venkatesh939/action-repo/downloads",
        "issues_url": "https://api.github.com/repos/venkatesh939/action-repo/issues{/number}",
        "pulls_url": "https://api.github.com/repos/venkatesh939/action-repo/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/venkatesh939/action-repo/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/venkatesh939/action-repo/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/venkatesh939/action-repo/labels{/name}",
        "releases_url": "https://api.github.com/repos/venkatesh939/action-repo/releases{/id}",
        "deployments_url": "https://api.github.com/repos/venkatesh939/action-repo/deployments",
        "created_at": "2024-09-03T22:33:18Z",
        "updated_at": "2024-09-04T10:30:34Z",
        "pushed_at": "2024-09-04T10:50:39Z",
        "git_url": "git://github.com/venkatesh939/action-repo.git",
        "ssh_url": "git@github.com:venkatesh939/action-repo.git",
        "clone_url": "https://github.com/venkatesh939/action-repo.git",
        "svn_url": "https://github.com/venkatesh939/action-repo",
        "homepage": null,
        "size": 30,
        "stargazers_count": 0,
        "watchers_count": 0,
        "language": "Python",
        "has_issues": true,
        "has_projects": true,
        "has_downloads": true,
        "has_wiki": true,
        "has_pages": false,
        "has_discussions": false,
        "forks_count": 0,
        "mirror_url": null,
        "archived": false,
        "disabled": false,
        "open_issues_count": 0,
        "license": null,
        "allow_forking": true,
        "is_template": false,
        "web_commit_signoff_required": false,
        "topics": [],
        "visibility": "public",
        "forks": 0,
        "open_issues": 0,
        "watchers": 0,
        "default_branch": "main",
        "allow_squash_merge": true,
        "allow_merge_commit": true,
        "allow_rebase_merge": true,
        "allow_auto_merge": false,
        "delete_branch_on_merge": false,
        "allow_update_branch": false,
        "use_squash_pr_title_as_default": false,
        "squash_merge_commit_message": "COMMIT_MESSAGES",
        "squash_merge_commit_title": "COMMIT_OR_PR_TITLE",
        "merge_commit_message": "PR_TITLE",
        "merge_commit_title": "MERGE_MESSAGE"
      }
    },
    "base": {
      "label": "venkatesh939:main",
      "ref": "main",
      "sha": "aa96d596745d03edcc2e310a4a540d2f93281985",
      "user": {
        "login": "venkatesh939",
        "id": 32451027,
        "node_id": "MDQ6VXNlcjMyNDUxMDI3",
        "avatar_url": "https://avatars.githubusercontent.com/u/32451027?v=4",
        "gravatar_id": "",
        "url": "https://api.github.com/users/venkatesh939",
        "html_url": "https://github.com/venkatesh939",
        "followers_url": "https://api.github.com/users/venkatesh939/followers",
        "following_url": "https://api.github.com/users/venkatesh939/following{/other_user}",
        "gists_url": "https://api.github.com/users/venkatesh939/gists{/gist_id}",
        "starred_url": "https://api.github.com/users/venkatesh939/starred{/owner}{/repo}",
        "subscriptions_url": "https://api.github.com/users/venkatesh939/subscriptions",
        "organizations_url": "https://api.github.com/users/venkatesh939/orgs",
        "repos_url": "https://api.github.com/users/venkatesh939/repos",
        "events_url": "https://api.github.com/users/venkatesh939/events{/privacy}",
        "received_events_url": "https://api.github.com/users/venkatesh939/received_events",
        "type": "User",
        "site_admin": false
      },
      "repo": {
        "id": 851909280,
        "node_id": "R_kgDOMscaoA",
        "name": "action-repo",
        "full_name": "venkatesh939/action-repo",
        "private": false,
        "owner": {
          "login": "venkatesh939",
          "id": 32451027,
          "node_id": "MDQ6VXNlcjMyNDUxMDI3",
          "avatar_url": "https://avatars.githubusercontent.com/u/32451027?v=4",
          "gravatar_id": "",
          "url": "https://api.github.com/users/venkatesh939",
          "html_url": "https://github.com/venkatesh939",
          "followers_url": "https://api.github.com/users/venkatesh939/followers",
          "following_url": "https://api.github.com/users/venkatesh939/following{/other_user}",
          "gists_url": "https://api.github.com/users/venkatesh939/gists{/gist_id}",
          "starred_url": "https://api.github.com/users/venkatesh939/starred{/owner}{/repo}",
          "subscriptions_url": "https://api.github.com/users/venkatesh939/subscriptions",
          "organizations_url": "https://api.github.com/users/venkatesh939/orgs",
          "repos_url": "https://api.github.com/users/venkatesh939/repos",
          "events_url": "https://api.github.com/users/venkatesh939/events{/privacy}",
          "received_events_url": "https://api.github.com/users/venkatesh939/received_events",
          "type": "User",
          "site_admin": false
        },
        "html_url": "https://github.com/venkatesh939/action-repo",
        "description": null,
        "fork": false,
        "url": "https://api.github.com/repos/venkatesh939/action-repo",
        "forks_url": "https://api.github.com/repos/venkatesh939/action-repo/forks",
        "keys_url": "https://api.github.com/repos/venkatesh939/action-repo/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/venkatesh939/action-repo/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/venkatesh939/action-repo/teams",
        "hooks_url": "https://api.github.com/repos/venkatesh939/action-repo/hooks",
        "issue_events_url": "https://api.github.com/repos/venkatesh939/action-repo/issues/events{/number}",
        "events_url": "https://api.github.com/repos/venkatesh939/action-repo/events",
        "assignees_url": "https://api.github.com/repos/venkatesh939/action-repo/assignees{/user}",
        "branches_url": "https://api.github.com/repos/venkatesh939/action-repo/branches{/branch}",
        "tags_url": "https://api.github.com/repos/venkatesh939/action-repo/tags",
        "blobs_url": "https://api.github.com/repos/venkatesh939/action-repo/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/venkatesh939/action-repo/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/venkatesh939/action-repo/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/venkatesh939/action-repo/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/venkatesh939/action-repo/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/venkatesh939/action-repo/languages",
        "stargazers_url": "https://api.github.com/repos/venkatesh939/action-repo/stargazers",
        "contributors_url": "https://api.github.com/repos/venkatesh939/action-repo/contributors",
        "subscribers_url": "https://api.github.com/repos/venkatesh939/action-repo/subscribers",
        "subscription_url": "https://api.github.com/repos/venkatesh939/action-repo/subscription",
        "commits_url": "https://api.github.com/repos/venkatesh939/action-repo/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/venkatesh939/action-repo/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/venkatesh939/action-repo/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/venkatesh939/action-repo/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/venkatesh939/action-repo/contents/{+path}",
        "compare_url": "https://api.github.com/repos/venkatesh939/action-repo/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/venkatesh939/action-repo/merges",
        "archive_url": "https://api.github.com/repos/venkatesh939/action-repo/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/venkatesh939/action-repo/downloads",
        "issues_url": "https://api.github.com/repos/venkatesh939/action-repo/issues{/number}",
        "pulls_url": "https://api.github.com/repos/venkatesh939/action-repo/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/venkatesh939/action-repo/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/venkatesh939/action-repo/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/venkatesh939/action-repo/labels{/name}",
        "releases_url": "https://api.github.com/repos/venkatesh939/action-repo/releases{/id}",
        "deployments_url": "https://api.github.com/repos/venkatesh939/action-repo/deployments",
        "created_at": "2024-09-03T22:33:18Z",
        "updated_at": "2024-09-04T10:30:34Z",
        "pushed_at": "2024-09-04T10:50:39Z",
        "git_url": "git://github.com/venkatesh939/action-repo.git",
        "ssh_url": "git@github.com:venkatesh939/action-repo.git",
        "clone_url": "https://github.com/venkatesh939/action-repo.git",
        "svn_url": "https://github.com/venkatesh939/action-repo",
        "homepage": null,
        "size": 30,
        "stargazers_count": 0,
        "watchers_count": 0,
        "language": "Python",
        "has_issues": true,
        "has_projects": true,
        "has_downloads": true,
        "has_wiki": true,
        "has_pages": false,
        "has_discussions": false,
        "forks_count": 0,
        "mirror_url": null,
        "archived": false,
        "disabled": false,
        "open_issues_count": 0,
        "license": null,
        "allow_forking": true,
        "is_template": false,
        "web_commit_signoff_required": false,
        "topics": [],
        "visibility": "public",
        "forks": 0,
        "open_issues": 0,
        "watchers": 0,
        "default_branch": "main",
        "allow_squash_merge": true,
        "allow_merge_commit": true,
        "allow_rebase_merge": true,
        "allow_auto_merge": false,
        "delete_branch_on_merge": false,
        "allow_update_branch": false,
        "use_squash_pr_title_as_default": false,
        "squash_merge_commit_message": "COMMIT_MESSAGES",
        "squash_merge_commit_title": "COMMIT_OR_PR_TITLE",
        "merge_commit_message": "PR_TITLE",
        "merge_commit_title": "MERGE_MESSAGE"
      }
    },
    "_links": {
      "self": {
        "href": "https://api.github.com/repos/venkatesh939/action-repo/pulls/11"
      },
      "html": {
        "href": "https://github.com/venkatesh939/action-repo/pull/11"
      },
      "issue": {
        "href": "https://api.github.com/repos/venkatesh939/action-repo/issues/11"
      },
      "comments": {
        "href": "https://api.github.com/repos/venkatesh939/action-repo/issues/11/comments"
      },
      "review_comments": {
        "href": "https://api.github.com/repos/venkatesh939/action-repo/pulls/11/comments"
      },
      "review_comment": {
        "href": "https://api.github.com/repos/venkatesh939/action-repo/pulls/comments{/number}"
      },
      "commits": {
        "href": "https://api.github.com/repos/venkatesh939/action-repo/pulls/11/commits"
      },
      "statuses": {
        "href": "https://api.github.com/repos/venkatesh939/action-repo/statuses/2ed2a7ff911e94327d043eac702ad6e8f5a50189"
      }
    },
    "author_association": "OWNER",
    "auto_merge": null,
    "active_lock_reason": null,
    "merged": true,
    "mergeable": null,
    "rebaseable": null,
    "mergeable_state": "unknown",
    "merged_by": {
      "login": "venkatesh939",
      "id": 32451027,
      "node_id": "MDQ6VXNlcjMyNDUxMDI3",
      "avatar_url": "https://avatars.githubusercontent.com/u/32451027?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/venkatesh939",
      "html_url": "https://github.com/venkatesh939",
      "followers_url": "https://api.github.com/users/venkatesh939/followers",
      "following_url": "https://api.github.com/users/venkatesh939/following{/other_user}",
      "gists_url": "https://api.github.com/users/venkatesh939/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/venkatesh939/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/venkatesh939/subscriptions",
      "organizations_url": "https://api.github.com/users/venkatesh939/orgs",
      "repos_url": "https://api.github.com/users/venkatesh939/repos",
      "events_url": "https://api.github.com/users/venkatesh939/events{/privacy}",
      "received_events_url": "https://api.github.com/users/venkatesh939/received_events",
      "type": "User",
      "site_admin": false
    },
    "comments": 0,
    "review_comments": 0,
    "maintainer_can_modify": false,
    "commits": 2,
    "additions": 1455,
    "deletions": 107,
    "changed_files": 3
  },
  "repository": {
    "id": 851909280,
    "node_id": "R_kgDOMscaoA",
    "name": "action-repo",
    "full_name": "venkatesh939/action-repo",
    "private": false,
    "owner": {
      "login": "venkatesh939",
      "id": 32451027,
      "node_id": "MDQ6VXNlcjMyNDUxMDI3",
      "avatar_url": "https://avatars.githubusercontent.com/u/32451027?v=4",
      "gravatar_id": "",
      "url": "https://api.github.com/users/venkatesh939",
      "html_url": "https://github.com/venkatesh939",
      "followers_url": "https://api.github.com/users/venkatesh939/followers",
      "following_url": "https://api.github.com/users/venkatesh939/following{/other_user}",
      "gists_url": "https://api.github.com/users/venkatesh939/gists{/gist_id}",
      "starred_url": "https://api.github.com/users/venkatesh939/starred{/owner}{/repo}",
      "subscriptions_url": "https://api.github.com/users/venkatesh939/subscriptions",
      "organizations_url": "https://api.github.com/users/venkatesh939/orgs",
      "repos_url": "https://api.github.com/users/venkatesh939/repos",
      "events_url": "https://api.github.com/users/venkatesh939/events{/privacy}",
      "received_events_url": "https://api.github.com/users/venkatesh939/received_events",
      "type": "User",
      "site_admin": false
    },
    "html_url": "https://github.com/venkatesh939/action-repo",
    "description": null,
    "fork": false,
    "url": "https://api.github.com/repos/venkatesh939/action-repo",
    "forks_url": "https://api.github.com/repos/venkatesh939/action-repo/forks",
    "keys_url": "https://api.github.com/repos/venkatesh939/action-repo/keys{/key_id}",
    "collaborators_url": "https://api.github.com/repos/venkatesh939/action-repo/collaborators{/collaborator}",
    "teams_url": "https://api.github.com/repos/venkatesh939/action-repo/teams",
    "hooks_url": "https://api.github.com/repos/venkatesh939/action-repo/hooks",
    "issue_events_url": "https://api.github.com/repos/venkatesh939/action-repo/issues/events{/number}",
    "events_url": "https://api.github.com/repos/venkatesh939/action-repo/events",
    "assignees_url": "https://api.github.com/repos/venkatesh939/action-repo/assignees{/user}",
    "branches_url": "https://api.github.com/repos/venkatesh939/action-repo/branches{/branch}",
    "tags_url": "https://api.github.com/repos/venkatesh939/action-repo/tags",
    "blobs_url": "https://api.github.com/repos/venkatesh939/action-repo/git/blobs{/sha}",
    "git_tags_url": "https://api.github.com/repos/venkatesh939/action-repo/git/tags{/sha}",
    "git_refs_url": "https://api.github.com/repos/venkatesh939/action-repo/git/refs{/sha}",
    "trees_url": "https://api.github.com/repos/venkatesh939/action-repo/git/trees{/sha}",
    "statuses_url": "https://api.github.com/repos/venkatesh939/action-repo/statuses/{sha}",
    "languages_url": "https://api.github.com/repos/venkatesh939/action-repo/languages",
    "stargazers_url": "https://api.github.com/repos/venkatesh939/action-repo/stargazers",
    "contributors_url": "https://api.github.com/repos/venkatesh939/action-repo/contributors",
    "subscribers_url": "https://api.github.com/repos/venkatesh939/action-repo/subscribers",
    "subscription_url": "https://api.github.com/repos/venkatesh939/action-repo/subscription",
    "commits_url": "https://api.github.com/repos/venkatesh939/action-repo/commits{/sha}",
    "git_commits_url": "https://api.github.com/repos/venkatesh939/action-repo/git/commits{/sha}",
    "comments_url": "https://api.github.com/repos/venkatesh939/action-repo/comments{/number}",
    "issue_comment_url": "https://api.github.com/repos/venkatesh939/action-repo/issues/comments{/number}",
    "contents_url": "https://api.github.com/repos/venkatesh939/action-repo/contents/{+path}",
    "compare_url": "https://api.github.com/repos/venkatesh939/action-repo/compare/{base}...{head}",
    "merges_url": "https://api.github.com/repos/venkatesh939/action-repo/merges",
    "archive_url": "https://api.github.com/repos/venkatesh939/action-repo/{archive_format}{/ref}",
    "downloads_url": "https://api.github.com/repos/venkatesh939/action-repo/downloads",
    "issues_url": "https://api.github.com/repos/venkatesh939/action-repo/issues{/number}",
    "pulls_url": "https://api.github.com/repos/venkatesh939/action-repo/pulls{/number}",
    "milestones_url": "https://api.github.com/repos/venkatesh939/action-repo/milestones{/number}",
    "notifications_url": "https://api.github.com/repos/venkatesh939/action-repo/notifications{?since,all,participating}",
    "labels_url": "https://api.github.com/repos/venkatesh939/action-repo/labels{/name}",
    "releases_url": "https://api.github.com/repos/venkatesh939/action-repo/releases{/id}",
    "deployments_url": "https://api.github.com/repos/venkatesh939/action-repo/deployments",
    "created_at": "2024-09-03T22:33:18Z",
    "updated_at": "2024-09-04T10:30:34Z",
    "pushed_at": "2024-09-04T10:50:39Z",
    "git_url": "git://github.com/venkatesh939/action-repo.git",
    "ssh_url": "git@github.com:venkatesh939/action-repo.git",
    "clone_url": "https://github.com/venkatesh939/action-repo.git",
    "svn_url": "https://github.com/venkatesh939/action-repo",
    "homepage": null,
    "size": 30,
    "stargazers_count": 0,
    "watchers_count": 0,
    "language": "Python",
    "has_issues": true,
    "has_projects": true,
    "has_downloads": true,
    "has_wiki": true,
    "has_pages": false,
    "has_discussions": false,
    "forks_count": 0,
    "mirror_url": null,
    "archived": false,
    "disabled": false,
    "open_issues_count": 0,
    "license": null,
    "allow_forking": true,
    "is_template": false,
    "web_commit_signoff_required": false,
    "topics": [],
    "visibility": "public",
    "forks": 0,
    "open_issues": 0,
    "watchers": 0,
    "default_branch": "main"
  },
  "sender": {
    "login": "venkatesh939",
    "id": 32451027,
    "node_id": "MDQ6VXNlcjMyNDUxMDI3",
    "avatar_url": "https://avatars.githubusercontent.com/u/32451027?v=4",
    "gravatar_id": "",
    "url": "https://api.github.com/users/venkatesh939",
    "html_url": "https://github.com/venkatesh939",
    "followers_url": "https://api.github.com/users/venkatesh939/followers",
    "following_url": "https://api.github.com/users/venkatesh939/following{/other_user}",
    "gists_url": "https://api.github.com/users/venkatesh939/gists{/gist_id}",
    "starred_url": "https://api.github.com/users/venkatesh939/starred{/owner}{/repo}",
    "subscriptions_url": "https://api.github.com/users/venkatesh939/subscriptions",
    "organizations_url": "https://api.github.com/users/venkatesh939/orgs",
    "repos_url": "https://api.github.com/users/venkatesh939/repos",
    "events_url": "https://api.github.com/users/venkatesh939/events{/privacy}",
    "received_events_url": "https://api.github.com/users/venkatesh939/received_events",
    "type": "User",
    "site_admin": false
  }
}
"""

# Parse JSON data
# data = json.loads(json_data)

def extract_info_from_github_webhook(payload):
    data = json.loads(payload)
    
    # Determine event type
    if 'ref' in data:
        event_type = 'push'
    elif 'pull_request' in data:
        if 'action' in data and data['action'] == 'closed' and data['pull_request'].get('merged'):
            event_type = 'merge'
        else:
            event_type = 'pull_request'
    else:
        event_type = 'unknown'
    
    print(f"Event type detected: {event_type}")
    
    result = {}

    if event_type == 'push':
        # Extract info for a push event
        result['author'] = data['pusher']['name']
        result['from_branch'] = data['ref'].split('/')[-1]
        result['to_branch'] = 'N/A'  # Push event doesn't have a 'to_branch'
        result['timestamp'] = data['commits'][0]['timestamp'] if data['commits'] else 'N/A'
    
    elif event_type == 'pull_request':
        # Extract info for a pull request event
        pr = data['pull_request']
        result['author'] = pr['user']['login']
        result['from_branch'] = pr['head']['ref']
        result['to_branch'] = pr['base']['ref']
        result['timestamp'] = pr['created_at']
    
    elif event_type == 'merge':
        # Extract info for a merge event
        pr = data['pull_request']
        result['author'] = pr['user']['login']
        result['from_branch'] = pr['head']['ref']
        result['to_branch'] = pr['base']['ref']
        result['timestamp'] = pr['merged_at']
    
    else:
        print(f"Unsupported event type: {event_type}")
        raise ValueError(f"Unsupported event type: {event_type}")

    print(result)

extract_info_from_github_webhook(json_data)





# result = {
#     "_id": data["pull_request"]["id"],
#     "object id": data["pull_request"]["node_id"],
#     "request_id": str(data["number"]),
#     "author": data["pull_request"]["user"]["login"],
#     "action": data["action"],
#     "from_branch": data["pull_request"]["head"]["ref"],
#     "to_branch": data["pull_request"]["base"]["ref"],
#     "timestamp": data["pull_request"]["created_at"]
# }




# # Print extracted information
# for key, value in result.items():
#     print(f"{key}: {value}")


# records = []
# for commit in data.get("commits", []):
#     record = {
#         "_id": commit.get("id"),
#         "request_id": commit.get("id"),  # Assuming `id` is the request_id
#         "author": commit.get("author", {}).get("name"),
#         "action": "PUSH" if "Merge pull request" not in commit.get("message", "") else "MERGE",
#         "from_branch": data.get("before"),
#         "to_branch": data.get("after"),
#         "timestamp": commit.get("timestamp")
#     }
#     records.append(record)
# print(records)