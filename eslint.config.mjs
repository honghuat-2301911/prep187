import js from "@eslint/js";
import globals from "globals";
import pluginSecurity from "eslint-plugin-security";
import pluginNoUnsanitized from "eslint-plugin-no-unsanitized";
import { defineConfig } from "eslint/config";

export default defineConfig([
  {
    files: ["**/*.{js,mjs,cjs}"],
    languageOptions: {
      ecmaVersion: 2021,
      sourceType: "module",
      globals: globals.browser,
    },
    plugins: {
      security: pluginSecurity,
      "no-unsanitized": pluginNoUnsanitized,
    },
    rules: {
      ...js.configs.recommended.rules,
      ...pluginSecurity.configs.recommended.rules,
      ...pluginNoUnsanitized.configs.recommended.rules,

      "security/detect-eval-with-expression": "error",
      "no-console": "warn",
    },
  },
]);
