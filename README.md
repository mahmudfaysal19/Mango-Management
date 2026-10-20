<div align="center">

# 🥭 Mango Management System

**A centralized management and tracking platform for mango inventory, sales, and supply chain operations.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=flat-square)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)

</div>

---

## 📌 Overview

The **Mango Management System** is a dedicated software solution engineered to streamline the end-to-end operations of mango orchards, wholesale distributors, and retail businesses. From tracking distinct mango cultivars and seasonal harvest batches to managing stock turnover, supplier contracts, customer invoices, and real-time sales reporting, this platform automates manual record-keeping to minimize spoilage and maximize operational efficiency.

---

## ✨ Key Features

* **📦 Cultivar & Inventory Tracking:** Maintain detailed profiles for different mango varieties (e.g., Gopalbhog, Himsagar/Khirsapat, Langra, Amrapali, Fazli) categorized by grade, weight, and shelf-life.
* **🚚 Supply Chain & Orchard Sourcing:** Monitor batch intakes directly from growers/orchards, track transportation logistics, and register initial quality-inspection metrics.
* **⚡ Sales & Order Processing:** Generate point-of-sale (POS) receipts or bulk commercial invoices with automated tax, discount, and balance calculations.
* **📊 Real-time Stock Alerts:** Automated warnings for low inventory levels and threshold alerts for ripening batches requiring expedited dispatch.
* **👥 Role-Based Access Control (RBAC):** Secure access tiers for Administrators, Inventory Managers, and Sales Staff with audited operation logging.
* **📈 Reporting & Analytics:** Visual summaries of daily/seasonal revenue, top-performing varieties, stock loss rates, and supplier payout balances.

---

## 🛠️ Tech Stack

### Frontend & UI
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![TailwindCSS](https://img.shields.io/badge/Tailwind-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

### Backend & Database
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)
![Prisma](https://img.shields.io/badge/Prisma-2D3748?style=flat-square&logo=prisma&logoColor=white)

### Tools & Utilities
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white)

---

## 📂 Repository Structure

```plaintext
Mango-Management/
├── client/                 # Frontend UI components, views, and state management
│   ├── public/             # Static assets and icons
│   └── src/
│       ├── components/     # Reusable UI widgets, modals, and navbars
│       ├── pages/          # Main dashboard, inventory, orders, and sales views
│       └── services/       # Client-side API request handlers
├── server/                 # Backend RESTful API service
│   ├── controllers/        # Request handling and business logic
│   ├── models/             # Database schemas and entity definitions
│   ├── routes/             # Express API route endpoints
│   ├── middlewares/        # Authentication, authorization, and validation
│   └── config/             # Database and environment configurations
├── .gitignore
├── package.json
└── README.md
