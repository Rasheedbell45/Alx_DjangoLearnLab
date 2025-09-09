# Permissions & Groups in LibraryProject

## Custom Permissions
Defined in `Book` model (`models.py`):
- `can_view` → Allows viewing books.
- `can_create` → Allows creating books.
- `can_edit` → Allows editing books.
- `can_delete` → Allows deleting books.

## Groups
- **Viewers** → `can_view`
- **Editors** → `can_view`, `can_create`, `can_edit`
- **Admins** → all permissions

## How It Works
- Views are protected with `@permission_required`.
- Users must belong to a group with the correct permissions to access functionality.
- Run `python manage.py setup_groups` after migrations to initialize groups and permissions.
