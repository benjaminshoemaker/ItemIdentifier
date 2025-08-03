# Overview

Item Disposal Helper is a Flask-based web application that uses Google Vision API to identify items from uploaded images and suggests appropriate disposal methods. Users can upload photos of items they want to dispose of, and the application provides recommendations for selling, donating, or recycling the identified items.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Template Engine**: Jinja2 templating with Flask
- **UI Framework**: Bootstrap 5 with dark theme for responsive design
- **Icon Library**: Font Awesome for consistent iconography
- **Form Handling**: HTML5 file upload with client-side validation
- **Template Inheritance**: Base template pattern for consistent layout and navigation

## Backend Architecture
- **Web Framework**: Flask with standard routing patterns
- **File Processing**: Multipart form data handling for image uploads
- **Image Processing**: Base64 encoding for API transmission
- **Error Handling**: Flash messaging system for user feedback
- **Validation**: Server-side file type and size validation
- **Logging**: Python logging module for debugging

## API Integration
- **Computer Vision**: Google Vision API for image label detection
- **Authentication**: API key-based authentication via environment variables
- **Request Structure**: RESTful API calls with JSON payloads
- **Response Processing**: Label extraction from Vision API responses

## Configuration Management
- **Environment Variables**: Secure storage of API keys and session secrets
- **Session Management**: Flask session handling with configurable secret keys
- **Development Mode**: Debug mode toggle for development environments

## External Dependencies

- **Google Vision API**: Core image recognition service for item identification
- **Bootstrap CDN**: UI framework and styling (via Replit dark theme)
- **Font Awesome CDN**: Icon library for enhanced user interface
- **Flask Framework**: Web application framework and templating
- **Requests Library**: HTTP client for external API calls