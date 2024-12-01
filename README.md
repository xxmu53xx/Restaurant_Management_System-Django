# DilaoRant RMS

<p align="center">
  <img src="https://drive.google.com/uc?id=1kBUkkwKfo-tLAptpC7a2n0HMTux_iLhQ" alt="Restaurant Management System Logo" />
</p>

<p align="center">
  <strong>DilaoRant is a Restaurant Management System designed to optimize daily restaurant operations by providing a comprehensive platform that supports user authentication, order management, inventory tracking, employee scheduling, and data security to enhance efficiency and customer satisfaction.</strong>
</p>

---

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Functional Requirements](#functional-requirements)
- [Gantt Chart](#gantt-chart)
- [Entity Relations Diagram (ERD)](#entity-relations-diagram-erd)
- [UI/UX Design](#uiux-design)
- [Contributors](#contributors)

---

## Introduction

<p align="center">
  <img src="https://drive.google.com/uc?id=1XNGwxy362Ff7IBXTHgoQwlDAwv9fDk0D" alt="System Overview" width="800" />
</p>

DilaoRant is a comprehensive web application designed to optimize restaurant operations for owners, managers, staff, and customers. It facilitates tasks such as order management, inventory tracking, employee scheduling, and payment processing, while ensuring secure user authentication and robust data protection. This project aims to create an efficient and reliable system that streamlines daily workflows, enhances user experience, and supports the overall growth and success of restaurants.

---

## Features

- **User Authentication and Access Control**
  - Secure login to ensure only authorized users can access specific areas.
  - Role-based access for admins and other user types.

- **Order Management**
  - Create, update, and track customer orders efficiently.
  - Generate kitchen tickets and order confirmations.

- **Inventory Management**
  - Track inventory levels and manage supplier details.
  - Generate alerts for low stock to prevent shortages.

- **Employee Scheduling**
  - Create and manage employee work schedules.
  - Track attendance and handle shift changes.

- **Menu Management**
  - Update and manage the restaurant menu, including prices and item availability.

- **Payment Processing**
  - Handle customer payments and integrate with third-party payment processors.
  - Generate payment confirmations and receipts.

- **Reporting**
  - Generate detailed reports for sales, inventory, and employee performance.

- **Notifications and Alerts**
  - Send notifications and alerts for order status updates and low inventory levels.

- **Advanced Search Functionality**
  - Locate specific orders, customers, or inventory items using advanced search options.

- **Password Management**
  - Password recovery and change mechanisms for enhanced security.

- **Security and Data Privacy**
  - Ensure compliance with relevant regulations and standards.
  - Implement encryption and robust access controls.

---

## Getting Started

Follow these steps to set up the project locally and start using it efficiently.

### Prerequisites

Below are the required tools and steps to install them for running the software.

1. **Install Python**
   - Install Python 3.12.5. Follow the steps from the [Python installation guide](https://docs.python-guide.org/starting/installation/) based on your operating system.

2. **Clone the Repository**
   ```bash
   git clone https://github.com/xxmu53xx/Restaurant_Management_System-Django.git
   ```

3. **Navigate to the Project Directory**
   ```bash
   cd restaurant_systme
   ```

4. **Set Up a Virtual Environment**
   ```bash
   # Create a virtual environment
   python -m venv venv

   # Activate the virtual environment
   venv/scripts/Activate # For macOS/Linux: source venv/bin/activate
   ```

5. **Install Dependencies**
   ```bash
   pip install openpyxl
   pip install pillow
   pip install -r requirements.txt
   ```

6. **Migrate the Database**
   ```bash
   py manage.py makemigrations
   py manage.py migrate
   ```

7. **Run the Server**
   ```bash
   py manage.py runserver
   ```

---

## Functional Requirements

[![Functional Requirements](https://img.shields.io/badge/Functional_Requirements-Document-green?style=for-the-badge)](https://cebuinstituteoftechnology-my.sharepoint.com/:w:/r/personal/drewadrein_odilao_cit_edu/_layouts/15/Doc.aspx?sourcedoc=%7BFB0D4748-24E2-4B84-B32B-41B53BE31011%7D&file=Restaurant_Management_System_Proposal.docx&action=default&mobileredirect=true)

---

## Gantt Chart

[![Gantt Chart](https://img.shields.io/badge/Gantt_Chart-Spreadsheet-orange?style=for-the-badge)](https://docs.google.com/spreadsheets/d/1nHaQQXiKmNXLnb4BZy2EdwC_1RaD1d1SZMbM3q2Jwzk/edit?gid=0#gid=0)

---

## Entity Relations Diagram (ERD)

[![ERD](https://img.shields.io/badge/ERD-Diagram-blue?style=for-the-badge)](https://online.visual-paradigm.com/share.jsp?id=333535313136332d31#diagram:workspace=uxzenwmp&proj=0&id=1)

---

## UI/UX Design

[![UI/UX](https://img.shields.io/badge/UI%2FUX-Design-purple?style=for-the-badge)](https://www.figma.com/design/jYx2dtJbb7f372bDBXB0Wg/UX%2FUI-Restauran-Management-System?node-id=0-1&node-type=canvas&t=FDfme61mIlGel94P-0)

---

## Contributors

| Profile                                                                 | GitHub                                                                                          |
|------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| <img src="https://drive.google.com/uc?export=view&id=1x2xYEhb5lUx6j9qeXOObERKHCKSWKGCH" width="100px;" alt="Mykel Seth C. Gella"/> | [![Mykel Seth C. Gella](https://img.shields.io/badge/Mykel%20C.%20Gella-GitHub-blue?style=for-the-badge)](https://github.com/MykelSeth) |
| <img src="https://drive.google.com/uc?export=view&id=1fVmyplB5lj4ElQ8A50HU0D2Nd7lQWXp6" width="100px;" alt="Drew Adrien C. Odilao"/> | [![Drew Adrien C. Odilao](https://img.shields.io/badge/Drew%20Adrien%20C.%20Odilao-GitHub-green?style=for-the-badge)](https://github.com/DrewingBook) |
| <img src="https://drive.google.com/uc?export=view&id=13l3nOZzVj83df6m5A9_MeR6W0FJvRmAJ" width="100px;" alt="John Wayne M. Largo"/> | [![John Wayne M. Largo](https://img.shields.io/badge/John%20Wayne%20M.%20Largo-GitHub-red?style=for-the-badge)](https://github.com/xxmu53xx) |
