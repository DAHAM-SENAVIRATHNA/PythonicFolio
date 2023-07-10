# PythonicFolio
The Python Streamlit Portfolio Project is a dynamic and interactive web application that creates a visually appealing portfolio website to showcase your skills, projects, and accomplishments.
It also provides a contact form for users to write and email the portfolio owner. An email notification is sent to the specified recipient email when a message is sent.

## Features
- Showcase your portfolio with images, descriptions, projects, and links.
- Provide a contact form for users to write and send an email to the portfolio owner.
- Receive email notifications for new messages.

## Usage
Update the send_email.py file with your email credentials and recipient email address.
```

 host = "smtp.gmail.com"
 port = 465
 username = "your-email@example.com"
 password = "your-email-password"

 receiver = "portfolio-owner@example.com"
```

## Deployment

To deploy this project run

```
  streamlit run Home.py
```