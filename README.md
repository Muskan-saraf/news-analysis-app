# News Analysis Application

A full-stack application that fetches, analyzes, and summarizes news articles using AI.

## Features

- Fetches latest news articles from News API
- Generates AI-powered summaries of articles
- Stores summaries and analysis in SQLite database
- RESTful API built with FastAPI
- React frontend for displaying news and summaries

## Backend Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
- Create a `.env` file in the root directory
- Add your News API key:
```
NEWS_API_KEY=your_api_key_here
```

4. Run the application:
```bash
uvicorn main:app --reload
```

## Frontend Setup

(To be added)

## API Endpoints

- GET `/news/`: Fetch and summarize latest news articles
- GET `/summarize/`: Summarize custom text

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details
