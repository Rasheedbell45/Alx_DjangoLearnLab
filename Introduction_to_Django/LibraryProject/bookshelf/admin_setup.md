# Django Admin Setup for Book Model

## Steps Performed:
1. Registered the Book model in `bookshelf/admin.py`.
2. Customized the admin to show:
   - **List Display:** title, author, publication_year
   - **Filters:** publication_year, author
   - **Search Fields:** title, author
3. Created a superuser with `python manage.py createsuperuser`.
4. Accessed Django Admin at `http://127.0.0.1:8000/admin/`.

## Expected Outcome:
- Admin dashboard shows "Books".
- List view displays book records with title, author, and publication year.
- Sidebar filter allows filtering by author and publication year.
- Search box supports title and author queries.
