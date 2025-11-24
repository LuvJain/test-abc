/**
 * DataLoader utilities
 *
 * This module provides utility functions for creating and configuring DataLoader instances
 * to optimize data fetching with batching and caching.
 */
const DataLoader = require('dataloader');

/**
 * Create a DataLoader with default configuration
 * @param {Function} batchFn - Function to load multiple items at once
 * @param {Object} options - Additional DataLoader options
 * @returns {DataLoader} - Configured DataLoader instance
 */
const createLoader = (batchFn, options = {}) => {
  return new DataLoader(batchFn, {
    cache: true, // Enable caching by default
    ...options
  });
};

/**
 * Create a DataLoader specifically for fetching items by ID
 * @param {Function} fetchFn - Function that takes an array of IDs and returns objects
 * @returns {DataLoader} - DataLoader for fetching by ID
 */
const createIdLoader = (fetchFn) => {
  return createLoader(async (ids) => {
    const items = await fetchFn(ids);

    // Ensure results are returned in the same order as requested IDs
    const itemMap = items.reduce((map, item) => {
      map[item.id] = item;
      return map;
    }, {});

    // Map each ID to its corresponding item or null if not found
    return ids.map(id => itemMap[id] || null);
  });
};

/**
 * Create a DataLoader for fetching items by a specific field
 * @param {Function} fetchFn - Function that takes field values and returns items
 * @param {String} field - Field name to batch by
 * @param {Boolean} multiple - Whether each key returns multiple items
 * @returns {DataLoader} - DataLoader for fetching by field
 */
const createFieldLoader = (fetchFn, field, multiple = false) => {
  return createLoader(async (fieldValues) => {
    const items = await fetchFn(fieldValues);

    if (multiple) {
      // For one-to-many relationships, group items by field
      const grouped = fieldValues.map(value =>
        items.filter(item => item[field] === value)
      );
      return grouped;
    } else {
      // For one-to-one relationships, map each value to a single item
      const itemMap = items.reduce((map, item) => {
        map[item[field]] = item;
        return map;
      }, {});

      return fieldValues.map(value => itemMap[value] || null);
    }
  });
};

module.exports = {
  createLoader,
  createIdLoader,
  createFieldLoader
};