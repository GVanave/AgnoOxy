# AgnoOxy Agent 🕸️🤖

A versatile and intelligent AI agent built using the **Agno Framework** and **Oxylabs** proxies, powered by **Ollama's llama3.2:1b** model. This agent is capable of web scraping and providing structured, concise responses to queries about nearby facilities, currently including Hotels and Fuel Stations, with plans to support more services in the future.

---

## 🚀 Features
- **Intelligent Agent:** Utilizes the Agno framework for building responsive and context-aware agents.
- **Web Scraping:** Integrated with **Oxylabs proxies** to reliably scrape accurate real-time data from the web.
- **Structured Output:** Provides neatly formatted markdown outputs for easy readability.
- **Scalable Architecture:** Designed to easily accommodate future extensions, supporting new types of data queries.

---

## 🛠️ Tech Stack
- **Framework:** [Agno](https://github.com/agno-ai) 
- **Model:** [Ollama - llama3.2:1b](https://ollama.com/)
- **Web Scraping:** [Oxylabs](https://oxylabs.io/)
- **UI:** [Streamlit](https://streamlit.io/) (Optional for frontend visualization)

---

## 🎯 Currently Supported Services
- **Hotel Search**: Lists nearby hotels within a 5km radius, including names, addresses, and ratings.
- **Fuel Station Search**: Lists nearby fuel stations within a specified radius, clearly formatted with names, addresses, and ratings.

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- An active Oxylabs subscription (API Key required)
- Ollama setup (`llama3.2:1b` model downloaded locally)

### Steps
1. Clone this repository:
```bash
git clone <your-repo-url>
cd <your-repo-directory>
