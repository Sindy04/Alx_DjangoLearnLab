"from .views import list_books", "LibraryDetailView", "path"
views.register",
"LogoutView.as_view(template_name=",
"LoginView.as_view(template_name="
"LoginView.as_view(template_name="

# Displaying Html

<!-- list_books.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>List of Books</title>
</head>
<body>
    <h1>Books Available:</h1>
    <ul>
        {% for book in books %}
        <li>{{ book.title }} by {{ book.author.name }}</li>
        {% endfor %}
    </ul>
</body>
</html>
