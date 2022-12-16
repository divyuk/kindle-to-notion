# kindle-to-notion
Pulls out the highlights from the MyClippings.txt and puts in Notion Database.

# Description
MyClippings.txt has a pattern for highlights and notes marked while reading the book. The Script extracts these pattern and sync the data into notion table with the book name author. It creates a new page for different books. Also it takes care of the duplicate data.

# Example
Atomic Habits (Unknown)
\- Your Highlight on Location 93-94 | Added on Wednesday, November 3, 2021 2:38:36 PM

changes that seem small and unimportant at first will compound into remarkable results if you’re willing to stick with them for years.

==========

==========

The 5 AM club (Unknown)

\- Your Highlight on Location 78-79 | Added on Thursday, August 18, 2022 7:12:13 PM

I need to tell you that too many among us die at thirty and are buried at eighty.

==========

## Put in the notion table
<p align="center">
  <img src="assets\1.jpg" />
</p>
<p align="center">
  <img src="assets\2.jpg" />
</p>

# How to run?
 1. Set up Notion
    1. Duplicate this template to your notion account
        1. Note: feel free to add properties to this database, but the “Type”, "Name", "Source" and “Author” properties shouldn’t be renamed.
    2. Save the database id somewhere
        1. Copy the url for your database.
        2. The database id is this sequence of letters and numbers 
        3. Copy and save this somewhere
    3. Create an integration
        1. Go to [https://www.notion.com/my-integrations](https://www.notion.com/my-integrations).
        2. Click the "+ New integration" button.
        3. Give your integration a name - e.g. "Kindle Syncer".
        4. Select the workspace where you want to install this integration.
        5. Select the capabilities that your integration will have (select them all).
        6. Click "Submit" to create the integration.
        7. Copy the "Internal Integration Token" on the next page and save it somewhere secure, e.g. a password manager.             
    4. Now go back to the kindle database, click "Add Connection" and then connect your integration.

2. Create env file with database_ID and secret_Key and paste the the ID and secret_key which we saved earlier.

3. Connect your Kindle through USB.

4. Copy the My Clippings.txt into src.

5. Run the main Script.