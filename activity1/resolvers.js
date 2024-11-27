const Books =

[

  { "id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "publishedYear": 1960 },

  { "id": 2, "title": "1984", "author": "George Orwell", "publishedYear": 1949 },

  { "id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "publishedYear": 1925 }

];

const Members =

[

  { "id": 1, "name": "Alice", "email": "alice@example.com", "membershipType": "Premium" },

  { "id": 2, "name": "Bob", "email": "bob@example.com", "membershipType": "Basic" }

];


const resolvers = {
    Query: {
        books: () => Books,
        members: () => Members,
        book: (_, { id }) => Books.find(book => book.id === Number(id)),
        member: (_, { id }) => Members.find(member => member.id === Number(id)),
        booksPublishedBefore1950: () => Books.filter(book => book.publishedYear < 1950),
        premiumMembers: () => Members.filter(member => member.membershipType === "Premium"),
        BookDetails: () => Books.map(book => `${book.title} by ${book.author}`)
    
    },

    Mutation: {
        addBook: (_, { title, author, publishedYear }) => {
            const newBook = { id: Books.length + 1, title, author, publishedYear };
            Books.push(newBook);
            return newBook;
        },
        addMember: (_, { name, email, membershipType }) => {
            const newMember = { id: Members.length + 1, name, email, membershipType };
            Members.push(newMember);
            return newMember;
        },
        updateMembership: (_, { id, membershipType }) => {
            const member = Members.find(member => member.id === Number(id));
            if (member) {
                member.membershipType = membershipType;
                return member;
            }
            return null;
    }
  }
};
module.exports = resolvers;

