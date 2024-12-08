from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from typing import List, Optional
from dotenv import load_dotenv
import httpx
from transformers import pipeline
import torch
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = FastAPI(
    title="News Summarization API",
    description="An API that fetches and summarizes news articles",
    version="1.0.0"
)

# Initialize the summarization pipeline
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn",
    device=0 if torch.cuda.is_available() else -1
)

class Article(BaseModel):
    title: str
    url: Optional[str]
    content: str
    summary: Optional[str] = None

class NewsResponse(BaseModel):
    articles: List[Article]
    total: int

async def generate_summary(text: str) -> str:
    try:
        max_chunk_length = 1024
        if len(text) > max_chunk_length:
            text = text[:max_chunk_length]
        
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        logger.error(f"Summarization error: {str(e)}")
        return "Summary generation failed"

@app.get("/news/", response_model=NewsResponse)
async def get_news(category: Optional[str] = None, limit: int = 10):
    try:
        NEWS_API_KEY = os.getenv("NEWS_API_KEY")
        logger.info(f"Checking NEWS_API_KEY: {'Present' if NEWS_API_KEY else 'Missing'}")
        
        if not NEWS_API_KEY:
            raise HTTPException(status_code=500, detail="News API key not configured")
        
        base_url = "https://newsapi.org/v2/top-headlines"
        params = {
            "apiKey": NEWS_API_KEY,
            "pageSize": limit,
            "language": "en"
        }
        if category:
            params["category"] = category

        logger.info(f"Making request to News API with params: {params}")
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(base_url, params=params)
                logger.info(f"News API Response Status: {response.status_code}")
                
                if response.status_code != 200:
                    error_detail = response.json().get("message", "Unknown error")
                    logger.error(f"News API Error: {error_detail}")
                    raise HTTPException(status_code=response.status_code, detail=error_detail)
                
                data = response.json()
                logger.info(f"Successfully received {len(data.get('articles', []))} articles")
                
                articles = []
                for article in data.get("articles", []):
                    content = article.get("content", "")
                    summary = await generate_summary(content) if content else "No content available"
                    
                    articles.append(Article(
                        title=article["title"],
                        url=article["url"],
                        content=content,
                        summary=summary
                    ))

                return NewsResponse(articles=articles, total=len(articles))
                
            except httpx.RequestError as e:
                logger.error(f"Request error: {str(e)}")
                raise HTTPException(status_code=500, detail=f"News API request failed: {str(e)}")

    except HTTPException as he:
        raise he
    except Exception as e:
        logger.error(f"Unexpected error in get_news: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/summarize/", response_model=Article)
async def summarize_text(text: str):
    if not text:
        raise HTTPException(status_code=400, detail="No text provided")
    
    summary = await generate_summary(text)
    return Article(
        title="Custom Text Summary",
        url=None,
        content=text,
        summary=summary
    )