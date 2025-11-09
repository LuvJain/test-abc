/**
 * GraphQL Context Provider
 *
 * This module creates the context object that is passed to each GraphQL resolver.
 * It includes DataLoader instances, caching utilities, and other shared resources.
 */
const { createIdLoader } = require('./dataLoaders');
const UserModel = require('../models/User');
const { cache } = require('./cache');
const { extractTokenFromRequest, verifyToken } = require('./auth');
const config = require('../config');

/**
 * Creates a new context for each GraphQL request
 * @param {Object} req - Express request object
 * @returns {Object} - Context object with loaders and utilities
 */
const createContext = ({ req }) => {
  // Create fresh DataLoader instances for each request to avoid cross-request caching issues
  const loaders = {
    // User loaders
    users: {
      byId: createIdLoader(ids => {
        console.log(`Batch loading ${ids.length} users by ID`);
        // Return array of users matching the IDs
        return Promise.resolve(
          ids.map(id => UserModel.getById(id))
            .filter(user => user !== null)
        );
      })
    }
  };

  // Extract and verify authentication token
  let user = null;
  try {
    const token = extractTokenFromRequest(req);
    if (token) {
      const decoded = verifyToken(token);
      if (decoded && decoded.id) {
        // Fetch user data from model using token info
        user = UserModel.getById(decoded.id);

        // Log auth attempt if enabled
        if (config.security.logUnauthorizedAttempts && !user) {
          console.warn(`[AUTH WARNING] Token validation succeeded but user not found for ID: ${decoded.id}`);
        }
      }
    }
  } catch (error) {
    console.error('[AUTH ERROR] Error processing authentication token:', error.message);
  }

  return {
    // Request information
    req,

    // DataLoader instances
    loaders,

    // Cache instance
    cache,

    // Authenticated user information
    user,

    // Helper function to check if user is authenticated
    isAuthenticated: () => !!user
  };
};

module.exports = { createContext };