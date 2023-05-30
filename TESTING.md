# ClassMate | Testing 

[Return to README](README.md)

## Code Validation

### HTML 
All pages were run through the official [W3C HTML Validator](https://validator.w3.org/).
This was in order to check for syntax errors or issues with rendering. 
Please see below for the results of each page in the site: 

<details>
<summary>Homepage - No issues or errors</summary>
<br>

![Homepage Validation](docs/images/nu-homepage.png)
</details>
<details>
<summary>Browse Schools Page - No issues or errors</summary>
<br>

![Browse Schools Validation](docs/images/nu-schools.png)
</details>
<details>
<summary>Sign Up Page - No issues or errors</summary>
<br>

![Sign Up Validation](docs/images/nu-signup.png)
</details>
<details>
<summary>Login Page - No issues or errors</summary>
<br>

![Login Validation](docs/images/nu-login.png)
</details>
<details>
<summary>Logout - No issues or errors</summary>
<br>

![Logout Validation](docs/images/nu-logout.png)
</details>
<details>
<summary>School Detail Page - Errors due to Summernote/Crispy Forms</summary>
<br>
    - These pages identifed a stray end 'form' tag. This is due to the opening tag of Crispy Forms not being identified as HTML in the browser.
    - There is also a stray 'p' end tag in scope, and this is due to Summernote rendering some HTML tags itself in the Django Admin backend.

    *These errors were kept in as they do not affect the functionality of the project, and are part of the imported external libraries.*


![Logout Validation](docs/images/nu-school-detail.png)
</details>
<details>
<summary>Edit Comment Page - No Issues or Errors</summary>
<br>

![Edit Comment Validation](docs/images/nu-edit-comment.png)
</details>
<details>
<summary>Delete Comment Page - No Issues or Errors</summary>
<br>

![Delete Comment Validation](docs/images/nu-delete-comment.png)
</details>

### JavaScript
JavaScript code used in the application was validated using [JSHint](https://jshint.com/)
- No issues or errors were raised when running through the JavaScript Validator
- No errors present in the console. 

### Python
Python code was validated using the [CI Python Linter](https://pep8ci.herokuapp.com/#).

---
No issues or errors were found on **Website App** pages: 

<details>
<summary>views.py - No issues or errors</summary>
<br>

![views](docs/images/views.png)
</details>
<details>
<summary>urls.py - No issues or errors</summary>
<br>

![urls](docs/images/urls.png)
</details>
<details>
<summary>models.py - No issues or errors</summary>
<br>

![models.py](docs/images/urls.png)
</details>
<details>
<summary>forms.py - No issues or errors</summary>
<br>

![forms.py](docs/images/forms.png)
</details>
<details>
<summary>apps.py - No issues or errors</summary>
<br>

![apps.py](docs/images/apps.png)
</details>
<details>
<summary>admin.py - No issues or errors</summary>
<br>

![admin.py](docs/images/admin.png)
</details>

--- 

In the **ClassMate Project**, some Django-generated codes caused 'line too long' errors. 
- These were kept in, due to the necessity of maintatining these lines of code for app functionality, and deployment. 
    - Specifically, the 'line too long' error was present in settings.py, for linking Cloudinary Storage. This cannot be shortened as it would lose the code functionality. 

<details>
<summary>settings.py - Line too Long Errors due to Cloudinary Storage</summary>
<br>

![settings.py](docs/images/settings.png)
</details>


- All other pages had no Python errors: 

<details>
<summary>urls.py - No issues or errors</summary>
<br>

![classmate-urls.py](docs/images/classmate-urls.png)
</details>
<details>
<summary>asgi.py - No issues or errors</summary>
<br>

![asgi.py](docs/images/asgi.png)
</details>
<details>
<summary>wasgi.py - No issues or errors</summary>
<br>

![wsgi.py](docs/images/wsgi.png)
</details>

---

## Acessibility
### Lighthouse Score


## Responsiveness 
- Chrome Dev tools responsive viewer was used to test the responsiveness of **all** pages of the site: 
- A wide variety of devices and screen sizes were tested: 
(images here)

*The application was also tested manually a range of devices including: iPhone 14, iPhone 11, MacBook Air, iPad 3,*

### Browsers
The Application was checked manually on the following browsers with no compatability issues:
- Google Chrome
- Apple Safari
- Mozilla Firefox
- Opera 

---
# Testing

## User Stories Testing

- talk about Kanban board & how acceptance critera were used


## Manual Testing


## Input Validation


## Unresolved Bugs / Issues 