## Comment System
This blog includes an interactive comment system attached to individual posts.

### Features & Implementation
* **Model Relationship:** The `Comment` model uses a `ForeignKey` to link to both the `Post` and `User` models, establishing a robust relational structure.
* **View Comments:** Comments are displayed directly on the `PostDetailView`.
* **Add Comment (`/post/<pk>/comments/new/`):** Authenticated users can post comments via `CommentCreateView`. The view automatically associates the comment with the correct post and logged-in user.
* **Update/Delete Comments (`/comment/<pk>/update/`, `/comment/<pk>/delete/`):** Authors can manage their own comments. Protected by `LoginRequiredMixin` and `UserPassesTestMixin`.