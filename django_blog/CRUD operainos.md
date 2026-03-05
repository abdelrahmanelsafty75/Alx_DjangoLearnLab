## Blog Post Management (CRUD)

This platform supports full CRUD operations for blog posts, implemented securely via Django's Class-Based Views (CBVs).

### Features:
* **Create (`/post/new/`):** Authenticated users can write new posts (`PostCreateView`). The `author` field is automatically set to the logged-in user.
* **Read (`/` & `/post/<pk>/`):** Publicly accessible views. `PostListView` displays all posts ordered by date (descending), and `PostDetailView` displays the full content of a specific post.
* **Update (`/post/<pk>/update/`):** Allows authors to edit their posts (`PostUpdateView`).
* **Delete (`/post/<pk>/delete/`):** Allows authors to remove their posts (`PostDeleteView`).

### Security & Permissions:
* **`LoginRequiredMixin`:** Ensures that unauthenticated users cannot access the create, update, or delete views.
* **`UserPassesTestMixin`:** Enforces object-level permissions, guaranteeing that only the exact author of a specific post has the right to update or delete it.