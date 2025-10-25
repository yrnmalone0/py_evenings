import mysql.connector

##Database Connection Details
my_db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "P@ssw0rd$$",
    database = "library_db"
)

mycursor = my_db.cursor()

##Create a Library DB
#mycursor.execute("CREATE DATABASE library_db")

#Create Book Table if it doesn't exist
mycursor.execute("""
CREATE TABLE IF NOT EXISTS Books(
    id INT  AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    ISBN VARCHAR(255)
)
""")

#print("Books Table created successfully..")

##Implement a function that takes book details (title, author, ISBN) as input and inserts a new record into the books table using an INSERT query.
def add_book(title, author, ISBN):
    sql = "INSERT INTO Books (title, author, ISBN) VALUES (%s, %s, %s)"
    val = (title, author, ISBN)
    mycursor.execute(sql, val)
    my_db.commit()
    print(f"Book '{title}' added successfully.")

# Usage
# add_book("Mockingbird", "Harper Lee", "978-006-112008-4")
# add_book("1984", "George Orwell", "978-045-152493-5")


def search_books_by_title(title):
    sql = "SELECT * FROM Books WHERE title = %s"
    val = (title,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    for result in myresult:
        return result

# Usage
search_results = search_books_by_title("1984")
print("Search Results:", search_results)


def list_all_books():
    sql = "SELECT * FROM Books"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    
    for result in myresult:
        print(result)

# Usage
list_all_books()


def delete_book(id):
    sql = "DELETE FROM Books WHERE id = %s"
    val = (id,)
    mycursor.execute(sql, val)
    my_db.commit()
    
    print(mycursor.rowcount, "record(s) deleted")

# Usage
delete_book(3)

#close the database connection
mycursor.close()
my_db.close()

print("Database connection closed.")