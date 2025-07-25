module.exports = {
  root: true, 
  env: {
    browser: true,
    es2021: true,     
  },
  extends: [
    'eslint:recommended',
    'plugin:security/recommended',
    'plugin:no-unsanitized/recommended',
  ],
  parserOptions: {
    ecmaVersion: 12,
    sourceType: 'module',
  },
  plugins: [
    'security',
    'security-node',
    'no-unsanitized'
  ],
  rules: {
    'security/detect-eval-with-expression': 'error',
    'no-console': 'warn',
  }
}