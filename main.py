from fastapi import FastAPI, Query
import instaloader

app = FastAPI()

@app.get("/scrape")
def scrape_reel(url: str = Query(...)):
    try:
        shortcode = url.strip("/").split("/")[-1]
        L = instaloader.Instaloader()
        post = instaloader.Post.from_shortcode(L.context, shortcode)

        return {
            "username": post.owner_username,
            "caption": post.caption,
            "shortcode": shortcode,
        }
    except Exception as e:
        return {"error": str(e)}
