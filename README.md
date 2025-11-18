# 📊 YouTube Engagement Dashboard

This project is part of my **3-month Data Analytics Internship** at **Codec Technologies**, where I built an end-to-end workflow to analyze **YouTube video engagement** using API data and developed a **Power BI dashboard** to visualize insights.

---

## 🚀 **Project Overview**

The goal of this project is to understand the performance of YouTube content by analyzing key engagement metrics.
Using Python and YouTube Data API, I extracted channel video data, cleaned it, identified top-performing Shorts, and constructed a dashboard to identify patterns in viewer engagement.

---

## 🛠️ **Tech Stack Used**

* **Python** (API extraction, cleaning, preprocessing)
* **YouTube Data API v3**
* **Pandas** for dataset creation
* **Power BI** for dashboard design
* **Git & GitHub** for version control

---

## 📥 **Data Collection Workflow**

1. Connected to YouTube Data API using a developer key
2. Extracted all uploaded video IDs for the channel
3. Filtered **YouTube Shorts** (≤60 sec or containing “#shorts”)
4. Collected metrics such as:

   * Title
   * Views
   * Likes
   * Comments
   * Duration
   * Published date
5. Cleaned the titles (removed hashtags, emojis, extra text)
6. Exported the final dataset to CSV
7. Pushed data + script to GitHub repository

Final exported file:

```
youtube_top6_clean.csv
```

---

## 📈 **Dashboard Insights**

The **Power BI dashboard** visualizes:

* **Top 6 Shorts by engagement**
* **Total views and likes**
* **Video-level comparison**
* **Cleaned titles for better readability**
* **Interactive filters for deeper analysis**

This helped identify:

* Which type of content performs best
* Viewer interest trends
* Engagement effectiveness of short videos

---

## 📂 **Repository Structure**

```
youtube-engagement-dashboard/
│
├── youtube-dashboard.py            # Python script for API & data cleaning
├── youtube_top6_clean.csv          # Final processed dataset
├── Youtube engagment dashboard.pbix         # Power BI dashboard file
└── README.md                       # Documentation
```

---

## 📌 **How to Run the Script**

1. Install required packages:

```bash
pip install google-api-python-client pandas matplotlib python-dotenv gitpython isodate
```

2. Add your YouTube API key inside the script:

```python
API_KEY = "YOUR_API_KEY"
```

3. Run:

```bash
python youtube-dashboard.py
```

This will generate the clean CSV automatically.

---

## 🌐 **Power BI Dashboard**

The dashboard was built and designed in Power BI Desktop.
It includes:

* Card KPIs
* Bar charts
* Cleaned titles
* Engagement metrics

You can import the CSV into Power BI to recreate the dashboard.

---

## 📎 **Project Purpose**

This project demonstrates:

* API integration
* Data cleaning & preprocessing
* Dashboard-building skills
* End-to-end analytics workflow
* Real-world social media analytics

---

## 📧 **Contact**

**Keerthi M**
🔗 GitHub: [https://github.com/keerthi15M]
📩 Email: [keerthi1052031@gmail.com]

---

If you want, I can also generate:
✅ A project banner for GitHub
✅ A shorter version of the README
✅ A more aesthetic version with emojis and icons
