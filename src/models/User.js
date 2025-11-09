// Mock database for users
let users = [
  {
    id: '1',
    name: 'John Doe',
    username: 'johndoe',
    email: 'john@example.com',
    displayName: 'John D.',
    bio: 'Software engineer and open source contributor',
    age: 30,
    role: 'USER',
    createdAt: new Date().toISOString(),
    lastLogin: new Date().toISOString()
  },
  {
    id: '2',
    name: 'Jane Smith',
    username: 'janesmith',
    email: 'jane@example.com',
    displayName: 'Jane S.',
    bio: 'UI/UX Designer with 5 years experience',
    age: 25,
    role: 'ADMIN',
    createdAt: new Date().toISOString(),
    lastLogin: new Date().toISOString()
  }
];

// User model with CRUD operations
class UserModel {
  // Get all users
  static getAll() {
    return users;
  }

  // Get user by ID
  static getById(id) {
    return users.find(user => user.id === id);
  }

  // Get user count
  static count() {
    return users.length;
  }

  // Create a new user
  static create(userData) {
    const newUser = {
      id: String(users.length + 1),
      ...userData,
      createdAt: new Date().toISOString()
    };
    users.push(newUser);
    return newUser;
  }

  // Update an existing user
  static update(id, userData) {
    const index = users.findIndex(user => user.id === id);
    if (index === -1) return null;

    const updatedUser = {
      ...users[index],
      ...userData
    };

    users[index] = updatedUser;
    return updatedUser;
  }

  // Delete a user
  static delete(id) {
    const initialLength = users.length;
    users = users.filter(user => user.id !== id);
    return users.length !== initialLength;
  }
}

module.exports = UserModel;