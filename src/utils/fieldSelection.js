/**
 * Field Selection Utilities
 *
 * This module provides utilities for handling GraphQL field selections
 * to optimize network payloads by only retrieving requested fields.
 */
const graphqlFields = require('graphql-fields');

/**
 * Gets requested fields from GraphQL info object
 * @param {Object} info - GraphQL resolver info object
 * @param {Array} defaultFields - Default fields to include even if not requested
 * @returns {Object} - Object representing requested fields
 */
const getRequestedFields = (info, defaultFields = ['id']) => {
  // Extract fields from GraphQL info
  const fields = graphqlFields(info);

  // Ensure default fields are included
  defaultFields.forEach(field => {
    if (!fields[field]) {
      fields[field] = true;
    }
  });

  return fields;
};

/**
 * Converts field selection object to array of field names
 * @param {Object} fields - Field selection object from graphqlFields
 * @param {String} prefix - Field path prefix for nested fields
 * @returns {Array} - Array of field paths
 */
const fieldsToArray = (fields, prefix = '') => {
  return Object.entries(fields).flatMap(([key, value]) => {
    const path = prefix ? `${prefix}.${key}` : key;

    // If value is an object, it's a nested selection
    if (value && typeof value === 'object' && !Array.isArray(value)) {
      return fieldsToArray(value, path);
    }

    return path;
  });
};

/**
 * Filters an object to only include requested fields
 * @param {Object} obj - Object to filter
 * @param {Object|Array} fields - Field selection (object or array)
 * @returns {Object} - Filtered object
 */
const filterObjectByFields = (obj, fields) => {
  // Handle empty cases
  if (!obj || !fields) return obj;

  // Convert fields to array if it's an object
  const fieldArray = typeof fields === 'object' && !Array.isArray(fields)
    ? fieldsToArray(fields)
    : fields;

  // Create filtered object
  const filtered = {};

  fieldArray.forEach(field => {
    // Handle nested paths
    const parts = field.split('.');
    let current = obj;
    let target = filtered;

    // Navigate through nested objects
    for (let i = 0; i < parts.length; i++) {
      const part = parts[i];

      if (i === parts.length - 1) {
        // Last part, set value
        if (current !== undefined && current !== null) {
          target[part] = current[part];
        }
      } else {
        // Navigate to next level
        current = current?.[part];
        if (current === undefined || current === null) break;

        // Create nested object if it doesn't exist
        if (!target[part]) target[part] = {};
        target = target[part];
      }
    }
  });

  return filtered;
};

/**
 * Creates projection for database queries based on GraphQL fields
 * @param {Object} info - GraphQL resolver info
 * @param {Object} mappings - Mappings between GraphQL and DB field names
 * @returns {Object} - Projection object for database queries
 */
const createProjection = (info, mappings = {}) => {
  const fields = getRequestedFields(info);
  const fieldArray = fieldsToArray(fields);

  // Create projection object (e.g., for MongoDB)
  const projection = { _id: 1 }; // Always include ID

  fieldArray.forEach(field => {
    const dbField = mappings[field] || field;
    projection[dbField] = 1;
  });

  return projection;
};

module.exports = {
  getRequestedFields,
  fieldsToArray,
  filterObjectByFields,
  createProjection
};