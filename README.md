# Oso Python Quickstart

Follow along [here](https://docs.osohq.com/getting-started/quickstart.html).

## Instructions

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
has_permission(_, "read", repository: Repository) if
  repository.public;
```

Now, when you visit
[http://localhost:5000/repo/react](http://localhost:5000/repo/react), you should
see a proper 200 response, because the `react` repository is marked as public
in `app/model.py`.
