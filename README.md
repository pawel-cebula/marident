# Marident

Marident (https://marident.herokuapp.com/) is a website for a dental clinic, which includes:
- Navigation
- Homepage (info about the services, dentist, clinic and testimonials)
- Price List (generated based on Django model and from the database)
- Contact Form (that registers inquiries in the database and sends an email to the clinic owner)

## Technology

Marident was built using Django in order to allow the clinic owner to make edits of the price list and view all inquiries from the contact form via admin.

It was the first Django app I deployed using Heroku.

The website was styled using [Tailwind CSS](https://tailwindcss.com/), so far loading Tailwind via a CDN for simplicity during development.

The price list is displayed from the model and database using [django-tables2](https://django-tables2.readthedocs.io/en/latest/index.html) package, which has been modified locally in order to style the table using Tailwind via the table.html template.

The form is generated using [crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/).

The contact form sends an email to the clinic owner on POST requests using [SendGrid](https://sendgrid.com/).

In production, SECRET_KEY and EMAIL_HOST_PASSWORD are stored in environment variables.

## Learnings
- Implementing own design (Figma) in Tailwind CSS in a Django app and packages (crispy-forms, django-tables2)
- Sending emails from Django using SendGrid
- Storing sensitive info as environment variables
- Deploying Django app to Heroku

## To Do's

- [ ] Write tests
- [ ] Switch from loading Tailwind via CDN
- [ ] Fix grey inner-border between round images and their actual borders
