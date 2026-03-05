## Advanced Features: Search and Tagging

This project incorporates advanced data retrieval and categorization to improve user experience.

### Tagging System
* **Implementation:** Integrated using the `django-taggit` third-party package.
* **Usage:** Users can add comma-separated tags when creating or updating a post.
* **Filtering (`/tags/<tag_slug>/`):** Tags are displayed as clickable links on posts. Clicking a tag dynamically filters the `PostListView` to show only posts containing that specific tag.

### Search Functionality
* **Implementation (`/search/`):** A custom view utilizes Django's complex `Q objects` to perform an `OR` query across multiple database fields simultaneously.
* **Usage:** A global search bar in the navigation header allows users to input keywords. The system searches for exact or partial matches within the post's `title`, `content`, and associated `tags`.
* **Results:** Displays matching posts clearly, handling empty result sets gracefully.