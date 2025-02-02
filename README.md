# FAQ Management System with Multi-Language Support

A Django-based FAQ management system with multi-language translation support. The system allows administrators to manage FAQs in English, and users can view FAQs in their preferred language through a REST API.

## Features:
- Store FAQs in English with the ability to display in different languages (Hindi, Gujarati, etc.).
- Use of `django-ckeditor` for WYSIWYG editor to format FAQ answers.
- Integration with **Google Translate API** to translate FAQs into multiple languages.
- Use of **Redis** for caching translated FAQs to improve performance.
- Admin interface to manage FAQs, only accessible to superusers.
- REST API to manage and fetch FAQs with language support.

## Table of Contents:
1. [Installation](#installation)
2. [API Usage](#api-usage)
3. [Contribution](#contribution)
4. [License](#license)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/niyatiipansuriya/faq-management-system.git
cd faq-management-system
