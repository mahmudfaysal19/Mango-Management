<div align="center">

# 🥭 Mango Management — Harvest & Inventory Tracking

**A lightweight, seasonal inventory and distribution tracking platform built to streamline orchard intake, cultivar cataloging, and sales records.**

[![Python](https://img.shields.io/badge/Backend-Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![HTML5](https://img.shields.io/badge/Frontend-HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/Styling-CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)

</div>

---

## 📌 Overview

**Mango Management** is an agricultural management system built to digitize and organize post-harvest workflows for mango orchards, suppliers, and distributors. Designed to replace paper ledgers, it provides clean HTML interfaces backed by Python logic to catalog incoming fruit batches, monitor active crate stock, and log outgoing customer sales.

---

## ⚡ Key Capabilities & Features

### 1. Cultivar Intake & Batch Cataloging
* Organize harvests by distinct regional varieties (e.g., Himsagar, Langra, Amrapali, Fazli, Gopalbhog).
* Record intake metadata including harvest dates, crate counts, gross weight, and source orchard blocks.

---

### 2. Live Inventory & Storage Tracking
* Real-time visibility into available crate reserves and warehouse stock levels.
* Track lot lifecycles from fresh harvest intake to distribution readiness to minimize post-harvest loss.

---

### 3. Sales Logging & Transaction Processing
* Record customer orders and wholesale distribution shipments with automated price and weight calculations.
* Maintain chronological sales histories and revenue totals across seasonal harvest cycles.

---

### 4. Responsive Template-Driven UI
* Clean, lightweight HTML5 views styled for rapid data entry in orchard and warehouse environments.
* Minimal dependency footprint ensuring fast load times and straightforward local deployment.

---

## 🛠️ Tech Stack & System Architecture

```plaintext
┌────────────────────────────────────────────────────────┐
│                   HTML5 / CSS3 Views                   │
│         (Inventory Tables · Forms · Dashboards)        │
└───────────────────────────┬────────────────────────────┘
                            │ HTTP Requests / Form Data
┌───────────────────────────▼────────────────────────────┐
│                  Python Application Core               │
│      ├── Request Routing & View Rendering              │
│      ├── Cultivar & Inventory Calculation Logic        │
│      └── File / Data Persistence Handlers              │
└────────────────────────────────────────────────────────┘
```

| Layer | Technologies |
| :--- | :--- |
| **Backend & Logic** | Python |
| **Frontend & Templates** | HTML5, CSS3 |
| **Storage & Data** | File-based / Structured Data Storage |
| **Environment & Tooling** | Virtualenv, Pip, Git |

---

## 📂 Repository Structure

```plaintext
Mango-Management/
├── client/                 # Frontend UI components, views, and state management
│   ├── public/             # Static assets and icons
│   └── src/
│       ├── components/     # Reusable UI widgets, modals, and navbars
│       ├── pages/          # Main dashboard, inventory, orders, and sales views
│       └── services/       # Client-side API request handlers
├── server/                 # Backend RESTful API service
│   ├── controllers/        # Request handling and business logic
│   ├── models/             # Database schemas and entity definitions
│   ├── routes/             # Express API route endpoints
│   ├── middlewares/        # Authentication, authorization, and validation
│   └── config/             # Database and environment configurations
├── .gitignore
├── package.json
└── README.md
```
---

## 🚀 Quickstart & Local Setup

### 1. Clone the repository
```bash
git clone [https://github.com/mahmudfaysal19/Mango-Management.git](https://github.com/mahmudfaysal19/Mango-Management.git)
cd Mango-Management
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch the application
```bash
python app.py
```

Open your browser and navigate to `http://localhost:5000` (or the local address printed in your terminal).

---
