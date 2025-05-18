## 🎙️ AI-Powered Audio Note-Taking with Search
This is a Streamlit-based voice note-taking app that lets users record, transcribe, save, and search audio notes using OpenAI's Whisper and Embeddings API, with Qdrant vector database for smart semantic retrieval. It's designed to be lightweight, private (runs in memory), and interactive.

## 🚀 What the App Does
- Record & Transcribe Notes<br>
Users record voice notes directly in the browser. Notes are transcribed using OpenAI Whisper

- Save Notes to Vector Database<br>
Transcriptions are converted to vector embeddings. Stored in an in-memory Qdrant vector database for retrieval

- Search Notes Semantically<br>
Users can type a search query. The app finds related notes by meaning using vector similarity

## ⚙️ How It Works (Flow Overview)
 - 🔐 API Setup<br>
User supplies an OpenAI API key (via .env or manual input). Key is stored in st.session_state for secure use

- 🎤 Audio Input<br>
Audio is recorded via audiorecorder component and stored as .mp3 in memory

- 📝 Transcription<br>
Audio bytes are sent to OpenAI Whisper (whisper-1).
Returned text is shown and editable before saving

- 💾 Note Storage<br>
Each note is embedded into a 3072-dimensional vector using text-embedding-3-large. Stored in Qdrant using cosine similarity for fast semantic search

- 🔍 Note Search
Query is embedded, then matched against stored notes. Results are shown along with similarity scores (if searching)

Follow the link below to view the source code and see how the application works — you can run it yourself: 
<br><a href="https://github.com/SebDziekonski/ds_ai_portfolio.git" target="_blank">Open in new tab</a>