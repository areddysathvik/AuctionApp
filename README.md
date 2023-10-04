# Auction App

This Django application allows users to participate in auctions, place bids, and manage their profiles. The application also includes an admin section for managing auction items and user authentication.

# Features Implemented

- User CRUD operations.
- Admin features and secret key (login credentials).
- Admin can add auction items and edit them.
- Bids are shown to every user.
- Token-based login (default: 100 tokens).
- Users can bid on auction items.
- The highest bidder wins at the end time of the respective auction.

### Prerequisites

- Docker installed on your machine.

### Building and Running

1. Clone the repository to your local machine:

       git clone https://github.com/areddysathvik/AuctionApp.git

2.Navigate to the project directory:

    cd AuctionAPP

3.Build the Docker container:
    
    docker build -t my-django-app .

4.Run the Docker container:

    docker run -p 8000:8000 my-django-app

5.Access the application in your web browser at 
    
    http://127.0.0.1:8000/signup

Admin Section

To access the admin section, follow these steps:

Open your code editor or terminal and navigate to the project directory:


    cd AuctionAPP

Create a superuser with admin privileges:

    python manage.py createsuperuser

You will be prompted to enter a username, email, and password for the admin user.

Start the Django development server:

    python manage.py runserver

Access the admin panel at 
     
    http://127.0.0.1:8000/admin/ and log in with the superuser credentials you just created.

# steps of working

1.signup and create an account

    http://127.0.0.1:8000/signup

2.signin 

    http://127.0.0.1:8000/signin


# Internal Working
- Two Apps
- one for auctionapp itself and
- another for all users and contents management (userSignUp) 
