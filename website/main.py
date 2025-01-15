from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Use lifespan to handle startup and shutdown events
@asynccontextmanager
async def lifespan(app: FastAPI):
    # On startup
    try:
        # Try a simple query to check the connection
        await db.command("ping")  
        print("MongoDB connected successfully!")
        yield  
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise e
    finally:
        # On shutdown
        client.close()  # Clean up the MongoDB client

# Create FastAPI app and pass lifespan
app = FastAPI(lifespan=lifespan)

# MongoDB configuration
MONGO_DETAILS = os.getenv("MONGODB_URL")  # Replace with your MongoDB URI

# Serve static files
app.mount("/static", StaticFiles(directory="../"), name="static")
app.mount("/web_images", StaticFiles(directory="web_images"), name="web_images")
app.mount("/styles", StaticFiles(directory="styles"), name="styles")
app.mount("/scripts", StaticFiles(directory="scripts"), name="scripts")
app.mount("/software", StaticFiles(directory="../software"), name="software")
app.mount("/Documentation", StaticFiles(directory="../Documentation"), name="Documentation")

# Set up Jinja2 templates for dynamic HTML rendering
templates = Jinja2Templates(directory="templates/")

# MongoDB setup
MONGODB_URL = os.getenv("MONGODB_URL")
client = AsyncIOMotorClient(MONGODB_URL)
db = client.social_media_products

# Image Collections
review_collection = db["reviews"]


# Include Routers

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request): 
    # Provide the context including the request object
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/documentation", response_class=HTMLResponse)
def documentation(request: Request):
    return templates.TemplateResponse("documentation.html", {"request": request})

@app.get("/versions", response_class=HTMLResponse)
def versions(request: Request):
    return templates.TemplateResponse("versions.html", {"request": request})

@app.get("/support", response_class=HTMLResponse)
def support(request: Request):
    return templates.TemplateResponse("support.html", {"request": request})

@app.get("/contributor", response_class=HTMLResponse)
def contributor(request: Request):
    return templates.TemplateResponse("contributor.html", {"request": request})

@app.get("/reviews", response_class=HTMLResponse)
def reviews(request: Request):
    return templates.TemplateResponse("reviews.html", {"request": request})

@app.get("/license", response_class=HTMLResponse)
def license(request: Request):
    return templates.TemplateResponse("license.html", {"request": request})

@app.get("/404", response_class=HTMLResponse)
def not_found(request: Request):
    return templates.TemplateResponse("404.html", {"request": request})


