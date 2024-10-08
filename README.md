# ChatBot_For_Document

## Overview

This project leverages LangChain to build a question-answering system using a dataset containing information about notable personalities, specifically designed to answer queries related to their personal lives. The system utilizes Hugging Face's Transformers and FAISS for efficient document storage and retrieval.

### ⚙️ Features

- **Document Loading:** Efficiently load documents from a text file.
- **Text Splitting:** Break down large documents into manageable chunks for processing.
- **Similarity Search:** Quickly retrieve relevant documents based on user queries.
- **Question Answering:** Generate accurate responses using state-of-the-art language models.

## 📦 Installation

To set up this project, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/RaST-EDITH/ChatBot_For_Document.git
   cd ChatBot_For_Document
   ```

2. **Set Up a Virtual Environment:**
   Create and activate a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages:**
   Install the necessary libraries using pip.
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**
   Create a `.env` file in the root directory and add your Hugging Face API token:
   ```
   HUGGINGFACEHUB_API_TOKEN=your_token_here
   ```

5. **Dataset Preparation:**
   Place your dataset file (`data.txt`) in the `Dataset` directory.

## 🚀 Running the Project

To run the project, use the following command:
```bash
python main.py
```


## 📚 Code Explanation

1. **Loading the Dataset:**
   The `TextLoader` is used to load the dataset from a specified text file.

2. **Text Splitting:**
   The `CharacterTextSplitter` splits the loaded documents into smaller chunks, making it easier for the model to process.

3. **Creating the Embedding Database:**
   Using FAISS, the project creates an embedding database for efficient similarity searches.

4. **Setting Up the Language Model:**
   A Hugging Face model (Flan-T5-XXL) is initialized to handle the question-answering tasks.

5. **Query Execution:**
   Users can input their queries, and the system will return relevant answers based on the dataset.

## 🎉 Contributing

Contributions are welcome! If you have suggestions for improvements or features, feel free to open an issue or submit a pull request.
