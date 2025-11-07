const userResolvers = require('./userResolvers');

// Combine all resolvers
const resolvers = {
  Query: {
    ...userResolvers.Query
  },
  Mutation: {
    ...userResolvers.Mutation
  }
};

module.exports = resolvers;