# Image Finder

The app uses GPT-4o to generate detailed text descriptions of images, then converts those descriptions into high-dimensional vector embeddings. It stores those embeddings in a Qdrant vector database. Users can later search by typing a description, and the app finds the most semantically similar images using vector search.

# 💡 Key Features:
## Multi-modal AI: 
- Understands images and translates them to descriptive text using GPT-4o.

## Semantic Search: 
- Finds similar images based on meaning, not keywords.

## Embeddings: 
- Uses OpenAI’s text-embedding-3-large to convert text into searchable vectors.

## Vector Database: 
- Stores and retrieves embeddings efficiently using Qdrant.

## Interactive UI: 
- Streamlit app with image upload and search functionality.

## 🧠 AI Techniques Involved:
- Multimodal AI (GPT-4o) – image → text.

- Natural Language Processing (NLP) – for embedding and understanding descriptions.

- Vector Similarity Search – via cosine similarity in Qdrant.

Follow the link below, to see for yourself how the application works:
<br><a href="https://github.com/SebDziekonski/ds_ai_portfolio.git" target="_blank">Open in new tab</a>