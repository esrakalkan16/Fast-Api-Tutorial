from fastapi import FastAPI, HTTPException

app = FastAPI()

text_posts = {
    1: {"title": "New Post", "content": "Cool test post"},
    2: {"title": "Python Tip", "content": "Use list comprehensions for cleaner and more readable loops."},
    3: {"title": "Daily Motivation", "content": "Consistency beats intensity every single time."},
    4: {"title": "Fun Fact", "content": "The first computer bug was an actual moth found in the Harvard Mark II."},
    5: {"title": "Update", "content": "Just launched my new project! Excited to share more soon."},
    6: {"title": "Tech Insight", "content": "Async IO in Python can massively speed up I/O-bound tasks."},
    7: {"title": "Quote", "content": "Programs must be written for people to read, and only incidentally for machines to execute."},
    8: {"title": "Weekend Plans", "content": "Might finally clean up my GitHub repos… or just play some games."},
    9: {"title": "Learning Note", "content": "FastAPI automatically generates interactive API documentation."},
    10: {"title": "Reminder", "content": "Small progress every day adds up to big results."},
    11:{"title": "Remove", "content": "FastAPI cool"}
}

@app.get("/posts")
def get_all_posts():
    return text_posts
@app.get("/posts/{id}")
def get_post(id: int):

    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")

    return text_posts.get(id)