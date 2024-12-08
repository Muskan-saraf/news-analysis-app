# News Analysis Application

A full-stack application that fetches and displays news articles using Next.js and FastAPI.

## Features

- Fetches latest news articles from News API
- Displays news in a responsive grid layout
- Shows article details including source and publication date

## Setup

### Backend Setup
1. Navigate to the backend directory:
```bash
cd backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your News API key:
```
NEWS_API_KEY=your_api_key_here
```

4. Start the backend server:
```bash
uvicorn main:app --reload
```

### Frontend Setup
1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000

## Project Structure

```
News-Analysis/
├── backend/
│   ├── main.py
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── components/
    │   └── app/
    ├── package.json
    └── tsconfig.json
```

## Technologies Used

- Frontend: Next.js, React, TypeScript, Tailwind CSS
- Backend: FastAPI, Python
- API: News API

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
