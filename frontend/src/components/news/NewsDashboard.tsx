"use client";

import React, { useState, useEffect } from 'react';
import NewsCard from './NewsCard';
import { Loader2 } from 'lucide-react';

const NewsDashboard = () => {
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const fetchNews = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/v1/news');
      if (!response.ok) throw new Error('Failed to fetch news');
      const data = await response.json();
      setNews(data.articles);
      setError('');
    } catch (err) {
      console.error('Error:', err);
      setError('Failed to load news');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchNews();
  }, []);

  if (loading) {
    return (
      <div className="flex justify-center items-center min-h-[400px]">
        <Loader2 className="h-8 w-8 animate-spin" />
      </div>
    );
  }

  if (error) {
    return (
      <div className="text-red-500 text-center p-4 border border-red-200 rounded-lg bg-red-50">
        <p className="font-semibold">Error loading news</p>
        <p className="text-sm">{error}</p>
        <button 
          onClick={fetchNews}
          className="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
        >
          Try Again
        </button>
      </div>
    );
  }

  return (
    <div className="container mx-auto p-4">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-3xl font-bold">Latest News</h1>
        <button 
          onClick={fetchNews}
          className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
        >
          Refresh
        </button>
      </div>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {news.map((article, index) => (
          <NewsCard
            key={index}
            title={article.title}
            summary={article.summary}
            url={article.url}
            source={article.source}
            publishedAt={article.publishedAt}
          />
        ))}
      </div>
    </div>
  );
};

export default NewsDashboard;