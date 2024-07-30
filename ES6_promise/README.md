# ES6 Promises

Promises in JavaScript are objects that represent the eventual completion or failure of an asynchronous operation. A promise can be in one of three states: `pending`, `fulfilled`, or `rejected`. When a promise is created, it is in the pending state, indicating that the operation has not yet finished.

A promise is resolved (fulfilled) with a value when the asynchronous operation succeeds or is rejected with a reason (error) when it fails. To handle these outcomes, the `.then()` and `.catch()` methods are used:

- __.then()__ is executed when the promise is fulfilled and handles the resulting value.
- __.catch()__ is executed when the promise is rejected and handles the error.

There is also the `.finally()` method, which is executed regardless of the outcome.

__Basic example:__

    const promise = new Promise((resolve, reject) => {
    const success = true;
    if (success) {
        resolve('Operation succeeded');
    } else {
        reject('Operation failed');
    }
    });

    promise
    .then(result => console.log(result))   // Handles success
    .catch(error => console.error(error))  // Handles error
    .finally(() => console.log('Done'));   // Always executed

Promises improve the handling of asynchronous operations, avoiding `"callback hell"` and making the code more readable and manageable.
