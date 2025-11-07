/**
 * GraphQL Context Provider
 *
 * This module creates the context object that is passed to each GraphQL resolver.
 * It includes DataLoader instances, caching utilities, and other shared resources.
 */
const { createIdLoader } = require('./dataLoaders');
const UserModel = require('../models/User');
const { cache } = require('./cache');

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

  return {
    // Request information
    req,

    // DataLoader instances
    loaders,

    // Cache instance
    cache,

    // User information (for authentication, to be implemented)
    user: null
  };
};

module.exports = { createContext };