# Web Admin Panel for Telegram Bot

A lightweight web-based admin panel for managing a Telegram bot: sending messages to individual users, broadcasting to all users, and viewing basic statistics.

---

## Overview

This project provides a simple interface for interacting with a Telegram bot via a REST API. It is designed for internal use, automation, and quick message distribution without requiring direct interaction with the bot code.

Core capabilities:

- Send messages to a specific user via `chat_id`
- Broadcast messages to all registered users
- View total number of users
- Store and reuse bot token in browser local storage

---

## Tech Stack

**Backend**
- Python
- FastAPI
- aiogram

**Frontend**
- HTML
- CSS
- JavaScript (Vanilla)

**Infrastructure**
- REST API
- CORS middleware
- LocalStorage