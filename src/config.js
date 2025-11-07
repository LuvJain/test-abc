// Configuration settings for the GraphQL server

const config = {
  // Server configuration
  server: {
    port: process.env.PORT || 4000,
    env: process.env.NODE_ENV || 'development'
  },

  // GraphQL configuration
  graphql: {
    // Enable introspection in non-production environments
    introspection: process.env.NODE_ENV !== 'production',

    // Path for the GraphQL endpoint
    path: '/graphql',

    // Enable GraphQL Playground in non-production environments
    playground: process.env.NODE_ENV !== 'production'
  },

  // Performance monitoring configuration
  monitoring: {
    // Enable performance monitoring
    enabled: true,

    // Log threshold in milliseconds (log queries taking longer than this)
    logThreshold: 50
  }
};

module.exports = config;