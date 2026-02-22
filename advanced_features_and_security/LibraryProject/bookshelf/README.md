# Permissions and Groups Setup

## Custom Permissions
Custom permissions (`can_view`, `can_create`, `can_edit`, `can_delete`) were added to the model's `Meta` class.

## Groups Configuration
Groups are created and managed via the Django Admin interface:
- **Viewers**: Assigned the `can_view` permission.
- **Editors**: Assigned `can_view`, `can_create`, and `can_edit` permissions.
- **Admins**: Assigned all permissions including `can_delete`.

## View Enforcement
Views are protected using the `@permission_required` decorator, specifying the app name and the required permission (e.g., `@permission_required('relationship_app.can_edit', raise_exception=True)`). This ensures that only users belonging to the appropriate groups can access these views.