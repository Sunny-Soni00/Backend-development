const {gql} = require('apollo-server');

const typeDefs = gql`
    type Movies {
        id: ID!
        title: String!
        director: String!
        releaseYear: Int!
        reviews: [Reviews!]!
    }

    type Reviews {
        id: ID!
        movieId: ID!
        rating: Float!
        reviewer: String!
    }

    type Query {
        movies: [Movies]
        reviews: [Reviews]

        movie(id: ID!): Movies
        review(movieId: ID!): Reviews
    }
`;
module.exports = typeDefs;