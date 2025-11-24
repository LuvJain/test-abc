const config = require('../config');

/**
 * GraphQL middleware to monitor query performance
 * Measures the execution time of each resolver and logs slow queries
 */
const performanceMonitoring = async (resolve, root, args, context, info) => {
  // Skip if monitoring is disabled
  if (!config.monitoring.enabled) {
    return await resolve(root, args, context, info);
  }

  // Get operation name and type
  const operationType = info.parentType.name;
  const fieldName = info.fieldName;
  const operationName = `${operationType}.${fieldName}`;

  // Record start time
  const startTime = process.hrtime();

  // Execute the resolver
  let result;
  try {
    result = await resolve(root, args, context, info);
    return result;
  } catch (error) {
    // Log error with operation details
    console.error(`[ERROR] Operation: ${operationName}`, {
      error: error.message,
      args,
      path: info.path,
    });
    throw error;
  } finally {
    // Calculate execution time
    const [seconds, nanoseconds] = process.hrtime(startTime);
    const executionTime = seconds * 1000 + nanoseconds / 1000000; // Convert to milliseconds

    // Log slow queries
    if (executionTime > config.monitoring.logThreshold) {
      console.warn(`[SLOW QUERY] ${operationName} took ${executionTime.toFixed(2)}ms`, {
        operationType,
        fieldName,
        args: JSON.stringify(args),
        executionTime: `${executionTime.toFixed(2)}ms`,
      });
    }

    // For detailed monitoring, we could log all operations
    if (process.env.NODE_ENV === 'development' && process.env.DEBUG_GRAPHQL) {
      console.log(`[GRAPHQL] ${operationName} executed in ${executionTime.toFixed(2)}ms`);
    }
  }
};

module.exports = performanceMonitoring;