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
  <img src="https://img.shields.io/badge/Railway-Deploy-black?logo=railway" />
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
