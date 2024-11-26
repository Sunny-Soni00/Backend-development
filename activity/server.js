const {ApolloServer} = require('apollo-server');
const typeDefs = require('./schema copy');
const resolvers = require('./resolvers copy');

const server = new ApolloServer({typeDefs, resolvers});

server.listen().then(({url}) => {
    console.log(`Server ready at ${url}`);
});