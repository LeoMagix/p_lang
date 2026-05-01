# Documentation for album.py
---
Program asks user for their favorite album;artiste, album name, number of songs on album. It checks if album is stored in the database (at this point, a simple dictonary), if it is the provided information is then displayed in a neat format with the name of the artiste, album name and number of songs each displayed on a new line. Otherwise, if the album is not in the database display a message to the user that says the requested album has not being added to the catalogue yet.
Now, an additional suggested feature is to after the user has provided the required data display in a neat format all the songs of the album with their corresponding playtime.
We would save our catalogue of artistes, albums and songs in a module **Catalogue** which will be imported anytime there's need to verify if a users album request is part of our catalogue. The function to prompt and receive the user's request-script to work on and process the user data-is in *album.py*.
