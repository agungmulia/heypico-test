# 🗺️ Local LLM + Google Maps API Integration

This project runs a local LLM via [Ollama](https://ollama.com) and [Open WebUI](https://github.com/open-webui/open-webui), and integrates it with a Node.js backend that connects to the Google Maps API. Users can ask natural questions like "search sushi places in 40.7128,-74.0060?" and get real map data + directions embedded from Google Maps.

---

## 🧰 Requirements

- Docker
- Node.js (v20+ recommended)
- Google Cloud Platform Account (to generate Maps API key)
- Ollama
- Ngrok or local dev tunnel
---
## 🔌 Backend API
[http://localhost:5000/api/v0/maps/places?query={{place}}&location={{long,lat}}](http://localhost:5000/api/v0/maps/places?query={{place}}&location={{long,lat}})
---
---
## ⚙️ Installation Steps

### 1. 🔧 Clone the Repository

```bash
git clone https://github.com/agungmulia/heypico-test
```
---
### 2. 🔐 Setup Environment Variables

Create a `.env` file in your backend folder:

```bash
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
PORT=5000
```

Replace `your_google_maps_api_key` with your actual API key. Make sure the key has the following enabled:
- Maps JavaScript API
- Places API
- Directions API
---
### 3. 🚀 Run Ollama + Open WebUI

> Make sure **port 11434** (Ollama) and **3000** (WebUI) are available.

Install Ollama locally:
```bash
# macOS / Linux
curl -fsSL https://ollama.com/install.sh | sh

# Windows (use installer from ollama.com)
```
Start Ollama server:
```bash
ollama serve
```

Pull a model (e.g., `llama3`, `mistral`, etc.) (for this project I use mistral):
```bash
ollama run mistral
```
Start Open WebUI (Docker):

```bash
docker compose up -d
```
or you can directly hit this docker command from the [official Open WebUI documentation](https://github.com/open-webui/open-webui)
```bash
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```
> Open WebUI will be available at: [http://localhost:3000](http://localhost:3000)

![image](https://github.com/user-attachments/assets/6def558b-08f7-4aeb-bee5-3c84846f9bcd)
> Make sure that the Open WebUI already finished setup so you can access [http://localhost:3000](http://localhost:3000)
---
### 4. 🔌 Start the Backend Server

Install dependencies:

```bash
#on the main project terminal
npm install
```

Start server:

```bash
npm start
# or
node server.js
# or if you have nodemon
nodemon server.js
```

> The backend runs at: [http://localhost:5000](http://localhost:5000)

---
### 5. 🔌 Connect the Open WebUI to the backend server
1. Login to Open WebUI
![image](https://github.com/user-attachments/assets/b5dd6f3d-47d3-4ccb-a721-709aebf6a908)
2. Open Workplace and import or create new tools
![image](https://github.com/user-attachments/assets/09258d0d-9bc3-4c45-b49c-569f8fece188)
    1. You can import new tools ussing the tools-export-1748790726877.json
    2. Or you can create new tools and paste the tools content from tools.py
    4. Tunnel your backend server with tools like Ngrok or local dev tunnel
      ![image](https://github.com/user-attachments/assets/f899e1b7-b5e0-4ae1-9658-adff27f082c3)
      >or you can use Ngrok with "ngrok http 5000"
    3. Go on the tools and edit the localhost tunnel link
      ```python
      class Valves(BaseModel):
          CITATION: bool = Field(default="True", description="True or false for citation")
          searchAPI: str = Field(
              default="{{your localhost tunnel link}}/api/v0/maps/places"
          )
      ```
    4. Save the changes
     
3. Make sure the created tools has been set to active
![image](https://github.com/user-attachments/assets/6e2e3f4b-d0df-41b0-911b-1237ea111dd5)
4. You can prompt things like "search sushi in 40.7128,-74.0060" or "search sushi in New York"
![image](https://github.com/user-attachments/assets/7372fbfc-d337-4121-9601-c79f0ea6310d)
![image](https://github.com/user-attachments/assets/c3ce6014-f3c3-4814-92ba-73c21e9f88f6)

5. Notice that on the backend server you can see that there is an API being hit
![image](https://github.com/user-attachments/assets/eee69cd5-ef44-4ed0-a5d7-11223412ea7e)
6. On the Open WebUI you can see the details of the tools in response that all the result are being outputed
![image](https://github.com/user-attachments/assets/b2a2ee24-ebdd-4bc0-84d2-4779f1b88b40)
7. you can use postman to hit and test the created API
![image](https://github.com/user-attachments/assets/fa2bfcea-d641-4d13-aaa4-4b9d251b9549)





