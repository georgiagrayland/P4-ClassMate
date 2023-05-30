# ClassMate

![Amiresponsive image](Link)

## Introduction

Welcome to ClassMate

ClassMate is my my Portfolio Project 4 submission for Code Institute’s Diploma in Full Stack Software Development Course.

The purpose of this project was to build a full-stack site based on user needs and a custom dataset.

ClassMate is a fictional forum website based around fictional schools, allowing users to browse schools in different regions and participate in discussion and comments on each school. 

ClassMate has been built built using the **Django full-stack framework** and uses a Relational Database. Technologies used are HTML, CSS, JavaScript, and Python. 

This project is entirely for educational purposes only, all information included is fictional and no revenue is generated.

## Live Project 
![View the Live Project Here](Link)

---
## UXD - User Experience Design
 The user was kept in mind through the entire development process of this project, so that experience using the site would be maximised and user needs would be satisfied. 
 Thus, the planning of the project was constructed of 5 planes, namely, the 5 elements of User Experience Design: 
- The Strategy Plane
- The Scope Plane
- The Structure Plane
- The Skeleton Plane
- The Surface Plane

These planes move from most-least abstract, with each previous one creating an outline for the next. Each plane has required meeting different goals and completing different tasks throughout project development. 

---
## Strategy
### Developer Goals
- As a site owner, I want the site to be easy to navigate 
- As a site owner, I want the site to look aesthetically pleasing, accessible, and relevant to the theme of the information.
- As a site owner, I want to be able to provide some value to users. 
- As an admin user, I want to be able to Add, Edit, and Delete Schools from the forum.
- As an admin user, I want to be able to approve or reject comments that have been made by logged in users. 

### User Stories
#### Regular Site User Stories
- As a site user, I want to know the purpose of the site upon reaching the first landing page (homepage) so that I do not have to waste time working out what it is for. 
- As a site user, I want to be able to seamlessly navigate through the site, so that I can view any desired page within the site.
- As a site user, I want to be able to sign up to the site, so that I can enjoy the additional benefits of having an account. 
- As a site user, I want to be able to view relevant information easily on all pages, and understand what is displayed on the site, with the use of icons, images, text, and headings. 
- As a site user, I want to be able to see the posts from other users on relevant pages, so that I can make informed decisions and understand other people’s opinions and experiences. 
- As a user, I want to be prompted to create an account and know why I should, so that I can enjoy the additional benefits of having one on this sit. 
- As a user I want to be able to view the footer on any page, and access Social media links directly from here by clicking on the icons, with the Social Media page opening in a new tab. 

#### Active User (Logged In) Stories 
- As a user with an account, I want to be able to log in easily, viewing a clear clear link to log in on any part of the site (on the Navigation Bar). 
- As a logged-in user, I want to be able to add comments on any School Detail page, with my username present so that I know who I am posting as. 
- As a logged-in user, I want to be able to see that my comments have been posted admins and are awaiting approval to be viewed on the site. 
- As a logged-in user, I want to be able to post multiple comments on an individual School Detail page, so that I can ask questions of other users and gather information I may desire about specific schools. 
- As a logged-in user, I want to be able to know where I can go to see all of my comments I have made on the site, and be able to access this page easily. 
- As a logged-in user, I want to be able to see all of my comments on any School on a single page, and from here, have the choice and ability to seamlessly Edit or Delete them. 

---
## Scope
In order to achieve the desired user and owner goals, the following features will be included in this version of the site:
Features included were implemented using **Agile Principles**, in the following order: 

**Block 1**
- Landing/Home page with an introduction and a prompt for users to create an account, and an overview of the site's     purpose. 
- Responsive navigation bar to be present on all pages, so users can move through the site seamlessly.
- Responsive footer to be present on all pages, with social media links.

**Block 2**
- Browse Schools page, allowing users to browse all Schools on the database in a list, so they can compare and contrast key information quickly and easily. 
- School Detail page, where users can click on a desired school from the browse page. Here they will find all information about this school, including a longer text description. 
- Login/Sign Up/Log out functionality, where new users can register for an account or users with an existing account can log in or log out when desired.

**Block 3**
- Comment section on each School Detail page, where all users can view comments made by others, and logged-in users can add their own comments. 
- Comment management page for logged-in users, where they can view all comments they have made across the site on one page. 
-   Comment edit/delete functionality for logged-in users on their 'My Activity' page. 

The ClassMate KanBoard (link) was created using GitHub projects, and was used to manage the entire planning and development process.  

