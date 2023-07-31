Sometimes you want to get started with React but don't want all the bloat of `create-react-app` or some other boilerplate. Here's a step by step walkthrough of how to set to setup React with just Webpack!

```bash
npm install webpack webpack-cli --save-dev
```

```bash
mkdir src
touch src/index.js
```

```js
// webpack.config.js

const path = require("path");

module.exports = {
  entry: "./src/index.js",
  output: {
    filename: "main.js",
    path: path.resolve(__dirname, "build"),
  },
};
```

In `package.json`, add a new "build" script:

```json
// ...
"scripts": {
    "build": "webpack"
},
```

after npm build it will work fine