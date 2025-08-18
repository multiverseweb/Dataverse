import os

try:
    # Optional: load variables from a local .env if present
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    # dotenv is optional; if not installed, we fall back to environment only
    pass

# Database configuration sourced from environment variables.
# Provide these in a local .env (see .env.example) or your shell environment.
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

# Optional explicit database name. Defaults to the application's expected schema.
DB_NAME = os.getenv("DB_NAME", "DATAVERSE")