# NEBULA
Teck stack=angular,flask,other
Understand the project requirements.

1. User Registration and Authentication:
   - Allow users to sign up with their email or social media accounts.
   - Implement a secure authentication system to manage user logins.

2. User Profiles:
   - Enable users to create and manage their profiles.
   - Allow users to upload profile pictures and add personal information.

3. Property Listings:
   - Enable hosts to create property listings with detailed descriptions and images.
   - Implement a search functionality to allow users to find properties based on location, dates, price range, and other filters.

4. Booking and Reservations:
   - Allow users to book properties by selecting check-in and check-out dates.
   - Implement a booking system to manage availability and prevent double bookings.
   - Integrate a payment gateway to handle transactions securely.

5. Reviews and Ratings:
   - Allow guests to leave reviews and ratings for the properties they have stayed in.
   - Display reviews and ratings on property listings to help users make informed decisions.

6. Messaging System:
   - Implement a messaging system to facilitate communication between hosts and guests.
   - Enable users to exchange messages about booking inquiries, property details, and other relevant information.

7. Notifications:
   - Set up email or in-app notifications to keep users informed about booking confirmations, messages, and other important events.

8. Host Verification and Safety Features:
   - Implement a host verification process to ensure the legitimacy of property listings.
   - Include safety features and guidelines for hosts and guests to follow.

9. Admin Panel:
   - Create an admin panel to manage user accounts, property listings, and reported content.
   - Allow administrators to moderate reviews and address any issues that may arise.


Pages:

Sure, let's describe the functionality of each page step-by-step:

1. **Homepage:**
   - The homepage serves as the main entry point for users visiting the platform.
   - It typically includes a search bar, allowing users to enter their destination, check-in and check-out dates, and the number of guests for their trip.
   - The homepage may have a hero section with an attractive background image or video related to travel, along with a catchy tagline or call-to-action (CTA) to encourage users to start searching for properties.
   - Featured destinations or properties may be displayed on the homepage to showcase popular or unique listings, enticing users to explore further.
   - Links to essential sections, such as "Host Your Space," "Help," and "Sign In" are usually included in the header for easy navigation.

2. **Search Results Page:**
Add price filter
   - After users enter their search criteria on the homepage and click the "Search" button, they are redirected to the search results page.
   - The page displays a list of properties that match the user's search parameters, including images, brief descriptions, and pricing information.
   - Users can further filter the search results by various criteria like property type, price range, amenities, and more.
   - Each property listing is typically clickable, leading to the individual property listing page with detailed information.

3. **Property Listing Page:**
   - The property listing page provides comprehensive details about a specific accommodation that the user is interested in.
   - It includes high-quality images, a detailed description of the property, the host's profile and reviews, available amenities, and any specific rules or policies.
   - Users can check the availability of the property for their desired dates and proceed with the booking process from this page.

4. **User Profile Page:**
   - The user profile page allows users to view and manage their personal information and settings.
   - Users can edit their profile information, add or update their profile picture, and view their booking history and reviews received as a guest.

5. **Host Dashboard:**
   - The host dashboard is a dedicated area where hosts can manage their property listings, reservations, and interactions with guests.
   - Hosts can create new property listings, edit existing ones, set pricing, and manage property availability.
   - The dashboard may also include messaging functionality for hosts to communicate with guests about inquiries and bookings.

6. **Booking and Reservation Page:**
   - The booking and reservation page appears when a user decides to book a specific property.
   - Users can select their check-in and check-out dates and view the total cost of their stay.
   - They can proceed with the booking by entering their payment details and confirming the reservation.

7. **Messaging System:**
   - The messaging system enables communication between hosts and guests.
   - Hosts and guests can exchange messages about property details, inquiries, and other relevant information through an in-app messaging interface.

8. **Admin Panel:**
   - The admin panel is accessible only to administrators and allows them to manage the platform's operations.
   - Administrators can oversee user accounts, property listings, reported content, and resolve any issues or disputes that may arise.

