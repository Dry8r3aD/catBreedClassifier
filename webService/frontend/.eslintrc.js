module.exports = {
  env: {
    es6: true,
    node: true
  },
  extends: ["eslint:recommended", "plugin:prettier/recommended", "plugin:vue/essential"],
  parserOptions: {
    ecmaVersion: 2018,
    sourceType: "module",
    parser: "babel-eslint"
  },
  plugins: ["prettier", "vue"],
  rules: {
    "no-console": "off",
    "no-undef": ["warn"],
    "no-unused-vars": ["warn"],
    "no-constant-condition": ["error", { checkLoops: false }],
    "vue/valid-v-slot": "off",
    "vue/no-parsing-error": "error",
    "vue/no-unused-components": ["warn"],
    "vue/order-in-components": ["warn"],
    "non-void-html-element-start-tag-with-trailing-solidus": "off",
    "arrow-parens": ["warn", "as-needed"],
    "prettier/prettier": [
      "warn",
      {
        endOfLine: "auto"
      }
    ]
  }
};
