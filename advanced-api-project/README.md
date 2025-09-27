# Advanced API Project

This project demonstrates advanced API development using Django REST Framework.

## Endpoints

- `GET /api/books/` → List all books (public).
- `GET /api/books/<id>/` → Retrieve book by ID (public).
- `POST /api/books/create/` → Create a new book (authenticated only).
- `PUT /api/books/<id>/update/` → Update book (authenticated only).
- `DELETE /api/books/<id>/delete/` → Delete book (authenticated only).

## Permissions
- Unauthenticated users → Read-only (List & Detail).
- Authenticated users → Full CRUD access.

## Notes
- Publication year validation prevents future dates.
- Nested serializers allow viewing Author → Book relationships.
