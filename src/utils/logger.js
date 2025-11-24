/**
 * Logging utilities for the application
 */
const winston = require('winston');
const config = require('../config');

// Create winston logger instance
const logger = winston.createLogger({
  level: config.security.logLevel,
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  defaultMeta: { service: 'graphql-api' },
  transports: [
    // Write to console in all environments
    new winston.transports.Console({
      format: winston.format.combine(
        winston.format.colorize(),
        winston.format.simple()
      )
    })
    // In a production environment, you would add file transports here
  ]
});

/**
 * Log profile change events with details
 *
 * @param {Object} params - Logging parameters
 * @param {String} params.userId - ID of user whose profile was changed
 * @param {String} params.action - The action performed (update, create, etc.)
 * @param {Object} params.changes - The fields that were changed
 * @param {String} params.performedBy - ID of user who performed the action
 * @param {Boolean} params.isAdminAction - Whether this was performed by an admin
 */
const logProfileChange = ({
  userId,
  action,
  changes,
  performedBy,
  isAdminAction = false
}) => {
  // Create a sanitized version of changes that doesn't include sensitive data
  const safeChanges = { ...changes };

  // Don't log any sensitive fields that might be added in the future
  const sensitiveFields = ['password', 'authToken'];
  sensitiveFields.forEach(field => {
    if (safeChanges[field]) {
      safeChanges[field] = '[REDACTED]';
    }
  });

  // Log the profile change
  logger.info('Profile change', {
    event: 'profile_change',
    userId,
    action,
    // Only include the field names that changed, not their values
    changedFields: Object.keys(safeChanges),
    performedBy,
    isAdminAction,
    timestamp: new Date().toISOString()
  });

  // For admin actions, log additional details
  if (isAdminAction) {
    logger.info('Admin profile action', {
      event: 'admin_profile_action',
      adminId: performedBy,
      targetUserId: userId,
      action,
      changedFields: Object.keys(safeChanges)
    });
  }
};

/**
 * Log authentication and authorization events
 *
 * @param {Object} params - Logging parameters
 * @param {String} params.userId - ID of the user
 * @param {String} params.action - The action (login, logout, access_denied, etc.)
 * @param {String} params.resource - The resource being accessed (optional)
 * @param {Boolean} params.success - Whether the action was successful
 * @param {String} params.reason - Reason for failure (if applicable)
 * @param {Object} params.metadata - Additional metadata
 */
const logAuthEvent = ({
  userId,
  action,
  resource,
  success = true,
  reason = null,
  metadata = {}
}) => {
  logger.info('Auth event', {
    event: 'auth_event',
    userId,
    action,
    resource,
    success,
    reason,
    ...metadata,
    timestamp: new Date().toISOString()
  });
};

module.exports = {
  logger,
  logProfileChange,
  logAuthEvent
};