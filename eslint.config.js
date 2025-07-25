import globals from 'globals';
import pluginJs from '@eslint/js';
import pluginSecurity from 'eslint-plugin-security';
import pluginNoUnsanitized from 'eslint-plugin-no-unsanitized';

/** @type {import('eslint').Linter.Config[]} */
export default [
  pluginJs.configs.recommended,
  {
    files: ['**/*.{js,mjs,cjs}'],
    languageOptions: {
      ecmaVersion: 2021,
      sourceType: 'module',
      globals: {
        ...globals.browser
      }
    },
    plugins: {
      security: pluginSecurity,
      'no-unsanitized': pluginNoUnsanitized
    },
    rules: {
      'security/detect-eval-with-expression': 'error',
      'no-console': 'warn'
    }
  },
  {
    files: ['tests/**/*.js'],
    languageOptions: {
      globals: {
        ...globals.mocha
      }
    }
  }
];
