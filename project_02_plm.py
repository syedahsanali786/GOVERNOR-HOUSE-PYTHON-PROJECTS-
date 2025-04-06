import streamlit as st

st.title("Personal Library Manager")

# Initialize session state
books = st.session_state.setdefault("books", [])

# Add book
new_book = st.text_input("Enter book name:")
if st.button("Add Book") and new_book:
    books.append(new_book)
    st.success(f'"{new_book}" added!')

# Show books
if books:
    st.subheader("Your Books:")
    st.write("\n".join(f"- {book}" for book in books))

    # Remove book
    remove_book = st.selectbox("Remove a book:", ["None"] + books)
    if st.button("Remove") and remove_book != "None":
        books.remove(remove_book)
        st.success(f'"{remove_book}" removed!')
else:
    st.write("No books in your library yet.")
