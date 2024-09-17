# DEPRECATED

We deprecated the legacy Oso open source library in December 2023. We have plans for the next open source release and we’re looking forward to getting feedback from the community leading up to that point. In the meantime, if you’re happy using the Oso open source library now, nothing needs to change – i.e., we are not end-of-lifing (EOL) the library and we’ll continue to provide support and critical bug fixes.

[This post](https://www.osohq.com/docs/oss/getting-started/deprecation.html) describes how we got here, what this change means for existing users, and what you can expect from Oso in the future. If you have questions, you can always reach out to us in our [community Slack](https://join-slack.osohq.com).

If you’re building authorization for more than one service or want to share a policy across multiple applications, read how to get started with [Oso Cloud](https://www.osohq.com/docs).

## Oso Python Quickstart Instructions

1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the server: `FLASK_APP=app.server python -m flask run`

## Make some changes

If you visit
[http://localhost:5000/repo/gmail](http://localhost:5000/repo/gmail), you
should get a 200 response. If you visit
[http://localhost:5000/repo/react](http://localhost:5000/repo/react), you
should see a 404.

Add this code to `app/main.polar`:
```python
has_permission(_actor: User, "read", repository: Repository) if
  repository.is_public;
```

Now, when you visit
[http://localhost:5000/repo/react](http://localhost:5000/repo/react), you should
see a proper 200 response, because the `react` repository is marked as public
in `app/models.py`.