9. **Login and Registration Pages:**
   - The login page allows users to sign in to their existing accounts using their registered email address or social media accounts.
   - The registration page allows new users to sign up for the platform by creating an account with their email or social media credentials.

10. **About Us Page:**
    - The about us page provides information about the platform's background, mission, and values, giving users insight into the company's story and purpose.

11. **Help or Support Page:**
    - The help or support page offers users access to FAQs, support resources, and contact information to seek assistance when needed.

12. **Terms of Service and Privacy Policy Pages:**
    - These pages outline the terms and conditions governing the use of the platform and the privacy policy that governs the handling of user data. They inform users about their rights and responsibilities while using the service.

Remember that while these descriptions cover the primary functionalities of each page, the actual implementation and design can be customized to suit your platform's specific requirements and branding. Additionally, the development process involves careful consideration of user experience, security measures, and compliance with relevant legal regulations.




Create an Entity Relationship (ER) diagram to visualize the relationship between entities:

**Entities:**

1. User:
   - Attributes: UserID (Primary Key), FirstName, LastName, Email, Password, ProfilePicture, SocialMediaAccounts, ...

2. Property:
   - Attributes: PropertyID (Primary Key), HostID (Foreign Key), Title, Description, PropertyType, Location, Bedrooms, Bathrooms, Amenities, ...

3. Booking:
   - Attributes: BookingID (Primary Key), PropertyID (Foreign Key), GuestID (Foreign Key), CheckInDate, CheckOutDate, TotalPrice, ...

4. Review:
   - Attributes: ReviewID (Primary Key), PropertyID (Foreign Key), GuestID (Foreign Key), Rating, Comment, ...

5. Message:
   - Attributes: MessageID (Primary Key), SenderID (Foreign Key), ReceiverID (Foreign Key), Content, Timestamp, ...

**Relationships:**

1. User-Property (Hosted By):
   - Many-to-One relationship from User to Property (One user can host multiple properties).
   - Foreign Key: HostID in the Property entity referencing UserID in the User entity.

2. User-Booking (Guest of):
   - One-to-Many relationship from User to Booking (One user can have multiple bookings).
   - Foreign Key: GuestID in the Booking entity referencing UserID in the User entity.

3. Property-Booking (Booked):
   - One-to-Many relationship from Property to Booking (One property can have multiple bookings).
   - Foreign Key: PropertyID in the Booking entity referencing PropertyID in the Property entity.

4. Property-Review (Has Reviews):
   - One-to-Many relationship from Property to Review (One property can have multiple reviews).
   - Foreign Key: PropertyID in the Review entity referencing PropertyID in the Property entity.

5. User-Message (Sent/Received):
   - Many-to-Many relationship between User and Message (A user can send/receive multiple messages).
   - The association between the User and Message entities will be represented by an associative entity.



                                                     +--------------+
                                               |   Homepage   |
                                                     +--------------+
                                                    |
                                                    v
+---------------------+                                         +-------------------+
| Search Results Page+Filter | <-----> | Property Listing  +map
+---------------------+                     /                       +-------------------+
                                             /
                                          v
                                  +---------+
                                 | Booking |Product     —------->         +-------------------+
                                   +---------+                                | Filtering & Map   |
                                   /                                                    +-------------------+
                                 /
                               v
                       +------------------+
                       | User Profile     |
                       |    Page          |
                       +------------------+
                          |
                          v
                  +---------------+
                  | Host Dashboard|
                  +---------------+
                      |
                      v
                +-------------+
                | Messaging   |
                |  System     |
                +-------------+
           

Api planning
### API Endpoints

