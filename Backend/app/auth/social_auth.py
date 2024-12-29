# backend/app/auth/social_auth.py
from fastapi import APIRouter, HTTPException
import requests

social_auth_router = APIRouter()

# Google Sign-In Endpoint
@social_auth_router.post("/google")
def google_sign_in(token: str):
    """
    Handle Google OAuth2 sign-in.
    :param token: Google ID token.
    :return: User information extracted from Google.
    """
    google_url = "https://oauth2.googleapis.com/tokeninfo"
    response = requests.get(google_url, params={"id_token": token})

    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Invalid Google token")

    user_info = response.json()
    return {
        "email": user_info.get("email"),
        "name": user_info.get("name"),
        "picture": user_info.get("picture")
    }

# GitHub Sign-In Endpoint
@social_auth_router.post("/github")
def github_sign_in(code: str):
    """
    Handle GitHub OAuth2 sign-in.
    :param code: GitHub authorization code.
    :return: User information extracted from GitHub.
    """
    github_url = "https://github.com/login/oauth/access_token"
    client_id = "your_github_client_id"  # Replace with your GitHub client ID
    client_secret = "your_github_client_secret"  # Replace with your GitHub client secret

    # Exchange code for access token
    token_response = requests.post(github_url, headers={"Accept": "application/json"}, data={
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code
    })

    if token_response.status_code != 200:
        raise HTTPException(status_code=400, detail="Invalid GitHub authorization code")

    access_token = token_response.json().get("access_token")

    # Fetch user info from GitHub
    user_response = requests.get("https://api.github.com/user", headers={
        "Authorization": f"Bearer {access_token}"
    })

    if user_response.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to fetch GitHub user info")

    user_info = user_response.json()
    return {
        "email": user_info.get("email"),
        "username": user_info.get("login"),
        "avatar_url": user_info.get("avatar_url")
    }
