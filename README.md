# Video to GIF Transcription and Tagging Tool

![Project Banner](https://your-image-url.com/banner.png) <!-- Replace with your image URL -->

## 📖 Overview

The **Video to GIF Transcription and Tagging Tool** allows users to convert video files into GIFs, transcribe audio, and generate relevant tags and captions. This versatile platform supports multiple video input sources and integrates functionalities for captioning, watermarking, and GIF uploading. The tool also utilizes advanced APIs for transcription and tagging, and incorporates payment and authentication features.

## 🚀 Features

- **Video Processing**: Upload, compress, resize, and trim videos.
- **GIF Generation**: Create GIFs or stickers with customizable text, watermarks, and animations.
- **Transcription**: Transcribe audio from videos using Anthropic's Claude model.
- **Tagging**: Automatically generate tags and captions.
- **Upload to GIPHY**: Option to upload generated GIFs to GIPHY.
- **Multiple Input Sources**: Support for video files, YouTube links, and Google Photos.
- **Subscription Management**: Integrate with Stripe for subscription handling.
- **User Authentication**: Authenticate users with Google OAuth.

## 🛠 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/videotogif-public.git
   cd videotogif
2. **File Structure**:
   ```bash
   /videotogif/
   ├── backend/
   │   ├── app.py               # FastAPI backend entry
   │   ├── models.py            # Database models
   │   ├── auth.py              # Authentication and authorization logic
   │   ├── tenor_api.py         # Tenor API automation logic
   │   ├── giphy_api.py         # GIPHY API logic
   │   └── db.py                # Database connection
   ├── frontend/
   │   ├── streamlit_app.py      # Frontend file for Streamlit app
   │   ├── main.py               # Core functionality (Video to GIF)
   │   └── styles.css            # UI/UX styling for frontend
   ├── .env                      # Environment variables
   ├── requirements.txt          # Python dependencies
   └── README.md                 # Project Documentation
Create and Activate a Virtual Environment:

  bash
  ```
    Copy code
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    Install Required Python Packages:
  ```
  bash
  ```
    Copy code
    pip install -r requirements.txt
    Set Up Environment Variables:
  ```
Create a .env file in the root directory and add the following:

  env
  ```
    Copy code
    ANTHROPIC_API_KEY=your_anthropic_api_key
    OPENAI_API_KEY=your_openai_api_key
    ALBUM_ID=your_google_photos_album_id
    Set Google Photos API credentials in secret/credentials.json.
  ```
###⚙️ Usage
Start the Application:

  bash
  ```
  Copy code
  streamlit run frontend/main.py
  ```
Select Input Source:

Upload Video File: Choose a video file from your local machine.
YouTube Link: Provide a YouTube video URL.
YouTube Channel: Enter a channel link and specify the number of videos to download.
Google Photos: Authenticate with Google and select an album.
Customize Your GIF:

Set text options like font, size, color, shadow, and outline.
Add a watermark if desired.
Optionally upload GIFs to GIPHY.
Generate and Download:

Create GIFs based on your selections.
Download the GIFs as a ZIP file.
### 🔧 Development Tasks
Understand Code Flow: Review and understand the existing code base.
Redesign Backend: Refactor the backend code using FastAPI for smoother integration.
Automate Tenor API: Implement automated GIF uploads to Tenor.
Fix Edit Caption: Resolve issues with the Edit Caption functionality.
Database Development: Create a database for user authentication, subscription management, and credit storage.
Stripe Integration: Integrate Stripe for subscription handling and secure data connections.
### 📝 Contributing
We welcome contributions to enhance the tool. To contribute:

### Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -am 'Add new feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
📄 License
This project is licensed under the MIT License. See the LICENSE file for details.

### 🌟 Acknowledgements
Streamlit - For building the app interface.
Anthropic's Claude - For advanced transcription.
GIPHY - For GIF hosting.
Stripe - For payment processing.
Google Photos API - For accessing user albums.
LottieFiles - For animations.

### Key Elements:

1. **Project Banner**: Add a project banner image at the top for a professional touch.
2. **Features**: Highlight the main features of your tool.
3. **Installation and Usage**: Provide clear instructions for getting started with the project.
4. **Development Tasks**: Outline specific tasks and goals for contributors.
5. **Contributing**: Encourage community involvement and provide a guide for contributing.
6. **License**: Include licensing information.
7. **Acknowledgements**: Credit any tools or libraries used.

Replace placeholders such as image URLs and email addresses with actual values relevant to your project.

https://github.com/user-attachments/assets/8e02b377-336b-4714-8aec-331be00b4cd7
















   




