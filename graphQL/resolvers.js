// const mockUsers = [
//     { id: 1, name: "Alice", email: "alice@example.com"},
//     { id: 2, name: "Bob", email: "bob@example.com"},
// ];

// const resolvers = {
//     Query: {
//         user: (_, {id}) => mockUsers.find(user => user.id === Number(id))
//         }
//     };

// module.exports = resolvers;

// jwt token 
// const jwt = require("jsonwebtoken");

// const users = [

//   { id: 1, email: "alice@example.com", password: "password123", role: "USER" },

//   { id: 2, email: "admin@example.com", password: "admin123", role: "ADMIN" },

// ];
// const Books = [
    
// ]

// const SECRET_KEY = "mysecretkey";
// const resolvers = {
//   Query: {
//     secretData: (_, __, { token }) => {
//       if (!token) {
//         throw new Error("Authentication required: Token not found");
//       }
//       try {
//         const user = jwt.verify(token, SECRET_KEY);
//         return `Welcome! Your role is ${user.role}`;
//       } catch (err) {
//         if (err.name === "TokenExpiredError") {
//           throw new Error("Authentication failed: Token has expired");
//         } else if (err.name === "JsonWebTokenError") {
//           throw new Error("Authentication failed: Invalid token");
//         }
//         throw new Error("Authentication failed: Unknown error");
//       }
//     },
//   },

//   Mutation: {

//     // Login mutation to authenticate the user and return a JWT token

//     login: (_, { email, password }) => {

//       // Find user by email and password

//       const user = users.find(

//         (user) => user.email === email && user.password === password

//       );

//       if (!user) {

//         throw new Error("Invalid credentials");

//       }

//       // Generate JWT token

//       const token = jwt.sign({ id: user.id, role: user.role }, SECRET_KEY, {

//         expiresIn: "1h",

//       });

//       return token;

//     },

//   },

// };

// module.exports = resolvers;

const jwt = require("jsonwebtoken");

const users = [
    { id: 1, email: "alice@example.com", password: "password123", role: "USER" },
    { id: 2, email: "admin@example.com", password: "admin123", role: "ADMIN" },
];

const Movies = [
    { id: 1, title: "Inception", director: "Christopher Nolan", releaseYear: 2010 },
    { id: 2, title: "The Dark Knight", director: "Christopher Nolan", releaseYear: 2008 },
    { id: 3, title: "Interstellar", director: "Christopher Nolan", releaseYear: 2014 },
    { id: 4, title: "Titanic", director: "James Cameron", releaseYear: 1997 },
    { id: 5, title: "Avatar", director: "James Cameron", releaseYear: 2009 }
];

const Reviews = [
    { id: 1, movieId: 1, rating: 4.8, reviewer: "Alice" },
    { id: 2, movieId: 2, rating: 4.9, reviewer: "Bob" },
    { id: 3, movieId: 3, rating: 4.7, reviewer: "Charlie" },
    { id: 4, movieId: 4, rating: 4.5, reviewer: "Alice" },
    { id: 5, movieId: 5, rating: 4.6, reviewer: "Bob" }
];

const resolvers = {
    Query: {
        secretData: () => {
            return "This is secret data";
        },
        movies: () => Movies,
        movie: (_, { id }) => Movies.find(movie => movie.id === Number(id)),
        reviews: () => Reviews,
    },
    Mutation: {
        login: (_, { email, password }) => {
            const user = users.find(user => user.email === email && user.password === password);
            if (!user) {
                throw new Error("Invalid credentials");
            }
            return jwt.sign({ userId: user.id, role: user.role }, "your_secret_key");
        },
        addMovie: (_, { title, director, releaseYear }, context) => {
            if (context.role !== "ADMIN") {
                throw new Error("Not authorized, only admin can add movies");
            }
            const newMovie = { id: Movies.length + 1, title, director, releaseYear };
            Movies.push(newMovie);
            return newMovie;
        },
        updateMovie: (_, { id, title, director, releaseYear }, context) => {
            if (context.role !== "ADMIN") {
                throw new Error("Not authorized");
            }
            const movie = Movies.find(movie => movie.id === Number(id));
            if (!movie) {
                throw new Error("Movie not found");
            }
            if (title) movie.title = title;
            if (director) movie.director = director;
            if (releaseYear) movie.releaseYear = releaseYear;
            return movie;
        },
    },
};

module.exports = resolvers;