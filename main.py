# Our code is going to go in here.

# # This file has been linked to the html file.

# function listLonger() {
#   let newLi = document.createElement('li');
#   newLi.innerHTML = "This was made in JS.";

#   document
#     .querySelector('ul')
#     .appendChild(newLi);
# }

# # This array represents a cyberpunk library.
# books = [
#     # This object represents a book.
#     {
#       title: "Neuromancer",
#       author: "William Gibson",
#       year_published: 1984,
#       isbn: "",
#       rating: 100
#     },
#     {
#       title: "Snow Crash",
#       author: "Neal Stephenson",
#       year_published: 1992,
#       isbn: "978-01336162-0",
#       rating: 100
#     },
#     {
#       title: "Altered Carbon",
#       author: "Richard K. Morgan",
#       year_published: 2002,
#       isbn: "",
#       rating: 100
#     }
#   ];
  
#   # This is an arrow function.
#   const bookFormatter = (book) => {
#     return `Title: ${book.title}, Author: ${book.author}`;
#   }
  
#   # This is just a plain function.
#   function bookYearFormatter(book) {
#     return `Year: ${book.year_published}`;
#   }
  
#   # --------------------------------------
  
#   # This is a for of loop.
#   for (book of books) {
#     # Javascript string formatting.
#     # console.log(bookFormatter(book));
#     # console.log(bookYearFormatter(book));
  
#     # String formatting
#     console.log(`
#       <div>
#         <h1>${book.title}</h1>
#         <h2>${book.author}</h2>
#       </div>
#     `);
  
#     # String concatenation
#     console.log(
#       '<div><h1>'
#         + book.title
#         + '</h1><h2>'
#         + book.author
#         + '</h2></div>'
#     );
#   }
  
#   # let string_a = "This is the beggining of the ";
#   # let string_b = "sentence that this is the end of."
  
#   # console.log(string_a);
#   # console.log(string_b);
#   # console.log(string_a + string_b);


# window.onload = function() {
#   # let today = "This was updated by script.js.";
#   # document.querySelector('p').innerHTML = today;

#   let someString = "This is a string.";
#   # document.querySelector('p').innerHTML = someString;

#   let someNumber = 1337;
#   # document.querySelector('p').innerHTML = someNumber;

#   let someBoolean = false;
#   # document.querySelector('p').innerHTML = (
#   #   1337 === "1337"
#   # );

#   #              | 0    1    2    3    4 |
#   let someArray = ["a", "b", "c", "d", "e"];
#   # document.querySelector('p').innerHTML = someArray[0];
#   # document.querySelector('li').innerHTML = someArray[4];

#   let someObject = {
#     someKey: "some value",
#     anotherKey: false,
#     aThirdKey: 9001,
#     noKey: null
#   };

#   # document.querySelector('p').innerHTML = someObject.anotherKey;

#   let someUndefined;
#   # document.querySelector('p').innerHTML = someUndefined;

#   let someNull = null;
#   # document.querySelector('p').innerHTML = someNull;

#   document
#     .getElementById("listLonger").onclick = listLonger;
# }

# This array represents a cyberpunk library.
# books = [
#   # This object represents a book.
#   {
#     title: "Neuromancer",
#     author: "William Gibson",
#     year_published: 1984,
#     isbn: "",
#     rating: 90,
#     is_checked_out: false,
#   },
#   {
#     title: "Snow Crash",
#     author: "Neal Stephenson",
#     year_published: 1992,
#     isbn: "978-01336162-0",
#     rating: 95,
#     is_checked_out: true,
#   },
#   {
#     title: "Altered Carbon",
#     author: "Richard K. Morgan",
#     year_published: 2002,
#     isbn: "",
#     rating: 100,
#     is_checked_out: false,
#   },
#   {
#     title: "Cryptonomicon",
#     author: "Neal Stephenson",
#     year_published: 1999,
#     isbn: "978-0-380-78862-0",
#     rating: 85,
#     is_checked_out: false,
#   }
# ];

# let lipsum = `Lorem ipsum dolor sit amet, consectetur adipiscing elit.
# Etiam consequat dapibus mauris ut accumsan.
# Integer suscipit metus justo, eget pharetra urna eleifend ut.
# Nam eu ultrices diam. Aenean bibendum tortor sed ligula vestibulum, eu iaculis neque euismod.
# Vivamus aliquet mauris sit amet tortor scelerisque cursus.
# Nunc pretium feugiat posuere.
# Curabitur congue ligula quis luctus laoreet.
# Praesent suscipit tempor ante nec fringilla.`;

# # String splitting
# # for (word of lipsum.split("\n")) {
# #   console.log(word.toUpperCase());
# # }

# # For loop on an array.
# # for (let iterator = 0; iterator < books.length; iterator++) {
# #   console.log(iterator, books[iterator]);
# # }

# # For loop on a string.
# # for (let i = 0; i < lipsum.length; i++) {
# #   console.log(lipsum[i]);
# # }

# # for ... in
# # for (idx in books) {
# #   console.log(idx);
# #   console.log(books[idx]);
# # }

# # for ... of
# # for (book of books) {
# #   console.log(book);
# # }

# # For Each
# # books.forEach(book => {
# #   console.log(book);
# # });

# # Map
# # console.log(books);
# # let new_books = books.map(book => {
# #   let new_book = book;
# #   book.is_checked_out = true;
# #   return new_book;
# # });
# # console.log(new_books);

# # let new_books = books;
# # console.log(books);
# # for (idx in new_books) {
# #   new_books[idx].is_checked_out = true;
# # }
# # console.log(new_books);

# # let i = 1;
# # while (i < 2**16) {
# #   console.log(i);
# #   i = i*2;
# # }

# # Filter
# # let booksInLibrary = books.filter(book => {
# #   return !book.is_checked_out;
# # });

# # function sortingFunction(a, b) {
# #   return a.rating - b.rating;
# # }

# # Sort
# # books.sort((a, b) => {
# #   # a > b if a - b > 0
# #   # a < b if a - b < 0
# #   # a = b if a - b = 0
# #   # return b.year_published - a.year_published;

# #   # Sorting by title based on alphabetical order.
# #   let a_upper = a.title.toUpperCase();
# #   let b_upper = b.title.toUpperCase();

# #   if (a_upper < b_upper) {
# #     return -1;
# #   } else if (a_upper > b_upper) {
# #     return 1
# #   } else {
# #     return 0;
# #   }
# # });

# # console.log(books);
# # console.log(booksInLibrary);

# # # Dense data structure
# # let grid = [
# #   [1,0,2],
# #   [0,1,2],
# #   [0,0,1]
# # ]

# # # Sparse data structure
# # let boardState = {
# #   x_moves: [0,4,8],
# #   o_moves: [2,5]
# # }

# # Push: Adds items to an array
# # console.log(books);
# # books.push({
# #   title: "Cryptonomicon",
# #   author: "Neal Stephenson",
# #   year_published: 1999,
# #   isbn: "978-0-380-78862-0",
# #   rating: 100,
# #   is_checked_out: false,
# # });
# # console.log(books);

# # Pop: removes and item from an array.
# # console.log(books);
# # console.log(books.pop());
# # console.log(books);
