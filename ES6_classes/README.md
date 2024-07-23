# ES6 classes

ES6 introduced classes in JavaScript, providing a cleaner and more intuitive syntax for creating objects and working with inheritance. A class is defined using the `class` keyword, followed by the class name and a constructor method for initializing object properties. Methods can be added directly within the class body. Inheritance is facilitated using the `extends` keyword, allowing a class to inherit methods and properties from a parent class. The `super` keyword is used to call the constructor and methods of the parent class. ES6 classes simplify object-oriented programming, making the code more readable and easier to maintain.

## Resources to Read

- [Classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes)
- [Metaprogramming](https://www.keithcirkel.co.uk/metaprogramming-in-es6-symbols/#symbolspecies)

### Version Notes

In JavaScript, it's sometimes necessary to use a specific version of the language to ensure that a file runs correctly. This is because JavaScript has evolved over the years, introducing new features and improvements in recent versions that may not be compatible with older versions or certain browsers.

### Key points include

1. __Browser Compatibility:__ Not all browsers support all JavaScript versions. Features introduced in ECMAScript 6 (ES6), for example, may not work in older versions of Internet Explorer.

2. __Development Tools and Environments:__ Tools like Babel can transpile modern JavaScript code to older versions to ensure compatibility.

3. __Dependencies and Libraries:__ Some libraries and frameworks require specific JavaScript versions to function correctly.

4. __Node.js Ecosystem:__ Different versions of Node.js support different JavaScript versions, so you may need a specific Node.js version to run your code.
  
__How to Manage This:__

- __Transpilers:__ Use tools like Babel to convert modern JavaScript code to an older version compatible with all browsers.

- __Polyfills:__ Include polyfills to add support for modern features in older browsers.

- __Version Managers:__ Use version managers like nvm (Node Version Manager) to easily switch between different Node.js versions in your development environment.

### Conclusion

Using the exact version of JavaScript can be crucial to ensure that your code works correctly across all required environments and devices. It's important to be aware of the versions you're using and the capabilities of the browsers or environments where your code will run.

- Need to make a setup first, fallow the steps on this Readme.

## Setup

    Install NodeJS 20.x.x

__(In your home directory):__

    curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh

    sudo bash nodesource_setup.sh

    sudo apt install nodejs -y

## In the Terminal

$ nodejs -v
 `v20.15.1`

$ npm -v
 `10.7.0`

## Install Jest, Babel, and ESLint

__In your project directory:__

Install Jest using:

    `npm install --save-dev jest`

Install Babel using:

    npm install --save-dev babel-jest @babel/core @babel/preset-env

Install ESLint using:

    npm install --save-dev eslint

- See [Version Note](#version-notes) if have any problem.

## Configuration files

Please create the following 3 files (with the provided contents) in the project directory:

### package.json

        {
    "scripts": {
        "lint": "./node_modules/.bin/eslint",
        "check-lint": "lint [0-9]*.js",
        "dev": "npx babel-node",
        "test": "jest",
        "full-test": "./node_modules/.bin/eslint [0-9]*.js && jest"
    },
    "devDependencies": {
        "@babel/core": "^7.6.0",
        "@babel/preset-env": "^7.6.0",
        "@babel/node": "^7.8.0",
        "eslint": "^6.8.0",
        "eslint-config-airbnb-base": "^14.0.0",
        "eslint-plugin-import": "^2.18.2",
        "eslint-plugin-jest": "^22.17.0",
        "jest": "^24.9.0"
    }
    }

### babel.config.js

    module.exports = {
    presets: [
        [
        '@babel/preset-env',
        {
            targets: {
            node: 'current',
            },
        },
        ],
    ],
    };

### .eslintrc.js

    module.exports = {
    env: {
        browser: false,
        es6: true,
        jest: true,
    },
    extends: [
        'airbnb-base',
        'plugin:jest/all',
    ],
    globals: {
        Atomics: 'readonly',
        SharedArrayBuffer: 'readonly',
    },
    parserOptions: {
        ecmaVersion: 2018,
        sourceType: 'module',
    },
    plugins: ['jest'],
    rules: {
        'no-console': 'off',
        'no-shadow': 'off',
        'no-restricted-syntax': [
        'error',
        'LabeledStatement',
        'WithStatement',
        ],
    },
    overrides:[
        {
        files: ['*.js'],
        excludedFiles: 'babel.config.js',
        }
    ]
    };

## Finally (DO NOT FORGET)

- Don’t forget to run `npm install` from the terminal of your project folder to install all necessary project dependencies. Do not push on your repository the folder `node_modules` that has been created.

- When you finish the task, run `npx eslint task_file_name.js` to show errors. Then, run `npx eslint task_file_name.js --fix` to fix some of the ESLint errors (this will not fix all errors, but it helps).