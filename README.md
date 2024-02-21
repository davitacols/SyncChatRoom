SyncChatRoom - Real-time Chat Application with Django Channels
==============================================================

SyncChatRoom is a real-time chat application developed using Django and Django Channels. It leverages WebSocket technology to provide users with an interactive and instant messaging experience. This project aims to demonstrate the implementation of real-time features in a Django web application.

Overview
--------

### Features

1.  Real-time Messaging: Utilizes WebSocket and Django Channels to enable real-time communication between users.

2.  User Authentication and Authorization: Implements user authentication and authorization features for secure access to the chat application.

3.  Message Broadcasting: Supports message broadcasting, allowing users to send and receive messages instantly.

4.  User Online Status: Provides an online status feature to indicate whether users are currently active in the chat.

### Technologies Used

-   Django: A high-level web framework for Python that encourages rapid development and clean, pragmatic design.

-   Django Channels: Extends Django to handle WebSockets, enabling real-time functionality in the application.

-   WebSocket: A communication protocol that provides full-duplex communication channels over a single TCP connection.

-   HTML, CSS, JavaScript: Front-end technologies used to create a user-friendly and responsive interface.

### Project Structure

-   syncchatroom: Django project directory containing settings, configuration, and top-level application routing.

-   syncchat: Django app responsible for handling chat-related functionalities, including models, views, and templates.

-   templates: Directory containing HTML templates for rendering pages.

-   static: Directory for storing static files like CSS and JavaScript.

-   consumers.py: Defines WebSocket consumers for handling connections, disconnections, and message reception.

-   routing.py: Configures URL routing for WebSocket connections using Django Channels.

### Getting Started

1.  Clone the Repository:

    bash

    `git clone https://github.com/your-username/SyncChatRoom.git
    cd SyncChatRoom`

2.  Install Dependencies:

    bash

    `python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt`

3.  Run Migrations:

    bash

    `python manage.py migrate`

4.  Start the Development Server:

    bashCopy code

    `python manage.py runserver`

5.  Open the Application: Visit `http://127.0.0.1:8000/` in your web browser.

### Usage

1.  User Registration:

    -   Navigate to `/register/` and sign up for an account.
2.  User Login:

    -   Go to `/login/` and log in with your credentials.
3.  Real-time Chat:

    -   Access the main chat interface at `/`.
    -   Send and receive real-time messages using the WebSocket-based chat.

### Contributing

Contributions to improve and expand the features of SyncChatRoom are welcome. Follow the guidelines mentioned in the README.md file to contribute to the project.

### License

This project is licensed under the MIT License. See the LICENSE file for details.