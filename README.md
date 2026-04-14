# Insta-DL

<img src="https://raw.githubusercontent.com/YOUR-IMAGE.png" width="200"/>

**A simple and professional Instagram Reel downloader API built with Python.**

*Lightweight • Clean structure • Easy to use*

---

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" />
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask" />
  <img src="https://img.shields.io/badge/API-REST-green" />
</p>

---
## **Quick Navigation**

[Overview](#overview)  [Features](#features)

[Where to Host](#where-to-host)

[Project Structure](#project-structure)  [Installation](#installation)

[Run the Application](#run-the-application)

[API Usage](#api-usage)  [Example Request](#example-request)

[Example Response](#example-response)

[Notes](#notes)  [License](#license)
---

## **Overview**

*Insta-DL* is a minimal API that extracts direct download links for Instagram reels.

It is designed with a **clean architecture**, making it easy to maintain, extend, and deploy.

The API returns structured JSON with video and thumbnail links.

---

## **Features**

- Clean and modular project structure  
- Fast and simple API  
- Returns direct video download link  
- Lightweight dependencies  
- Easy to run locally

---

## **Where to Host**

*You can deploy this API on multiple platforms depending on your needs.*

<p align="left">
  <img src="https://img.shields.io/badge/Localhost-Run%20Locally-blue?logo=linux" />
  <img src="https://img.shields.io/badge/Render-Deploy-green?logo=render" />
  <img src="https://img.shields.io/badge/Railway-Deploy-cyan?logo=railway" />
  <img src="https://img.shields.io/badge/Heroku-Cloud-purple?logo=heroku" />
  <img src="https://img.shields.io/badge/Cloudflare-Workers-orange?logo=cloudflare" />
  <img src="https://img.shields.io/badge/VPS-Ubuntu%2FServer-red?logo=ubuntu" />
</p>

### **Supported Platforms**

- **Localhost** – *Best for development and testing*  
- **Render** – *Simple deployment with good free tier*  
- **Railway** – *Quick setup and developer-friendly*  
- **Heroku** – *Classic cloud platform (may require paid plan)*  
- **Cloudflare Workers** – *Fast edge deployment (limited for Python apps)*  
- **VPS (Ubuntu / Linux Server)** – *Full control and best performance*  

---

### **Recommendation**

- For beginners → **Render / Railway**  
- For production → **VPS (Ubuntu server)**  
- For testing → **Localhost**

---

## **Project Structure**

*Organized for clarity and scalability*

    insta-dl/
    ├── app/
    │   ├── __init__.py
    │   ├── main.py
    │   ├── routes/
    │   │   └── downloader.py
    │   ├── services/
    │   │   └── scraper.py
    │   └── utils/
    │       └── headers.py
    ├── requirements.txt
    ├── README.md
    ├── LICENSE

---

## **Installation**

*Install dependencies*

    pip install -r requirements.txt

---

## **Run the Application**

*Start the server locally*

    python app/main.py
            OR
    python3 app/main.py
---

## **API Usage**

*Endpoint*

    GET /api/downloader?url=INSTAGRAM_URL

---

## **Example Request**

    curl "http://localhost:5000/api/downloader?url=https://www.instagram.com/reel/ABCDEF1234/"

---

## **Example Response**

    {
      "status": "success",
      "data": {
        "download": "video_url",
        "thumbnail": "image_url"
      }
    }

---
## **Notes**

*Important considerations*

- This API uses an external provider for extraction  
- Availability depends on provider response  
- For production use, consider adding fallback logic

---

## **License**

*This project is licensed under the MIT License.*
