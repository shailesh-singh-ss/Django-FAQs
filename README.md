# **FAQ Management System**

This is a Django-based FAQ management system that supports multi-language translations, a WYSIWYG editor for answers, and a REST API for managing FAQs. The project uses Redis for caching and supports automated translations using the `googletrans` library.

---

## **Features**
- **WYSIWYG Editor**: Rich text editor for FAQ answers.
- **Multi-language Support**: Automatically translates FAQs into Hindi and Bengali, etc.
- **REST API**: Manage FAQs with language-specific responses.
- **Caching**: Uses Redis to cache translations for improved performance.
- **Admin Panel**: User-friendly interface for managing FAQs.

---

## **Table of Contents**
1. [Installation](#installation)
3. [Running the Project](#running-the-project)
2. [API Usage](#api-usage)
4. [Testing](#testing)
5. [Contribution Guidelines](#contribution-guidelines)
6. [License](#license)

---

## **Installation**

### **Prerequisites**
- Docker and Docker Compose installed on your machine.
- Python 3.12 (optional, if running locally without Docker).

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/shailesh-singh-ss/Django-FAQs.git
   cd Django-FAQs
   ```

2. Create a `.env` file in the project root and add the following environment variables:
   ```env
   # Django settings
   DEBUG=1
   SECRET_KEY=your-secret-key
   ALLOWED_HOSTS=*

   # Redis settings
   REDIS_URL=redis://redis:6379/0
   ```

3. Build and run the Docker containers:
   ```bash
   docker-compose up --build
   ```

4. Apply migrations:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

6. Access the application:
   - Django app: `http://localhost:8000`
   - Admin panel: `http://localhost:8000/admin`

---

## **Running the Project**

### **Using Docker**
1. Start the containers:
   ```bash
   docker-compose up
   ```

2. Stop the containers:
   ```bash
   docker-compose down
   ```

### **Running Locally**
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   python manage.py runserver
   ```

3. Access the application at `http://localhost:8000`.

---

## **API Usage**

### **Endpoints**
- **Get All FAQs**: `GET /api/faqs/`
- **Get FAQs in a Specific Language**: `GET /api/faqs/?lang=<language_code>`

### **Examples**
1. **Get All FAQs (Default: English)**:
   ```bash
   curl -X GET http://localhost:8000/api/faqs/
   ```
   **Response**:
   ```json
   [
       {
           "id": 1,
           "question": "What is Artificial Intelligence?",
           "answer": "Artificial Intelligence (AI) is the simulation of human intelligence in machines that are programmed to think and learn like humans.",
           "created_at": "2024-01-01T00:00:00Z"
       }
   ]
   ```

2. **Get FAQs in Hindi**:
   ```bash
   curl -X GET http://localhost:8000/api/faqs/?lang=hi
   ```
   **Response**:
   ```json
   [
       {
           "id": 1,
           "question": "कृत्रिम बुद्धिमत्ता क्या है?",
           "answer": "कृत्रिम बुद्धिमत्ता (AI) मशीनों में मानव बुद्धिमत्ता का अनुकरण है जो मनुष्यों की तरह सोचने और सीखने के लिए प्रोग्राम किए जाते हैं।",
           "created_at": "2024-01-01T00:00:00Z"
       }
   ]
   ```

3. **Get FAQs in Bengali**:
   ```bash
   curl -X GET http://localhost:8000/api/faqs/?lang=bn
   ```
   **Response**:
   ```json
   [
       {
           "id": 1,
           "question": "কৃত্রিম বুদ্ধিমত্তা কি?",
           "answer": "কৃত্রিম বুদ্ধিমত্তা (AI) হল মানুষের বুদ্ধিমত্তার অনুকরণ যা মানুষের মতো চিন্তা এবং শেখার জন্য প্রোগ্রাম করা মেশিনে।",
           "created_at": "2024-01-01T00:00:00Z"
       }
   ]
   ```


---

## **Testing**

### **Run Tests**
To run the tests, use the following command:
```bash
docker-compose exec web pytest
```

### **Test Coverage**
To generate a test coverage report:
```bash
docker-compose exec web pytest --cov=faqs_app
```

---

## **Contribution Guidelines**

### **How to Contribute**
1. Fork the repository.
2. Create a new branch for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your commit message here"
   ```
4. Push your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request and describe your changes.

### **Code Style**
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.
- Use descriptive commit messages.

### **Reporting Issues**
If you find a bug or have a feature request, open an issue on GitHub.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
