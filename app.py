"""
Muhammad Haseeb - Portfolio Website
"""
import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_from_directory
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'portfolio-secret-2025')

PROFILE = {
    "name": "Muhammad Haseeb",
    "title": "Network Engineer",
    "subtitle": "Network Engineer | IT Specialist | Developer",
    "email": "haseebarif112234@gmail.com",
    "location": "Lahore, Pakistan",
    "github": "https://github.com/haseeb-linux",
    "linkedin": "https://linkedin.com/in/muhammad-haseeb-451264432",
    "university": "Virtual University of Pakistan",
    "bio": "Network Engineer and IT specialist with hands-on experience in network infrastructure, system administration, and building production-grade web applications.",
}

PROJECTS = [
    {
        "id": "mitcon-lms",
        "title": "Mitcon Grammar School LMS",
        "category": "Client Project",
        "description": "Multi-Campus Learning Management System for K-10 institution with 3,500+ students across 7 campuses. Delivered to real client.",
        "long_description": "A production-grade LMS built with Flask Blueprints for Mitcon Grammar School. Delivered as a complete client solution with 5-role RBAC system, multi-tenancy, diary management, attendance tracking, and fee management.",
        "tech": ["Python", "Flask", "SQLAlchemy", "SQLite", "Bootstrap 5"],
        "features": [
            "5-Role Access Control (Super Admin, Principal, Teacher, Student, Parent)",
            "Multi-Campus Architecture (7 campuses)",
            "3,500+ Students, 175+ Teachers, 630+ Subjects",
            "Daily Diary System with chapter-wise notes",
            "Attendance Tracking & Fee Management",
            "Public Announcements (no login required)",
            "Delivered to real client - Mitcon Grammar School",
        ],
        "github": "https://github.com/haseeb-linux/mitcon-grammar-school-lms",
        "status": "Delivered",
        "year": "2025",
    },
    {
        "id": "stockpulse",
        "title": "StockPulse - Stock Tracker",
        "category": "FinTech",
        "description": "PSX-inspired stock tracking & virtual trading platform with 100K PKR starting balance.",
        "long_description": "A real-time stock tracker for Pakistan Stock Exchange + global markets. Features virtual trading, portfolio tracking, and multi-stock comparison.",
        "tech": ["Python", "Flask", "SQLAlchemy", "yfinance", "Chart.js"],
        "features": [
            "113+ PSX-listed companies across 22 sectors",
            "Virtual trading with PKR 100,000 starting balance",
            "5-year interactive charts with moving averages",
            "Portfolio P&L tracking",
            "CSV export & JSON API",
            "Light/Dark mode",
        ],
        "github": "https://github.com/haseeb-linux/stockpulse",
        "status": "Completed",
        "year": "2025",
    },
    {
        "id": "maildeck",
        "title": "MailDeck - Email Sender",
        "category": "Automation",
        "description": "Full-stack automated email sender with templates, attachments, and scheduling.",
        "long_description": "A bulk email automation tool using Gmail SMTP with template management, file attachments, scheduled sending, and open-rate tracking.",
        "tech": ["Python", "Flask", "SQLAlchemy", "APScheduler", "Gmail SMTP"],
        "features": [
            "Bulk email sending with CSV import",
            "HTML email templates",
            "File attachments (PDF, DOCX, Images)",
            "Email scheduling with APScheduler",
            "Open-rate tracking pixel",
            "History with CSV/PDF export",
        ],
        "github": "https://github.com/haseeb-linux/Maildeck",
        "status": "Completed",
        "year": "2025",
    },
]

EXPERIENCE = [
    {
        "role": "Computer Science Teacher (9th & 10th Grade)",
        "company": "Mitcon Grammar School",
        "duration": "2024 - Present",
        "description": "Teaching Computer Science to 9th and 10th grade students. Developing curriculum and practical lab sessions.",
        "achievements": [
            "Teaching CS to 9th & 10th grade students",
            "Conducting practical lab sessions",
            "Developed complete CS curriculum",
        ],
    },
    {
        "role": "Freelance Developer",
        "company": "Self-Employed",
        "duration": "2024 - Present",
        "description": "Building production-grade web applications for clients using Python, Flask, and modern web technologies.",
        "achievements": [
            "Delivered Mitcon Grammar School LMS (client project)",
            "Built 3+ production-level applications",
            "Mastered Flask Blueprint architecture",
        ],
    },
]

EDUCATION = [
    {
        "degree": "BS Information Technology",
        "institution": "Virtual University of Pakistan",
        "duration": "2023 - Present",
        "description": "Pursuing Bachelor's in Information Technology with focus on Networking, Web Development, and System Administration.",
    },
]


@app.route("/")
def index():
    return render_template("index.html",
                           profile=PROFILE,
                           projects=PROJECTS,
                           experience=EXPERIENCE,
                           education=EDUCATION,
                           year=datetime.now().year)


@app.route("/projects")
def projects():
    return render_template("projects.html",
                           profile=PROFILE,
                           projects=PROJECTS,
                           year=datetime.now().year)


@app.route("/projects/<project_id>")
def project_detail(project_id):
    project = next((p for p in PROJECTS if p["id"] == project_id), None)
    if not project:
        return render_template("404.html", profile=PROFILE), 404
    return render_template("project_detail.html",
                           profile=PROFILE,
                           project=project,
                           year=datetime.now().year)


@app.route('/sitemap.xml')
def sitemap():
    return send_from_directory('static', 'sitemap.xml')


@app.route('/robots.txt')
def robots():
    return send_from_directory('static', 'robots.txt')


@app.route("/api/contact", methods=["POST"])
def contact_api():
    data = request.get_json()
    print(f"Message from {data.get('name')} ({data.get('email')}): {data.get('message')}")
    return jsonify({"success": True, "message": "Thank you! I'll get back to you soon."})


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", profile=PROFILE), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)