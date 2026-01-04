from fastapi import FastAPI
from scraper import scrape_zomato

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Zomato Scraper API is live 🚀"}

@app.get("/scrape/{city}")
def scrape_city(city: str):
    df = scrape_zomato(city)
    return {
        "city": city,
        "total_restaurants": len(df),
        "data": df.to_dict(orient="records")
    }
