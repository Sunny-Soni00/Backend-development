// const {gql} = require('apollo-server');

// const typeDefs = gql`
//     type User {
//         id: ID!
//         name: String!
//         email: String!
//         }

//     type Query {
//         user(id: ID!): User
//     }
// `;

// module.exports = typeDefs;

// const { gql } = require('apollo-server');

// const typeDefs = gql`
//     type Books {
//         id: ID!
//         title: String!
//         author: String!
//         publishedYear: Int! 
//     }

//     type Members {
//         id: ID!
//         name: String!  
//         email: String!
//         membershipType: String!
//     }

//     type Query {
//         Book(id: ID!): Books 
//         Member(id: ID!): Members
//         Books : [Books!]!
//         Members : [Members!]!
//         BooksFilter: [Books!]!
//         MembersFilter: [Members!]!
//     }
//     type Mutation {
//         AddBook(title: String!, author: String!, publishedYear: Int!): Books!
//         AddMember(name: String!, email: String!, membershipType: String!): Members!
//         UpdateMembershipType(id:ID!,membershipType: String!): Members!
//     }
// `;

// module.exports = typeDefs;

// schema
// const { gql } = require("apollo-server");

// const typeDefs = gql`
//     type User {
//     id: ID!
//     email: String!
//     role: String
//     }


//     type Query {
//         secretData: String!
//     }

//     type Mutation {
//         login(email: String!, password: String!): String!
//     }
    
// `;

// module.exports = typeDefs;

// schema
const { gql } = require("apollo-server");

const typeDefs = gql`
    type User {
        id: ID!
        email: String!
        role: String
    }

    type Movie {
        id: ID!
        title: String!
        director: String!
        releaseYear: Int!
    }

    type Review {
        id: ID!
        movieId: ID!
        rating: Float!
        reviewer: String!
    }

    type Query {
        secretData: String!
        movies: [Movie!]!
        movie(id: ID!): Movie
        reviews: [Review!]!
    }

    type Mutation {
        login(email: String!, password: String!): String!
        addMovie(title: String!, director: String!, releaseYear: Int!): Movie!
        updateMovie(id: ID!, title: String, director: String, releaseYear: Int): Movie!
    }
`;

module.exports = typeDefs;