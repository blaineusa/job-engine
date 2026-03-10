import streamlit as st
import sqlite3

conn = sqlite3.connect("jobs.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    organization TEXT,
    location TEXT,
    score INTEGER,
    status TEXT
)
""")
conn.commit()

st.title("Blaine Hone Job Search Engine")

if st.button("Create Test Job"):
    cursor.execute(
        "INSERT INTO jobs(title, organization, location, score, status) VALUES (?, ?, ?, ?, ?)",
        ("Vice President, Global Engagement", "Example University", "Remote", 90, "new")
    )
    conn.commit()
    st.success("Test job created.")

st.subheader("Tracked Jobs")

jobs = cursor.execute("SELECT id, title, organization, location, score, status FROM jobs ORDER BY id DESC").fetchall()

if not jobs:
    st.info("No jobs yet. Click 'Create Test Job' to add one.")
else:
    for job in jobs:
        st.write(job)

