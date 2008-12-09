**Note:** [There are active admin CSS changes in Django trunk](http://groups.google.com/group/django-users/browse_thread/thread/173cdfb52a05437c/54d8faa41721f86a "admin css, is this still supported? - Django users | Google Groups"), so proceed with caution.

---

A starting point for customizing the look of [Django's automatic admin interface](http://www.djangobook.com/en/1.0/chapter06/ "Chapter 6: The Django Administration Site").

These colors suit my tastes a bit better than the default.

Folder structure:

	.
	|-- static
	|   `-- admin
	|       |-- css
	|       |   |-- base.css
	|       |   `-- img
	|       `-- img
	|-- templates
	|   `-- admin
	|       `-- base_site.html
	`-- urls.py

To customize more parts of the admin's markup, you copy things from

`django/contrib/admin/templates/admin/` to  `yoursite/templates/admin/`.

- [General information](http://djangobook.com/en/1.0/chapter06/#b70 "Chapter 6: The Django Administration Site")
- [Customizing the CSS](http://docs.djangoproject.com/en/dev/obsolete/admin-css/ "Django | Customizing the Django admin interface | Django Documentation")