| #   | Functionality                                    | HTTP Method | Route                                 | Description                                                                                                        |
| --- | ------------------------------------------------ | ----------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| 1   | Authentication and User Management              | POST        | /api/signup                           | Create a new user account.                                                                                         |
|     |                                                  | POST        | /api/login                            | Authenticate a user and generate an access token.                                                                   |
|     |                                                  | GET         | /api/user/profile                    | Fetch the user's profile information.                                                                              |
|     |                                                  | PUT         | /api/user/profile                    | Update the user's profile information.                                                                              |
| 2   | Property Listing                                 | POST        | /api/property                         | Create a new property listing.                                                                                      |
|     |                                                  | GET         | /api/property/:propertyId             | Get detailed information about a specific property.                                                                 |
|     |                                                  | GET         | /api/properties                       | Fetch a list of properties based on search criteria and filters.                                                   |
|     |                                                  | PUT         | /api/property/:propertyId             | Update the information of a property.                                                                               |
|     |                                                  | DELETE      | /api/property/:propertyId             | Delete a property listing.                                                                                          |
|     | a. Search Properties by Location, Dates, Filters | GET         | /api/properties/search                | Allows users to search for available properties based on various criteria and filters.                             |
|     | b. Sort Properties by Price, Ratings, Criteria   | GET         | /api/properties/sort                  | Enables users to sort properties based on price, ratings, or other criteria.                                        |
|     | c. Get Bookings by User and Property             | GET         | /api/bookings/user/:userId            | Fetch all bookings made by a specific user.                                                                         |
|     |                                                  | GET         | /api/bookings/property/:propertyId    | Fetch all bookings for a specific property.                                                                         |
|     | d. Filter Bookings by Dates and Status           | GET         | /api/bookings/filter                  | Allows users to filter their bookings based on check-in/out dates and booking status.                              |
|     | e. Get Reviews by Property                       | GET         | /api/reviews/property/:propertyId     | Fetch all reviews for a specific property.                                                                          |
|     | f. Sort Reviews by Ratings or Date               | GET         | /api/reviews/sort                     | Enables users to sort reviews based on ratings or the date they were submitted.                                    |
| 3   | Booking and Reservations                         | POST        | /api/booking/:propertyId              | Create a new booking for a specific property.                                                                       |
|     |                                                  | GET         | /api/booking/:bookingId               | Get details about a specific booking.                                                                               |
|     |                                                  | GET         | /api/bookings/user                    | Fetch all bookings made by the currently logged-in user.                                                            |
|     |                                                  | GET         | /api/bookings/host                    | Fetch all bookings for properties hosted by the currently logged-in host.                                           |
|     |                                                  | PUT         | /api/booking/:bookingId               | Update booking details (e.g., check-in/out dates).                                                                  |
|     |                                                  | DELETE      | /api/booking/:bookingId               | Cancel a booking.                                                                                                   |
| 4   | Reviews and Ratings                              | POST        | /api/review/:propertyId               | Create a new review for a specific property.                                                                        |
|     |                                                  | GET         | /api/review/:reviewId                 | Get details about a specific review.                                                                                |
|     |                                                  | GET         | /api/reviews/property/:propertyId     | Fetch all reviews for a specific property.                                                                          |
| 5   | Messaging System                                 | POST        | /api/message/:receiverId              | Send a new message to a specific user (receiver).                                                                   |
|     |                                                  | GET         | /api/messages/:userId                 | Fetch all messages for the currently logged-in user.                                                                |
|     |                                                  | GET         | /api/messages/:userId/:otherUserId    | Fetch all messages exchanged between two users.                                                                     |
| 6   | Admin Panel (Administrator Access Only)          | GET         | /api/admin/users                      | Fetch a list of all users.                                                                                         |
|     |                                                  | GET         | /api/admin/properties                 | Fetch a list of all property listings.                                                                              |
|     |                                                  | GET         | /api/admin/bookings                   | Fetch a list of all bookings.                                                                                       |
|     |                                                  | PUT         | /api/admin/user/:userId               | Update user information or privileges (e.g., host verification).                                                    |
|     |                                                  | DELETE      | /api/admin/user/:userId               | Delete a user account (if necessary).                                                                               |
|     |                                                  | DELETE      | /api/admin/property/:propertyId       | Delete a property listing (if necessary).                                                                           |
| 7   | Additional Pages                                | -           | -                                    | These pages may contain static content displayed directly on the frontend and might not require specific routes.   |












