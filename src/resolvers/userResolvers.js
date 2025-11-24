const UserModel = require('../models/User');

const userResolvers = {
  Query: {
    // Get user by ID
    user: (_, { id }) => {
      return UserModel.getById(id);
    },

    // Get all users
    users: () => {
      return UserModel.getAll();
    },

    // Get total user count
    userCount: () => {
      return UserModel.count();
    }
  },

  Mutation: {
    // Create a new user
    createUser: (_, { input }) => {
      return UserModel.create(input);
    },

    // Update an existing user
    updateUser: (_, { id, input }) => {
      return UserModel.update(id, input);
    },

    // Delete a user
    deleteUser: (_, { id }) => {
      return UserModel.delete(id);
    }
  }
};

module.exports = userResolvers;