# AI CHATBOT WITH AUTHENTICATION

## Installation and Setup
### Setting up .env
 Set Up Environment Variables. Create a .env file 
```  
SECRET_KEY="your-super-secret-jwt-key" 
GROQ_API_KEY="gsk_your_actual_groq_api_key_here"
```
### Downloading dependencies
   
        cd backend
        python3 -m venv venv
        source venv/bin/activate 
        pip install -r requirements.txt
        
## Running the servers 
#### Terminal 1 (Auth Backend):
        
        cd backend/Auth
        uvicorn main:app --reload
**Auth API Docs:** http://localhost:8000/docs        

#### Terminal 2 (Chatbot Backend):        
    
        cd backend/chatbot
        uvicorn grog:app --reload --port 8080

**Auth API Docs:** http://localhost:8080/docs  
#### Terminal 3 (Frontend):  

        cd chatbot
        npm install
        npm run dev
**Frontend App:** http://localhost:3000        

## TECH-STACK

### Frontend:
- Next.js
- React
- Tailwind CSS
- shadcn/ui

### Backend 
- FastAPI(python)

### Database
- SQLite

### Authentication
- JWT (JSON Web Token)

### LLM 
- Groq API (Llama-3.1-8b-instant model)

