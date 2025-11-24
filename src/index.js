const express = require('express');
const { ApolloServer } = require('apollo-server-express');
const { ApolloServerPluginLandingPageGraphQLPlayground } = require('apollo-server-core');
const { makeExecutableSchema } = require('graphql-tools');
const { applyMiddleware } = require('graphql-middleware');
const config = require('./config');

// Import schema and resolvers
const typeDefs = require('./schemas/typeDefs');
const resolvers = require('./resolvers');

// Import middleware
const performanceMonitoring = require('./middleware/performance');

// Import context factory
const { createContext } = require('./utils/context');

async function startServer() {
  const app = express();

  // Create executable schema with type definitions and resolvers
  const schema = makeExecutableSchema({
    typeDefs,
    resolvers
  });

  // Apply middleware to schema
  const schemaWithMiddleware = applyMiddleware(schema, performanceMonitoring);

  // Create Apollo Server instance
  const server = new ApolloServer({
    schema: schemaWithMiddleware,
    context: createContext,
    introspection: config.graphql.introspection,
    plugins: [
      ApolloServerPluginLandingPageGraphQLPlayground({
        // Options for the playground
      }),
    ]
  });

  // Start Apollo Server
  await server.start();

  // Apply middleware
  server.applyMiddleware({ app, path: config.graphql.path });

  // Define port
  const PORT = config.server.port;

  // Start Express server
  app.listen(PORT, () => {
    console.log(`🚀 Server ready at http://localhost:${PORT}${server.graphqlPath}`);
    console.log(`📚 GraphQL Playground available at http://localhost:${PORT}${server.graphqlPath}`);
    console.log(`Environment: ${config.server.env}`);
  });
}

// Start the server
startServer().catch((err) => {
  console.error('Error starting server:', err);
});