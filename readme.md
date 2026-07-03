#How to Use the RAG based AI Teaching Assistant

Follow the steps below to prepare the video database and start searching for relevant videos.

Step 1: Add Videos

Place all the videos you want to process into the video/ folder.

Step 2: Convert Videos to Audio

Run the Video to MP3 script to extract audio from each video.

Step 3: Convert Audio to Text

Run the Speech-to-Text script to generate transcripts from all MP3 files.

Step 4: Create Text Chunks

Split the generated transcripts into smaller chunks and save them as JSON files.

Step 5: Generate Embeddings

Run the embedding script to create vector embeddings for all text chunks and store them in the vector database.

Step 6: Search Videos Using RAG

Once all embeddings have been generated, run the query processing script. The system will:

Convert the user's query into an embedding.
Retrieve the most relevant transcript chunks from the vector database.
Send the retrieved context to the LLM.
Return the most relevant video(s) along with the matching timestamps.
Workflow
Videos
   │
   ▼
Video to MP3
   │
   ▼
Speech to Text
   │
   ▼
Transcript Chunks (JSON)
   │
   ▼
Generate Embeddings
   │
   ▼
Vector Database
   │
   ▼
User Query
   │
   ▼
Retrieve Relevant Chunks
   │
   ▼
LLM
   │
   ▼
Relevant Video + Timestamp