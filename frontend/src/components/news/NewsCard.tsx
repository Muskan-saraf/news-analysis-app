"use client";

import React from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '../ui/card';
import { ExternalLink, Clock } from 'lucide-react';

const NewsCard = ({ title, summary, url, source, publishedAt }) => {
  const formatDate = (dateString) => {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric'
    });
  };

  return (
    <Card className="h-full flex flex-col hover:shadow-lg transition-duration-300">
      <CardHeader>
        <div className="flex items-center gap-2 text-sm text-gray-500 mb-2">
          {source && <span className="font-medium">{source}</span>}
          {publishedAt && (
            <div className="flex items-center gap-1">
              <Clock className="h-4 w-4" />
              {formatDate(publishedAt)}
            </div>
          )}
        </div>
        <CardTitle className="text-lg">{title}</CardTitle>
      </CardHeader>
      <CardContent className="flex-grow flex flex-col justify-between">
        <p className="text-gray-600 mb-4">{summary}</p>
        {url && (
          <a
            href={url}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center text-blue-500 hover:text-blue-600"
          >
            Read full article <ExternalLink className="ml-1 h-4 w-4" />
          </a>
        )}
      </CardContent>
    </Card>
  );
};

export default NewsCard;