import globals from 'globals';
import pluginJs from '@eslint/js';
import pluginSecurity from 'eslint-plugin-security';
import pluginSecurityNode from 'eslint-plugin-security-node';
import pluginNoUnsanitized from 'eslint-plugin-no-unsanitized';

/** @type {import('eslint').Linter.Config[]} */
export default [
  pluginJs.configs.recommended,
  pluginSecurity.configs.recommended,
  pluginSecurityNode.configs.recommended,
  pluginNoUnsanitized.configs.recommended,
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
      'security-node': pluginSecurityNode,
      'no-unsanitized': pluginNoUnsanitized
    },
    rules: {
      'security/detect-eval-with-expression': 'error',
      'no-unsanitized/method': 'error',
      'no-unsanitized/property': 'error'
    }
  }
];
