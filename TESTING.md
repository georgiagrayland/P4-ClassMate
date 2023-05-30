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
Talk about errors here 

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
- These were kept in, due to the necessuity of maintatining these lines of code for app functionality, and deployment. 
    - Specifically, the 'line too long' error was present in settings.py, for linking Cloudinary Storage. This cannot be shortened as it would lose the code functionality. 

<summary>settings.py - Line too Long Errors due to Cloudinary Storage</summary>
<br>

![settings.py]()
</details>


- All other pages had no Python errors: 

<summary>urls.py - No issues or errors</summary>
<br>

![classmate-urls.py]()
</details>
<summary>asgi.py - No issues or errors</summary>
<br>

![asgi.py]()
</details>
<summary>wasgi.py - No issues or errors</summary>
<br>

![wsgi.py]()
</details>