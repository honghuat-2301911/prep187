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
      // ESLint core recommended rules
      ...js.configs.recommended.rules,
      // Security plugin recommended rules if using ESLint 9.x and plugin supports flat config
      ...(pluginSecurity.configs?.recommended?.rules || {}),
      // No-unsanitized plugin recommended rules
      ...(pluginNoUnsanitized.configs?.recommended?.rules || {}),

      // Custom rules
      "security/detect-eval-with-expression": "error",
      "no-console": "warn",
    },
  },
]);
