module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: ["plugin:vue/essential","plugin:vue/strongly-recommended", "eslint:recommended", "@vue/prettier", "plugin:vue/base"],
  parserOptions: {
    parser: "babel-eslint",
  },
  rules: {
    "linebreak-style": ["error", "unix"],
    "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off",
  },
};
