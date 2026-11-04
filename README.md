# 🎓 University Management System

A comprehensive desktop application for managing university operations, built with Python and Tkinter using the MVC (Model-View-Controller) architectural pattern.

## 📋 Table of Contents
- [Features](#-features)
- [Architecture](#️-architecture)
- [Technologies Used](#️-technologies-used)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Modules](#-modules)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

### Core Functionalities
- 👥 **Student Management** - Complete registration and tracking of student records.
- 👨‍🏫 **Professor Management** - Manage professors, their salaries, and assigned teaching courses.
- 📚 **Course Management** - Define and manage university courses with names, units, and codes.
- 📝 **Enrollment Management** - Process and track student course selections with strict validation.
- 💯 **Score Management** - Manage score submissions, validation, and pass/fail tracking.

### User Interface
- 🎨 Modern and clean Graphical User Interface built with Tkinter.
- 📊 Data tables with vertical scrollbar support.
- ✨ Uniform button layouts and seamless user experience.
- 🔄 Select and populate functionality across all views.

### Data Management
- ✅ Comprehensive input validation for all fields.
- 💾 File-based persistence using the `pickle` module (Data Access Layer).
- 📝 Strict Business Logic layer to prevent duplicate entries and invalid data.

## 🏗️ Architecture

This project follows the MVC (Model-View-Controller) architectural pattern:

```text
┌─────────────┐
│    View     │  UI Layer
└──────┬──────┘
       │
       ↓
┌─────────────┐
│ Controller  │  Business Logic Layer
└──────┬──────┘
       │
       ↓
┌─────────────┐
│Business Log.│  Rules & Validation Layer
└──────┬──────┘
       │
       ↓
┌─────────────┐
│Data Access  │  Data Access Layer
└──────┬──────┘
       │
       ↓
┌─────────────┐
│  Database   │  File Storage (Pickle)
└─────────────┘