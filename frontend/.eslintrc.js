// module.exports = {
//   root: true,
//   env: {
//     node: true,
//   },
//   extends: ["plugin:vue/essential", "eslint:recommended", "@vue/prettier"],
//   parserOptions: {
//     parser: "babel-eslint",
//   },
//   rules: {
//     "linebreak-style": ["error", "unix"],
//     "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
//     "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off",
//   },
// };
module.exports = {
  env: {
    browser: true,
    es2021: true,
  },
  extends: [
    "eslint:recommended",
    "plugin:vue/recommended",
    "airbnb-base",
    // "plugin:prettier/recommended",
  ],
  parserOptions: {
    ecmaVersion: 12,
    sourceType: "module",
  },
  plugins: ["vue"],
  rules: {
    "no-param-reassign": [
      "error",
      {
        props: true,
        ignorePropertyModificationsFor: ["state"],
      },
    ],
    "vue/valid-v-slot": [
      "error",
      {
        allowModifiers: true,
      },
    ],
    "linebreak-style": ["error", "unix"],
    // "linebreak-style": ["error", "windows"],

    quotes: ["error", "double"],
    camelcase: ["error", { properties: "never", ignoreDestructuring: true }],
    "no-underscore-dangle": "off",
  },
};
