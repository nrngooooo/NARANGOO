from django.shortcuts import render,redirect
import xml.etree.ElementTree as ET
# from .models import Book, Category
# from xml.dom import minidom
# from .forms import BookForm, CategoryForm


def book_info(request):
    # Parse the XML file
    tree = ET.parse('books.xml')
    root = tree.getroot()

    # Create a list of dictionaries with the book information
    books = []
    for book in root.findall('book'):
        title = book.find('title').text
        author = book.find('author').text
        genre = book.find('genre').text
        year = book.find('year').text
        books.append({'title': title, 'author': author,
                     'genre': genre, 'year': year})

    # Pass the book information to the template
    context = {'books': books}
    return render(request, 'bookinfo/book_info.html', context)
# def category_add(request):
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('category_list')
#     else:
#         form = CategoryForm()
#     return render(request, 'category_add.html', {'form': form})
# def add_book(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             book = form.save()
#             book_element = ET.Element('book')
#             book_title = ET.SubElement(book_element, 'title')
#             book_title.text = book.title
#             book_author = ET.SubElement(book_element, 'author')
#             book_author.text = book.author
#             book_genre = ET.SubElement(book_element, 'category')
#             book_genre.text = book.category
#             book_year = ET.SubElement(book_element, 'year')
#             book_year.text = str(book.year)
#             # Parse the existing XML file
#             tree = ET.parse('books.xml')
#             root = tree.getroot()
#             # Add the new book element to the XML file
#             root.append(book_element)
#             # Write the updated XML file to disk
#             xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")
#             with open('books.xml', 'w') as f:
#                 f.write(xml_str)
#             # Redirect to the book info page
#             return redirect('book_info')
#     else:
#         form = BookForm()
#     return render(request, 'add_book.html', {'form': form})
