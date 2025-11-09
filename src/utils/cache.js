/**
 * Cache utilities
 *
 * This module provides caching functionality for GraphQL resolvers
 * to optimize performance and reduce redundant data fetching.
 */
const NodeCache = require('node-cache');

// Create cache instance with default TTL of 5 minutes
const cache = new NodeCache({
  stdTTL: 300, // 5 minutes in seconds
  checkperiod: 60, // Check for expired entries every 1 minute
  useClones: false // For better performance, don't clone objects
});

/**
 * Wraps a function with caching functionality
 * @param {Function} fn - The function to cache
 * @param {String} prefix - Cache key prefix
 * @param {Number} ttl - Time to live in seconds (optional)
 * @returns {Function} - Wrapped function with caching
 */
const cacheResolver = (fn, prefix, ttl = 300) => {
  return async (...args) => {
    // Generate a cache key based on function arguments
    const key = `${prefix}:${JSON.stringify(args)}`;

    // Try to get value from cache
    const cachedValue = cache.get(key);
    if (cachedValue !== undefined) {
      return cachedValue;
    }

    // Execute the original function if cache miss
    const result = await fn(...args);

    // Store result in cache
    cache.set(key, result, ttl);

    return result;
  };
};

/**
 * Clears cache entries by prefix
 * @param {String} prefix - Cache key prefix to clear
 */
const clearCacheByPrefix = (prefix) => {
  const keys = cache.keys();
  keys.forEach(key => {
    if (key.startsWith(`${prefix}:`)) {
      cache.del(key);
    }
  });
};

/**
 * Clears all cache entries
 */
const clearAllCache = () => {
  cache.flushAll();
};

/**
 * Gets cache statistics
 * @returns {Object} - Cache statistics
 */
const getCacheStats = () => {
  return {
    keys: cache.keys().length,
    hits: cache.getStats().hits,
    misses: cache.getStats().misses,
    ksize: cache.getStats().ksize,
    vsize: cache.getStats().vsize
  };
};

module.exports = {
  cache,
  cacheResolver,
  clearCacheByPrefix,
  clearAllCache,
  getCacheStats
};