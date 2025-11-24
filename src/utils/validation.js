/**
 * Validation utilities for input data
 */

/**
 * Profile field validation rules
 */
const PROFILE_VALIDATIONS = {
  username: {
    minLength: 3,
    maxLength: 30,
    pattern: /^[a-z0-9_]+$/i,
    errorMessage: 'Username must be between 3-30 characters and contain only letters, numbers, and underscores'
  },
  displayName: {
    minLength: 1,
    maxLength: 50,
    errorMessage: 'Display name must be between 1-50 characters'
  },
  firstName: {
    minLength: 1,
    maxLength: 50,
    errorMessage: 'First name must be between 1-50 characters'
  },
  lastName: {
    minLength: 1,
    maxLength: 50,
    errorMessage: 'Last name must be between 1-50 characters'
  },
  profileImage: {
    pattern: /^https?:\/\/.+/i,
    errorMessage: 'Profile image must be a valid URL'
  },
  bio: {
    maxLength: 500,
    errorMessage: 'Bio cannot exceed 500 characters'
  }
};

/**
 * Validates profile input data
 *
 * @param {Object} profileData - Profile data to validate
 * @returns {Object} - Object with isValid and errors properties
 */
const validateProfileData = (profileData) => {
  const errors = [];

  // Skip fields that are not provided (for partial updates)
  Object.entries(profileData).forEach(([field, value]) => {
    // Skip validation for undefined or null values in partial updates
    if (value === undefined || value === null) return;

    const validation = PROFILE_VALIDATIONS[field];

    // Skip if no validation rules exist for this field
    if (!validation) return;

    // String length validations
    if (typeof value === 'string') {
      if (validation.minLength && value.length < validation.minLength) {
        errors.push(`${field}: ${validation.errorMessage}`);
      }

      if (validation.maxLength && value.length > validation.maxLength) {
        errors.push(`${field}: ${validation.errorMessage}`);
      }

      // Pattern matching validations
      if (validation.pattern && !validation.pattern.test(value)) {
        errors.push(`${field}: ${validation.errorMessage}`);
      }
    } else {
      // Field should be a string but is not
      errors.push(`${field}: Must be a string value`);
    }
  });

  return {
    isValid: errors.length === 0,
    errors
  };
};

/**
 * Validates that a profile update has at least one field
 *
 * @param {Object} profileData - Profile data to check
 * @returns {Boolean} - True if at least one field is present
 */
const validateProfileUpdateHasFields = (profileData) => {
  // Check if there's at least one field with a non-null/undefined value
  return Object.values(profileData).some(value =>
    value !== undefined && value !== null
  );
};

/**
 * Sanitizes profile data by removing any fields that don't belong in a profile
 *
 * @param {Object} profileData - Raw profile data to sanitize
 * @returns {Object} - Sanitized profile data
 */
const sanitizeProfileData = (profileData) => {
  const allowedFields = Object.keys(PROFILE_VALIDATIONS);
  const sanitized = {};

  allowedFields.forEach(field => {
    if (profileData[field] !== undefined) {
      sanitized[field] = profileData[field];
    }
  });

  return sanitized;
};

module.exports = {
  validateProfileData,
  validateProfileUpdateHasFields,
  sanitizeProfileData
};