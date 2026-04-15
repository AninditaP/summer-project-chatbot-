# Fullstack AI Chatbot Application


This project is a full-stack chatbot application featuring a Next.js frontend, a FastAPI authentication server (with SQLite and JWT), and a dedicated FastAPI chatbot backend powered by the Groq API (Llama 3).

## Project Structure

```text
.
├── frontend/             # Next.js frontend application
└── backend/
    ├── Auth/             # FastAPI Authentication server (SQLite + JWT)
    ├── chatbot/          # FastAPI Chatbot server (Groq LLM)
    └── requirements.txt  # Consolidated Python dependencies

## Project Structure
1. Clone the Repository
First, clone the repository to your local machine:

git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

2. Set Up Environment Variables (.env)
    You need to configure your secret keys for both the authentication and chatbot servers.

    Create a .env file in the backend/Auth directory AND the backend/chatbot directory (or point them to a shared one) and add the following variables:

    # Required for JWT Token generation (Auth Server)
    SECRET_KEY="your-super-secret-jwt-key"

    # Required for Llama 3 Chatbot (Chatbot Server)
    GROQ_API_KEY="gsk_your_actual_groq_api_key_here"

3.Running the Application

    To run the application locally, you will need to open three separate terminal windows: one for the Auth server, one for the Chatbot server, and one for the Frontend.

    Terminal 1: Install Dependencies & Run the Auth Server (Port 8000)
    This server handles user login, registration, password hashing, and JWT token generation.

        # Navigate to the backend directory
        cd backend

        # Create and activate a virtual environment (Recommended)
        python3 -m venv venv
        source venv/bin/activate  # On Windows use: venv\Scripts\activate

        # Install all backend dependencies
        pip install -r requirements.txt

        # Navigate to the Auth directory and run the server
        cd Auth
        uvicorn main:app --reload
    
    Terminal 2: Run the Chatbot Server (Port 8080)
    This server securely connects to the Groq API to generate AI responses.
        # Navigate to the backend directory
        cd backend

        # Activate the same virtual environment
        source venv/bin/activate  # On Windows use: venv\Scripts\activate

        # Navigate to the chatbot directory and run the server on port 8080
        cd chatbot
        uvicorn grog:app --reload --port 8080

    Terminal 3: Run the Frontend (Next.js)
    This runs the UI layer where users can log in, sign up, and chat.    
        # Navigate to the frontend directory
        cd frontend  

        # Install dependencies
        npm install

        # Start the development server
        npm run dev

Tech Stack
Frontend: Next.js, React, Tailwind CSS, shadcn/ui
Backend: FastAPI (Python)
Database: SQLite
Authentication: JWT (JSON Web Tokens) with passlib/bcrypt
AI/LLM: Groq API (Llama-3.1-8b-instant model)