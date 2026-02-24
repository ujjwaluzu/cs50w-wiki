# Wiki

## 📘 Project Description
[screencast](https://youtu.be/hnYdDZRMS50?si=FAiwGwBMiWvpxc_5)
---
Wiki is a web-based encyclopedia application built as part of **CS50’s Web Programming with Python and JavaScript (CS50W)**. The project allows users to view, search, create, edit, and explore encyclopedia entries written in **Markdown**, which are dynamically converted into **HTML** for display.

The application is designed to mimic the core functionality of Wikipedia while focusing on server-side logic using **Django**, template rendering, and user interaction through forms and URL routing.

---

## 🎯 Project Objectives

The primary goals of this project are to:

- Understand Django’s URL routing, views, and templates  
- Work with server-side form handling  
- Store and retrieve content from the filesystem  
- Implement search and redirect logic  
- Convert Markdown content to HTML  
- Handle errors and edge cases gracefully  

---

## 🚀 Features

- View encyclopedia entries via unique URLs  
- Clickable index of all available entries  
- Search functionality with exact and partial match support  
- Create new encyclopedia entries using Markdown  
- Edit existing entries with pre-filled content  
- Visit a randomly selected encyclopedia entry  
- Automatic Markdown-to-HTML conversion  

---

## 🛠️ Technologies Used

- Python  
- Django  
- HTML & CSS  
- Markdown  
- markdown2 (for Markdown to HTML conversion)  

---

## 📂 Project Structure

- `entries/` – Stores encyclopedia entries as Markdown files  
- `templates/` – Contains HTML templates  
- `views.py` – Handles application logic  
- `urls.py` – Manages URL routing  
- `util.py` – Helper functions for reading and writing entries  


# CS50W Wiki Project – Requirements

## Entry Page
- Visiting `/wiki/TITLE`, where `TITLE` is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry.
- The view should retrieve the content of the encyclopedia entry by calling the appropriate utility function.
- If an entry is requested that does not exist:
  - The user should be presented with an error page indicating that the requested page was not found.
- If the entry exists:
  - The page should display the content of the entry.
  - The title of the page should include the name of the entry.

---

## Index Page
- Update `index.html` so that instead of merely listing the names of all encyclopedia entries:
  - Each entry name is clickable.
  - Clicking an entry name takes the user directly to that entry’s page.

---

## Search
- Allow the user to type a query into the search box in the sidebar.
- If the query matches **exactly** the name of an encyclopedia entry:
  - Redirect the user directly to that entry’s page.
- If the query does **not** match exactly:
  - Display a search results page showing all encyclopedia entries that contain the query as a substring.
  - **Example:** If the search query is `ytho`, then `Python` should appear in the results.
- Clicking any entry name in the search results should take the user to that entry’s page.

---

## New Page
- Clicking **“Create New Page”** in the sidebar should take the user to a page for creating a new encyclopedia entry.
- The user should be able to:
  - Enter a title for the page.
  - Enter Markdown content in a textarea.
- The user should be able to click a button to save the new page.
- When saving:
  - If an encyclopedia entry with the same title already exists, display an error message.
  - Otherwise:
    - Save the entry to disk.
    - Redirect the user to the newly created entry’s page.

---

## Edit Page
- On each entry page, the user should be able to click a link to edit the entry.
- The edit page should:
  - Display a textarea pre-populated with the existing Markdown content.
- The user should be able to save their changes.
- After saving:
  - Redirect the user back to the entry’s page.

---

## Random Page
- Clicking **“Random Page”** in the sidebar should redirect the user to a random encyclopedia entry.

---

## Markdown to HTML Conversion
- On each entry page:
  - Convert Markdown content to HTML before displaying it.
- You may use the `markdown` Python package for conversion.
- Install using:
  ```bash
  pip3 install markdown
