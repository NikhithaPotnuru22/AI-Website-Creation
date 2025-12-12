# **AI Website Generator**

This project uses **Generative AI** to create a fully functional, responsive website from a simple user prompt. Powered by **LangChain** and **Google’s Generative AI**, the system automatically generates clean **HTML**, **CSS**, and **JavaScript** code that can be downloaded and deployed instantly.

---

## **Features**

* **AI-Generated Website Code**
  Automatically produces HTML, CSS, and JavaScript based on the user’s description.

* **User-Friendly Interface**
  Built with **Streamlit**, making it accessible and easy to use for all skill levels.

* **Downloadable ZIP File**
  Instantly download the complete website package (index.html, style.css, script.js).

* **Customizable Output**
  Users can further edit and tailor the generated website to match their personal style or branding.

---

## **How It Works**

1. Enter a prompt describing the website or portfolio you want.
2. The AI processes your input and generates the full website code.
3. The code is saved and packaged into a downloadable ZIP file.
4. Download the ZIP and deploy your new website anywhere you like.

---

## **Technologies Used**

* **Streamlit** – Front-end web interface
* **LangChain** – AI orchestration and model pipeline
* **Google Generative AI** – Natural language understanding and code generation
* **zipfile** – Bundles generated files into a ZIP archive

---

## **Getting Started**

### **Prerequisites**

* Python **3.7+**

### **Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Set Up API Keys**

Add your Google API key to a `.env` file:

```
GOOGLE_API_KEY=your_key_here
```

---

## **Running the App**

### **Clone the repository**

```bash
git clone https://github.com/your-username/ai-website-generator.git
cd ai-website-generator
```

### **Run the Streamlit App**

```bash
streamlit run main.py
```