---
## Structure
### Colors
![Colour Palette](docs/images/color-palette.png)
Color Palette Generated Using [Coolors](https://coolors.co/)

Colors for this project were selected based on contrast, and adherence to the theme. 

**#FDF0D5:** The base body colour, providing a backdrop for all pages. This was chosen due to its similarity to the colour of old book paper, to give the site a book effect. 

**#F1D302:** The ClassMate logo colour. This was chosen due to the contrast with the 'Barn Red' Nav bar and footer colour. 

**#780000:** The base color for the navbar and footer. This colour was selected as many school uniforms are comprised of this colour, and many schools have this color incorporated into their logo/crest/uniform/books. 

**#235789:** The blue color of most of the heading text and icons throughout the site. This was chosen due to its silimarity to blue pen ink, hence fitting the school theme. It also contrasts well with the white background of the cards, and the base body colour. 

**#C1292E/White:** Most links show Fire Engine Red or white upon hover, for the reason of colour contrast so ease of sight for the user. 

### Typography 

Google fonts were used to style text on this site. 

- Merriweather: 
    - The font for the ClassMate logo, School Titles, and titles on user authentication and comment management pages. 
    - This font was chosen as it reflects the School theme, is easily readable, and is relatively heavy so it is obvious what page headings are. 

- Assistant:
    - All body text including that on cards, descrptions, and comments is in Assistant. 
    - Assistant is simple and easy to read. 

### Images

Images on the site were selected based on their colour palette, as well as having a mixture of different-looking schools so that the site was varied and a range of users can enjoy the site. 
All images are responsive to a range of screen sizes. 

*See credits section for more information on image sources.*

### Databases 
PostgreSql is used for hosting the data on this site. 

### Models 

### School 
- The School model is where all Schools in the database are held. 
- It has a number of varying fiels to hold key information and number about schools, a longer description and images. 
- It is connected to the Comment model through each School name. 

### Comment 
- The comment model allows (logged-in) to leave comments on individual school pages. 
- It is connected to the School model, via the School name. 
- It is also connected to users through each comment id. 
- It allows users to leave their username and timestamp on comments for their own reference. 
- The Comment model has full Create, Read, Update, Delete (CRUD) functionality on the front-end. 

### User (Django Allauth)
- The User database was automatically created upon installation of Djang-allauth. 
- This is for users to log in, sign up, log out, and leave comments on School Pages. 
- It is linked to the comment model, through the user id. 

![link to database diagram](docs/images/database.png)

--- 
## The Skeleton Plane
- The theme of this website follows through in the design. 
- Bootsrap columns, rows, and cards have been utilised throughout to divide the pages, and maintain the layout throughout the site. 
- The School theme is present throughout the images, colours, and icons. 
- The layout of each page is relatively simple, for ease of use for users, and to maintian responsiveness across all screen sizes. 


---
## The Surface Plane 
## Features 
*Across the project*:
- All pages of the project are responsive to a wide range of screen sizes.
- Semantic HTML is used throughout.
- Custom CSS is blended with Bootstrap 5 to give the site a user-friendly, aesthetic, and intuitive experience. 

### Features Present on *all* pages:

### Navigation Bar
- Navigation Bar is present on all pages of the site. 
    - It is fully responsive to all possible screen sizes, with a collapsible menu that forms on narrower screen widths.
- Using the Navigation bar, users can move through the site seamlessly, with clear messaging used on it to where the links will take them.  
- The ClassMate logo is present on the left, which changes to white when hovered, and when clicked, takes the user back to the homepage, no matter where they are currently in the site. 
- For all users, there is a link to the page to 'Browse all Schools'.
    - This link changes color and adds an underline when hovered, for accessibility and ease of use for the user. 

- If a user is not logged in, the navbar will display a button link that says 'SIGNUP/LOGIN'. 
    - This link changes to a contrasting colour and underlines when hovered. 
    - When clicked, it takes the user to the 'Sign in' page. Here, they may either Sign in if they have an existing accoutn or there is also a link and message on this page that takes them to the 'singup' page. 

    ![Regular navbar](docs/images/navbar.png)

- If a user is logged in, the navbar will display an additional link, called 'My Activity'. 
    - This link changes to a contrasting colour and underlines when hovered. 
    - This will take the user to their 'My comments' page, where they will see the comments they have made and can edit or delete them. 
 - If the user is logged in, the authentication button will instead display 'Logout'.
    - When this button is clicked, it takes the user to the confirm logout page.

    ![Logged in user navbar](docs/images/logged-navbar.png)

### Footer 
- The Footer is present on all pages of the site 
- ClassMate logo
- Short 'about' description
- Social Media links as icons, which open in new tab when clicked. This avoids disturbance of user experience.

![Footer](docs/images/footer.png)

---
## Individual Pages:

## Homepage

### Header & Introduction Message:
- Under the nav bar, the homepage has a header which explains to users the purpose of the site.

- The message and link of the header changes whether the user is logged in or not:

**New user / user not logged in**
- If a user is not logged in the site, the header will show an introduction and message saying the purpose of the site. 
- The message prompts the user to create an account or log in, so they can enjoy the additional benfits of having an account, with a link to the login/signup page. 
- The link changes to a contrasting colour upon hover, for ease of use and accessibility. 

![Header](docs/images/header.png)

**Logged-in User**
- If a user is logged in, the header will display a different message and link. 
- The message welcomes the user back, and the link changes to prompting the user to visit the browse schools page. 

![Header logged in user](docs/images/logged-header.png)

### Popular on this Site Section
- Under the header, there is a flashing title for 'Popular on this site'
- This catches the users attention and displays cards to 3 schools from the database below. 
- This section is aimed at geting people interested in viewing the rest of the site and creating an account. 

![Popular on this Site](docs/images/popular-section.png)

---
## Browse Schools Page
- When any user clicks 'Browse all Schools' from the Navbar, or a logged-in user clicks 'View School Pages' from the homepage header, they are taken to the Schools List page. 
- This page has a header clearly demonstrating what the purpose of this page is:

![Browse Header](docs/images/list-heaer.png)

- Underneath this, all Schools currently in the database are displayed as a list of cards on the page. 
- Each school has a card with an image on the left. 
- On the right of each card is a School name, which is a link to the relevant 'School Detail' Page. 
- Under the name, there are 3 key pieces of information with related icons: Location, School Type, and School Gender. 
- There is a short description of each school, aimed at getting the user interested in clicking on the School Detail page. 
- There are also 2 more key data points for each school: any subjects they specialise in, and average class size. 
- **The inclusion of these pieces of information was aimed at allowing users to compare and contrast important parts of each schoool from this page, whilst also making them want to learn more by clicking on an individual school detail page.** 

*Each school is displayed in a responsive card in a vertical list:*

![List card](docs/images/list-card.png)

---
## School Detail Page


## My Activity Page 

## Edit Comment Page

## Delete Comment Page 

## Login Page

## Singup Page

## Sign Out Page

---

## Technologies Used 

- [Python](https://www.python.org/):
    - [Django 3.2](https://www.djangoproject.com/)
    - [AllAuth](https://django-allauth.readthedocs.io/en/latest/)
    - [Summernote](https://summernote.org/)
    - [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html)

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [Bootsrap](https://getbootstrap.com/)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/javascript)
- [Google Fonts](https://fonts.google.com/)
- [Font Awesome](https://fontawesome.com/)
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/)

### Storage& Hosting
- [Heroku]()
- [GitHub](https://github.com/)
- [ElephantSQL](https://www.elephantsql.com/)
- [Cloudinary](https://cloudinary.com/)

### IDE & Version Control
- Git
    - Used as a version control in the terminal.

- Gitpod
    - Where files were created and the code was written.

### Other Tools
- [TinyPNG](https://tinypng.com/)
    - Used to Compress images for faster loading and to improve Lighthouse score. 

- [Dbdiagram](https://dbdiagram.io/home/)
    - Used to visualise the database. 

- [ChatGPT](https://chat.openai.com/)
    - OpenAI's ChatGPT was partially used to provide inspiration for the fictional school names and descriptions. 

---

## Deployment 


---

## Credits
### School Names/ Descriptions
- Inspiration for many of the fictional school names and descriptions was helped by Chat GPT. 
    - This was to ensure all information was completely fictional, an no bias of real information from myself as the developer would be present in the site. 

### Images 
- All images on the site were sourced from:
    - [Unsplash](https://unsplash.com/)
    - [Pexels](https://www.pexels.com/)
    - [Pixabay](https://pixabay.com/)

### Code
- Parts of the code, and base inspiration for other parts, was taken from the Code Institute 'Django Blog' walkthrough project. 
- [Code Institute Codestar Blog Project](link)
    - 'Codestar Blog' is a walkthrough project by Code Institute. This project is designed to give students an introduction to the Django Framework, PostgreSQL, and using relational databases. 
    - Parts of the core functionality were adopted from this project, including the 'Comment' model. 

### Bootstrap
- The [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/) library (version 5.3) is used across this project, and is present on all pages. 
- This was used for page layout, in order to create an intuitive, aesthetic, and pleasing experience for site users. 
    - The Navigation bar, cards, forms, and buttons all all Bootstrap components that have been adoapted and built apon for this project. 

### Django Documentation
- The official [Django Documentation](https://docs.djangoproject.com/en/4.2/) was utilised throughout the development of this project.
    - Explanations of Django concepts such as creating views and urls were very helpful.

---
## Acknowledgements 

### Code Institute
- **Harry Dhillon**, my mentor at Code Institute, has been incredibly helpful and insightful throughout the development of this project. 
   - Has provided me with suggestions, advice, and encouragement, as well as helping me stay on track to meet the tight deadline of this project. 
- The tutors at Code Institute, who were very helpful and always available to offer solutions for issues and providing strategies to achieve my desired fucntionality for this project. 

- My peers at Code Institute, who have provided valuable feedback, and solutions to PEP8 errors I have come across during the development of this project.
