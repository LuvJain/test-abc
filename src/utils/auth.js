/**
 * Authentication utilities for JWT token generation and verification
 */
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const config = require('../config');

/**
 * Generates a JWT token for a user
 *
 * @param {Object} user - User object to include in the token payload
 * @returns {String} JWT token
 */
const generateToken = (user) => {
  // Create payload with user information, excluding sensitive data
  const payload = {
    id: user.id,
    email: user.email,
    role: user.role
  };

  // Sign token with secret and set expiration
  return jwt.sign(
    payload,
    config.auth.jwtSecret,
    { expiresIn: config.auth.jwtExpiresIn }
  );
};

/**
 * Verifies a JWT token and returns the decoded user data
 *
 * @param {String} token - JWT token to verify
 * @returns {Object|null} Decoded user data or null if invalid
 */
const verifyToken = (token) => {
  try {
    // Verify token signature and expiration
    const decoded = jwt.verify(token, config.auth.jwtSecret);
    return decoded;
  } catch (error) {
    // Handle different verification errors
    console.error('JWT verification failed:', error.message);
    return null;
  }
};

/**
 * Extracts JWT token from request headers
 *
 * @param {Object} req - Express request object
 * @returns {String|null} JWT token or null if not found
 */
const extractTokenFromRequest = (req) => {
  // Check if authorization header exists
  if (!req || !req.headers || !req.headers.authorization) {
    return null;
  }

  // Parse authorization header
  const authHeader = req.headers.authorization;
  const parts = authHeader.split(' ');

  // Validate format: "Bearer [token]"
  if (parts.length !== 2 || parts[0] !== 'Bearer') {
    return null;
  }

  return parts[1];
};

/**
 * Hashes a password using bcrypt
 *
 * @param {String} password - Plain text password to hash
 * @returns {Promise<String>} Hashed password
 */
const hashPassword = async (password) => {
  return await bcrypt.hash(password, config.auth.saltRounds);
};

/**
 * Compares a plain text password with a hashed password
 *
 * @param {String} password - Plain text password to check
 * @param {String} hashedPassword - Hashed password to compare against
 * @returns {Promise<Boolean>} True if password matches
 */
const comparePasswords = async (password, hashedPassword) => {
  return await bcrypt.compare(password, hashedPassword);
};

module.exports = {
  generateToken,
  verifyToken,
  extractTokenFromRequest,
  hashPassword,
  comparePasswords
};