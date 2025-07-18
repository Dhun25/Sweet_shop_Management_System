# 🍬 Sweet Shop Inventory Management System

A simple web application to manage the inventory of a sweet shop using **Python (Flask)** and **HTML**. You can add, delete, purchase, restock, and search sweets with a user-friendly interface.

---

## 🚀 Features

- ➕ Add new sweets to inventory
- 🗑️ Delete sweets
- 🛒 Purchase sweets (reduces quantity)
- 📦 Restock sweets (increases quantity)
- 🔍 Search sweets by name, category, and price range
- 💾 Data is saved in `sweets.json`

---

## 🛠️ Project Structure
sweetshop/
├── App.py # Main Flask application

├── Sweet.py # Sweet model class

├── SweetShop.py # Handles business logic & data persistence

├── index.html # Frontend UI (in templates folder or public)

├── sweets.json # JSON file for data storage

├── testSweetShop.py # Basic unit tests

└── README.md # Project documentation


---

## ⚙️ How to Run the Project

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/Dhun25/Sweet-shop-Management-System.git
cd sweetshop
#### 2. Create a Virtual Environment
        python -m venv venv
▶️ 3. Activate the Environment:venv\Scripts\activate
4. Install Flask:pip install Flask
▶️ 5. Run the App:python App.py
Then, open your browser and go to:
http://127.0.0.1:5000
🧪 Run Tests
python testSweetShop.py
You should see:
✅ All tests passed!
Data Storage
The sweets data is stored in a file named sweets.json. It is automatically created/updated when you add, delete, purchase, or restock sweets.

📌 Future Enhancements
✅ Bootstrap UI for better styling

✅ SQLite/PostgreSQL backend

✅ User authentication (Admin Login)

✅ REST API for mobile clients

✅ Export inventory to Excel or PDF

🙋‍♂️ Author
Dhun Brijeshbhai Patel
Computer Engineering Student
