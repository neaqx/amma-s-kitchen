# **Ammas Kitchen - Introduction**

## ***Eat and Enjoy***

Welcome yourself to  *Ammas Kitchen*, also know as **Best restaurant in the world** - a rejoiceful place where you can find the best of both worlds, all on one plate.

![Am I Responsive]()

Amma's Kitchen is a unique fusion restaurant that brings together the rich flavors of European and Asian cuisine. At Amma's Kitchen, we believe in blending culinary traditions to create a dining experience that is both familiar and adventurous. Our chefs meticulously craft each dish, drawing inspiration from diverse cultures and adding a modern twist to time-honored recipes.

From the vibrant streets of Berlin to the bustling markets of Tokyo, our menu offers a journey across continents. Whether you're indulging in a classic European dish with an Asian flair or savoring a traditional Asian meal with a European touch, every bite at Amma's Kitchen is a celebration of flavors. With a cozy, welcoming atmosphere and a commitment to fresh, high-quality ingredients, we invite you to experience the best of both worlds, all on one plate.

Opening Hours:
We are open daily from 11:00 AM to 10:00 PM, ready to serve you an unforgettable culinary experience.

Make a reservation now and discover a new world of flavor at Amma's Kitchen!

View live website here: [Happy Hacks]().

<hr>

## **TABLE OF CONTENTS**

