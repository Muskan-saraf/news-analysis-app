from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
import httpx
from datetime import datetime

load_dotenv()

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_BASE_URL = "https://newsapi.org/v2"

@app.get("/api/v1/news")
async def get_news():
    if not NEWS_API_KEY:
        raise HTTPException(status_code=500, detail="News API key not configured")
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{NEWS_API_BASE_URL}/top-headlines",
                params={
                    "apiKey": NEWS_API_KEY,
                    "language": "en",
                    "pageSize": 12  # Number of articles to fetch
                }
            )
            
            if response.status_code != 200:
                raise HTTPException(
                    status_code=response.status_code,
                    detail=f"News API error: {response.text}"
                )

            data = response.json()
            
            # Transform the response to match our frontend expectations
            articles = []
            for article in data.get("articles", []):
                articles.append({
                    "title": article.get("title", ""),
                    "url": article.get("url", ""),
                    "content": article.get("content", ""),
                    "summary": article.get("description", ""),
                    "source": article.get("source", {}).get("name", ""),
                    "publishedAt": article.get("publishedAt", ""),
                    "imageUrl": article.get("urlToImage", "")
                })

            return {"articles": articles}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))