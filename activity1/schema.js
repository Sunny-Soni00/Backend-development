const { gql } = require('apollo-server');

const typeDefs = gql`
    type Book {
        id: ID!
        title: String!
        author: String!
        publishedYear: Int!
    }

    type Member {
        id: ID!
        name: String!
        email: String!
        membershipType: String!
    }

    type Query {
        books: [Book!]!
        members: [Member!]!
        book(id: ID!): Book
        member(id: ID!): Member
        booksPublishedBefore1950: [Book!]!
        premiumMembers: [Member!]!
        BookDetails: [String!]!
    }

    type Mutation {
        addBook(title: String!, author: String!, publishedYear: Int!): Book
        addMember(name: String!, email: String!, membershipType: String!): Member
        updateMembership(id: ID!, membershipType: String!): Member
    }
`;

module.exports = typeDefs;