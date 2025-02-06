Mental Health Predictor:
A Machine Learning & LLM-Based System for Mental Health Condition Detection and Explanation


📌 Project Overview:

Mental health is a crucial aspect of well-being, yet early detection and awareness remain challenging. This project presents an AI-driven mental health condition predictor that:
- Classifies user input into categories such as Depression, Anxiety, Stress, Bipolar, Personality Disorder, Suicidal, or Normal.
- Generates natural language explanations for the detected condition using a fine-tuned Mistral model.
- Provides coping mechanisms and potential next steps based on the predicted mental health condition.
- Features a Streamlit-based UI for seamless user interaction.


🚀 Key Features:

- Text-Based Classification: Predicts mental health conditions from user input.
- LLM-Generated Explanations: Uses a fine-tuned Mistral model for natural language explanations.
- Coping Mechanisms & Suggestions: Provides recommendations to manage symptoms.
- User-Friendly Interface: Interactive Streamlit UI for easy testing.
- Open-Source & Expandable: Built using free, open-source LLMs and models for transparency and scalability.


🔧 Tech Stack & Tools:

- Natural Language Processing (NLP): Fine-tuned Mistral (via Ollama) & transformer models (T5)
- Machine Learning Frameworks: PyTorch, Hugging Face Transformers
- UI Implementation: Streamlit
- Model Training & Experimentation: Google Colab
- Version Control & Deployment: GitHub


📖 How to Use:

1️⃣ Clone the Repository

git clone https://github.com/ArshdeepKaur04/Mental-Health-Predictor.git

cd mental-health-predictor

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run ui/app.py

Enter text describing your symptoms, and the model will predict the condition, generate an explanation, and suggest coping mechanisms.


🏆 Results & Findings:

The model has been fine-tuned using labeled mental health datasets, and results show high accuracy in detecting conditions. The fine-tuned Mistral model effectively generates contextual explanations and relevant coping strategies.


🛠 Future Improvements:

- Enhance dataset with more diverse and real-world inputs.
- Optimize response personalization using retrieval-augmented generation (RAG).
- Expand UI to include interactive visualization of mental health trends.
- Integrate with mental health APIs for additional resources.


🤝 Contributing:

Contributions are welcome! Feel free to fork the repository, raise issues, or submit pull requests.


📝 License:

This project is open-source under the MIT License.


🔗 Large Files (Model, Video & Project Documentation):

Download trained models and the demo video here: https://drive.google.com/drive/folders/1Qv1-XGQkH_Nyibz2v_A3fVqL7ZDRbnN6?usp=sharing
