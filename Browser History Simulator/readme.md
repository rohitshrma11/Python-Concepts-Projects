# 🌐 Browser History Simulator using LRU Cache

A simple browser history simulator built using Python and the **LRU (Least Recently Used) Cache** concept.

This project stores recently visited pages, removes old pages automatically when the cache is full, and allows searching through browser history.

---

# 🚀 Features

- Store recently visited pages
- Automatically remove oldest pages
- Open previously visited pages
- Search browser history
- LRU Cache implementation
- Fast O(1) operations using OrderedDict

---

# 🛠️ Tech Stack

- Python
- OrderedDict
- OOP Concepts
- LRU Cache

---

# 📂 Project Structure

```bash
Browser-History-Simulator/
│
├── main.py
├── browser.py
├── LRU_cache.py
└── README.md
```

---

# ⚙️ How It Works

The project uses the **LRU Cache** mechanism:

- Recently opened pages move to the top
- Least recently used pages get removed automatically
- Cache size remains fixed

---

# 🧠 Concepts Used

## LRU Cache
Least Recently Used caching strategy.

## OrderedDict
Used to maintain insertion order and perform efficient cache operations.

## Time Complexity

| Operation | Complexity |
|----------|------------|
| get() | O(1) |
| put() | O(1) |
| delete oldest | O(1) |
| search | O(n) |

---

# ▶️ Run the Project

## Clone Repository

```bash
git clone https://github.com/your-username/browser-history-simulator.git
```

## Move into Folder

```bash
cd browser-history-simulator
```

## Run Project

```bash
python main.py
```

---

# 💻 Example Output

```bash
Visiting google.com

Visiting youtube.com

Visiting github.com

Print the recent history
github.com -> github
youtube.com -> youtube
google.com -> google

Visiting chatgpt.com
Removed Oldest page: google.com

Print the recent history
chatgpt.com -> ChatGPT
github.com -> github
youtube.com -> youtube
```

---

# 📌 Future Improvements

- GUI using Tkinter
- SQLite database support
- Back & Forward navigation
- Export history to CSV
- Incognito mode
- Most visited analytics

---

# 🎯 Learning Outcome

This project helps understand:

- LRU Cache
- HashMap concepts
- OrderedDict
- Cache optimization
- Real-world browser storage logic

---

# ⭐ Author

Developed by Rohit Sharma 🚀