- [**Team Goal**](#happy-hackers-team-goal)
- [**Design**](#design)
   * [Colours](#colours)
   * [Typography](#typography)
   * [Wireframes](#wireframes)
   * [Database Schema](#database-schema)
- [**Features**](#features)
  * [Navigation](#navigation)
  * [Footer](#footer)
  * [Home Page](#home-page)
  * [Booking Page](#add-hack-page)
  * [May resevation Page](#hacks-page)
  * [CRUD Functionality](#crud-functionality)
- [**Testing**](#testing)
- [**Bugs**](#bugs)
- [**Technologies Used**](#technology-used)
- [**Credits**](#credits)
- [**The Team**](#the-team)

<hr>

## **Ammas Kitchen Goals**

- Deliver a unique fusion of European and Asian cuisine
- Provide an exceptional dining experience with innovative dishes
- Use high-quality, fresh ingredients in every meal
- Create a warm and welcoming atmosphere for all guests
- Promote cultural diversity through culinary innovation
- Ensure customer satisfaction with excellent service
- Expand the brand to international markets
- Foster sustainability by using eco-friendly practices
- Build a loyal community of food lovers and regular patrons
- Offer a convenient online reservation system for easy dining

<hr>

## **DESIGN**

### **Colours**
- Research indicated that the happiest colour was black, with grey also featuring.
- We selcted a serious and professional colour palette to reflect the serious nature of the project.
- Colours were selected using the coolors color palette generator.

![Coolors Palette](/)

<hr>

### **Typography**
- All fonts were sourced through [Google fonts](https://fonts.google.com/).
- Fonts were selected for their simple and readable design to avoid distracting from the content.
- Roboto Slab and Quicksand were selected.
- Later, Lilita One, was selected for the home page title for impact.

![Fonts](/static/docs/fonts.png)
![Title Font](/static/docs/lilitaonefont.jpg)

<hr>

### **Media**
- [Balsamiq](https://balsamiq.com/) was used for the design of wireframes.
- [Fontawesome](https://fontawesome.com/) was used for the icons on various buttons.
- [DrawSQL](https://drawsql.app/) was used to sketch out the database models at an early stage.
- [Pexels](https://unsplash.com/) was used to source the background image.

<hr>

### **Wireframes**
Wireframes for different views are linked here:

![Mobile Wireframe](/static/docs/mob-wireframe.jpg)
![Mobile Wireframe](/static/docs/mob-wireframe-2.jpg)

![Desktop Wireframe](/static/docs/desktop-wireframe.jpg)
![Desktop Wireframe](/static/docs/desktop-wireframe-2.jpg)

<hr>

### **Database Schema**

- The database scheme was completed an an early stage, but later ammended to include emoji's

![Database Schema](/static/docs/dataschema1.jpg)

<hr>

## **FEATURES**

### **Navigation**

#### **Desktop Navigation**
- The navigation bar is located at the top of each page on the site.
- The menu contains links for the 'Home Page' (which is also linked via the Brand Logo), the 'Add Hack', 'Hacks', 'Team' page links, along with 'Login' and 'Register' links. 
- Once the user is logged in the menu the 'Register' link is replaced with the 'Logout' page link.
- The navbar is fully responsive and collapses into a burger menu for mobile devices.

![Desktop Nav](/static/docs/navbar.jpg)

#### **Mobile Navigation**
- Presented as a burger menu for design responsiveness.
- Once clicked a dropdown menu appears including all the page links as above.

![Mobile Nav](/static/docs/nav-mob.jpg)

![Mobile Nav Expanded](/static/docs/nav-mob-expanded.jpg)

<hr>

### **Footer**
- Located at the bottom of the page the footer loads text with todays date and a random happy thought.

![Footer](/static/docs/footer.jpg)

<hr>

### **Home Page**
- Upon landing on the homepage the user is presented with the title 'Happy Hacks Generator'.
- Below the title, a message instructs the user to press the button to 'generate happiness'.
- When the button is pressed, a random post (hack) is displayed to the user.
- A button at the left, illustrated with a music note, will play a happy song.
- A button at the right, illustrated with a '+' sign, will take the user to the 'Add Hack' page.

![Home Page](/static/docs/home.jpg)

![Home Page Hack](/static/docs/home-hack.jpg)

<hr>

### **Add Hack Page**
- The Add Event page is essentially a form to complete.
- If the user is not logged in, they will be redirected to login.
- The user can type their 'happy hack' and pick an emoji to illustrate the hack.
- A sound will be played when the user successfully submits a post, along with a happy animation.

![Add Event](/static/docs/add-hack.jpg)

![Add Emoji](/static/docs/add-emoji.jpg)

<hr>

### **Hacks Page**
- The Hacks page displays all the hacks in the order they were last created.
- User can type in the search box or select an emoji to filter posts so they can find suggestions that interest them.

![Hacks Page](/static/docs/hacks.jpg)

<hr>

### **Team Page**
- The team page displays cards for each member.
- Team member main roles in the project are provided.
- Each member has a space to record their own 'Happy Hack'.
- Links are provided for team members' Github and LinkedIn profiles.

![Team Page](/static/docs/team.jpg)

<hr>

### **CRUD Functionality**
- The edit and delete hack page can be accessed via the Hacks page.
- Hacks which the logged in user has created show a button which reveals an 'edit' or 'delete' link.

![CRUD Links](/static/docs/crud.jpg)

<hr>

### **Love Hacks**
- Logged in users can 'love' a hack by pressing the heart symbol displayed on the hack.
- A number displays the number of 'loves' for each hack.

<hr>

## **TESTING**

- Testing and results can be found [here](TESTING.md)
- Manual tests were carried out throughout the process.
- Responsiveness has been checked and adjusted in Chrome Dev Tools and the site has been viewed on mobiles and an mac without issues.

<hr>

## **Bugs**

* Issue - Error when signing up
* Cause - Caused by entering email address
* Resolution - Email address not required, so removed.

<hr>

## **Technologies Used**
* DJANGO
* HTML
* CSS
* Bootstrap
* Javascript
* EmojiMart

<hr>

## **Credits**

- The background image was sourced from [Daniel Space on Pexels](https://www.pexels.com/photo/shallow-focus-photography-of-yellow-flowers-1028542/)

## **The Team**

- The team worked incredibly well and managed to overcome the different time demands, supported junior member with conflict issues and got stuck into the code.
- All members were encouraged to get involved in some way and gain experience in Hackathons and agile practices.
- Regular meetings were held on slack, often to assist others in overcoming problems.