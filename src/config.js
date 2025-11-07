// Configuration settings for the GraphQL server
require('dotenv').config();

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

  // Authentication configuration
  auth: {
    // JWT secret key - should be stored in environment variables in production
    jwtSecret: process.env.JWT_SECRET || 'dev-secret-key-change-in-production',

    // JWT token expiration time
    jwtExpiresIn: process.env.JWT_EXPIRES_IN || '24h',

    // Password hashing rounds for bcrypt
    saltRounds: 10,

    // Whether to require authentication for all resolvers by default
    requireAuthByDefault: process.env.REQUIRE_AUTH_DEFAULT === 'true' || false
  },

  // Performance monitoring configuration
  monitoring: {
    // Enable performance monitoring
    enabled: true,

    // Log threshold in milliseconds (log queries taking longer than this)
    logThreshold: 50
  },

  // Security and logging configuration
  security: {
    // Enable logging of unauthorized access attempts
    logUnauthorizedAttempts: true,

    // Log level for security events
    logLevel: process.env.SECURITY_LOG_LEVEL || 'info'
  }
};

module.exports = config;