# Collec: a collection tracker webapp

*Collec* is a webapp for tracking several types of collections. It was originally made for [Code Institute](https://codeinstitute.net/)'s 4th submission project.

## Important notes

The documentation is split across two files:

-   [README.md](README.md) (this file): Overview of the app. Read this to get an idea of the premise of the app, technologies used and project conventions.
-   [DESIGN.md](doc/DESIGN.md): UX design notes crafting during early stages of development. The design process is described entirely, from the concept and market research, through information structuring to visual design principles and color palettes.

The project is managed via a [GitHub project](https://github.com/users/Tearnote/projects/1/views/1). Issues are created in a "User story" format, and assigned size/complexity and importance. Each issue contains a title, user story sentence, and a list of technical expectations.

## Highlights

![Screenshot of the landing page](doc/highlights/landing.png)

The landing page is simple and to the point, cleanly explaining the purpose of the app.

![Screenshot of the sign-up modal](doc/highlights/signup.png)

The sign-in and sign-up screens are modals, with their content loaded from the server via AJAX.

![Screenshot of the dashboard page](doc/highlights/dashboard.png)

After signing in, the user can open their Dashboard which shows 5 most recently modified items from each collection. Item creation and editing is available from here as a shortcut.

![Screenshot of the item list](doc/highlights/item_list.png)

Each collection can be viewed in detail, with sorting and search functionality.

![Screenshot of the item editor modal](doc/highlights/item_editor.png)

Items can be created, modified and deleted using the editor modal, loaded from the server like the sign-in/up ones.

![Screenshot of the dashboard page in read-only mode](doc/highlights/read_only.png)

Opening a user's page without signing in as them enters read-only mode, allowing anyone to browse your collection.

![Screenshot of the dashboard page on a mobile display](doc/highlights/responsive.png)

Every page is trivially responsive with wrapping UI elements and grids.

## Technologies used

-   Python 3: Used for the backend portion of the app
-   HTML5+CSS3: Design of the frontend

## Dependencies

All dependencies are included, or installed via requirements.txt.

-   [Django 4.1](https://www.djangoproject.com): backend framework used to serve the app to the browser and as a RESTful interface to manipulate the models
-   [Bootstrap 5](https://getbootstrap.com): CSS framework for grid layout and improved based styles
-   [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms): Django library that improves form rendering
-   [django-allauth](https://www.intenct.nl/projects/django-allauth/): Django library that expands on the built-in user authentication

## Credits

[Landing page photo](https://www.pexels.com/photo/books-768125/) by [Emily](https://www.pexels.com/@emily-252615/)
